# -*- coding: utf-8 -*-
import os, re
SRC = r"E:\WKB-OB\WIKI\sources"
# Use explicit char classes, never \s, to dodge bash/heredoc mangling in any downstream invocation
PAT_LINE = re.compile(r"^source_path:[ \t]*(\S+)", re.M)
PAT_LIST = re.compile(r"^source_paths:[ \t]*\n((?:[ \t]*-[ \t]*.+\n)+)", re.M)

n = 0
samples = []
for fn in os.listdir(SRC):
    if not fn.endswith(".md"):
        continue
    head = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read(4000)
    m = PAT_LINE.search(head)
    if m:
        n += 1
        if len(samples) < 3:
            samples.append((fn, m.group(1)))
print("pages with source_path:", n)
for s in samples:
    print("  ", s[0], "->", s[1])
print()
# test the specific file
fn = "Absorbent Technology Introduction.md"
head = open(os.path.join(SRC, fn), encoding="utf-8", errors="replace").read(4000)
m = PAT_LINE.search(head)
print("test file match:", repr(m.group(1)) if m else None)
print("pattern repr:", repr(PAT_LINE.pattern))
