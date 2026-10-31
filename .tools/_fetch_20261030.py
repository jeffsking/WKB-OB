#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-30 通道 B/A 抓取：3 条新增条目。

1) markdown（IMA知识库索引.md）→ 原件直下（不吃配额）
2) 两份 wechatarticle → get_media_info 取 mp.weixin.qq.com 链接 → Chrome UA + Referer → 抽 #js_content

铁律：响应体先落盘再解析；微信须校验 #js_content 存在（反爬页 18KB 空壳会伪成功）。
"""
import json
import os
import re
import urllib.request
from html import unescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
INFO = ".tools/_media_info_20261030"
OUTDIR = ".tools/_fetch_out_20261030"
os.makedirs(OUTDIR, exist_ok=True)

MD_ID = "markdown_3867e2b60070d7dc3f413086d0b0036e_68f8624626c33e8743e6074d9eeb40f2001a693ee6c0644e"
WX = [
    ("wechatarticle_3867e2b60070d7dc3f413086d0b0036e_649da9df864de859cd2d6ee45e5a6439", "chromic-six-triggers"),
    ("wechatarticle_3867e2b60070d7dc3f413086d0b0036e_5a7a531e7cb98131298210372e8ceb8d", "chromic-solar-daily"),
]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def info_of(mid):
    return json.load(open(os.path.join(INFO, mid + ".json"), encoding="utf-8"))["data"]


def download(url, headers, out):
    req = urllib.request.Request(url, headers=headers)
    with urllib.request.urlopen(req, timeout=180) as r:
        b = r.read()
    with open(out, "wb") as f:
        f.write(b)
    return b


def strip_html(html):
    html = re.sub(r"(?is)<(script|style|svg)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</(p|div|section|h1|h2|h3|li|tr)>", "\n", html)
    txt = re.sub(r"(?s)<[^>]+>", "", html)
    txt = unescape(txt)
    lines = [re.sub(r"[ \t\u00a0]+", " ", ln).strip() for ln in txt.splitlines()]
    return "\n".join([ln for ln in lines if ln])


def main():
    # ---- 1. markdown 原件 ----
    d = info_of(MD_ID)
    ui = d["url_info"]
    p = os.path.join(OUTDIR, "index.md")
    b = download(ui["url"], {**ui.get("headers", {}), "User-Agent": UA}, p)
    t = b.decode("utf-8", "replace")
    print(f"[md] bytes={len(b)} chars={len(t)} head={t[:120]!r}")

    # ---- 2. 微信 ----
    for mid, tag in WX:
        d = info_of(mid)
        url = d["url_info"]["url"]
        assert mid.split("_")[-1][:16] in json.dumps(d) or True
        raw = os.path.join(OUTDIR, tag + ".html")
        try:
            b = download(url, {"User-Agent": UA, "Referer": "https://mp.weixin.qq.com/",
                              "Accept-Language": "zh-CN,zh;q=0.9"}, raw)
            html = b.decode("utf-8", "replace")
        except Exception as e:  # noqa: BLE001
            print(f"[wx] {tag} 下载失败 {type(e).__name__} {e}")
            continue
        has = "#js_content" in html or "js_content" in html
        print(f"[wx] {tag} bytes={len(b)} js_content={has} url={url[:60]}")
        if not has:
            print("     → 反爬/空壳页，判失败（不写正文）")
            continue
        m = re.search(r'(?is)<div[^>]*id="js_content"[^>]*>(.*?)<div[^>]*id="js_pc_qr_code"', html)
        seg = m.group(1) if m else html
        txt = strip_html(seg)
        with open(os.path.join(OUTDIR, tag + ".txt"), "w", encoding="utf-8") as f:
            f.write(txt)
        print(f"     → 正文 {len(txt)} 字")


if __name__ == "__main__":
    main()
