#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""2026-10-23 通道 B/C 抓取：markdown 原件 + 录音 m4a + 微信公众号正文。

- markdown：get_media_info 签名 URL 直下 → 原样写入暂存（作为正文）
- 录音：get_media_info 签名 URL 下 m4a → 保存到 RAW_FULL/attachments；正文由 AudioTranscribe 另行产出
- 公众号：URL 即原文链接 → urllib 抓 HTML → 抽 #js_content 文本

落盘：暂存正文 .tools/_kb_sync_bodies/<media_id>.md（供 kb_sync_handler apply 使用）
      m4a 原件 RAW_FULL/<目录>/attachments/<title>.m4a
"""
import hashlib
import json
import os
import re
import sys
import time
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CRED = os.path.join(os.path.expanduser("~"), ".config", "ima")
BASE = "https://ima.qq.com"
BODIES = os.path.join(ROOT, ".tools", "_kb_sync_bodies")
INFO = os.path.join(ROOT, ".tools", "_media_info_20261023")
os.makedirs(BODIES, exist_ok=True)

PLAN = os.path.join(ROOT, ".tools", "_kb_sync_plan.json")


def load_creds():
    def rd(n):
        with open(os.path.join(CRED, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


CID, KEY = load_creds()


CACHE = {}


def media_info(mid):
    """一律现取（不缓存跨条目），避免「签名 URL 误命中他条目」——2026-10-23 已踩。"""
    if mid in CACHE:
        return CACHE[mid]
    payload = {"media_id": mid}
    req = urllib.request.Request(
        BASE + "/openapi/wiki/v1/get_media_info",
        data=json.dumps(payload).encode("utf-8"),
        headers={"ima-openapi-clientid": CID, "ima-openapi-apikey": KEY,
                 "Content-Type": "application/json"},
        method="POST")
    with urllib.request.urlopen(req, timeout=60) as r:
        body = r.read()
    p = os.path.join(INFO, "fresh_" + hashlib.md5(mid.encode()).hexdigest()[:8] + ".json")
    with open(p, "wb") as f:
        f.write(body)
    d = json.loads(body.decode("utf-8"))
    # 自证：返回 URL 必须携带本条目 media_id（防串号）
    u = ((d.get("data") or {}).get("url_info") or {}).get("url", "")
    if "media_id=" in u and mid not in u:
        raise RuntimeError(f"URL media_id 不匹配: want={mid[:30]} got={u[:120]}")
    CACHE[mid] = d
    return d


def http_get(url, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=120) as r:
        return r.read(), r.headers.get("Content-Type", "")


def download_original(mid, dst_dir_hint, ext_hint):
    d = media_info(mid)
    info = (d.get("data") or {}).get("url_info") or {}
    url = info.get("url") or ""
    hdrs = info.get("headers") or {}
    if not url:
        raise RuntimeError("no url: " + json.dumps(d, ensure_ascii=False)[:200])
    body, ct = http_get(url, hdrs)
    return body, ct, url


def wechat_text(url):
    html, ct = http_get(url, {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
    s = html.decode("utf-8", errors="ignore")
    m = re.search(r'<div class="rich_media_content[^"]*"[^>]*id="js_content"[^>]*>(.*?)</div>\s*(?:<script|<div class="rich_media_tool)', s, re.S)
    if not m:
        m = re.search(r'id="js_content"[^>]*>(.*?)</div>', s, re.S)
    body = m.group(1) if m else s
    body = re.sub(r"<script.*?</script>", "", body, flags=re.S)
    body = re.sub(r"<style.*?</style>", "", body, flags=re.S)
    body = re.sub(r"<br\s*/?>", "\n", body)
    body = re.sub(r"</p>|</section>|</h\d>", "\n\n", body)
    body = re.sub(r"<[^>]+>", "", body)
    body = (body.replace("&nbsp;", " ").replace("&amp;", "&").replace("&lt;", "<")
            .replace("&gt;", ">").replace("&quot;", '"').replace("&#39;", "'"))
    body = re.sub(r"\n{3,}", "\n\n", body)
    return body.strip()


def main():
    plan = json.load(open(PLAN, encoding="utf-8"))
    only = set(sys.argv[1:])
    for it in plan["items"]:
        mid = it.get("media_id") or ""
        title = it.get("title") or ""
        mt = it.get("media_type")
        raw = it.get("raw_path") or ""
        if only and title not in only:
            continue
        if mt == 7:
            body, ct, url = download_original(mid, raw, ".md")
            txt = body.decode("utf-8", errors="ignore")
            p = os.path.join(BODIES, mid + ".md")
            with open(p, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"[md] {title[:34]} · {len(txt)} 字 · ct={ct[:30]} → {p}")
            json.dump({"extract_status": "ok", "channel": "B-markdown-original",
                       "content_type": ct, "chars": len(txt)},
                      open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
        elif mt == 6:
            d = media_info(mid)
            url = ((d.get("data") or {}).get("url_info") or {}).get("url", "")
            txt = wechat_text(url)
            p = os.path.join(BODIES, mid + ".md")
            with open(p, "w", encoding="utf-8") as f:
                f.write(txt)
            print(f"[wx] {title[:34]} · {len(txt)} 字 · src={url[:50]} → {p}")
            json.dump({"extract_status": "ok" if len(txt) > 300 else "empty",
                       "channel": "B-wechat-html", "source_url": url, "chars": len(txt)},
                      open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)
        elif mt == 15:
            body, ct, url = download_original(mid, raw, ".m4a")
            rel = raw.replace("RAW/", "").replace(".md", "")
            dst = os.path.join(ROOT, "RAW_FULL", os.path.dirname(rel), "attachments",
                               os.path.basename(rel) + ".m4a")
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "wb") as f:
                f.write(body)
            print(f"[rec] {title[:34]} · {len(body):,} B → {dst}")
            json.dump({"extract_status": "pending_transcribe", "channel": "B-recording-m4a",
                       "audio_path": dst, "bytes": len(body)},
                      open(os.path.join(BODIES, mid + ".json"), "w", encoding="utf-8"),
                      ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main()
