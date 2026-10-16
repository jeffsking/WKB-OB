import os, glob, re
os.chdir(r'E:\WKB-OB')
repl = {
    "Wires for Selective Proton Transport, Part 1: Wires Preparation":
        "Wires for Selective Proton Transport, Part 1",
    "Wires for Selective Proton Transport, Part 2: Ion Transport in Solid-state":
        "Wires for Selective Proton Transport, Part 2",
}
total = 0
for f in glob.glob('WIKI/sources/*.md'):
    t = open(f, encoding='utf-8').read()
    new = t
    for k, v in repl.items():
        if k in new:
            new = new.replace(k, v)
            total += 1
    if new != t:
        open(f, 'w', encoding='utf-8').write(new)
        print("FIXED:", os.path.basename(f))
print("总替换:", total)
