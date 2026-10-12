# -*- coding: utf-8 -*-
r"""WKB 判重权威工具 —— 唯一合法的「已编译」判定入口。

用法：
  python .tools/wkb_dedup.py scan            # 全库对账：报出真实未编译清单
  python .tools/wkb_dedup.py check <相对路径>  # 判定单条是否已编译

背景：2026-10-11 三度出现「已编译却报未编译」的假欠账。根因全在判读侧：
  ① 只查单值source_path，漏掉 source_paths 多值与跨条目合并页（漏判 12 条）
  ② 正则用 \s* 贪婪吞换行，导致全库 912 个已登记路径一条都匹配不到
  ③ 跨文件判重只看 sha1，漏掉 sha1 不同但内容近似的副本
本脚本把正确判定固化为唯一入口，禁止再手写一次性脚本。

判重锚设计意图（2026-09-30 立规，2026-10-11 复核确认）：
  09-30 只读对账发现同一资料曾因 RAW/ 与 RAW_FULL/ 双路径导致漏判 → 重同步重复编译，
  故统一锚到 RAW 侧单一路径：source_path 一律指 RAW/，RAW_FULL 只作编译输入。
  本脚本的 3 形态扩展（多值 source_paths / 跨条目合并页）是在「一律指 RAW/」前提下的
  登记粒度扩展，**不引入 RAW_FULL 锚**，与原设计意图一致，不破坏「防双路径漏判」目标。

merged 指针页口径（2026-10-11 补正）：
  09-30 重复页治理把 dup 页转成 status: merged 指针页，**刻意保留原 source_path** 作为
  合并存档线索（治理脚本从不改写 source_path）。故这些页会呈现「一条 RAW 被 2 页登记」，
  但那是**已治理的历史存档**，不是新的重复编译。本脚本据此：
    - merged 页 **保留在 idx**（否则其 RAW 会被误报未编译）；
    - merged 页 **从重复登记告警中剔除**，单列「已治理登记」提示。

铁律（AGENTS.md §1.1.2）：任何判重脚本必须先自证覆盖率，输出匹配数/缺失数。
"""
import os, re, io, sys, glob, json, hashlib, argparse

os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


# ---------- 核心：三种登记形态一次收全 ----------
def collect_paths(fm: str) -> set:
    """从 front matter 收集该页登记的全部 RAW 路径。
    注意 [ \\t] 不能写成 \\s —— \\s 会贪婪吞掉换行与后续多行（2026-10-11 实证 bug）。"""
    paths = set()
    m = re.search(r'^source_path:[ \t]*(.+)$', fm, re.M)
    if m:
        paths.add(m.group(1).strip())
    ml = re.search(r'^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n?)+)', fm, re.M)
    if ml:
        for ln in ml.group(1).splitlines():
            v = ln.strip().lstrip('-').strip()
            if v:
                paths.add(v)
    return paths


def _front_matter(text: str) -> str:
    if not text.startswith('---'):
        return ''
    parts = text.split('---', 2)
    return parts[1] if len(parts) > 2 else ''


def build_index(verbose=True):
    """建立 RAW相对路径 -> WIKI 页 的反向索引。

    返回 (idx, merged_pages)：
      idx          —— 全部登记页（含 merged 指针页）的反向索引。
                      **merged 页必须留在 idx 内**，否则其 RAW 条目会因「无人登记」
                      被误报为未编译（2026-10-11 复核确认）。
      merged_pages —— status: merged 的指针页集合，仅用于把「已治理的重复登记」
                      从重复告警里剔除，不影响「已编译」判定。
    """
    idx = {}
    merged_pages = set()
    pages = glob.glob('WIKI/**/*.md', recursive=True)
    hit_pages = 0
    for p in pages:
        t = io.open(p, encoding='utf-8', errors='ignore').read()
        fm = _front_matter(t)
        if not fm:
            continue
        ps = collect_paths(fm)
        if not ps:
            continue
        hit_pages += 1
        if re.search(r'^status:[ \t]*merged[ \t]*$', fm, re.M):
            merged_pages.add(os.path.normpath(p))
        for v in ps:
            idx.setdefault(v, []).append(p)
    if verbose:
        print('[自证] merged 指针页      : %d' % len(merged_pages))
        print('[自证] WIKI 页面总数      : %d' % len(pages))
        print('[自证] 含登记的 source 页 : %d' % hit_pages)
        print('[自证] 登记路径去重总数   : %d' % len(idx))
        # 三种形态分别计数，用于确认多值/合并页被正确收全
        single = multi = 0
        for p in pages:
            fm = _front_matter(io.open(p, encoding='utf-8', errors='ignore').read())
            if not fm:
                continue
            if re.search(r'^source_paths:[ \t]*\n', fm, re.M):
                multi += 1
            elif re.search(r'^source_path:[ \t]*(.+)$', fm, re.M):
                single += 1
        print('[自证]单值登记页: %d / 多值登记页: %d' % (single, multi))
        if hit_pages == 0:
            print('[致命] 未匹配到任何已登记路径 —— 结论无效，请检查正则与工作目录！')
            sys.exit(1)
    return idx, merged_pages


def raw_entries():
    out = []
    for r, d, fs in os.walk('RAW'):
        if 'attachments' in r or '.obsidian' in r:
            continue
        for f in fs:
            if f.endswith('.md'):
                out.append(os.path.relpath(os.path.join(r, f), '.').replace('\\', '/'))
    return sorted(out)


def raw_body(rel: str):
    """取 RAW_FULL 侧正文（镜像命名空间），失败返回 None。"""
    fp = rel.replace('RAW/', 'RAW_FULL/', 1)
    if not os.path.exists(fp):
        return None
    return io.open(fp, encoding='utf-8', errors='ignore').read().split('---', 2)[-1]


def cmd_scan(args):
    idx, merged_pages = build_index()
    raws = raw_entries()
    print()
    print('[自证] RAW 条目数（排除 attachments）: %d' % len(raws))
    uncompiled = [r for r in raws if r not in idx]
    print()
    print('=' * 60)
    print('真实未编译: %d 条' % len(uncompiled))
    print('已编译    : %d 条' % (len(raws) - len(uncompiled)))
    print('=' * 60)
    # 重复登记告警：剔除已治理的 merged 指针页 —— 它们的 source_path 是刻意保留的
    # 合并存档线索（09-30 治理脚本从不改写 source_path），并非新的重复编译。
    dup = {}
    dup_governed = {}
    for r in raws:
        holders = idx.get(r, [])
        if len(holders) <= 1:
            continue
        live = [p for p in holders if os.path.normpath(p) not in merged_pages]
        governed = [p for p in holders if os.path.normpath(p) in merged_pages]
        if len(live) > 1:
            dup[r] = live
        if governed:
            dup_governed[r] = (live, governed)
    print('\n[!] 一条 RAW 被多个「活跃」页登记（真实重复编译，需人工裁定）: %d' % len(dup))
    for r, ps in sorted(dup.items()):
        print('  ', r)
        for p in ps:
            print('      ->', p)
    print('\n[i] 已被 merged 指针页治理过的登记（非新问题，仅存档线索）: %d' % len(dup_governed))
    for r, (live, governed) in sorted(dup_governed.items()):
        print('  ', r[-72:])
        for p in governed:
            print('      (merged)', p)
        for p in live:
            print('      (active)->', p)
    if args.out:
        json.dump({'uncompiled': uncompiled,
                   'duplicate_registration': dup,
                   'duplicate_governed_by_merged': {k: {'active': v[0], 'merged': v[1]}
                                                    for k, v in dup_governed.items()}},
                  io.open(args.out, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
        print('\n已写出: %s' % args.out)


def cmd_check(args):
    idx, _ = build_index(verbose=False)
    rel = args.path
    if not rel.startswith('RAW/'):
        rel = 'RAW/ima_sync/个人知识库/WKB/' + rel
    hits = idx.get(rel, [])
    if hits:
        print('已编译 ->')
        for h in hits:
            print('  ', h)
    else:
        print('未编译（已按 3 种登记形态判定）: %s' % rel)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('scan'); s.add_argument('--out'); s.set_defaults(func=cmd_scan)
    c = sub.add_parser('check'); c.add_argument('path'); c.set_defaults(func=cmd_check)
    a = ap.parse_args()
    a.func(a)