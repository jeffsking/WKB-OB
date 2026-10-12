import json, sys, os

src, dst_rel, media_id, name = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4]

raw = open(src, encoding='utf-8').read().strip()
# 工具结果文件就是 JSON: {"content":"..."}
try:
    data = json.loads(raw)
    content = data.get('content', '')
except Exception:
    # 容错：截取第一个 { 到最后一个 }
    s = raw[raw.find('{'): raw.rfind('}') + 1]
    data = json.loads(s)
    content = data.get('content', '')

dst_rel = dst_rel.replace('/', '\\')
dst_abs = os.path.join(r'E:\WKB-OB', dst_rel)
orig = dst_rel.replace('RAW_FULL', 'RAW', 1)

os.makedirs(os.path.dirname(dst_abs), exist_ok=True)

doc = (
    '---\n'
    f'media_id: "{media_id}"\n'
    f'source_file: "{name}"\n'
    f'original_path: "{orig}"\n'
    'extracted: "2026-09-27"\n'
    'extract_method: "ima-mcp fetch_media_content"\n'
    'extract_status: "ok"\n'
    '---\n\n'
    f'# {name}\n\n'
    f'{content}'
)

with open(dst_abs, 'w', encoding='utf-8', newline='') as f:
    f.write(doc)

print(f'OK {len(content)} {dst_abs}')
