#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""全量枚举器（2026-10-25 · 周度对账专用）：**不剪枝**递归整库。

与日更 REST 枚举器的差异：
  1. 不做任何 file_number 剪枝 —— 每个文件夹必递归、每层必翻页到底
  2. 保留 media_state，只输出 media_state=2（MEDIA_PARSE_SUCCESS）的条目
  3. 输出 .tools/_ima_enum_full_<date>.json（全量口径，含 folders 树）
  4. 额外输出媒体类型/状态分布，供对账报告直接引用

⚠ 2026-10-22 KB ID 迁移：REST 亦须用 ima_kb_l24tiCGM（旧 F8Dbmy... 报 220004）
⚠ 2026-10-25 实测：REST 响应不含 knowledge_total_size（None）→ 总数须用 MCP 交叉核验

限频治理（2026-10-15 教训）：请求间隔 2.5s + 单次失败 sleep 12s 退避（8 次）。
REST 子层参数名 = folder_id（非 parent_folder_id）。folder 条目在源头剔除，只进 folders。

容错：每完成一个文件夹即增量落盘快照，中途被 kill 不丢已枚举部分。
"""
import json
import os
import time
import urllib.request
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
KB_REST = "ima_kb_l24tiCGM"
DATE = "20261027"
INTERVAL = 2.5
SNAP = os.path.join(ROOT, ".tools", f"_ima_enum_full_{DATE}.partial.json")


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()


def post(path, payload):
    req = urllib.request.Request(
        BASE + "/" + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                 "Content-Type": "application/json"},
        method="POST")
    last = None
    for _attempt in range(8):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except Exception as e:  # noqa: BLE001
            last = e
            code = getattr(e, "code", None)
            print(f"    retry after {type(e).__name__} code={code}")
            time.sleep(12)
    raise last


def list_folder(folder_id):
    out = []
    cursor = ""
    while True:
        payload = {"knowledge_base_id": KB_REST, "limit": 50, "cursor": cursor,
                   "sort_type": "MEDIA_DESC_SORT_TYPE"}
        if folder_id:
            payload["folder_id"] = folder_id
        r = post("openapi/wiki/v1/get_knowledge_list", payload)
        if r.get("code") != 0:
            print(f"  ! code={r.get('code')} msg={r.get('message')} folder={folder_id}")
            break
        d = r.get("data", {})
        out.extend(d.get("knowledge_list", []))
        if d.get("is_end") or not d.get("next_cursor"):
            break
        cursor = d.get("next_cursor")
        time.sleep(INTERVAL)
    return out


def is_folder(e):
    return e.get("media_type") == 99 or str(e.get("media_id", "")).startswith("folder_")


def snapshot(items, folders, seen):
    """增量快照：已完成的部分落盘，供中断后审计。"""
    try:
        with open(SNAP, "w", encoding="utf-8") as f:
            json.dump({"_partial": True, "_date": DATE,
                       "items_so_far": len(items), "folders_visited": len(seen),
                       "items": items, "folders": folders}, f, ensure_ascii=False)
    except Exception:  # noqa: BLE001
        pass


def main():
    t0 = time.time()
    items = []
    folders = []
    root = list_folder(None)
    print(f"root: {len(root)}")
    for e in root:
        e["_kb_chain"] = ""
    items.extend(root)

    # 全量递归：folder 队列，永不剪枝
    # ⚠ 2026-10-25 修正：原实现把「条目自身标题」当父目录追加，导致 kb_path 末段重复
    #   （1348/1431 条被写成 A/x/x）。队列现携带 (folder_id, 父链, 本folder标题)，
    #   出队时才算本 folder 的完整链 fchain；子条目的 _kb_chain 一律等于 fchain。
    queue = [(e["media_id"], "", e.get("title", "")) for e in root if is_folder(e)]
    seen = set()
    depth = 0
    while queue:
        fid, pchain, ftitle = queue.pop(0)
        if fid in seen:
            continue
        seen.add(fid)
        fchain = (pchain + "/" + ftitle) if pchain else ftitle
        sub = list_folder(fid)
        depth += 1
        print(f"  [{depth}/{depth + len(queue)}] {fchain or '(root)'}: {len(sub)}")
        for e in sub:
            e["_kb_chain"] = fchain
        items.extend(sub)
        for e in sub:
            if is_folder(e):
                queue.append((e["media_id"], fchain, e.get("title", "")))
        if depth % 10 == 0:
            snapshot(items, folders, seen)
        time.sleep(INTERVAL)

    file_items = []
    for e in items:
        if is_folder(e):
            folders.append({
                "media_id": e.get("media_id"),
                "title": e.get("title"),
                # folder 自身路径 = 父链 + 自身标题（_kb_chain 存的是父链）
                "chain": ((e.get("_kb_chain") or "") + "/" + (e.get("title") or "")
                          if e.get("_kb_chain") else (e.get("title") or "")),
                "file_number": e.get("file_number"),
                "folder_number": e.get("folder_number"),
                "parent_folder_id": e.get("parent_folder_id"),
            })
            continue
        chain = e.get("_kb_chain", "")
        title = e.get("title", "")
        file_items.append({
            "media_id": e.get("media_id"),
            "media_type": e.get("media_type"),
            "title": title,
            "create_time": e.get("create_time"),
            "media_state": e.get("media_state"),
            "kb_path": (chain + "/" + title) if chain else title,
            "parent_folder_id": e.get("parent_folder_id"),
        })

    # 去重（同一 media_id 被多路径枚举只留第一条）
    dedup, dup = {}, 0
    for it in file_items:
        mid = it["media_id"]
        if mid in dedup:
            dup += 1
            continue
        dedup[mid] = it
    all_items = list(dedup.values())

    # 注：REST get_knowledge_list 响应**不含 media_state 字段**（2026-10-18/10-25 实测，全为 None）
    # → 无法在 REST 侧做 state=2 过滤；条目总数与 MCP 根层 knowledge_total_size 对账即可。
    #   state 过滤交由 MCP 侧按需复核；此处按 (2, None) 收全，不丢条目。
    ok_items = [it for it in all_items if it.get("media_state") in (2, None)]
    others = [it for it in all_items if it.get("media_state") not in (2, None)]

    st = Counter(it.get("media_state") for it in all_items)
    mt = Counter(it.get("media_type") for it in ok_items)

    stats = {
        "_mode": "full-no-prune-rest",
        "_date": DATE,
        "_kb_id": KB_REST,
        "_caveat": "REST 不返回 media_state；state 过滤无法在 REST 侧执行，改以总数对账替代",
        "_elapsed_s": round(time.time() - t0, 1),
        "folders_visited": len(seen),
        "file_items_raw": len(file_items),
        "dup_paths": dup,
        "unique_items": len(all_items),
        "parse_success": sum(1 for it in all_items if it.get("media_state") == 2),
        "state_unknown": sum(1 for it in all_items if it.get("media_state") is None),
        "not_success": len(others),
        "media_state_hist": {str(k): v for k, v in st.items()},
        "media_type_hist": {str(k): v for k, v in mt.items()},
        "not_success_detail": [{"media_id": x["media_id"], "title": x["title"],
                                "media_state": x["media_state"]} for x in others],
    }

    out = dict(stats)
    out["root"] = [{"media_id": e.get("media_id"), "title": e.get("title"),
                    "media_type": e.get("media_type"),
                    "folder_info": {"folder_id": e.get("media_id"),
                                    "file_number": e.get("file_number", 0),
                                    "folder_number": e.get("folder_number", 0),
                                    "parent_folder_id": ""}}
                   for e in root if is_folder(e)]
    out["items"] = ok_items
    out["folders"] = folders

    p = os.path.join(ROOT, ".tools", f"_ima_enum_full_{DATE}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    if os.path.exists(SNAP):
        os.remove(SNAP)

    print(f"\n遍历文件夹 {len(seen)} · 原始文件条目 {len(file_items)} · 去重后 {len(all_items)}"
          f" · 重复路径 {dup}")
    print(f"media_state 解析成功 {stats['parse_success']} · 状态未知(REST 未返回) {stats['state_unknown']}")
    print(f"媒体类型分布 {dict(sorted(mt.items(), key=lambda x: -x[1]))}")
    print(f"耗时 {stats['_elapsed_s']}s")
    print(f"\n→ {p}")
    for x in others[:20]:
        print("  ! 非解析成功:", x["media_id"][:40], x["media_state"], x["title"][:60])


if __name__ == "__main__":
    main()
