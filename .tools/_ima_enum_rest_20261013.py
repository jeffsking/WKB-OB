#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""临时枚举器（2026-10-13）：本会话无 IMA MCP connector → REST 只读兜底。
递归枚举整库（get_knowledge_list），落 .tools/_ima_enum_<date>.json。
契约 {"root":[...],"items":[...]}。
REST 子层参数名 = folder_id（非 parent_folder_id）。
"""
import json
import os
import sys
import time
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
KB_REST = "F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI="
DATE = "20261013"


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
    for attempt in range(4):
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode("utf-8"))
        except urllib.error.HTTPError as e:  # noqa
            if attempt == 3:
                raise
            time.sleep(6)
        except Exception:  # noqa
            if attempt == 3:
                raise
            time.sleep(6)


def list_folder(folder_id):
    """枚举一个 folder 下全部条目（自动翻页）。folder_id 为 None 表示根层。"""
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
        time.sleep(0.3)
    return out


def is_folder(e):
    return e.get("media_type") == 99 or str(e.get("media_id", "")).startswith("folder_")


def main():
    items = []
    folders = []
    # 根层
    root = list_folder(None)
    items.extend(root)
    print(f"root: {len(root)}")
    # BFS 递归
    queue = [(e["media_id"], e.get("title", "")) for e in root if is_folder(e)]
    seen = set()
    while queue:
        fid, chain = queue.pop(0)
        if fid in seen:
            continue
        seen.add(fid)
        sub = list_folder(fid)
        print(f"  folder {chain} ({fid}): {len(sub)}")
        items.extend(sub)
        for e in sub:
            if is_folder(e):
                queue.append((e["media_id"], chain + "/" + e.get("title", "")))
        time.sleep(0.3)

    # 归一：给每条补 kb_path 提示（文件夹链+标题），parent_folder_id
    out = {"_mode": "daily-incremental-rest", "_date": DATE,
           "root": root, "items": items}
    p = os.path.join(ROOT, ".tools", f"_ima_enum_{DATE}.json")
    with open(p, "w", encoding="utf-8") as f:
        json.dump(out, f, ensure_ascii=False, indent=1)
    print(f"\n总枚举 {len(items)} 条 → {p}")


if __name__ == "__main__":
    main()
