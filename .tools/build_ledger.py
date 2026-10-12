# -*- coding: utf-8 -*-
"""构建全量提取台账：队列 1117 份的实际状态（done / pending / skipped_no_text / empty_body），并汇总排除项"""
import json, os, glob, re

queue = json.load(open('.tools/_extract_queue.json', encoding='utf-8'))
skipped = json.load(open('.tools/_extract_skipped.json', encoding='utf-8'))

# 已确认 IMA 端无正文的条目（无转写的录音 / 源侧未解析的扫描件），不再计入 pending
try:
    no_content = set(json.load(open('.tools/_extract_no_content.json', encoding='utf-8')))
except Exception:
    no_content = set()


def net_len(path):
    """净正文长度：去 front matter / 标题行 / 空白后计。防止「仅 front matter 的空壳」被误判为 done。"""
    t = open(path, encoding='utf-8').read()
    t = re.sub(r'^---\r?\n[\s\S]*?\r?\n---\r?\n', '', t)   # 去 front matter
    t = re.sub(r'^\s*#.*$', '', t, flags=re.M)             # 去标题行
    return len(t.strip())


MIN_NET = 50   # 净正文低于此值视为空壳

ledger = []
n_done = n_nc = n_empty = 0
for q in queue:
    dst = q['dst'].replace('/', os.sep)
    if q['dst'] in no_content:
        ledger.append({**q, 'status': 'skipped_no_text', 'bytes': 0})
        n_nc += 1
        continue
    if not os.path.isfile(dst):
        ledger.append({**q, 'status': 'pending', 'bytes': 0})
        continue
    size = os.path.getsize(dst)
    if net_len(dst) >= MIN_NET:
        ledger.append({**q, 'status': 'done', 'bytes': size})
        n_done += 1
    else:
        # 文件在但正文为空：源侧未解析（扫描件等），不计入 pending，也不计 done
        ledger.append({**q, 'status': 'empty_body', 'bytes': size})
        n_empty += 1

json.dump(ledger, open('.tools/_extract_ledger.json', 'w', encoding='utf-8'),
          ensure_ascii=False, indent=1)

from collections import Counter
print('=== 提取总账 ===')
print('队列总数     :', len(ledger))
print('已完成 done  :', n_done)
print('待处理 pending:', sum(1 for l in ledger if l['status'] == 'pending'))
print('无正文 skipped_no_text:', n_nc)
print('空正文 empty_body    :', n_empty)
print('已排除       :', len(skipped), '（img / 微信图片 / 加密件）')
print()
print('=== 按价值档 x 状态 ===')
for s in sorted({l['score'] for l in ledger}, reverse=True):
    sub = [l for l in ledger if l['score'] == s]
    d = sum(1 for l in sub if l['status'] == 'done')
    print('  score=%-3d  共 %4d，已完成 %3d' % (s, len(sub), d))
print()
print('=== 剩余待处理按类型 ===')
pend = [l for l in ledger if l["status"] == "pending"]
for k, v in Counter(l['type'] for l in pend).most_common():
    print('  %5d  %s' % (v, k))
print()
print('台账已写 .tools/_extract_ledger.json')
