import re
s = open(r"C:\Users\Chris Wang\.workbuddy\projects\e-WorkBuddy-Workplace-Obsidian\7c5f96dd-83e0-4965-9cd5-4594fb238c9f\subagents\agent-9b088954ca5d4019\tool-results\mcp-ima-mcp-fetch_media_content-1790578755727-e70497.txt", encoding="utf-8").read().rstrip("\r\n")
assert s.startswith('{"content":"') and s.endswith('"}'), (s[:20], s[-20:])
content = s[12:-2]
content = re.sub(r'\\u([0-9a-fA-F]{4})', lambda m: chr(int(m.group(1), 16)), content)
open(r"E:/WKB-OB/RAW_FULL/ima_sync/WKB/Resources/Open Innovation/Performance/Rewet/Competitive Benchmark - 1Q 2026.xlsx.md","w",encoding="utf-8").write(content)
print("item3 written", len(content), "amp:", content.count('&'))
