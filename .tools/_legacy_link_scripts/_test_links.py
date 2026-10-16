import re, os, glob
os.chdir(r'E:\WKB-OB')
files = {os.path.splitext(os.path.basename(p))[0] for p in glob.glob('WIKI/**/*.md', recursive=True)}
files |= {'index', 'log'}
idx = r'WIKI/sources/Liquid Crystalline Polymers Smart Applications.md'
t = open(idx, encoding='utf-8').read()
t2 = re.sub(r'`[^`]*`', '', t)
links = set(re.findall(r'\[\[([^\]|#]+)', t2))
print("Extracted links from index (those containing 'Wires'):")
for l in links:
    if 'Wires' in l:
        print("  ", repr(l), "-> in files?", l.strip() in files)
print()
print("Exact file basenames containing 'Wires':")
for f in files:
    if 'Wires' in f:
        print("  ", repr(f))
