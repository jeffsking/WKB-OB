#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""极简 xlsx → markdown 表格（无 openpyxl 依赖，zipfile + ElementTree）。

支持 sharedStrings 与 inlineStr；输出每 sheet 一个 ## 段落 + pipe 表。
用法： python .tools/_xlsx_dump.py <xlsx> [out.md]
"""
import re
import sys
import zipfile
import xml.etree.ElementTree as ET

NS = "{http://schemas.openxmlformats.org/spreadsheetml/2006/main}"
RNS = "{http://schemas.openxmlformats.org/package/2006/relationships}"


def col_idx(ref):
    m = re.match(r"([A-Z]+)", ref or "")
    if not m:
        return 0
    n = 0
    for ch in m.group(1):
        n = n * 26 + (ord(ch) - 64)
    return n - 1


def main():
    src = sys.argv[1]
    out = sys.argv[2] if len(sys.argv) > 2 else None
    z = zipfile.ZipFile(src)
    names = z.namelist()

    shared = []
    if "xl/sharedStrings.xml" in names:
        root = ET.fromstring(z.read("xl/sharedStrings.xml"))
        for si in root.findall(f"{NS}si"):
            shared.append("".join(t.text or "" for t in si.iter(f"{NS}t")))

    # sheet 名与文件映射
    wb = ET.fromstring(z.read("xl/workbook.xml"))
    rels = {}
    if "xl/_rels/workbook.xml.rels" in names:
        rr = ET.fromstring(z.read("xl/_rels/workbook.xml.rels"))
        for r in rr:
            rels[r.get("Id")] = r.get("Target")
    sheets = []
    for sh in wb.find(f"{NS}sheets"):
        rid = sh.get("{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id")
        tgt = (rels.get(rid, "") or "").lstrip("/")
        if tgt and not tgt.startswith("xl/"):
            tgt = "xl/" + tgt
        sheets.append((sh.get("name"), tgt))

    lines = [f"<!-- source: {src} -->", ""]
    for name, target in sheets:
        if target not in names:
            continue
        root = ET.fromstring(z.read(target))
        data = root.find(f"{NS}sheetData")
        rows = []
        if data is not None:
            for row in data:
                cells = {}
                for c in row.findall(f"{NS}c"):
                    idx = col_idx(c.get("r"))
                    t = c.get("t")
                    v = c.find(f"{NS}v")
                    isel = c.find(f"{NS}is")
                    if t == "s" and v is not None:
                        val = shared[int(v.text)] if v.text and int(v.text) < len(shared) else ""
                    elif t == "inlineStr" and isel is not None:
                        val = "".join(x.text or "" for x in isel.iter(f"{NS}t"))
                    elif v is not None:
                        val = v.text or ""
                    else:
                        val = ""
                    cells[idx] = val.replace("\n", " ").replace("|", "/").strip()
                if cells:
                    width = max(cells) + 1
                    arr = [cells.get(i, "") for i in range(width)]
                    if any(x for x in arr):
                        rows.append(arr)
        if not rows:
            continue
        width = max(len(r) for r in rows)
        rows = [r + [""] * (width - len(r)) for r in rows]
        lines.append(f"## Sheet 工作表: {name}")
        lines.append("")
        lines.append("| " + " | ".join(rows[0]) + " |")
        lines.append("|" + "---|" * width)
        for r in rows[1:]:
            lines.append("| " + " | ".join(r) + " |")
        lines.append("")
    text = "\n".join(lines)
    if out:
        open(out, "w", encoding="utf-8").write(text)
        print(f"written {out} ({len(text)} chars)")
    else:
        sys.stdout.reconfigure(encoding="utf-8")
        print(text)


if __name__ == "__main__":
    main()
