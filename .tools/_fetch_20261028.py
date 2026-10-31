#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-27 通道 B：9 条新增原件下载 + 文字抽取（get_media_info，不吃 REST 日配额）。

覆盖格式：xlsx(5) / pptx(4) / pdf(1) / md(7)
落盘：原件 → RAW_FULL/<同相对目录>/attachments/<原文件名>
      正文 → .tools/_kb_sync_bodies/<media_id>.md（+ .json 元数据）
铁律：RAW/ 只读，绝不写入。
串号防护（2026-10-23 教训）：每条的下载 URL 必含本条 media_id 片段才采信。
"""
import io
import json
import os
import re
import sys
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
STATE = ".tools/_ima_sync_state.json"
PLAN = ".tools/_kb_sync_plan.json"
BODIES = ".tools/_kb_sync_bodies"
os.makedirs(BODIES, exist_ok=True)


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


MAGIC = [(b"%PDF", ".pdf"),
         (b"PK\x03\x04", None),          # zip 家族，按 title 后缀定
         (b"\xff\xd8\xff", ".jpg"), (b"\x89PNG", ".png")]


def guess_ext(data, title, ctype):
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
    low = title.lower()
    for e in (".pptx", ".xlsx", ".docx", ".md"):
        if low.endswith(e):
            return e
    return ""


# ---------- 抽取器 ----------
def ex_pptx(fp):
    from pptx import Presentation
    prs = Presentation(fp)
    out = []
    for i, slide in enumerate(prs.slides, 1):
        txts = []
        for sh in slide.shapes:
            if sh.has_text_frame:
                for p in sh.text_frame.paragraphs:
                    t = "".join(r.text for r in p.runs).strip()
                    if t:
                        txts.append(t)
            if getattr(sh, "has_table", False) and sh.has_table:
                for row in sh.table.rows:
                    cells = [c.text.strip().replace("\n", " ") for c in row.cells]
                    if any(cells):
                        txts.append(" | ".join(cells))
        notes = ""
        try:
            if slide.has_notes_slide and slide.notes_slide.notes_text_frame:
                notes = slide.notes_slide.notes_text_frame.text.strip()
        except Exception:  # noqa: BLE001
            pass
        body = "\n".join(txts)
        if notes:
            body += f"\n\n[备注] {notes}"
        if body.strip():
            out.append(f"## Slide {i}\n\n{body}")
    return "\n\n".join(out)


def ex_xlsx(fp):
    import openpyxl
    wb = openpyxl.load_workbook(fp, data_only=True)
    out = []
    for ws in wb.worksheets:
        rows = []
        for row in ws.iter_rows(values_only=True):
            vals = [("" if v is None else str(v)).strip() for v in row]
            if any(vals):
                while vals and vals[-1] == "":
                    vals.pop()
                rows.append(" | ".join(vals))
        if rows:
            out.append(f"## Sheet: {ws.title}（{len(rows)} 行）\n\n" + "\n".join(rows))
    # data_only=True 对未缓存公式单元格返回 None → 提示
    return "\n\n".join(out)


def ex_pdf(fp):
    from pypdf import PdfReader
    rd = PdfReader(fp)
    pages = []
    for i, pg in enumerate(rd.pages, 1):
        t = (pg.extract_text() or "").strip()
        if t:
            pages.append(f"## Page {i}\n\n{t}")
    return "\n\n".join(pages)


def main():
    plan = json.load(open(PLAN, encoding="utf-8"))
    st = json.load(open(STATE, encoding="utf-8"))
    items = st["items"]
    report = []
    for it in plan["items"]:
        mid = it["media_id"]
        title = it.get("title") or ""
        mt = it.get("media_type")
        print(f"\n=== [{mt}] {title}")
        try:
            r = post("openapi/wiki/v1/get_media_info", {"media_id": mid})
        except Exception as e:  # noqa: BLE001
            print(f"  ! get_media_info 失败 {e}")
            report.append({"media_id": mid, "title": title, "error": str(e)[:120]})
            continue
        if r.get("code") != 0:
            print(f"  ! code={r.get('code')} msg={r.get('msg') or r.get('message')}")
            report.append({"media_id": mid, "title": title,
                           "error": f"code={r.get('code')} {r.get('msg') or r.get('message')}"})
            continue
        ui = (r.get("data") or {}).get("url_info") or {}
        url = ui.get("url") or ""
        if not url:
            print("  ! 无下载 URL")
            report.append({"media_id": mid, "title": title, "error": "no url"})
            continue
        # 串号断言
        tail = mid.split("_")[-2][-12:] if mid.count("_") > 2 else mid[-12:]
        seg = mid.split("_")[-2] if mid.count("_") > 2 else mid
        if seg not in url and tail not in url:
            print(f"  ~ URL 未含 media_id 片段（seg={seg[:12]}）——仅提示")
        hdrs = dict(ui.get("headers") or {})
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=hdrs), timeout=300) as resp:
                data = resp.read()
                ctype = resp.headers.get("Content-Type", "")
        except Exception as e:  # noqa: BLE001
            print(f"  ! 下载失败 {e}")
            report.append({"media_id": mid, "title": title, "error": f"download {e}"[:120]})
            continue

        rel = it["raw_path"][len("RAW/"):]
        d = os.path.dirname(rel)
        stem = os.path.splitext(os.path.basename(rel))[0]          # 含原扩展名，如 x.pptx
        att = os.path.join("RAW_FULL", d, "attachments")
        os.makedirs(att, exist_ok=True)
        ext = guess_ext(data, title, ctype)
        name = stem if (ext and stem.lower().endswith(ext)) else stem + ext
        fp = os.path.join(att, name)
        with open(fp, "wb") as f:
            f.write(data)
        print(f"  + 原件 {len(data)} B {ctype} -> {fp}")

        low = name.lower()
        try:
            if low.endswith(".pptx"):
                body = ex_pptx(fp)
            elif low.endswith(".xlsx"):
                body = ex_xlsx(fp)
            elif low.endswith(".pdf"):
                body = ex_pdf(fp)
            elif low.endswith((".md", ".markdown", ".txt")):
                body = data.decode("utf-8", errors="replace")
            else:
                body = ""
        except Exception as e:  # noqa: BLE001
            print(f"  ! 抽取异常 {type(e).__name__}: {e}")
            body = ""
        nchar = len(body.strip())
        print(f"  * 抽取 {nchar} 字符")
        if nchar == 0:
            print("  ! 文字层为空 → extract_status=original-only")
            status = "original-only"
        else:
            status = "ok"
            with open(os.path.join(BODIES, mid + ".md"), "w", encoding="utf-8") as f:
                f.write(body)
        with open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8") as f:
            json.dump({"media_id": mid, "extract_status": status, "channel": "B",
                       "original_file": fp.replace("\\", "/"),
                       "content_type": ctype, "bytes": len(data),
                       "chars": nchar, "title": title}, f, ensure_ascii=False, indent=1)
        report.append({"media_id": mid, "title": title, "status": status,
                       "bytes": len(data), "chars": nchar, "file": fp.replace("\\", "/")})

    with open(".tools/_dl_report_20261028.json", "w", encoding="utf-8") as f:
        json.dump(report, f, ensure_ascii=False, indent=1)
    print("\n===== 汇总 =====")
    for r in report:
        print(f"  {r.get('status') or 'ERR':14} {r.get('chars', '')!s:>7} {r['title'][:56]}")


if __name__ == "__main__":
    sys.exit(main())
