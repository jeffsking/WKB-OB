import re,sys
sys.stdout.reconfigure(encoding='utf-8')
p='WIKI/sources/CN 101641398 B（包覆吸水性聚合物颗粒的方法·BASF）.md'
t=open(p,encoding='utf-8',errors='ignore').read()
m=re.search(r'^source_path:[ \t]*(.+)$',t,re.M)
print('MATCH:',m.group(1) if m else None)
