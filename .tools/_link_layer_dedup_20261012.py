# -*- coding: utf-8 -*-
"""清理 `## Related Sources` 小节内的重复 `- [[X]]` 行（保留首次出现）。幂等，apply 前备份。"""
import glob, os, re, sys, shutil

VAULT = 'E:/WKB-OB'; WIKI = os.path.join(VAULT, 'WIKI')
APPLY = '--apply' in sys.argv
BACKUP = os.path.join(VAULT, '.tools', '_link_layer_dedup_backup_20261012')
H = re.compile(r'^##[ \t]*Related Sources[^\n]*\n', re.M)

def fix(t):
    m = H.search(t)
    if not m: return t, 0
    start = m.end()
    nm = re.search(r'^##[ \t]', t[start:], re.M)
    end = start + (nm.start() if nm else len(t[start:]))
    sec = t[start:end]
    seen = set(); out = []; removed = 0
    for ln in sec.split('\n'):
        s = ln.strip()
        if s.startswith('- [['):
            if s in seen:
                removed += 1; continue
            seen.add(s)
        out.append(ln)
    return t[:start] + '\n'.join(out) + t[end:], removed

nfile = nline = 0
for f in glob.glob(os.path.join(WIKI, 'concepts', '*.md')) + glob.glob(os.path.join(WIKI, 'entities', '*.md')):
    t = open(f, encoding='utf-8', errors='ignore').read()
    nt, r = fix(t)
    if r:
        nfile += 1; nline += r
        if APPLY:
            os.makedirs(BACKUP, exist_ok=True)
            shutil.copy2(f, os.path.join(BACKUP, os.path.basename(f)))
            open(f, 'w', encoding='utf-8', newline='\n').write(nt)

print('[%s] 去重页数 %d，删除重复行 %d' % ('APPLY' if APPLY else 'DRY-RUN', nfile, nline))
