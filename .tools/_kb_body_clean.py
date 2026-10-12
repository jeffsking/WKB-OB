#!/usr/bin/env python3
"""Clean fetched media content: strip XML tags, unescape entities, keep text.

Handles layered escapes like &amp;lt;tag&amp;gt; -> <tag> -> '' (stripped).
Strategy: unescape HTML entities repeatedly, then strip all tags.
"""
import sys, re, html, json

def clean(raw: str) -> str:
    s = raw
    # Loop: unescape entities and strip tags until stable.
    # First replace literal &amp;#x -> &# so numeric refs resolve.
    prev = None
    for _ in range(8):
        if s == prev:
            break
        prev = s
        s = s.replace('&amp;#', '&#')
        s = html.unescape(s)
    # Remove XML declaration
    s = re.sub(r'<\?xml[^>]*\?>', '', s)
    # br -> newline
    s = re.sub(r'<br\s*/?>', '\n', s)
    # block closing tags -> newline
    s = re.sub(r'</(p|h|div|section|tr|li|body|doc|content|table|td|th)>', '\n', s)
    # td/th open -> tab separator (for entity-encoded tables)
    s = re.sub(r'<(td|th)[^>]*>', '\t', s)
    # remove all remaining tags
    s = re.sub(r'<[^>]+>', '', s)
    # clean stray leading tag-name fragments like "p id=..." already gone.
    # normalize whitespace
    s = re.sub(r'[ \t]+\n', '\n', s)
    s = re.sub(r'\n[ \t]+', '\n', s)
    s = re.sub(r'\n{3,}', '\n\n', s)
    s = s.strip()
    return s

if __name__ == '__main__':
    inp = sys.argv[1]
    outp = sys.argv[2]
    with open(inp, 'r', encoding='utf-8') as f:
        raw = f.read()
    try:
        obj = json.loads(raw)
        if isinstance(obj, dict) and 'content' in obj:
            raw = obj['content']
    except Exception:
        pass
    out = clean(raw)
    with open(outp, 'w', encoding='utf-8') as f:
        f.write(out)
    print(f"wrote {len(out)} chars to {outp}")
