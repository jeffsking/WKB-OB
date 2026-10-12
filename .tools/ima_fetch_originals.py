#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""IMA 原件下载通道（方案 C 扩展项）

场景：部分条目（图纸类图片、扫描件 PDF、pptx/docx）在 IMA 侧**没有可提取的文字层**，
      MCP `fetch_media_content` 只能拿到空壳 → 正文回填通道失效。
      这些条目必须走**原件下载**：get_media_info 取带签名的下载 URL，再 GET 保存原文件。

落盘位置：RAW_FULL/<原条目所在目录>/attachments/<标题>-<hash>.<ext>
          （RAW/ 是插件维护 + AI 只读红线，一律不写）

幂等：目标文件已存在则跳过。

用法：
  python ima_fetch_originals.py --list          列出待下载条目
  python ima_fetch_originals.py --run           执行下载
  python ima_fetch_originals.py --run --limit 3 只下 3 个（试跑）
"""

import argparse
import hashlib
import json
import os
import re
import sys
import urllib.error
import urllib.request

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_FULL = os.path.join(ROOT, "RAW_FULL")
BASE = "https://ima.qq.com"
CRED_DIR = os.path.join(os.path.expanduser("~"), ".config", "ima")

# 值得下载原件的 media_id 前缀（有实体文件、且原件可打开）
DL_PREFIXES = {"img", "pdf", "word", "ppt", "excel"}
EXT_BY_PREFIX = {
    "img": None, "pdf": ".pdf", "word": ".docx", "ppt": ".pptx", "excel": ".xlsx",
}
CT_EXT = {
    "image/jpeg": ".jpg", "image/png": ".png", "image/gif": ".gif",
    "image/webp": ".webp", "image/bmp": ".bmp", "image/tiff": ".tiff",
    "application/pdf": ".pdf",
    "application/vnd.openxmlformats-officedocument.wordprocessingml.document": ".docx",
    "application/vnd.openxmlformats-officedocument.presentationml.presentation": ".pptx",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet": ".xlsx",
    "application/vnd.ms-excel": ".xls",
    "text/csv": ".csv", "text/plain": ".txt", "text/markdown": ".md",
}

MAGIC_EXT = [
    (b"%PDF", ".pdf"),
    (b"\x89PNG", ".png"),
    (b"\xff\xd8\xff", ".jpg"),
    (b"GIF8", ".gif"),
    (b"RIFF", ".webp"),
    (b"BM", ".bmp"),
]


def sniff_bytes(data, fallback=""):
    """按魔数/内容判定扩展名；ZIP 容器区分 docx/xlsx/pptx；文本回退 .csv"""
    for sig, ext in MAGIC_EXT:
        if data.startswith(sig):
            return ext
    if data[:4] == b"PK\x03\x04":
        head = data[:8192]
        for marker, ext in ((b"word/", ".docx"), (b"xl/", ".xlsx"), (b"ppt/", ".pptx")):
            if marker in head:
                return ext
        return ".zip"
    if b"\x00" not in data[:4096]:
        try:
            data[:4096].decode("utf-8")
            return ".csv" if fallback in ("", ".xlsx", ".xls") else fallback
        except UnicodeDecodeError:
            pass
    return fallback


def rename_with_ext(path, ext):
    base = os.path.splitext(path)[0]
    if path.endswith(ext):
        return path
    new = base + ext
    if os.path.exists(new) and os.path.samefile(path, new):
        return path
    os.replace(path, new)
    return new


def cmd_fix_ext():
    """归一化已下载原件：① 去掉早期 <名字>-<hash> 后缀 ② 按魔数纠正扩展名"""
    renamed, fixed = [], []
    for dirpath, _d, files in os.walk(RAW_FULL):
        if os.path.basename(dirpath) != "attachments":
            continue
        for fn in files:
            if fn.lower().endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            cur = os.path.basename(strip_hash_suffix(p))
            if cur != fn:
                renamed.append((fn, cur))
                p = os.path.join(dirpath, cur)
            if not os.path.isfile(p):
                continue
            with open(p, "rb") as f:
                head = f.read(8192)
            ext = sniff_bytes(head, os.path.splitext(cur)[1].lower())
            cur_ext = os.path.splitext(cur)[1].lower()
            if ext and ext != cur_ext:
                new = rename_with_ext(p, ext)
                fixed.append((os.path.basename(p), os.path.basename(new)))
    for a, b in renamed:
        print(f"  [去 hash] {a}  →  {b}")
    for a, b in fixed:
        print(f"  [纠正扩展名] {a}  →  {b}")
    print(f"共归一化 {len(renamed)} 个文件名、{len(fixed)} 个扩展名")

MD_ID = re.compile(r'media_id:\s*"([^"]+)"')
TITLE = re.compile(r'source_file:\s*"([^"]*)"')
O_PATH = re.compile(r'original_path:\s*"([^"]*)"')


def load_creds():
    def rd(n):
        with open(os.path.join(CRED_DIR, n), encoding="utf-8") as f:
            return f.read().strip()
    return rd("client_id"), rd("api_key")


def post(path, payload, cid, key):
    req = urllib.request.Request(
        BASE + "/" + path,
        data=json.dumps(payload).encode("utf-8"),
        headers={
            "ima-openapi-clientid": cid,
            "ima-openapi-apikey": key,
            "Content-Type": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        return json.loads(r.read().decode("utf-8"))


def find_empty_items():
    out = []
    for dirpath, _d, files in os.walk(RAW_FULL):
        for fn in files:
            if not fn.endswith(".md"):
                continue
            p = os.path.join(dirpath, fn)
            try:
                with open(p, encoding="utf-8", errors="replace") as f:
                    t = f.read()
            except OSError:
                continue
            if 'extract_status: "empty"' not in t:
                continue
            m = MD_ID.search(t)
            if not m:
                continue
            mid = m.group(1)
            prefix = mid.split("_")[0] if "_" in mid else ""
            if prefix not in DL_PREFIXES:
                continue
            ttl = TITLE.search(t)
            op = O_PATH.search(t)
            out.append({
                "media_id": mid,
                "prefix": prefix,
                "title": ttl.group(1) if ttl else os.path.splitext(fn)[0],
                "original_path": op.group(1) if op else "",
                "stub_path": os.path.relpath(p, ROOT).replace("\\", "/"),
            })
    out.sort(key=lambda x: x["stub_path"])
    return out


def target_path(item, ext):
    """RAW_FULL/<原目录>/attachments/<原始文件名>（用回原名，便于 Obsidian 直接引用）

    RAW 侧 stub 文件名 = 标题 + '.md'，标题通常已含真实扩展名；
    ext 为按 Content-Type/魔数判定的真实扩展名，若与原名不符则替换。
    """
    orig = item["original_path"]  # RAW/ima_sync/...
    if orig.startswith("RAW/"):
        rel = orig[len("RAW/"):]
    else:
        rel = item["stub_path"]
    d = os.path.dirname(rel)
    name = os.path.splitext(os.path.basename(rel))[0]      # 去掉 .md
    stem, cur = os.path.splitext(name)
    if ext:
        if cur and ext.lower() == cur.lower():
            pass                                            # 原名已正确
        elif cur:
            name = stem + ext                               # 纠正扩展名
        else:
            name = name + ext                               # 原名无扩展名
    safe = re.sub(r'[\\/:*?"<>|]', "-", name)
    return os.path.join(RAW_FULL, d, "attachments", safe)


# 本流水线早期版本残留的 <名字>-<8位hash> 命名
HASHED = re.compile(r"^(?P<root>.+?)-(?P<hash>[0-9a-f]{8})(?P<ext>\.[A-Za-z0-9]{1,6})?$")


def strip_hash_suffix(path):
    fn = os.path.basename(path)
    m = HASHED.match(fn)
    if not m:
        return path
    root, ext = m.group("root"), m.group("ext") or ""
    new = root if root.lower().endswith(ext.lower()) and ext else root + ext
    if new == fn:
        return path
    dest = os.path.join(os.path.dirname(path), new)
    if os.path.exists(dest):
        return path
    os.replace(path, dest)
    return dest


def fetch(url, headers):
    req = urllib.request.Request(url, headers=headers or {}, method="GET")
    with urllib.request.urlopen(req, timeout=300) as r:
        ct = (r.headers.get("Content-Type") or "").split(";")[0].strip().lower()
        return r.read(), ct


def run(limit=None):
    items = find_empty_items()
    cid, key = load_creds()
    ok = skip = fail = 0
    for it in items:
        if limit and ok + fail >= limit:
            break
        try:
            resp = post("openapi/wiki/v1/get_media_info", {"media_id": it["media_id"]}, cid, key)
        except Exception as e:  # noqa: BLE001
            print(f"  [FAIL] get_media_info {it['title'][:36]}: {e}")
            fail += 1
            continue
        if resp.get("code") != 0:
            print(f"  [FAIL] {it['title'][:36]}: code={resp.get('code')} {resp.get('msg')}")
            fail += 1
            continue
        ui = (resp.get("data") or {}).get("url_info") or {}
        url = ui.get("url")
        if not url or url.startswith("chrome://"):
            print(f"  [SKIP] {it['title'][:36]}: 无下载 URL（url_info 为空）")
            skip += 1
            continue
        try:
            data, ct = fetch(url, ui.get("headers"))
        except Exception as e:  # noqa: BLE001
            print(f"  [FAIL] download {it['title'][:36]}: {e}")
            fail += 1
            continue
        # 扩展名优先级：Content-Type → 魔数嗅探 → 前缀默认
        ext = CT_EXT.get(ct) or sniff_bytes(data[:8192], EXT_BY_PREFIX.get(it["prefix"]) or "")
        dest = target_path(it, ext)
        if os.path.isfile(dest):
            print(f"  [SKIP] 已存在 {os.path.basename(dest)}")
            skip += 1
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        with open(dest, "wb") as f:
            f.write(data)
        print(f"  [OK]   {it['title'][:36]}  {len(data)} B  ({ct or '?'})  → {os.path.basename(dest)}")
        ok += 1
    print(f"\n合计 共 {len(items)} 条目标：下载成功 {ok} / 跳过 {skip} / 失败 {fail}")


MANIFEST = os.path.join(ROOT, ".tools", "_ima_originals_manifest.json")


def build_manifest():
    """把「RAW_FULL 侧 extract_status: empty 的 stub」与「已下载的原件」配对成清单，
    供识读代理按图索骥（避免在提示词里手抄路径）。"""
    rows = []
    for dirpath, _d, files in os.walk(RAW_FULL):
        if os.path.basename(dirpath) != "attachments":
            continue
        parent = os.path.dirname(dirpath)
        try:
            siblings = os.listdir(parent)
        except OSError:
            continue
        for fn in siblings:
            if not fn.endswith(".md"):
                continue
            stub = os.path.join(parent, fn)
            with open(stub, encoding="utf-8", errors="replace") as f:
                t = f.read()
            if 'extract_status: "empty"' not in t:
                continue
            m = MD_ID.search(t)
            if not m:
                continue
            mid = m.group(1)
            base = os.path.splitext(fn)[0]
            hit = [a for a in files
                   if a == base or os.path.splitext(a)[0] == base]
            if not hit:
                continue
            rows.append({
                "stub": os.path.relpath(stub, ROOT).replace("\\", "/"),
                "att_rel": os.path.relpath(os.path.join(dirpath, hit[0]), parent).replace("\\", "/"),
                "att_name": hit[0],
                "media_id": mid,
                "prefix": mid.split("_")[0] if "_" in mid else "",
            })
    rows.sort(key=lambda x: (x["prefix"], x["stub"]))
    with open(MANIFEST, "w", encoding="utf-8") as f:
        json.dump(rows, f, ensure_ascii=False, indent=1)
    return rows


def cmd_manifest():
    rows = build_manifest()
    print(f"原件↔stub 清单 {len(rows)} 条 → {os.path.relpath(MANIFEST, ROOT)}")
    for i, r in enumerate(rows):
        print(f"{i:>2} [{r['prefix']:<5}] {r['att_name'][:52]}")
    return rows


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--run", action="store_true")
    ap.add_argument("--limit", type=int)
    ap.add_argument("--fix-ext", action="store_true", help="按魔数修正已下载原件的扩展名")
    ap.add_argument("--manifest", action="store_true", help="生成原件↔stub 配对清单")
    a = ap.parse_args()
    if a.manifest:
        cmd_manifest()
        return
    if a.fix_ext:
        print("修正扩展名：")
        cmd_fix_ext()
        return
    if a.list or not a.run:
        items = find_empty_items()
        print(f"待下载原件 {len(items)} 条")
        for x in items:
            print(f"  [{x['prefix']:<5}] {x['title'][:56]}")
        if not a.run:
            return
    run(a.limit)


if __name__ == "__main__":
    sys.exit(main())
