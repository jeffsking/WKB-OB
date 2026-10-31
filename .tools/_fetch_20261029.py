#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-29 通道 B：原件直下 + 文字抽取（get_media_info，不吃 REST 日配额）。

本批覆盖：markdown(1) / word-docx(1) / soundrecording-m4a(1)
落盘：原件 → RAW_FULL/<同相对目录>/attachments/<原文件名>
      正文 → .tools/_kb_sync_bodies/<media_id>.md（+ .json 元数据）
铁律：RAW/ 只读，绝不写入。
串号防护（2026-10-23 教训）：URL 不含本条 media_id 片段 → 不采信。
录音：m4a 下载后由 Agent 侧 AudioTranscribe 转写，正文另落。
"""
import json
import os
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
PLAN = ".tools/_kb_sync_plan.json"
BODIES = ".tools/_kb_sync_bodies"
os.makedirs(BODIES, exist_ok=True)

TARGETS = sys.argv[1:]  # 可选：限定 media_id 前缀，如 markdown word soundrecording


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


MAGIC = [(b"%PDF", ".pdf"), (b"PK\x03\x04", None),
         (b"\xff\xd8\xff", ".jpg"), (b"\x89PNG", ".png"),
         (b"\x00\x00\x00", ".m4a"), (b"ID3", ".mp3")]


def guess_ext(data, title, ctype):
    if data[:4] == b"\x00\x00\x00" and b"ftyp" in data[:32]:
        return ".m4a"
    for magic, ext in MAGIC:
        if data.startswith(magic):
            if ext:
                return ext
            low = title.lower()
            for e in (".pptx", ".xlsx", ".docx"):
                if low.endswith(e):
                    return e
            if "spreadsheet" in ctype:
                return ".xlsx"
            if "presentation" in ctype:
                return ".pptx"
            return ".docx"
    if "pdf" in ctype:
        return ".pdf"
    if "audio" in ctype or "octet-stream" in ctype:
        return ".m4a"
    low = title.lower()
    for e in (".pptx", ".xlsx", ".docx", ".md", ".m4a"):
        if low.endswith(e):
            return e
    return ""


def ex_docx(fp):
    import zipfile
    import re
    with zipfile.ZipFile(fp) as z:
        xml = z.read("word/document.xml").decode("utf-8", errors="replace")
    xml = re.sub(r"</w:p>", "\n", xml)
    xml = re.sub(r"</w:tr>", "\n", xml)
    xml = re.sub(r"</w:tc>", " | ", xml)
    txt = re.sub(r"<[^>]+>", "", xml)
    txt = txt.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">")
    lines = [ln.strip(" |") for ln in txt.splitlines()]
    return "\n".join(ln for ln in lines if ln.strip())


def main():
    plan = json.load(open(PLAN, encoding="utf-8"))
    report = []
    for it in plan["items"]:
        mid = it["media_id"]
        title = it.get("title") or ""
        mt = it.get("media_type")
        pfx = mid.split("_")[0]
        if TARGETS and pfx not in TARGETS:
            continue
        print(f"\n=== [{mt}] {title}")
        try:
            r = post("openapi/wiki/v1/get_media_info", {"media_id": mid})
        except Exception as e:  # noqa: BLE001
            print(f"  ! get_media_info 失败 {e}")
            report.append({"media_id": mid, "title": title, "error": str(e)[:120]})
            continue
        if r.get("code") != 0:
            msg = f"code={r.get('code')} msg={r.get('msg') or r.get('message')}"
            print(f"  ! {msg}")
            report.append({"media_id": mid, "title": title, "error": msg})
            continue
        ui = (r.get("data") or {}).get("url_info") or {}
        url = ui.get("url") or ""
        if not url:
            print("  ! 无下载 URL")
            report.append({"media_id": mid, "title": title, "error": "no url"})
            continue
        # 串号断言
        seg = mid.split("_")[-2] if mid.count("_") > 2 else mid
        ok_id = (seg and seg in url) or (mid[-12:] in url)
        hdrs = dict(ui.get("headers") or {})
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdrs),
                                        timeout=600) as resp:
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
        except Exception as e:  # noqa: BLE001
            print(f"  ! 下载失败 {e}")
            report.append({"media_id": mid, "title": title, "error": f"download {e}"[:120]})
            continue
        if not ok_id:
            print(f"  [!] URL 不含 media_id 片段 seg={seg[:14]} —— 串号风险，跳过落盘")
            report.append({"media_id": mid, "title": title,
                           "error": "url-media_id mismatch (串号防护)", "bytes": len(data)})
            continue

        rel = it["raw_path"][len("RAW/"):]
        d = os.path.dirname(rel)
        stem = os.path.splitext(os.path.basename(rel))[0]
        att = os.path.join("RAW_FULL", d, "attachments")
        os.makedirs(att, exist_ok=True)
        ext = guess_ext(data, title, ctype)
        name = stem if (ext and stem.lower().endswith(ext)) else stem + ext
        fp = os.path.join(att, name)
        with open(fp, "wb") as f:
            f.write(data)
        print(f"  + 原件 {len(data)} B {ctype} -> {fp}")

        low = name.lower()
        body, status = "", "ok"
        try:
            if low.endswith(".docx"):
                body = ex_docx(fp)
            elif low.endswith((".md", ".markdown", ".txt")):
                body = data.decode("utf-8", errors="replace")
            elif low.endswith((".m4a", ".mp3", ".wav")):
                body = ""           # 待 Agent 侧 AudioTranscribe
                status = "pending-asr"
        except Exception as e:  # noqa: BLE001
            print(f"  ! 抽取异常 {type(e).__name__}: {e}")
            body = ""

        nchar = len(body.strip())
        if status == "pending-asr":
            print("  * 录音原件已落盘 → 待 AudioTranscribe 转写")
        elif nchar == 0:
            print("  ! 文字层为空 → extract_status=original-only")
            status = "original-only"
        else:
            print(f"  * 抽取 {nchar} 字符")
            with open(os.path.join(BODIES, mid + ".md"), "w", encoding="utf-8") as f:
                f.write(body)
        with open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8") as f:
            json.dump({"media_id": mid, "extract_status": status, "channel": "B",
                       "original_file": fp.replace("\\", "/"),
                       "content_type": ctype, "bytes": len(data),
                       "chars": nchar, "title": title}, f, ensure_ascii=False, indent=1)
        report.append({"media_id": mid, "title": title, "status": status,
                       "bytes": len(data), "chars": nchar, "file": fp.replace("\\", "/")})

    with open(".tools/_dl_report_20261029.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print("\n===== 汇总 =====")
    for r in report:
        print(f"  {r.get('status') or 'ERR':14} {r.get('chars', '')!s:>7} {r['title'][:56]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
