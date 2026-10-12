import os, glob
for f in glob.glob('WIKI/sources/Liquid Crystalline Polymeric Wires*'):
    b = os.path.basename(f)
    print(repr(b))
    print('  has_trailing_space:', b != b.rstrip())
