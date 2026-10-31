#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-26 通道 B：6 条新增 pdf 原件下载（get_media_info，不吃 REST 日配额）。

落盘：RAW_FULL/<同相对目录>/attachments/<原文件名>
铁律：RAW/ 只读，一律不写；下载成功即写 RAW_FULL 占位壳（extract_status: original-only）。
"""
import json
import os
import re
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
STATE = ".tools/_ima_sync_state.json"


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
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8"))


def main():
    s = json.load(open(STATE, encoding="utf-8"))
    items = s["items"]
    todo = [(m, it) for m, it in items.items()
            if it.get("stage") == "discovered" and m.startswith("pdf_") and it.get("raw_path")]
    print(f"待下载 {len(todo)} 条")
    for mid, it in todo:
        title = it["title"]
        r = post("openapi/wiki/v1/get_media_info", {"media_id": mid})
        if r.get("code") != 0:
            print(f"  ! {title[:40]} code={r.get('code')} msg={r.get('msg') or r.get('message')}")
            continue
        ui = (r.get("data") or {}).get("url_info") or {}
        url = ui.get("url") or ""
        if not url:
            print(f"  ! {title[:40]} 无下载 URL")
            continue
        # 断言 URL 与本条 media_id 对得上（防串号，2026-10-23 踩坑）
        tail = mid.split("_")[-1][-16:]
        if tail not in url and mid.split("_")[-1] not in url:
            print(f"  ~ {title[:40]} URL 未含 media_id 片段（继续，仅提示）")
        hdrs = {k: v for k, v in (ui.get("headers") or {}).items()}
        req = urllib.request.Request(url, headers=hdrs)
        with urllib.request.urlopen(req, timeout=300) as resp:
            data = resp.read()
            ctype = resp.headers.get("Content-Type", "")
        rel = it["raw_path"][len("RAW/"):]                      # ima_sync/.../x.pdf.md
        d = os.path.dirname(rel)
        stem = os.path.splitext(os.path.basename(rel))[0]       # x.pdf
        att = os.path.join("RAW_FULL", d, "attachments")
        os.makedirs(att, exist_ok=True)
        ext = ".pdf" if (stem.lower().endswith(".pdf") or "pdf" in ctype) else ""
        name = stem if stem.lower().endswith(".pdf") else stem + ext
        fp = os.path.join(att, name)
        with open(fp, "wb") as f:
            f.write(data)
        print(f"  + {title[:45]} -> {fp} ({len(data)} B, {ctype})")
        # 写 RAW_FULL 占位壳
        full = "RAW_FULL/" + rel
        os.makedirs(os.path.dirname(full), exist_ok=True)
        fm = "\n".join([
            "---",
            f'media_id: "{mid}"',
            'extract_status: "original-only"',
            'extract_channel: "B"',
            'synced_at: "2026-10-26T18:30:00+08:00"',
            f'source_path: "{it["raw_path"]}"',
            f"media_type: {it.get('media_type') or 1}",
            f'original_path: "{it["raw_path"]}"',
            f'original_file: "{fp.replace(chr(92), "/")}"',
            "---",
            "",
            f"# {title}",
            "",
            f"原件已下载：`{fp}`（{len(data)} B）。文字层见同目录 attachments。",
            "",
        ])
        open(full, "w", encoding="utf-8").write(fm)


if __name__ == "__main__":
    main()
