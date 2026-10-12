# -*- coding: utf-8 -*-
"""批次落盘脚本：读取超限临时文件 -> 解析正文 -> 写 E:/WKB-OB/<dst>"""
import json
import sys
import os
import io


def load_content(path):
    with io.open(path, 'r', encoding='utf-8', errors='replace') as f:
        raw = f.read()
    s = raw.strip()
    # 情形 A：整体是 JSON（单行或格式化）
    try:
        obj = json.loads(s)
        if isinstance(obj, dict):
            for k in ('content', 'text', 'markdown', 'data'):
                if isinstance(obj.get(k), str):
                    return obj[k]
    except Exception:
        pass
    # 情形 B：纯文本中夹带 JSON
    try:
        idx = raw.find('{')
        if idx != -1:
            obj = json.loads(raw[idx:].strip())
            if isinstance(obj, dict) and isinstance(obj.get('content'), str):
                return obj['content']
    except Exception:
        pass
    # 情形 C：纯文本，原样
    return raw


def main():
    tmp, media_id, dst, name, original_path = sys.argv[1:6]
    content = load_content(tmp)
    if content.strip() == '':
        print('EMPTY')
        return
    out = os.path.join('E:/WKB-OB', dst.replace('/', os.sep))
    d = os.path.dirname(out)
    if d and not os.path.isdir(d):
        os.makedirs(d)
    fm = (
        '---\n'
        'media_id: "%s"\n'
        'source_file: "%s"\n'
        'original_path: "%s"\n'
        'extracted: "2026-09-27"\n'
        'extract_method: "ima-mcp fetch_media_content"\n'
        'extract_status: "ok"\n'
        'clean_rules: ""\n'
        'processed: ""\n'
        '---\n\n# %s\n\n%s' % (media_id, name, original_path, name, content)
    )
    with io.open(out, 'w', encoding='utf-8', newline='\n') as f:
        f.write(fm)
    print('CHARS=%d' % len(content))
    print('OUT=%s' % out)


main()
