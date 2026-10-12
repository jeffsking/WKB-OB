# -*- coding: utf-8 -*-
"""全量递归枚举 IMA 知识库（REST 兜底通道）。

MCP ima-mcp 未接入本会话时使用 REST openapi/wiki/v1/get_knowledge_list 递归整库。
不做 file_number 剪枝 —— 全量对账必须递归整库。

输出契约：{"root":[...],"items":[...]}
  root  : 根层文件夹条目（含 folder_info 占位）
  items : 所有非文件夹条目（media_type != 99），含 media_id/media_type/title/create_time/kb_path/parent_folder_id

REST 通道限制（已知）：
  - 无 media_state 字段 → 无法按 PARSE_SUCCESS 过滤（本脚本全量收录，由账本侧自然判定）
  - 无 create_time 字段 → 写空串（账本侧 create_ts 记为 None）
  - folder_info.file_number 为 null → 本脚本自行递归，不用剪枝
"""
import json
import subprocess
import sys
import time
from pathlib import Path

KB_ID_REST = "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="
IMA_CJS = r"C:\Users\Chris Wang\.workbuddy\skills\ima-skill\ima_api.cjs"
OUT = Path(r"E:\WKB-OB\.tools\_ima_enum_full_%s.json" % time.strftime("%Y%m%d"))


def call(payload, retries=4):
    for attempt in range(retries):
        p = subprocess.run(
            ["node", IMA_CJS, "openapi/wiki/v1/get_knowledge_list", json.dumps(payload, ensure_ascii=False)],
            capture_output=True, text=True, encoding="utf-8", cwd=str(Path(IMA_CJS).parent),
        )
        out = (p.stdout or "").strip()
        try:
            d = json.loads(out)
        except Exception:
            sys.stderr.write("BAD JSON: %s\n" % out[:300])
            time.sleep(8)
            continue
        code = d.get("code")
        if code == 0:
            return d["data"]
        if code == 200001:  # 频率超限
            sys.stderr.write("rate limit, sleep 9s\n")
            time.sleep(9)
            continue
        if code == 200005:
            raise SystemExit("get_doc_content 日配额耗尽 200005（枚举非该端点，异常）: %s" % out[:200])
        sys.stderr.write("code=%s msg=%s\n" % (code, d.get("msg")))
        time.sleep(6)
    raise RuntimeError("call failed after %d retries: %s" % (retries, payload))


def list_folder(folder_id, path, items, folders, root_marker):
    cursor = ""
    while True:
        payload = {"knowledge_base_id": KB_ID_REST, "limit": 50, "cursor": cursor}
        if folder_id:
            payload["folder_id"] = folder_id
        data = call(payload)
        kl = data.get("knowledge_list") or []
        for it in kl:
            mid = it.get("media_id")
            mtype = it.get("media_type")
            title = it.get("title") or ""
            if mtype == 99:  # folder
                child_path = (path + "/" + title) if path else title
                folders.append({
                    "media_id": mid,
                    "media_type": 99,
                    "title": child_path,
                    "folder_info": {"folder_id": mid, "name": title,
                                    "file_number": None, "folder_number": None,
                                    "parent_folder_id": it.get("parent_folder_id") or ""},
                })
                if not root_marker:
                    list_folder(mid, child_path, items, folders, False)
                else:
                    root_marker[title] = mid
            else:
                rel = (path + "/" + title) if path else title
                items.append({
                    "media_id": mid,
                    "media_type": mtype,
                    "title": title,
                    "create_time": "",
                    "kb_path": rel,
                    "parent_folder_id": it.get("parent_folder_id") or "",
                })
        if data.get("is_end") or not data.get("next_cursor"):
            break
        cursor = data["next_cursor"]
        time.sleep(1)


def main():
    items, folders = [], []
    # 根层：先只列根层条目，收集文件夹，再逐个递归
    root_payload = {"knowledge_base_id": KB_ID_REST, "limit": 50, "cursor": ""}
    root_items = []
    data = call(root_payload)
    for it in (data.get("knowledge_list") or []):
        if it.get("media_type") == 99:
            root_items.append(it)
        else:
            items.append({
                "media_id": it.get("media_id"), "media_type": it.get("media_type"),
                "title": it.get("title") or "", "create_time": "",
                "kb_path": it.get("title") or "", "parent_folder_id": it.get("parent_folder_id") or "",
            })
    for f in root_items:
        mid = f.get("media_id")
        title = f.get("title") or ""
        folders.append({
            "media_id": mid, "media_type": 99, "title": title,
            "folder_info": {"folder_id": mid, "name": title, "file_number": None,
                            "folder_number": None, "parent_folder_id": ""},
        })
        list_folder(mid, title, items, folders, False)

    result = {
        "root": [{"media_id": f["media_id"], "media_type": 99, "title": f["title"],
                  "create_time": "", "folder_info": f["folder_info"]} for f in folders if "/" not in f["title"]],
        "items": items,
        "_source": "REST openapi/wiki/v1/get_knowledge_list 全量递归 @%s（MCP 未接入兜底）" % time.strftime("%Y-%m-%d"),
        "_folders_all": folders,
    }
    OUT.write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    print("folders=%d items=%d -> %s" % (len(folders), len(items), OUT))


if __name__ == "__main__":
    main()
