# -*- coding: utf-8 -*-
import io,os,sys,re,glob
sys.stdout.reconfigure(encoding='utf-8')
os.chdir(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
MAIN='WIKI/sources/STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx.md'
SUB ='WIKI/sources/STM-01078 OD产品折叠后长度、宽度测量方法（产品折叠长度）.docx.md'
SUBLINK='[[STM-01078 OD产品折叠后长度、宽度测量方法（产品折叠长度）.docx]]'
MAINLINK='[[STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx]]'
SUBREL='RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/产品折叠长度/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md'

# 1) 主页并入副本路径
t=io.open(MAIN,encoding='utf-8').read()
assert SUBREL not in t, '副本路径已存在，避免重复'
t=t.replace('source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md',
            'source_path: RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md\n'
            'source_paths:/n'
            '  - RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md\n'
            f'  - {SUBREL}')
# 2) 正文中的副本提示改为「已合并」记录
old_note='> 📌 **重复副本提示（2026-09-29）**：同一方法在 `RAW/…/成品/产品折叠长度/STM-01078 …docx.md` 另有内容相同的副本，已单独建源摘要页 '+SUBLINK+'；**两者正文一致，结论只计一次**。'
new_note=('> 📌 **重复副本已合并（2026-10-11）**：该方法在 IMA 内有两份存储副本，本页为主件，已用 `source_paths` 同时登记两条 RAW 路径：\n'
          '>\n'
          '> 1. `RAW/…/成品/NJ/STM-01078 …docx.md`（主件，页面源）\n'
          '> 2. `RAW/…/成品/产品折叠长度/STM-01078 …docx.md`（副本，2026-09-29 曾单独建页）\n'
          '>\n'
          '> 两者**正文逐字一致**（正文指纹 `e39cab83f1b4`）。原副页已于 2026-10-11 合并入本页并删除，'
          '**同一结论只计一次证据**。原副页备份见 `.tools/_backup_stm01078_20261011/`。')
assert old_note in t, '未匹配到副本提示段'
t=t.replace(old_note,new_note)
t=t.replace('- 副本：'+SUBLINK,
            '- 副本（已合并入本页）：`RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/产品折叠长度/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md`\n- 原副页：'+SUBLINK+'（2026-10-11 已合并并删除，备份见 `.tools/_backup_stm01078_20261011/`）')
io.open(MAIN,'w',encoding='utf-8',newline='\n').write(t)
print('主页已并入副本路径')

# 3) 全库改写引用（先改引用方，最后删副页）
REF=['WIKI/concepts/Folded Product Dimension Test（折叠后长度·宽度测量）.md',
     'WIKI/sources/STM-00064 Diaper尺寸.docx.md']
for p in REF:
    s=io.open(p,encoding='utf-8').read(); o=s
    s=s.replace(SUBLINK,MAINLINK)
    s=s.replace('**STM-01078**（两份副本，正文一致）','**STM-01078**（两份副本已合并为单页）')
    s=s.replace('[[STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx]]、[[STM-01078 OD产品折叠后长度、宽度测量方法（产品折叠长度）.docx]]',
                '[[STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx]]')
    s=s.replace('- [[STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/NJ/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md`\n- [[STM-01078 OD产品折叠后长度、宽度测量方法（产品折叠长度）.docx]] —— `RAW/ima_sync/个人知识库/WKB/Areas/Test Method/成品/产品折叠长度/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md`',
                '- [[STM-01078 OD产品折叠后长度、宽度测量方法（成品·NJ）.docx]] —— **主件** `RAW/…/成品/NJ/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md`\n  - 副本 `RAW/…/成品/产品折叠长度/STM-01078 OD产品折叠后长度、宽度测量方法.docx.md`（正文逐字一致，2026-10-11 已合并登记入主页 `source_paths`）')
    if s!=o: io.open(p,'w',encoding='utf-8',newline='\n').write(s); print('引用改写:',p)

# 4) 删除副页
os.remove(SUB)
print('副页已删除')
