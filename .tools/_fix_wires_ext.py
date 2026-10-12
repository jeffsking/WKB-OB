import os, glob
os.chdir(r'E:\WKB-OB')
# rename Wires files to add .md if missing
for f in glob.glob('WIKI/sources/Liquid Crystalline Polymeric Wires*'):
    b = os.path.basename(f)
    if not b.endswith('.md'):
        new = f + '.md'
        os.rename(f, new)
        print("RENAMED:", b, "->", b + '.md')
    else:
        print("OK already .md:", b)
