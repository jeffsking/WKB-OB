#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""临时枚举器（2026-10-17）：本会话无 IMA MCP connector → REST 只读兜底。

递归枚举整库（openapi/wiki/v1/get_knowledge_list），落 .tools/_ima_enum_<date>.json。
契约 {"root":[...],"items":[...]}，条目含 kb_path（文件夹链+标题）。
REST 子层参数名 = folder_id（非 parent_folder_id）。
限频治理（2026-10-15 教训）：请求间隔 2.5s + 单次失败 sleep 12s 退避。
folder 条目（media_type=99）在源头剔除，只进 folders 字典。
"""
import json
import os
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
KB_REST = "ima_kb_l24tiCGM"
DATE = "20261022"


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
        time.sleep(2.5)
    return out


def is_folder(e):
    return e.get("media_type") == 99 or str(e.get("media_id", "")).startswith("folder_")


def main():
    items = []
    folders = []
    root = list_folder(None)
    items.extend(root)
    print(f"root: {len(root)}")
    queue = [(e["media_id"], e.get("title", "")) for e in root if is_folder(e)]
    seen = set()
    while queue:
        fid, chain = queue.pop(0)
        if fid in seen:
            continue
        seen.add(fid)
        sub = list_folder(fid)
        print(f"  folder {chain} ({fid}): {len(sub)}")
        for e in sub:
            e["_kb_chain"] = chain
        items.extend(sub)
        for e in sub:
            if is_folder(e):
                queue.append((e["media_id"], chain + "/" + e.get("title", "")))
        time.sleep(2.5)

    file_items = []
    for e in items:
        if is_folder(e):
            folders.append({"media_id": e.get("media_id"), "title": e.get("title"),
                            "chain": e.get("_kb_chain", ""),
                            "file_number": e.get("file_number"),
                            "folder_number": e.get("folder_number")})
            continue
        chain = e.pop("_kb_chain", "")
        title = e.get("title", "")
        e["kb_path"] = (chain + "/" + title) if chain else title
        file_items.append(e)

    print(f"\n剔除 folder 条目 {len(items) - len(file_items)} 条 · 文件条目 {len(file_items)} 条")
    out = {"_mode": "daily-incremental-rest", "_date": DATE,
           "root": root, "items": file_items, "folders": folders}
    p = os.path.join(ROOT, ".tools", f"_ima_enum_{DATE}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n总枚举 {len(items)} 条 → {p}")


if __name__ == "__main__":
    main()
