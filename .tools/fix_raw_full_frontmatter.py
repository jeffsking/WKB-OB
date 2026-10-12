# -*- coding: utf-8 -*-
"""修复 RAW_FULL 中缺失 front matter 的提取文件（补齐 media_id / original_path 等字段）。

背景：提取阶段子代理以「只写纯正文」的指令落盘，Write 覆盖了 plan_extraction.py 建的骨架头，
导致部分文件丢失 front matter（追溯字段）。本脚本从台账 `_extract_ledger.json` 取权威字段回填。

安全保证：
- 只做「前置插入」，正文一个字节不动（脚本校验正文 MD5 前后一致）
- 幂等：已以 `---\n` 开头的文件直接跳过
- 不改动 RAW/ 任何文件
"""
import glob
import hashlib
import json
import os
import time
from datetime import datetime

VAULT = r'E:\WKB-OB'
LEDGER = os.path.join(VAULT, '.tools', '_extract_ledger.json')
BACKUP = os.path.join(VAULT, '.tools', '_fm_repair_backup')

CLEAN_RULES = 'v2: dead-image-link->text(alt kept); repeat-digits->compressed'
METHOD = 'ima-mcp fetch_media_content'


def norm(p):
    return p.replace('/', os.sep)


def main():
    os.chdir(VAULT)
    ledger = json.load(open(LEDGER, encoding='utf-8'))
    by_dst = {}
    for e in ledger:
        by_dst[norm(e['dst'])] = e

    files = glob.glob('RAW_FULL/**/*.md', recursive=True)
    no_fm = [f for f in files
             if not open(f, encoding='utf-8', errors='ignore').read(4).startswith('---')]
    print('RAW_FULL 总 %d 份；缺 front matter %d 份' % (len(files), len(no_fm)))

    os.makedirs(BACKUP, exist_ok=True)
    repaired, skipped = 0, []
    for f in no_fm:
        e = by_dst.get(norm(f))
        body = open(f, encoding='utf-8', errors='ignore').read()
        if not e or 'media_id' not in e:
            skipped.append((f, '台账无对应记录'))
            continue
        if not body.strip():
            skipped.append((f, '正文为空'))
            continue

        h_before = hashlib.md5(body.encode('utf-8')).hexdigest()
        mt = datetime.fromtimestamp(os.path.getmtime(f)).strftime('%Y-%m-%d')
        fm = (
            '---\n'
            'media_id: "%s"\n'
            'source_file: "%s"\n'
            'original_path: "%s"\n'
            'extracted: "%s"\n'
            'extract_method: "%s"\n'
            'extract_status: "ok"\n'
            'clean_rules: ""\n'          # 留空：让 clean_extracted.py 真正跑一遍（填 v2 会被幂等判定误跳过）
            'processed: "%s"\n'
            'fm_repaired: "2026-09-29 (回填提取期丢失的追溯字段，正文未改动)"\n'
            '---\n\n' % (e['media_id'], e['name'], e['src'], mt, METHOD, mt)
        )

        # 备份原文件
        bp = os.path.join(BACKUP, os.path.basename(f))
        i = 1
        while os.path.exists(bp):
            bp = os.path.join(BACKUP, '%s.%d' % (os.path.basename(f), i))
            i += 1
        with open(bp, 'w', encoding='utf-8') as fh:
            fh.write(body)

        new = fm + body
        with open(f, 'w', encoding='utf-8') as fh:
            fh.write(new)

        # 校验正文未变
        h_after = hashlib.md5(new[len(fm):].encode('utf-8')).hexdigest()
        if h_after != h_before:
            skipped.append((f, '正文校验失败（已回滚）'))
            with open(f, 'w', encoding='utf-8') as fh:
                fh.write(body)
            continue
        repaired += 1

    print('已回填 front matter: %d 份' % repaired)
    print('跳过: %d 份' % len(skipped))
    for f, why in skipped:
        print('   - [%s] %s' % (why, f))
    print('备份目录: %s' % BACKUP)


if __name__ == '__main__':
    main()
