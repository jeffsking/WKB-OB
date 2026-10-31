#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-31 通道 A/B 抓取：3 条新增条目。

1) 两份 markdown（PEG 基 slot die 复配乳液技术方案）→ get_media_info 原件直下（不吃配额）
2) 一份 wechatarticle（NC 盐调控氢键网络）→ get_media_info 取 mp.weixin 链接 → curl(Chrome UA + Referer) → 抽 #js_content

铁律：响应体先落盘再解析；微信须校验 #js_content 存在（18KB 反爬空壳会伪成功）；urllib 抓微信可能 SSL:UNEXPECTED_EOF → 换 curl。
"""
import json
import os
import re
import subprocess
import urllib.request
from html import unescape

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
KDIR = ".tools/_media_info_20261031"
OUTDIR = ".tools/_fetch_out_20261031"
os.makedirs(KDIR, exist_ok=True)
os.makedirs(OUTDIR, exist_ok=True)

MD = [
    ("markdown_3867e2b60070d7dc3f413086d0b0036e_49240900fa45de87fba84f5c102fc290001a693ee6c0644e", "peg_general"),
    ("markdown_3867e2b60070d7dc3f413086d0b0036e_3bb235881e629b6e72a4b2a94d21ab15001a693ee6c0644e", "peg_knight_iv"),
]
WX = [("wechatarticle_3867e2b60070d7dc3f413086d0b0036e_47b652bdde6ef08fa72bc6e041e28a3c", "nc_lce_mechanochromic")]
UA = ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
      "(KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36")


def creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


def post(path, payload, cid, key):
    req = urllib.request.Request(
        BASE + "/" + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={"ima-openapi-clientid": cid, "ima-openapi-apikey": key,
                 "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=90) as r:
        return json.loads(r.read().decode("utf-8", "replace"))


def media_info(mid, cid, key):
    p = os.path.join(KDIR, mid + ".json")
    if os.path.exists(p):
        return json.load(open(p, encoding="utf-8"))["data"]
    d = post("openapi/wiki/v1/get_media_info", {"media_id": mid}, cid, key)
    with open(p, "w", encoding="utf-8") as f:
        json.dump(d, f, ensure_ascii=False, indent=1)
    if d.get("code") != 0:
        raise RuntimeError(f"get_media_info code={d.get('code')} msg={d.get('message')}")
    return d["data"]


def strip_html(html):
    html = re.sub(r"(?is)<(script|style|svg)[^>]*>.*?</\1>", " ", html)
    html = re.sub(r"(?i)<br\s*/?>", "\n", html)
    html = re.sub(r"(?i)</(p|div|section|h1|h2|h3|li|tr|blockquote)>", "\n", html)
    txt = re.sub(r"(?s)<[^>]+>", "", html)
    txt = unescape(txt)
    lines = [re.sub(r"[ \t\u00a0]+", " ", ln).strip() for ln in txt.splitlines()]
    return "\n".join([ln for ln in lines if ln])


def main():
    cid, key = creds()

    # ---- markdown 原件直下 ----
    for mid, tag in MD:
        d = media_info(mid, cid, key)
        ui = d["url_info"]
        headers = {**ui.get("headers", {}), "User-Agent": UA}
        req = urllib.request.Request(ui["url"], headers=headers)
        with urllib.request.urlopen(req, timeout=180) as r:
            b = r.read()
        raw = os.path.join(OUTDIR, tag + ".raw")
        with open(raw, "wb") as f:
            f.write(b)
        t = b.decode("utf-8", "replace")
        with open(os.path.join(OUTDIR, tag + ".md"), "w", encoding="utf-8") as f:
            f.write(t)
        print(f"[md] {tag} bytes={len(b)} chars={len(t)} head={t[:100]!r}")

    # ---- 微信（curl 绕 SSL/反爬）----
    for mid, tag in WX:
        d = media_info(mid, cid, key)
        url = d["url_info"]["url"]
        print(f"[wx] {tag} url={url[:80]}")
        html_path = os.path.join(OUTDIR, tag + ".html")
        cmd = ["curl", "-sL", "--max-time", "120", "-o", html_path,
               "-H", f"User-Agent: {UA}",
               "-H", "Referer: https://mp.weixin.qq.com/",
               "-H", "Accept-Language: zh-CN,zh;q=0.9", url]
        subprocess.run(cmd, check=False)
        if not os.path.exists(html_path):
            print(f"[wx] {tag} 下载失败（无文件）")
            continue
        html = open(html_path, encoding="utf-8", errors="replace").read()
        has = 'id="js_content"' in html
        print(f"[wx] {tag} bytes={len(html)} js_content={has}")
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
