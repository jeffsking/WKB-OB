import os, re, json

SRC = 'E:/WKB-OB/WIKI/sources'
BASE = 'E:/WKB-OB/RAW_FULL/ima_sync/个人知识库/WKB/Resources/Ebook'
manifest = json.load(open(os.path.join('E:/WKB-OB/.tools/ebook_compile_manifest.json'), encoding='utf-8'))
books = manifest.get('books', manifest) if isinstance(manifest, dict) else manifest

# scan all source_path values
registered = set()
for fn in os.listdir(SRC):
    if not fn.endswith('.md'):
        continue
    fp = os.path.join(SRC, fn)
    try:
        with open(fp, encoding='utf-8', errors='replace') as f:
            head = f.read(5000)
        m = re.search(r'^source_path:\s*(.+?)\s*$', head, re.M)
        if m:
            registered.add(m.group(1).strip().strip('"'))
        m2 = re.search(r'^source_paths:\s*$\n((?:\s*-\s*.+\n?)+)', head, re.M)
        if m2:
            for line in m2.group(1).splitlines():
                v = line.strip().lstrip('- ').strip().strip('"')
                if v:
                    registered.add(v)
    except:
        pass

def norm(p):
    p = p.replace('\\', '/').strip().strip('"')
    p = re.sub(r'^(?:RAW_FULL|RAW)/ima_sync/[^/]*/WKB/', '', p, flags=re.I)
    return p.lower()

reg_norm = {norm(r) for r in registered if r}

# Report remaining uncompiled books
print('=== REMAINING UNCOMPILED BOOKS ===')
for b in books:
    name = b.get('name', '?')
    pr = b.get('priority', '?')
    ch = b.get('chapter_source_paths', [])
    rf = b.get('root_file_rel') or ''
    if not ch and not rf:
        continue
    done_ch = 0
    todo_ch = []
    for c in ch:
        cn = norm(c)
        if cn in reg_norm:
            done_ch += 1
        else:
            todo_ch.append(c)
    root_done = norm(rf) in reg_norm if rf else False
    
    if todo_ch or (rf and not root_done):
        if todo_ch:
            print(f'{pr:4} {name}')
            print(f'    章节: {done_ch}/{len(ch)} 完成, {len(todo_ch)} 待编译')
            for t in todo_ch[:3]:
                print(f'      TODO: {os.path.basename(t)}')
            if len(todo_ch) > 3:
                print(f'      ... 还有 {len(todo_ch)-3} 个')

# Summary
print('\n=== 按优先级汇总 ===')
for pr in ['P0', 'P1', 'P2']:
    total_ch = 0
    done_ch = 0
    total_root = 0
    done_root = 0
    for b in books:
        if b.get('priority') != pr:
            continue
        ch = b.get('chapter_source_paths', [])
        rf = b.get('root_file_rel') or ''
        if ch:
            total_ch += len(ch)
            done_ch += sum(1 for c in ch if norm(c) in reg_norm)
        if rf:
            total_root += 1
            if norm(rf) in reg_norm:
                done_root += 1
    print(f'{pr}: 章节 {done_ch}/{total_ch}, 整书 {done_root}/{total_root}')
