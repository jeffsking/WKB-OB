import json, os, sys, re

JSONL = sys.argv[1]
BATCH = sys.argv[2]
OUT_MANIFEST = sys.argv[3]
ROOT = 'E:\\WKB-OB'

calls = {}   # callId -> (name, arguments)
results = {} # callId -> output text

for line in open(JSONL, encoding='utf-8'):
    line = line.strip()
    if not line:
        continue
    try:
        d = json.loads(line)
    except Exception:
        continue
    t = d.get('type')
    if t == 'function_call':
        calls[d.get('callId')] = (d.get('name'), d.get('arguments'))
    elif t == 'function_call_result':
        out = d.get('output') or {}
        results[d.get('callId')] = out.get('text', '')

batch = json.load(open(BATCH, encoding='utf-8'))
manifest = []

for item in batch['items']:
    mid = item['media_id']
    name = item['name']
    dst = item['dst']
    rec = {"name": name, "media_id": mid, "dst": dst, "status": "fail",
           "chars": 0, "error": "no tool result found"}
    # find matching call
    found_text = None
    for cid, (nm, args) in calls.items():
        if nm != 'DeferExecuteTool':
            continue
        if args and mid in args:
            out = results.get(cid)
            if out:
                found_text = out
                break
    if found_text is None:
        manifest.append(rec)
        continue
    # if output was persisted to a side file, read from there
    if 'exceeds maximum allowed tokens' in found_text or '<persisted-output>' in found_text:
        m = re.search(r'([A-Za-z]:\\[^"\r\n]*?\.txt)', found_text)
        if m:
            side = m.group(1).strip()
            if os.path.exists(side):
                found_text = open(side, encoding='utf-8').read()
    # parse content out of output text
    content = None
    try:
        obj = json.loads(found_text)
        content = obj.get('content')
    except Exception:
        m = re.search(r'^\s*\{\s*"content"\s*:\s*"(.*)"\s*\}\s*$', found_text, re.S)
        if m:
            try:
                content = json.loads('"' + m.group(1) + '"')
            except Exception:
                content = None
    if content is None:
        rec['error'] = 'content field not parseable; output head=' + found_text[:120].replace('\n', ' ')
        manifest.append(rec)
        continue
    n = len(content)
    rec['chars'] = n
    if n < 20:
        rec['error'] = f'content too short ({n})'
        manifest.append(rec)
        continue
    dst_abs = os.path.join(ROOT, dst.replace('/', '\\'))
    orig = dst.replace('RAW_FULL', 'RAW', 1)
    os.makedirs(os.path.dirname(dst_abs), exist_ok=True)
    fm = ('---\n'
          f'media_id: "{mid}"\n'
          f'source_file: "{name}"\n'
          f'original_path: "{orig}"\n'
          'extracted: "2026-09-27"\n'
          'extract_method: "ima-mcp fetch_media_content"\n'
          'extract_status: "ok"\n'
          '---\n\n'
          f'# {name}\n\n')
    with open(dst_abs, 'w', encoding='utf-8', newline='') as f:
        f.write(fm + content + '\n')
    rec['status'] = 'ok'
    manifest.append(rec)

with open(OUT_MANIFEST, 'w', encoding='utf-8') as f:
    json.dump(manifest, f, ensure_ascii=False, indent=1)

for r in manifest:
    print(r['status'], r['chars'], r['name'], ('| ' + r['error']) if r['status'] == 'fail' else '')
