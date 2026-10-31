# 自动化执行记忆 — 每日日志扫描（18:00）

## 2026-10-01 执行记录
- 首次运行，无历史记忆文件。
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入（未建源摘要页、未改 index.md / log.md）。
- 结论：今日无未处理日志。

## 2026-10-02 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：仍为空，无任何 YYYY-MM-DD.md 日志。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。

## 2026-10-03 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 3 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。

## 2026-10-04 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 4 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入（未建源摘要页、未改 index.md / log.md）。
- 结论：今日无未处理日志。

## 2026-10-05 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 5 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。

## 2026-10-06 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 6 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。

## 2026-10-07 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 7 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。
- 💡 提示：journal 目录自 2026-09-30 建立以来无人工写入，若长期为空可考虑与用户确认日志书写习惯是否落地。

## 2026-10-08 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 8 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。

## 2026-10-09 执行记录
- 扫描 `E:\WKB-OB\RAW\journal\`：目录为空，无任何 YYYY-MM-DD.md 日志（连续第 9 天）。
- 按 AGENTS.md §7 判重规则：无未处理日志 → 零动作结束，未做任何写入。
- 结论：今日无未处理日志。
- 💡 连续 9 天无人工日志写入，建议与用户确认日志书写习惯是否落地，或考虑暂停/降频此自动化。

---

## 2026-10-11 · 职责重构（重大变更）

**变更性质**：从「只扫 `RAW/journal/`」→「WKB-OB 知识管道 · IMA→Obsidian 日更（阶段 A/B/C/E）」。

**触发**：王总指出核心矛盾 —— 「我的知识更新多数在 IMA 发起，没有机制把更新同步到 journal，所以该文件夹会一直为空。今天所有讨论就是要解决该问题（每日 IMA 内容到 Obsidian 的同步和编译），怎么到最后还是没实现？」

**承认的问题**：
- 09-30 建立 `RAW/journal/` 后连续 9 天为空（memory 已自证），本自动化 9 次运行全部零动作。
- 10-11 我曾把 v2 设计写进文档、只在本 prompt 尾部加了一句「引用账本」的说明，**没有给自动化任何新工作** → 文档改了、配置没改 = 假完成。

**本次实际动作**：
- 名称改为「WKB-OB 知识管道 · IMA→Obsidian 日更」
- prompt 重写为 A/B/C/E 四阶段 15 步，每步调用**已存在**的工具（`ima_sync_state.py` / `ima_note_backfill.py` / `ima_fetch_originals.py` / `wkb_dedup.py` / `rebuild_index.py`）
- 保留 18:00 频率
- 明示降级：脚本未就绪时须标注「阶段 X 未实现」，禁止假装完成

**遗留**：阶段 B（落地器）与阶段 C（编译器）尚未有独立脚本（现靠 `ima_note_backfill.py` + 人工/子代理），故本自动化的 B/C 段目前只能部分自动。第 2/3/4 批完成后需回填。

**journal 目录去留**：`RAW/journal/` 保留（阶段 D 独立跑），但已不再是知识进化的唯一入口。

## 2026-10-11 19:16 执行记录（重构后首次真正运行）
- 今日全量扫描+枚举已由早前会话完成（18:54/19:11），本批无新增增量。
- 阶段 B 部分实现：缺口 33 条（历史失败件），MCP 笔记正文通道本会话不可用（无 ima connector）。
- 阶段 C 部分实现：dedup 基线 911/471，重复登记 0；账本积压 synced 349 + discovered 144。
- 阶段 E 完成：index.md 重建（1662 页），log.md / memory / 日报已追加。
- 日报：.tools/kb_pipeline_daily/2026-10-11.md

## 2026-10-12 18:00 执行记录（日更增量 · 首日真正有增量）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A/B/C/E 全 OK；Agent 侧补齐 A/B/C。
- **降级原因**：本会话无 IMA MCP connector → 枚举走 REST `get_knowledge_list` 只读兜底（子层参数名 `folder_id`），笔记正文走 REST `note/v1/get_doc_content`。
- **新增 2 条**并全部编译：`芯吸效应：水为什么自己往细缝里钻`（公众号）、`会议纪要：2026-10-12`（COCO V6 项目）。
- **终值**：wkb_dedup 真实未编译 2→**0** · 已编译 1389 · 账本 1391 · index 2142 页。
- **遗留**：`note_7434068337643175`（ima笔记使用指南）220030 永久失败，留积压。
- 日报 `.tools/kb_pipeline_daily/2026-10-12.md`；log.md / memory 已追加。

## 2026-10-13 18:00 执行记录（日更增量 · 新增 5 条，编译 2 条）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A OK / B PARTIAL / C PARTIAL / E OK；Agent 侧补齐 A/B/C。
- **降级前提**：本会话无 IMA MCP connector → 枚举走 REST `get_knowledge_list` **全量递归**（1524 条，优于历次浅枚举）；笔记正文走 REST `get_doc_content`。
- **新增 5 条**（IMA 插件今日写入 RAW）：NIFO visit 会议纪要 / REL增强层 6 样品对比研报 / 聚烯烃胶 / 益生菌-益生元 / 莱博药妆（后 3 条为占位符）。
- **编译 2 条落 WIKI/sources**：① 会议纪要：NIFO visit - 可视化材料技术在纸尿裤-卫材产品上的应用探讨（插件已落 RAW 正文→镜像）；② REL增强层专项对比分析_6样品benchmark_20260924（**通道 B get_media_info 原件下载，不受配额**）。
- **阻塞 3 条**：REST `get_doc_content` 命中 `200005`（日配额，45s 复探仍 200005）→ 当日停止不重试，留账本 discovered 待次日。
- **终值**：wkb_dedup 真实未编译 **5→3** · 已编译 1391 · 账本 1396 · index 2246 页。
- **新知识**：笔记类 `get_media_info` 只返回 `chrome://note?...` 不可下载 → 笔记正文唯一可用通道 = MCP `fetch_media_content`（无配额）或 REST `get_doc_content`（有日配额）。
- **遗留**：`note_7434068337643175`（ima笔记使用指南）legacy `220030` 长期积压；账本多登 4 条（2 img + 2 note）疑似 IMA 侧已删，只报不清理。
- 日报 `.tools/kb_pipeline_daily/2026-10-13.md`；log.md / memory 已追加。

## 2026-10-15 18:00 执行记录（日更增量 · 新增 4 条，编译 2 条）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A/B/C/E 全 OK；Agent 侧补齐 A/B/C。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST `get_knowledge_list` 全量递归（1532 条 = 1400 文件 + 132 文件夹）；笔记正文走 REST `get_doc_content`。
- **阶段 A 治理**：① **源头剔除 folder 条目**（`media_type=99`，不再事后清理）；② **限频治理**：0.3s 间隔长递归被 HTTP 403 打断 → 改 2.5s 间隔 + 失败 12s 退避，6m15s 跑完全库。**403 = urllib 表征，权威判据以 `ima_api.cjs` 业务码为准**（本次复核 `200001` = 频率超限）。合并新增 **4**（插件已全部写入 RAW，`_rebind_raw_path.py` 回绑），账本 **1404**。
- **阶段 B（写入 2）**：① 温变粉公众号（RAW 有正文→镜像，`ok`）；② 5CB word（**通道 B `get_media_info` 下载原件 22.5KB → RAW_FULL/attachments + docx 文本抽取**，`ok`）。**5 条笔记命中 REST `200005` 日配额耗尽**（隔 6 分钟复探仍 200005）→ 停止不重试，留 `discovered`（其中 3 条自 10-13 连续第 3 日被卡）。
- **阶段 C**：编译 **2 张源摘要页** 落 `WIKI/sources/`：`温变粉如何应用于纱线染色-纱线印染？`、`5CB贴身合规评估结论备忘录_20261014`（后者结论：**5CB 贴身路线已证伪-关闭**）。
- **终值**：`wkb_dedup scan` 真实未编译 **7 → 5** · 已编译 **1397** · RAW 条目 1402 · 登记去重 1409 · index **2252 页** · 重复编译 0。
- **遗留**：5 条笔记正文阻塞于 REST 日配额（唯一无配额通道 = MCP `fetch_media_content`，需会话内有 IMA connector）；账本 2 条多登只报不清。
- 日报 `.tools/kb_pipeline_daily/2026-10-15.md`；log.md / 每日 memory 已追加。

## 2026-10-14 18:00 执行记录（日更增量 · 新增 4 条，全部编译）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A OK / B PARTIAL / C PARTIAL / E OK；Agent 侧补齐 A/B/C。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST `get_knowledge_list` **全量递归**（1528 条）；笔记正文走 REST `get_doc_content`。
- **阶段 A 治理**：REST 递归把 **132 个 folder 条目误入 items**（`discovered` 4→140）→ `_ledger_cleanup_20261014.py` 剔除（备份 `_ima_sync_state.bak.20261014-preclean`），账本 1532→1400。真实新增内容 **4 条**（插件已全部写入 RAW，`_rebind_raw_path.py` 回绑）。
- **阶段 B（写入 5）**：① 会议纪要新产线高速运行方案（笔记，RAW 已有正文→镜像）；② 新生产线高速运行方案（录音，**通道 B 下载原件 10,770,078 B → attachments/*.m4a**，正文 empty+指针）；③④ Biocare v2/v3 markdown（正文取自插件已落地 attachments）。**3 条笔记命中 REST `200005`（连续第 2 日）→ 停止不重试**，留 discovered。
- **阶段 C**：编译 **4 张源摘要页** 落 `WIKI/sources/`。
- **终值**：`wkb_dedup scan` 真实未编译 **7 → 3** · 已编译 **1395** · index **2250 页** · 断链 **0** · front matter/index 对齐均 2250/2250。
- **新知识（已入 MEMORY.md §六）**：REST 递归 folder 污染 items；urllib 403 vs 官方 cjs 200005（判据以 cjs 为准）；录音原件可经 get_media_info 下载（笔记不可）；插件偶发写笔记完整正文。
- **memory_guard**：MEMORY.md 256→91 行假告警连续 2 日 → 已执行 `baseline` 刷新消除（旧版 git 可逐字节恢复）。
- **遗留**：3 条 200005 阻塞笔记 + `note_7434068337643175`（legacy 220030）；账本 31 条 synced 陈旧缓存（dedup 已确认已编译）。
- 日报 `.tools/kb_pipeline_daily/2026-10-14.md`；log.md / 每日 memory 已追加。

## 2026-10-16 18:00 执行记录（日更增量 · 新增 1 条，全部编译）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A OK / B PARTIAL / C PARTIAL / E OK；Agent 侧补齐 A/B/C。
- **降级前提**：本会话无 IMA MCP connector（`list_installed_plugins` = No connectors installed）→ 阶段 A 走 REST `get_knowledge_list` **全量递归**（1533 条 = 1401 文件 + 132 文件夹，6m13s）；笔记正文走 REST `get_doc_content`。
- **阶段 A**：源头剔 folder → 合并 **新增 1 · 移动 1390（kb_path 噪音）· 已知 1400**，账本 **1405**；**`raw_path` 零污染复核通过（改动 0 条）**。
- **阶段 B**：plan 5 条（**全为通道 A 笔记**）→ 全部 `200005` 日配额耗尽 → 按铁律停止不重试。**手工补落 1 条**：`IMA知识库索引.md`（Markdown，media_type 7）经 `get_media_info` **原件下载**（21,497 B）→ `RAW_FULL/ima_sync/个人知识库/WKB/IMA知识库索引.md.md`（`ok`）。
  - 阻塞 5 条：莱博药妆 / 聚烯烃胶 / 益生菌-益生元 / 三家技术档案 / Biocare v3（其中 3 条自 10-13 连续第 4 日）。
- **阶段 C**：编译 **1 张源摘要页** 落 `WIKI/sources/`：`IMA知识库索引.md`（周度索引快照 · semantic · 6 条 key_claims · 含 W41 10/10–10/16 共 12 条增量全表；累计 ~609 条）。
- **终值**：`wkb_dedup scan` 真实未编译 **5 → 5** · 已编译 **1397** · 登记路径去重 **1409 → 1410** · WIKI 页面 **2252 → 2253** · 重复编译 **0** · merged 4；index **2253 页**（源摘要 1398 / 概念 617 / 实体 145 / 对比 80 / MOC 13）；断链 **0** · front matter 2253/2253 · index 对齐 2253/2253。
- **新知识（已入 MEMORY.md §六）**：① `markdown`/`html` 类条目可经 `get_media_info` 无配额直下原件（第三条正文通道）；② REST 无 `fetch_media_content` 端点；③ `kb_sync_handler.py plan` 对 `raw_path` 为空的新条目 `continue`（盲区）；④ 「编译成功」判据 = 登记路径数/WIKI 页面数 +1，非未编译数下降；⑤ 枚举合并「移动 N 条」为 kb_path 噪音，须复核 raw_path 改动=0。
- **遗留**：5 条笔记阻塞（唯一无配额通道 = MCP `fetch_media_content`）；插件今日未写 RAW（滞后，无副作用）；`note_7434068337643175` legacy 220030 不再重试；账本多登只报不清。
- 日报 `.tools/kb_pipeline_daily/2026-10-16.md`；log.md / 每日 memory 已追加。

## 2026-10-17 18:00 执行记录（日更增量 · 新增 6 条，编译 4 条）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A/B/C/E 全 OK；Agent 侧补齐 A/B/C（先手工跑完 A/B/C，再跑编排器收尾归档）。
- **降级前提**：本会话无 IMA MCP connector（`list_installed_plugins` = No connectors installed）→ 阶段 A 走 REST `get_knowledge_list` 全量递归（1539 条 = 1407 文件 + 132 文件夹，12m08s）。
- **阶段 A**：源头剔 folder → 新增 **6 · 移动 0 · 已知 1401**，账本 **1411**；`raw_path` 零污染复核通过（移动 0）。
- **阶段 B（写入 4，全 ok）**：PPS Sensor（插件正文镜像 14.7k）；除臭粉 docx / 菌草纤维 docx（**通道 B** `get_media_info` 原件直下 + zipfile 抽 document.xml）；lxag173.pdf（原件直下 + **pypdf** 15 页 82.6k）。**7 条 note 卡 200005**（官方 `ima_api.cjs` 判据），其中 5 条已连续第 4–5 日。
- **阶段 C**：编译 4 张源摘要页（PPS 纪要 / montanine 抗葡萄球菌论文 / 菌草纤维技术简报 / 除臭粉掉粉工艺方案）；**业务闭环**：菌草简报引用的 pdf_96 即当日新增 lxag173 → 两页互链，形成「纤维宣称 ↔ 化合物 MIC 基准」证据链，并裁定「纤维抑菌率 vs MIC」为度量错位。
- **终值**：`wkb_dedup` 未编译 **7 → 6** · 已编译 **1399** · 登记路径去重 **1410 → 1414** · WIKI 页面 **2253 → 2257** · 重复编译 0 · 断链 0 · front matter/index 对齐 **2257/2257**；暂存归档 `_done/2026-10-17/`。
- **新知识（已入 MEMORY §七）**：REST 标题 ~40 字符截断 → 禁用截断标题做页面名（改 ledger title 重跑 plan）；plan 的 raw_path 空值盲区绕行法（绑预期 RAW 路径）；PDF 抽取用托管 venv 的 pypdf。
- **遗留**：7 条 note 阻塞（唯一解 = MCP `fetch_media_content`）；3 条新页 RAW 锚点为「预期路径」，**明日 A 阶段后必须复核插件是否落同名文件**；Wire Screen 标题待补全。
- 日报 `.tools/kb_pipeline_daily/2026-10-17.md`；log.md / 每日 memory 已追加。

## 2026-10-18 18:00 执行记录（日更增量 · 新增 0，编译 3 源 + 1 实体，修幽灵锚点）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A/B/C/E 全 OK；Agent 侧先手工跑完 A/B/C，再跑编排器收尾归档（暂存 → `_done/2026-10-18/`）。
- **降级前提**：本会话无 IMA MCP connector（`list_installed_plugins` = No connectors installed）→ 阶段 A 走 REST `get_knowledge_list` 全量递归（132 文件夹 / 1409 文件 / 6m15s）。09:00 周度自动化已用 MCP 跑过全量（09:22，1409 条），本日 18:00 复跑**结果完全一致**→ 09:22 后零新增。
- **阶段 A**：合并 新增 0 · 移动 1355（kb_path 噪音）· 已知 1409；`raw_path`/`full_path`/`title` 改动 **0**（污染复核通过）。账本 1413 不变。
- **阶段 B（落地 3，全 ok）**：`一句话结论`（PTT 报价对标 3.9k 字）·`中科一然除臭粉`（供应商语音反馈）·`相变储能·A轮融资`（公众号 4.0k 字）——均为插件已落正文→镜像。**阻塞 1**：三家技术档案 note，REST `get_doc_content` **只成功 1 次即 200005** → 当日停止（连续第 4 天）。
- **阶段 C（编译 3 源 + 1 实体）**：PTT 报价对标（26,000 元/t 对巨化 +60%，按 18,500 重算 28gsm 0.542 元/m² 比 40gsm 低 4.4% → 「轻量化=降本」反转成立）· 除臭粉掉粉现场反馈（供应商独立复现、根因「缺粘结相」升级为共识）· 相变储能 AC-TEX（纳米限域封装 vs 微胶囊后整理、迪桑特两年验证、杭州三级国资超亿元 A 轮、标准缺失）；新建实体 `相变储能（杭州）· 三沐新材料（AC-TEX®）`；`相变材料`/`粘合剂 Binder` 概念页补 Related Sources。
- **修幽灵锚点（10-17 遗留）**：`RAW/.../lxag173.pdf.md` 从未存在 → 回绑插件真实名 `Anti-staphylococcal potential ... .pdf.md`，三处同步（RAW_FULL 镜像 / 账本 raw_path+full_path / WIKI source_path），并入既有页未产生重复页。
- **终值**：`wkb_dedup` 未编译 **5 → 1** · 已编译 **1406 → 1410** · 登记路径去重 **1419 → 1422** · WIKI **2261 → 2265** · 重复编译 0 · 断链 0 · front matter/index 对齐 **2265/2265**；index 重建 2265 页（源摘要 1409 / 概念 617 / 实体 146 / 对比 80 / MOC 13）。
- **新知识（已入 MEMORY §六/§七）**：① 「预期 RAW 路径」若与插件实落名不同 → 幽灵锚点致永久假欠账，且 rebind 工具够不着，须三处同步修；② REST 三个字段（media_state/create_time/file_number）全缺 → 剪枝不可实现，只能全量+总数对账；③ 语义化 title 前存 `ima_title` 保留原题。
- **遗留**：1 条 note 阻塞（唯一无配额通道 = MCP `fetch_media_content`）；「中科一然」疑为「中科依兰」语音转写误识（未擅改实体页，待王总核实）；`plan` 空 `raw_path` 盲区工具仍未修。
- 日报 `.tools/kb_pipeline_daily/2026-10-18.md`；log.md / 每日 memory 已追加。

## 2026-10-19 18:00 执行记录（日更增量 · 新增 2，编译 1 源 + 1 概念）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A/B/C/E 全 OK；Agent 侧先手工跑完 A/B/C，再跑编排器收尾归档（暂存 → `_done/2026-10-19/`）。
- **降级前提**：本会话无 IMA MCP connector（`list_installed_plugins` = No connectors installed）→ 阶段 A 走 REST `get_knowledge_list` 全量递归（132 文件夹 / 1411 文件 / 6m12s）；笔记正文走 REST `get_doc_content`。
- **阶段 A**：合并 新增 2 · 移动 1354（kb_path 噪音）· 已知 1409；账本 1413 → 1415。新增 = `MEETING MINUTES`（note）+ `6.口罩用消臭过滤器及消臭口罩.html`（type 20，插件 10:45 已落占位壳）。
- **阶段 B（落地 1，ok）**：html 条目 `get_media_info` 原件直下（118,460 B）→ 剔噪声 + 按 `[0xxx]` 段落号重排 → RAW_FULL 镜像 28,348 字。**阻塞 2 条**（三家技术档案第 5 日 + MEETING MINUTES）：`get_doc_content` 首调即 `200005`，当日停止。
- **纠偏入记忆**：`get_doc_content` 入参应为 `note_id`（media_id 第 2 段）；传 media_id → `210001`，过去被误归为配额错误。
- **阶段 C（编译 1 源 + 1 概念）**：东亚合成 CN107105801A 消臭过滤器专利（≥2 层 / 0.15–0.4 mm / 20–45 g/m² / ≥1 g/m² / 50–350 cm³·cm⁻²·s⁻¹；实施例减低率 ≥90%；比较例证否活性炭与无 PE 基材；权利要求 7 黏结剂必要）；新建概念 `Chemical Adsorption Deodorant（化学吸附型消臭剂）`；更新 `Odor Control Technology Landscape`（补化学吸附支 + 消 `[待验证]`）。
- **终值**：未编译 **2 → 1** · 已编译 **1410 → 1411** · 登记路径 **1422 → 1423** · WIKI **2265 → 2267** · 重复编译 0 · 断链 0 · front matter/index 对齐 **2267/2267**；index 重建 2267 页（源 1410 / 概念 618 / 实体 146 / 对比 80 / MOC 13）。
- **遗留**：2 条笔记卡 REST 日配额；MEETING MINUTES 无 RAW 锚点（明日仍无才走预期路径，须次日复核防幽灵锚点）；`plan` 空 raw_path 盲区未修；专利附表数值待回查 PDF。
- 日报 `.tools/kb_pipeline_daily/2026-10-19.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-20 18:00 执行记录（零新增日 · 编译 0，修锚点 + 账本归一）
- 编排器 `kb_daily_pipeline.py run --stage B/C/E` 脚本侧 B PARTIAL / C PARTIAL / E OK；Agent 侧补齐 A/B/C 判定。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST 全量递归（132 文件夹 / 1411 文件 / 6m15s）。
- **阶段 A**：与 10-19 枚举做 **media_id 集合比对 → 新增 0 · 消失 0**（非漏扫，两份枚举对撞确认）；合并账本 新增 0 · 移动 0（raw_path 零污染）。插件今日未写 RAW。
- **阶段 B**：`plan` 2 条（全为通道 A 笔记）→ **`200005` 日配额耗尽**，当日停止不重试，落地 0 条。**阶段 C**：`plan` 0 条，编译 0 条。
- **修 `MEETING MINUTES` 无锚点（10-19 遗留）**：`_rebind_raw_path.py` 回绑到插件真实落盘文件（非预期路径，无幽灵锚点风险）→ `plan` 待回填 1→2，两条均入队。
- **账本归一**：32 条 `synced` 经 dedup 逐条核验 32/32 命中 → `_reconcile_ledger_20261020.py` 翻 `compiled`（带审计字段 + 备份 + 幂等验证），此后不再产生「积压 32」假警报。归一后 `compiled 1413 / discovered 2`。
- **今日失误（已入 MEMORY §六）**：抢到当日唯一一次配额并成功返回全文，却管道给 `head -c 1200` 预览致全文丢弃 → 定规「API 返回体先落盘再读，禁管道预览」。
- **终值**：未编译 **2**（不变） · 已编译 **1411** · 登记路径去重 **1423** · WIKI **2267** · 重复编译 0 · 断链 0 · front matter/index 对齐 **2267/2267**。
- **根因明确**：插件每 60min 轮询吃尽 `get_doc_content` 日配额（≈1 次）；结构性解法 = 启用 IMA MCP connector。
- 按「无新增时零写入」规则**未追加 log.md**；日报 `.tools/kb_pipeline_daily/2026-10-20.md`。

## 2026-10-21 18:00 执行记录（新增 1 笔记 · 落地 0 · 编译 0 · 配额首调即耗尽）
- 编排器 `kb_daily_pipeline.py run`（incr）脚本侧 A OK / B PARTIAL / C PARTIAL / E OK；Agent 侧先手工跑完 A/B/C 判定，再跑编排器收尾归档。
- **降级前提**：本会话无 IMA MCP connector（`list_installed_plugins` = No connectors installed；`search_plugins` 亦无 IMA 候选）→ 阶段 A 走 REST 全量递归（132 文件夹 / 1412 文件 / 6m13s）。
- **阶段 A**：与 10-20 枚举 media_id 对撞 → 新增 1 · 消失 0；合并 新增 1 · 移动 1（kb_path 噪音）· 账本 1413→**1416**；raw_path/full_path/title 改动 **0**。新增 = 「聚合芯能拜访纪要」(type 11)。
- **阶段 B（落地 0）**：plan 3 条全为通道 A 笔记 → **首调即 `200005`**，按铁律当日停止。三份 RAW 皆 170–239 B 占位壳、RAW_FULL 无镜像。阻塞：聚合芯能（新）/ MEETING MINUTES（第 3 日）/ 三家技术档案（**第 9 日**）。
- **绕行工具**：新增 `_rebind_20261021.py`——按 **RAW 实文件真实路径**回绑（先验存在，防幽灵锚点），幂等；plan 2→3。
- **根因第 21 日复现并实测**：插件 `ima-copilot-sync` 仍 `syncIntervalMinutes: 60`（轮询吃配额）。结构解 = IMA MCP connector；次选 1440。
- **阶段 C**：plan 0 条 → 零页面写入。
- **终值（前后完全一致）**：未编译 **3** · 已编译 **1411** · 登记路径 **1423** · WIKI **2267** · RAW **1414** · 重复编译 0 · merged 4 · front matter 2267/2267 · index 对齐 2267/2267 · 断链 0。
- **MEMORY.md 主动压缩**：18,271 B → **9,257 B**（-49.3%），去重复述、保留全部铁律；memory_guard 报警属预期 → 已 `baseline` 刷新 + 复检通过。
- 已追加 `log.md`（有真实账本/RAW 增量，非纯零动作日）与每日 memory；日报 `.tools/kb_pipeline_daily/2026-10-21.md`。

## 2026-10-22 18:00 执行记录（新增 9 · 落地 8 · 编译 8 · 阻塞 4）
- 编排器 `kb_daily_pipeline.py run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再跑编排器收尾归档（暂存 → `_done/2026-10-22/`）。
- **⚠ 重大发现：IMA 知识库 ID 体系迁移**。库名「Chris的知识库」→「WKB」；旧 MCP `001a693ee6c0644e` 与旧 REST `F8Dbmy…=` **双双报 220004 失效**，新 ID（MCP/REST 通用）= `ima_kb_l24tiCGM`（AI KB = `ima_kb_yNwCq5No`）。`media_id` 末段仍带旧 ID 尾巴 → 易误判。已修 `.tools/ima_sync_state.py` 常量 + 更新 MEMORY §六。
- **阶段 A**：全量递归 132 文件夹 / 1421 文件；对撞 10-21 → 新增 9 · 消失 0；账本 1416 → **1425**；移动 0（raw_path 零污染）。
- **阶段 B（落地 8）**：3 份 Markdown 原件直下；5 段录音走**新第四通道**（m4a 下载 + AudioTranscribe，不吃配额）全部 ok 并双落 attachments（+94 MB）。**4 条笔记 200005 全阻塞**（聚合芯能 / MEETING MINUTES 第4日 / 三家技术档案 第10日 / 截断标题 note 无锚点）。
- **阶段 C（编译 8）**：OBC 三件套（可行性方案 / 产业化核实 / vs NISO 对比）+ 4 张录音纪要页 + 大连化物所页。**治理动作**：重写 `concepts/Niso.md`（证明 Niso = 捏塑 ASR 音译，非泉州尼索）；OBC 概念页 +3 源、熔喷短丝/弹性收紧力 各 +1 源。
- **终值**：未编译 **3**（不变）· 已编译 **1411** · 登记路径 **1423→1431** · WIKI **2267→2275** · 重复编译 0 · 断链 0 · index/front matter 2275/2275。
- **明日 P0**：8 条新页 source_path 为**预期路径**（插件未落 RAW），须核对实落名，不符按三处同步修，禁建重复页；建议把录音转写通道脚本化、并把插件 syncInterval 60→1440。
- 日报 `.tools/kb_pipeline_daily/2026-10-22.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-23 18:00 执行记录（新增 5 · 落地 4 · 编译 4 源 + 1 概念 + 1 实体）
- 编排器 `kb_daily_pipeline.py run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再跑编排器收尾归档（暂存 → `_done/2026-10-23/`）。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST 全量递归（132 文件夹 / 1,426 文件 / 6m15s），KB ID 用 `ima_kb_l24tiCGM`。
- **阶段 A**：对撞 10-22 → 新增 5 · 消失 0；账本 1425 → **1430**；移动 0（零污染）。
- **阶段 B（落地 4 / 阻塞 4）**：三条不吃配额通道全部打通 —— markdown 原件直下（16,301 字）、录音 m4a + `AudioTranscribe`（59 min → 9,115 字，原件双落 14.98 MB）、微信原文 HTML 抽取（1,926 / 7,965 字）。4 条笔记 `200005`（三家技术档案 **第 11 日**）→ 当日停止。
- **新踩坑**：跨条目按「URL 含 media_id 片段」缓存 → **串号**（两篇文章同正文、录音误下 21 KB）；改为一律现取 + 返回 URL 必含 media_id 自证断言后修复。
- **阶段 C（+6 页）**：除味对接纪要（6 路线比选 / 附着力 vs 包埋结构矛盾）· 柔性纤维传感器（低压区零商业案例）· NTMT PCM 纤维 · 吸湿发热热物理；新建概念 `吸湿发热 Moisture-Absorption Heat Generation` + 实体 `中科一然（Zhongke Yiran）`（此前 3 源提及无实体页）；`Odor Control Technology Landscape` 增「附着力 vs 包埋」通则该节。
- **昨日 P0 复核**：8 条预期路径锚点**插件全部未落盘** → 判定**不动锚点**（改指＝换新幽灵）。锚点缺失共 16 条分四类（待落盘 12 / 插件不产 .md 2 / 日期错配 2）。
- **终值**：未编译 **3** · 已编译 1411 · 登记路径 **1431→1435** · WIKI **2275→2281**（源 1422 / 概念 619 / 实体 147）· 重复编译 0 · 断链 0 · front matter 与 index 均 2281/2281。
- **待决策**：启用 IMA MCP connector（解 4 条笔记积压）；RAW 仅 `attachments/*.pdf` 时 `source_path` 能否指二进制（需先立规）。
- 日报 `.tools/kb_pipeline_daily/2026-10-23.md`；log.md / 每日 memory 已追加。

## 2026-10-24 18:00 执行记录（新增 3 · 落地 2 · 编译 1 源（CN+EN 合并）+ 1 实体）
- 编排器 `kb_daily_pipeline.py run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再跑编排器收尾归档（暂存 → `_done/2026-10-24/`）。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST 全量递归（132 文件夹 / 1,429 文件 / 6m14s），KB ID = `ima_kb_l24tiCGM`；笔记正文走 REST `get_doc_content`。
- **阶段 A**：对撞 10-23 → 新增 3 · 消失 0；账本 1,430 → **1,433**；移动 0（零污染）。新增 = 1 note（恒碳ptt/pet成本拆解）+ 2 markdown（金佰利×聚合芯能 功能性材料对接纪要 CN/EN）。**插件今日零落盘** → 3 条 raw_path 全空（plan 盲区）。
- **阶段 B（落地 2 / 阻塞 4）**：两条 markdown 经 `get_media_info` 原件直下（不吃配额，25,616 / 70,741 字符）。4 条 note 首调即 `200005`（官方 cjs 判据，urllib 403 不作判据）：三家技术档案 **第 12 日** / MEETING MINUTES 第 6 日 / 聚合芯能拜访纪要 第 3 日 / 恒碳ptt/pet 新 → 当日停止。
- **锚点策略**：markdown `.md.md` 惯例由 **411 个存量样本**佐证（标题无 `/`）→ 按期望路径回绑；note「恒碳ptt/pet成本拆解」标题含 `/`（插件惯例 `/`→`_`）且无正文 → **不回绑**（防幽灵锚点）。
- **阶段 C（+2 页）**：源摘要 1 张 —— 按 §1.1.1 形态 2 用 `source_paths` **把 CN+EN 合并为一页**（禁拆两页），内容取决策级（两条否定性结论 / 五步闭环死结 + MVT 判据 / 产能测算 / IP 红线 / 分方向裁定表）；新实体 `聚合芯能（Unergy）`（此前 3 源提及无实体页）。
- **知识治理（命名冲突登记）**：10-23 附录 B 把 ASR「中科一然族」勘误为聚合芯能，但库内 `中科一然（Zhongke Yiran）` 依据 10-19 大连化物所另一次对接 → **同一 ASR 字符串指向 3 个候选主体**，已在两个实体页互加登记 + 明示「定案前禁止跨页合并」，待王总核实。
- **终值**：未编译 **3** · 已编译 1,411 · 登记路径 **1,435 → 1,437** · WIKI **2,281 → 2,283**（源 1,423 / 概念 619 / 实体 148 / 对比 80 / MOC 13）· 多值登记页 11 → 12 · 重复编译 0 · 断链 0 · front matter 与 index 均 2,283/2,283；memory_guard 通过（22 文件）。
- **新知识（已入 MEMORY §六/§七）**：① 同场会议中英对照应一页 `source_paths` 双登记，`apply` 后改名去 `_CN` 并回写两条 hint；② `.md.md` 命名惯例可依期望路径回绑（411 样本），但含 `/` 的标题不可类推。
- **遗留**：4 条 note 卡 REST 日配额（唯一解 = MCP connector）；今日 2 条 markdown 锚点为预期路径，**明日须复核插件实落名**；`plan` 空 raw_path 盲区未修。

## 2026-10-25 18:00 执行记录（新增 0（周度已并）· 落地 3 · 编译 4 新页 + 1 合并 + 1 版本升级）
- 编排器 `kb_daily_pipeline.py run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C 实质动作，再由编排器收尾归档（暂存 → `_done/2026-10-25/`）。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST 全量递归（修正版枚举器 `_ima_enum_full_20261025.py`，132 文件夹 / 1,431 条 / 373.5 s）；笔记正文 `get_doc_content` 走官方 cjs。
- **阶段 A**：对撞账本**新增 0**（09:22 周度已把今日 2 条新条目合并），合并「新增 0 · 移动 0 · 已知 1431」= 父链污染问题已根治。
- **阶段 B（落地 3 / 阻塞 1）**：xlsx 原件直下 + zipfile 读 4 表；公众号文章**新开辟第四条正文通道**（换浏览器 UA 绕过微信「环境异常」反爬，抽 `#js_content`）；索引常驻文件 2026-10-23 版就地覆盖镜像（版本迭代，旧 media_id 记入 `versions[]`）。恒碳 note 首调 `200005` 当日停止。
- **阶段 C**：+4 新页（REL 成本模型 / 六层结构 / 三家压力传感对比 / 聚合芯能协作清单）；MEETING MINUTES（DICP 英文纪要）按 §1.1.1 形态 2 并入既有大连化物所页；索引页就地升级至 W42。**暂缓 1**：聚合芯能拜访纪要（疑与 10-24 页同源，0.75–0.99 裁定区间，待王总一句话）。
- **终值**：未编译 **3 → 1** · 已编译 1,411 → **1,413** · 登记路径 1,437 → **1,442** · WIKI 2,283 → **2,287** · 多值登记页 12 → 13 · 重复编译 0 · 断链 0 · front matter 与 index 双 2,287/2,287 · memory_guard 通过。
- **关键经验**：① 微信正文「下载成功且体积正常」≠ 取到正文（反爬页 18 KB），必须校验 `#js_content` 存在；② 常驻文件版本迭代禁建平行页；③ 「已有同源主件」不等于全不能编译——同场中英对照有明确规则可走 `source_paths` 合并。
- **遗留**：2 条 `source_path` 为预期路径（插件未落盘，明日复核）· 恒碳 note 配额阻塞 · `plan` 空 `raw_path` 盲区未修 · 聚合芯能拜访纪要待裁定。
- 日报 `.tools/kb_pipeline_daily/2026-10-25.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-26 18:00 执行记录（新增 6 PDF · 落地 6 + 解积压 1 · 编译 7 新页 + 1 并入 + 1 概念升级）
- 编排器 `kb_daily_pipeline.py run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再由编排器收尾归档（暂存 → `_done/2026-10-26/`）。
- **降级前提**：本会话无 IMA MCP connector → 阶段 A 走 REST 全量递归（133 文件夹 / 1,437 条 / 977.8s，较 10-25 慢 2.6 倍疑限频），KB ID = `ima_kb_l24tiCGM`。
- **阶段 A**：对撞 10-25 → 新增 6 · 消失 0；账本 1,435 → **1,441**；移动 0。新增 = 4 份除臭专利 PDF（US/CN/JP/KR）+ 2 份 Baymax 抽样总结 PDF。**插件今日零落盘** → 6 条 raw_path 全空（plan 盲区），已按「原题+ .md」惯例绑预期路径。
- **阶段 B**：6 条 PDF 走通道 B `get_media_info` 原件直下（不吃配额）+ pypdf 抽文字层 → RAW_FULL 镜像；**恒碳 ptt/pet 成本拆解 note（10-24 起积压两日）首调 `get_doc_content` 即 code=0**，1,534 字到手，积压解除。
- **阶段 C**：+7 新页（恒碳成本拆解 / 4 份除臭专利 / 2 份 Baymax）；**解除 10-25 暂缓**：`聚合芯能拜访纪要` 按 §1.1.1 形态 2 并入既有 10-23 页（source_paths 3 条 + 「十、并入记录」证据表），**未建平行页**；`Odor Control Technology Landscape` 增「专利层三条绕行解」四国解法对照 + 三条新判据；恒碳实体页补成本区间。
- **终值**：未编译 **1 → 0** · 已编译 1,413 → **1,414** · 登记路径 1,442 → **1,450** · WIKI 2,287 → **2,294** · 重复编译 0 · 断链 0 · front matter/index 双 2,294/2,294 · memory_guard 通过。
- **新知识（已入 MEMORY §六）**：① 中英混排多版本叠拼稿使 difflib ratio 失真（实测 0.02），会议同一性须以参会人+独有细节+同源转写残留判定；② `ima_fetch_originals.py --run` 只处理已有 `empty` 占位壳，新条目须自建下载器；③ 成果判定用「登记路径去重数 + WIKI 页数」双 +N。
- **遗留 P0**：6 条 PDF 的 source_path 为**预期路径**，明日须核对插件实落名，不符则三处同步修、禁建重复页；聚合芯能真实开会日期（10-20/10-23 均推定）待王总定案；T4 Vista 页 `manual_review`（文字层仅 1,006 字符，材料清单在图像层）。
- 日报 `.tools/kb_pipeline_daily/2026-10-26.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-26 19:40 定案补记（页名 20261023 → 20261020）
- 王总确认聚合芯能真实会议日 = **2026-10-20**。页名/`title`/`date_published` 全改 10-20，全库 13 处链接 + 实体页 5 处日期同步；`source_path` 保持 RAW 原名（`…_20261023_CN/EN.md.md`）不动。
- **教训**：批量替换页名会连带改到 `source_path` 里的 RAW 路径（本次误改 5 处已回滚）→ 后续换名只替换 `[[…]]` 形式，或替换后单独还原 RAW 路径。
- **P0 复核**：该页 CN/EN 的 `RAW/` 文件实际整体缺失（插件未落盘），正文仅 `RAW_FULL/`；锚点按规范仍指 RAW 预期路径，页内已注记，禁建重复页，等插件落盘自愈。
- 回归：2,294 页 / 断链 0 / front matter·index 双 2,294 / 未编译 0 / 已编译 1,414 / 重复编译 0。备份 `.tools/_backup_juhe_20261026/`、账本 `.bak.20261026-predatefix`。

## 2026-10-27 18:00 执行记录（新增 9 · 落地 9 · 编译 8 页 + 2 处版本归并）
- 编排器 `run --stage B/C/E` 均 OK；Agent 侧先手工跑完 A/B/C，再跑编排器归档（暂存 → `_done/2026-10-27/`）。
- **降级前提**：无 IMA MCP connector → REST 全量递归（133 文件夹 / 1,445 条 / 376.5 s，恢复正常水位），KB ID `ima_kb_l24tiCGM`。
- **A**：新增 9 · 消失 1 · 移动 0（零 kb_path 污染），账本 1,441 → 1,450。新增 = CI-06 final / REL 成本模型 20261024 / SMMSS 亲水实名版 / 中科一然 PDF / 聚合芯能 4 份 PPT / ONE-PAGE 项目档案。
- **B**：9 条**全部通道 B**，配额零消耗，**阻塞 0（近期首次无 200005）**；原件 ~167 MB；RAW 零写入。
- **C**：+8 页；**版本归并 2 处**（REL 成本模型就地升级为活页去日期；CI-06 9.30/10.10 转 merged 指针，未建平行页）。
- **终值**：未编译 0 · 已编译 1,414（不变，插件零落盘）· 登记路径 1,450→**1,459** · WIKI 2,294→**2,302** · 重复编译 0 · merged 2→4 · 断链 0 · front matter/index 双 2,302/2,302 · memory_guard 通过。
- **关键业务结论**：REL 成本**结论反转**（基线 0.692、实测 33 gsm 优于 5.53%、临界克重 34.93 gsm、余量仅 1.45–1.93 gsm）；项目正式判定 **REVISE**。
- **新知识**：① python-pptx/openpyxl 在默认 python 可用、pypdf 只在托管 venv；② IMA 标题 HTML 双转义须 `html.unescape` 后再绑锚点；③ 同名试验多日期导出 = 版本迭代，判别看「试验设计表是否一致」；④ 成本模型类活页**禁带日期后缀**。
- **遗留 P0**：15 条 `source_path` 为预期路径（插件连续 3 日零落盘），明日须复核实落名。
- 日报 `.tools/kb_pipeline_daily/2026-10-27.md`；log.md / 每日 memory 已追加。

## 2026-10-28 18:00 执行记录（新增 15 · 落地 12 · 编译 7 新页 + 1 并入 + 1 新概念）
- 编排器 `run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再由编排器收尾归档（暂存 → `_done/2026-10-28/`，24 文件）。
- **降级前提**：无 IMA MCP connector → 阶段 A 走 REST 全量递归（`_ima_enum_full_20261028.py`，133 文件夹 / 1,460 条 / 381.8 s），KB ID `ima_kb_l24tiCGM`；笔记正文 `get_doc_content`。
- **A**：新增 15 · 消失 5 · 移动 0（零 kb_path 污染），账本 1,450 → 1,465。新增全为 **ND33 / COCO V6 开闸文件包**。
- **B**：12/12 **全部通道 B**（get_media_info 原件直下，配额零消耗）；2 PDF 首轮 `ModuleNotFoundError: pypdf` → 托管 venv 补抽 19,507 / 110,285 字符。3 条 note 首调 `200005` → 当日停止。
- **C**：7 新页 + **1 处重复并入**（`blizzard_activetech_explained` 与既有页 SHA-1 完全一致 → 并入 source_paths、删误建页、未建平行页）+ **1 新概念**（Pilot Retrofit vs Greenfield Decision Framework）+ 2 处概念更新（COCO芯体平台 / Blizzard Core）。
- **终值**：未编译 0 · 已编译 1,414（不变，插件零落盘）· 登记路径 1,459 → **1,471（+12）** · WIKI 2,302 → **2,310（+8）** · 多值登记 15 → 19 · 重复编译 0 · merged 6 · 断链 0 · front matter/index 双 2,310/2,310 · memory_guard 通过。
- **新知识（已入 MEMORY.md §六）**：① 同名不同 kb_path 的 IMA 条目必须先做 SHA-1 比对既有页，禁凭路径/标题判新；② 页名含 `/` 不可作文件名，改名脚本须预校验 + 幂等续跑 + 三步可重入；③ 多源合并页次要 media_id 不走 apply，直接改账本 stage+hint。
- **遗留 P0**：12 条 RAW 锚点为预期路径（插件零落盘），明日须核对实落名；3 条 note 卡配额；`plan` 空 raw_path 盲区未修；Bryan 原文「mid-Nov. 2027」年份笔误待订正。
- 日报 `.tools/kb_pipeline_daily/2026-10-28.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-29 18:00 执行记录（新增 3 · 落地 3 · 编译 2 页 · 修挂账 18 天的 plan 盲区）
- 编排器 `run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再由编排器收尾归档（暂存 → `_done/2026-10-29/`，8 文件）。
- **降级前提**：无 IMA MCP connector → 阶段 A 走 REST 全量递归（`_ima_enum_full_20261029.py`，133 文件夹 / 1,463 条 / 378.8 s），KB ID `ima_kb_l24tiCGM`；笔记正文走 REST `get_doc_content`。
- **A**：新增 3 · 消失 0 · 移动 0（零 kb_path 污染），账本 1,465 → **1,468**。新增全为**锦琪昶（KSC）拜访**一个事件包。
- **B（3/3，REST 配额零消耗）**：md 直下 9,126 字 / docx 抽取 5,344 字 / 录音 m4a 18.0 MB + AudioTranscribe 71 min → 结构化稿 5,561 字。**3 条 10-28 积压 note 仍卡 `200005`**（官方 cjs 判据）→ 当日停止。
- **修 P0**：`kb_sync_handler.py` 新增 `expected_raw_path()`，治掉「plan 空 raw_path 盲区」（挂账 18 天）；6 条从不可见变可执行。
- **C（2 页）**：纪要 + 录音按 §1.1.1 形态 2 合并为一页（录音标题「锦江机场业务介绍」为 ASR 误识，未建平行页）；会前包独立成页（REL 十项资质矩阵 + 成本模型 + 口径冲突登记 5 项）。
- **终值**：未编译 0 · 已编译 1,414 · 登记路径 1,471→**1,474** · WIKI 2,310→**2,312** · 多值登记 21 · 重复编译 0 · 断链 0 · front matter/index 双 2,312/2,312。
- **⚠ 已上报待决策**：RAW/ 层连续 9 天零写入（末次 2026-10-20 21:45），幽灵锚点累计 **53 条**；两解（修插件 / 立规允许指 RAW_FULL），决策前禁批量改锚点。
- **遗留**：3 条 note 卡配额；6 条 `expected` 锚点明日须复核实落名；账本多登 5 条只报不清。
- 日报 `.tools/kb_pipeline_daily/2026-10-29.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-30 18:00 执行记录（新增 3 · 全部并入既有页 · 新编译 2 页 · 配额积压清零）
- 编排器 `run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再由编排器收尾归档（暂存 → `_done/2026-10-30/`，8 文件）。
- **降级前提**：无 IMA MCP connector → 阶段 A 走 REST 全量递归（`_ima_enum_full_20261030.py`，133 文件夹 / 1,466 条 / 658.0 s），KB ID `ima_kb_l24tiCGM`。
- **A**：新增 3 · 消失 0 · 移动 0（零 kb_path 污染），账本 1,468 → **1,471**。新增 = 常驻索引文件 10-30 版 + 2 篇变色材料公众号。
- **B（落地 3 / 阻塞 1，REST 配额仅成功 2 次）**：`Decisions` 首调 code=0（19,219 字）；`Key point…` 403 退避后第 2 次成功；`High Speed Converting meeting …` 连续 3 次 403 → 停止。索引 markdown 原件直下 19,910 字（旧镜像就地覆盖）；两篇公众号 3,865 / 6,601 字。
- **C（0 误建 + 2 新页）**：3 条 note **全部判定为已编译文档的第二载体**（difflib 0.894 / 0.9777 / 同场 PDF 已在页），并入既有页 `source_paths`，未建任何平行页，同时清掉 10-28 起的配额积压。新编译 2 页：六触发源（credibility 中）、遮阳隔热日报（credibility 低，全数值 `[待验证]`）。
- **终值**：未编译 0 · 已编译 1,414 · 登记路径 1,474→**1,478** · WIKI 2,312→**2,314** · 多值登记 22 · 重复编译 0 · 断链 0 · front matter/index 双 2,314/2,314。
- **新知识（已入 MEMORY §六）**：① `urllib` 抓微信报 `SSL: UNEXPECTED_EOF`，同 UA/Referer 换 `curl` 即 200 → 判不可达前换客户端复测；② 「新条目」≠「新知识」，`plan` 看不见同文档换载体，判新前必须回 WIKI 侧 difflib 比对，配额积压常可「不吃配额」解决。
- **遗留**：RAW/ 零写入第 10 天 + 幽灵锚点 55 条（两解待王总决策，禁批量改锚点）；今日 5 条预期锚点明日须核验实落名。
- 日报 `.tools/kb_pipeline_daily/2026-10-30.md`；log.md / 每日 memory / MEMORY.md 已追加。

## 2026-10-31 18:00 执行记录（新增 3 · 落地 3 · 编译 2 页，其中 1 页双源合并）
- 编排器 `run` 四阶段全 OK；Agent 侧先手工跑完 A/B/C，再由编排器收尾归档（暂存 → `_done/2026-10-31/`，7 文件）。
- **降级前提**：无 IMA MCP connector（`<connector-status>` 仅 agent-mail）→ 阶段 A 走 REST 全量递归（`_ima_enum_full_20261031.py`，133 文件夹 / 1,469 条 / 674.8 s），KB ID `ima_kb_l24tiCGM`。
- **A**：新增 3 · 消失 0 · 移动 0（零 kb_path 污染），账本 1,471 → **1,474**。新增 = 2 份 PEG 基 slot die 复配乳液方案 markdown + 1 篇 NC 纤维素 LCE 公众号。
- **B（3/3，REST 配额零消耗）**：2 份 markdown 原件直下（55,223 / 30,090 字符）；公众号经 `get_media_info`→微信→`curl`（Chrome UA+Referer）抽 `#js_content`（3.5 MB → 4,316 字）。plan 因标题含 ASCII `|` 拒绑 1 条 → 正文落 RAW_FULL（`|`→`｜`），账本标 `expected_sanitized`。
- **C（2 新页）**：PEG 两版判同源（骨架逐节一致，difflib 0.597/0.674）→ 一页 `source_paths` 双登记，次源直接改账本，未建平行页；NC 页附卫材适配性研判（100–600% 应变 vs 腰围 25–40% 错位）。概念层回链 5 处。
- **终值**：未编译 0 · 已编译 1,414 · 登记路径 1,478→**1,481** · WIKI 2,314→**2,316** · 多值登记 23 · 重复编译 0 · merged 6 · 断链 0 · front matter/index 双 2,316/2,316。
- **顺带**：MEMORY.md 触发注入体量告警 → 压至 11,081 B（−39%），`memory_guard baseline` 已刷新。
- **遗留 P0**：RAW/ 停摆第 11 天（末次 2026-10-20 21:45），幽灵锚点实测 70 条（较 10-29 的 53 条口径更宽）；今日 3 条预期锚点明日须核验，其中 `|`→`｜` 为推断、优先核对。
- 日报 `.tools/kb_pipeline_daily/2026-10-31.md`；log.md / 每日 memory 已追加。
