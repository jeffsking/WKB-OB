import json, sys, os, glob

src, media_id, name, dst_rel = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

with open(src, 'r', encoding='utf-8') as f:
    raw = f.read()
try:
    obj = json.loads(raw)
    content = obj.get('content', '')
except Exception:
    # not JSON: treat whole file as content
    content = raw

n = len(content)
dst_abs = os.path.join('E:\\WKB-OB', dst_rel.replace('/', '\\'))
orig = dst_rel.replace('RAW_FULL', 'RAW', 1)
os.makedirs(os.path.dirname(dst_abs), exist_ok=True)

fm = (
    '---\n'
    f'media_id: "{media_id}"\n'
    f'source_file: "{name}"\n'
    f'original_path: "{orig}"\n'
    'extracted: "2026-09-27"\n'
    'extract_method: "ima-mcp fetch_media_content"\n'
    'extract_status: "ok"\n'
    '---\n\n'
    f'# {name}\n\n'
)
with open(dst_abs, 'w', encoding='utf-8', newline='') as f:
    f.write(fm + content + '\n')

print(f'WROTE|{dst_abs}|{n}')
