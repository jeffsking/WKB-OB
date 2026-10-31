# -*- coding: utf-8 -*-
"""下载今日 markdown 原件 + 录音 m4a 到 .tools/_dl_20261022/（不写 RAW/）。"""
import json, os, urllib.request, time
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, ".tools", "_dl_20261022")
probe = json.load(open(os.path.join(ROOT, ".tools", "_media_probe_20261022.json"), encoding="utf-8"))
def fetch(url, headers):
    hdr = {}
    if isinstance(headers, dict):
        hdr = dict(headers)
    elif isinstance(headers, list):
        for h in headers:
            if isinstance(h, dict):
                hdr[h.get("key") or h.get("name")] = h.get("value")
    req = urllib.request.Request(url, headers=hdr)
    with urllib.request.urlopen(req, timeout=300) as r:
        return r.read(), (r.headers.get("Content-Type") or "")
report = {}
for i, (mid, r) in enumerate(probe.items()):
    ui = (r.get("data") or {}).get("url_info") or {}
    url = ui.get("url") or ""
    pfx = mid.split("_")[0]
    if pfx == "note":
        report[mid] = {"skip": "chrome:// 不可下载"}
        continue
    ext = ".md" if pfx == "markdown" else ".m4a"
    try:
        data, ct = fetch(url, ui.get("headers"))
    except Exception as e:
        report[mid] = {"err": str(e)}
        print("[FAIL]", mid[:40], e)
        continue
    p = os.path.join(OUT, mid + ext)
    with open(p, "wb") as f:
        f.write(data)
    report[mid] = {"bytes": len(data), "ct": ct, "path": p}
    print(f"[OK] {pfx:<16} {len(data):>9} B  {mid[-24:]}")
    time.sleep(1.5)
json.dump(report, open(os.path.join(ROOT, ".tools", "_dl_report_20261022.json"), "w", encoding="utf-8"),
          ensure_ascii=False, indent=1)
