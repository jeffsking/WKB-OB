# WKB-OB 项目长期记忆

_跨会话铁律。日常流水记 `.workbuddy/memory/YYYY-MM-DD.md`。精简版（2026-10-31 压缩去重 18.2KB→9KB）。_

---

## 一、自动化治理

1. 接管既有自动化 → **原地改造，禁「删除+新建」**（删建=切断执行记忆血脉+双条冲突）。
2. **文档修改 ≠ 配置修改**，交付须给实况核验证据。
3. 真实行为唯一硬证据 = DB `automation_runs`（`~/.workbuddy/workbuddy.db`，`runs_json.conversationId` 回溯全文），**无「立即运行」字段**。
4. `automation_update list` ≠ DB ACTIVE；UUID 型 ID 工具够不着，脱管仅噪音，清理先备份整库。自动化会话可被人工接管续聊 → 查历史任务首要排除项。

---

## 二、数据一致性与判重

1. **判重唯一权威 = `.tools/wkb_dedup.py scan`**，禁手写另算（旧 101/415/518/480 均错口径，禁引）。
2. **三层架构**：`RAW/` 只读（唯一事实锚+判重锚，**绝不写入**）；`RAW_FULL/` 正文镜像（`extract_status`）；`WIKI/` 编译层。`source_path` **一律指 `RAW/`**。
3. **判重须收 3 形态**：单值 `source_path` / 多值 `source_paths` / 跨条目合并页。**正则禁 `\s*`（用 `[ \t]*`）**；先自证覆盖率再下结论。
4. merged 指针页保留原 source_path → 留在已编译索引内、从重复告警剔除。
5. **「编译成功」判据** = 登记路径去重数 + WIKI 页数各 +1，**不是**未编译数下降。
6. 缓存字段降格：hint 命名 + 顶部 `_warning` + 一致性校验（只提示不改）。
7. 同步层：`enumerate` 只写 `kb_path` 不写 `raw_path`；全量 kb_path 重建不可靠（深层 parent 常空）→ 只喂新增；kb_path 口径 = `ima_sync/个人知识库/WKB/<链>`，经 `norm_kb_path()`。
8. `_compile_extractive.py`：source_path 逐字等于 plan raw_path；key_claims 不臆造；幂等。

---

## 三、front matter 字段口径

**三处必须一致：AGENTS §2 示例 + `TEMPLATES/*.md` + 生成器代码；改字段三处同改。** 已三踩（漏 `knowledge_update_status` 483 页；自造 `source_credibility`/`compiled_at`/`related`）。禁自定义同义字段。

---

## 四、concept 库治理

- **新建 concept 前必须库内语义检索**（读定义不只看页名）——20 条「该建页」中 11 条实为重复。
- domain 已治 **133→13**；裁定表 `_unclassified_assign_20261012.json`，重建器 `_rebuild_concept_domains_20261012.py`（新概念入库后跑）。
- **幂等铁律**：归一化脚本输入须取自「不随自身输出改变」的源。
- **人工裁定表须作最高优先覆盖表接入**（`ASSIGN.get(name) or classify(...)`），否则自动归类冲掉人工成果。

---

## 五、断链治理

- 唯一入口 **`.tools/wkb_link_guard.py`**（check/plan/apply/report）；白名单 `link_guard_curated.json`（ast 提取，禁手抄）。改指仅「同名变体」，语义近似一律 SEED，BLOCK 强制 SEED，apply 前备份。断链 **129→0**。**修工具，不改页面迁就工具。**
- **「断链 0」≠「无孤立点」**：孤立点多来自 `RAW_FULL/`、`TEMPLATES/` → 图谱过滤须含 `-path:RAW_FULL -path:TEMPLATES`。
- 语义建链已完成（源页 `## 关联页面`、概念/实体页 `## Related Sources`）→ 孤立 485→139。拉丁字母候选须**词边界**（`cti` 命中 `practice`）；存在性比对**不剥 `.md`**。

---

## 六、IMA ID 与 API 实测

**ID（2026-10-22 迁移，双 ID 结束，MCP/REST 通用）**：WKB `ima_kb_l24tiCGM` / AI KB `ima_kb_yNwCq5No`。旧 MCP `001a693ee6c0644e`、旧 REST `F8Dbmy…=` **均失效**（220004），勿回退；`media_id` 末段仍带旧尾巴属历史命名。写操作前先调 `get_addable_knowledge_base_list` 取 ID。

**取正文通道（按优先级）**：
① MCP `fetch_media_content`（**不吃 REST 配额**；REST 无此端点）；
② `get_media_info` 直下原件（不吃配额）：录音/word/markdown/html/PDF/xlsx 均可；`note_` 只返回 `chrome://note?` 不可下载；
③ 插件偶发已写完整正文 → 直接镜像；
④ **录音**：m4a 下载 → `AudioTranscribe` → 清 `[mm:ss,mm:ss,speaker]` 时间戳；
⑤ **公众号**：默认 urllib UA 必得「环境异常」18KB 空壳（**像正文**）→ 须 Chrome UA + `Referer: mp.weixin.qq.com` 抽 `#js_content`；urllib 还可能 `SSL: UNEXPECTED_EOF` → **同 UA 换 `curl` 即 200**。判「不可达」前必须换客户端复测；
⑥ **xlsx 公式无缓存值** → 只能取输入参数与文字结论（`.tools/_xlsx_dump.py`）。`search_knowledge` 对笔记 `highlight_content` 恒空。

**错误码**：`200001` 频率超限（退避 12s）；`200005` 日配额耗尽（≈1 次/日，当日停）；`210001` note_id 错（= media_id **第 2 段**）；`220030` 条目永久失败（不重试）。**urllib 403 不作判据** → 以官方 `ima_api.cjs` 业务码为准。
**铁律：返回体必须 `>` 落盘后再读，禁管道 head/tail**（10-20 烧掉当日唯一配额）。
**配额根因**：插件 `ima-copilot-sync` 60min 轮询 + 白名单笔误 `20005`（少一位）→ `200005` 误判永久失败。结构解 = IMA MCP connector；次选间隔 1440；**不可关 `syncNotes`**。

**REST 枚举**：不返回 `media_state`/`create_time`/`file_number` → **无法状态过滤或计数剪枝**，只能全量递归 + 总数对账（约 133 文件夹/1,470 文件，6–16 min，间隔 ≥2.5s）。folder(type 99) 源头剔除。标题 ~40 字符截断 → **页名禁用截断标题**（改账本 `title` 语义化、原题存 `ima_title`、重跑 plan）。「移动 N 条」= kb_path 噪音 → 须复核 `raw_path` 改动 = 0。
**账本多登**：`only_in_ledger_no_anchor`（插件未落盘）/ `only_in_ledger_deleted`（双边皆无，只报不删页）。`ima_sync/notes/` 2 条范围外 → 账本恒比枚举多 2。**「IMA 侧消失」≠「知识丢失」**。

**plan 空 `raw_path` 盲区（10-29 已修）**：`expected_raw_path()` 按 kb_path + 命名惯例推导 `RAW/<kb_path>.md`（`.md` 标题得 `.md.md`），标 `raw_path_source: expected`；**标题含 `/\:*?"<>|` 拒绑**。apply 后 `page_name` 仍按 raw stem → 须改名并回写 hint。

**⚠ 幽灵锚点（53 条）+ RAW/ 停摆（末次落盘 2026-10-20 21:45）**：预期路径 ≠ 实落名 → **永久假欠账**，rebind「仅绑空值」够不着；修须**三处同步**（RAW_FULL 镜像 + 账本 raw_path/full_path + WIKI source_path），并入既有页、禁建重复页。判重按字符串故日常无感。**决策前禁批量改锚点**（改指即换新幽灵）。两解：修插件 / 立规允许指 RAW_FULL（须改 AGENTS §1.1.5 + 全库迁移）。

**「新条目」≠「新知识」——判新前必回 WIKI 比对**：`plan` 只比账本 stage，**看不见「同文档换载体重新入库」**。拿 plan 条目正文与库内同题页原件做**逐词 difflib**（10-30 实测 0.894/0.9777；PDF↔note 的 0.80–0.89 差异**全部**来自连字 `ﬂ/ﬁ` 与丢词间空格，去空白不升反降属正常）。同源 → 并入 `source_paths` + 账本标 compiled 写理由。**推论：配额阻塞的 note 积压常可「不吃配额」解决**。同名不同 kb_path 必先 **SHA-1**（10-28 实证一致）。
**difflib 失真**：中英混排+章节乱序的叠拼稿 ratio 可低至 **0.02** → 0.75–0.99 假设「定型稿对定型稿」，**不可机械套用**；会议同一性以参会人 + 独有细节 + 同源转写残留判定。

**多源合并页**：同场会议中英对照 → **一页 `source_paths` 双登记**（§1.1.1 形态 2），禁拆两页；apply 后改名去 `_CN` + 回写两条 hint（范本 `_postcompile_md_20261024.py`）。`apply` 以暂存 `<media_id>.md` 为准、`page_name` 由 raw_path 推导 → 次要 media_id **不走 apply**，直接改账本 `stage=compiled` + hint + `stage_source`。
**版本迭代 / ASR / 命名冲突**：① 常驻文件（索引 md 每周五重写）media_id 变但 RAW 壳不刷新 → 就地更新镜像 + 页面原地升级 + 旧 ID 记 `versions[]`，**禁建平行页**；② 录音标题常为 ASR 误识（「锦江机场」实为「锦琪昶」）→ 页名取语义真名 + 页内注明；③ 同一 ASR 字符串可指多家（「中科一然族」→ 大连化物所/聚合芯能/中科依兰）→ 两页并行 + 互加「命名冲突登记」，定案前禁跨页合并。
**页名规则**：`source_path` 永指插件原名（含批次日不改）；页名与 `date_published` 取**事件真实日**并页内注记。改页名时**批量替换必须排除 `source_path`/`source_paths` 的 RAW 路径**（10-26 误改已回滚）→ 只替换 `[[wikilink]]`。页名禁含 `/`（用全角或 `·`）。改名脚本：写前校验 `/\:*?"<>|`、缺文件跳过、改名/换链接/修 hint 三步分离可重入。
**RAW 锚点缺失 ≠ 判重失效**：RAW 侧可能整体缺失，正文仅在 RAW_FULL；`source_path` 仍指 RAW 预期路径 + 页内「锚点状态」注记 + 待自愈，**禁建重复页**。
**工具**：PDF 用托管 venv `...\envs\default\Scripts\python.exe`（pypdf）；docx 用 `zipfile` 抽 `word/document.xml`；pptx/xlsx 用 python-pptx/openpyxl；专利检索 HTML 常只留表号 → 标 `[待验证]`。`ima_fetch_originals.py --run` 只处理**已有 `empty` 占位壳**，新条目须自建下载器。

---

## 七、知识管道自动化

| ID | 名称 | 频率 | 职责 |
|---|---|---|---|
| `bcaf361b-` | 日更 IMA→Obsidian | 每日 18:00 | A/B/C/E 增量 |
| `808e9058-` | 周度全量对账 | 每周日 09:00 | A/B/C/R/E 全量校准 |
| `5700cc40-` | 记忆防覆盖巡检 | 每日 08:45 | `memory_guard.py check` |
| `8523233b-` | IMA 正文回填巡检 | PAUSED | 已被 `bcaf361b` 覆盖 |

- 模型均 deepseek-v4.1-flash。**架构定案：高频增量 + 低频全量双轨**（增量剪枝累积漂移，全量强制递归打平）。
- **脚本矩阵**：`ima_sync_state.py`(init/enumerate/status) · `kb_sync_handler.py`(plan/apply/gaps/status) · `kb_compiler.py`(plan/apply/stub/verify/status) · `kb_daily_pipeline.py`(run/stage/status)。
- **中继铁律**：MCP 调用只在 Agent 会话内完成，脚本只做合并/落盘。`archive_staging()` 搬 `_done/<date>/`，重复跑 B/C 报 PARTIAL 属正常。状态 OK / PARTIAL(正常) / SKIP / WARN(R 漂移) / FAIL。
- **账本 synced 归一**：`.tools/_reconcile_ledger_20261020.py`（仅 dedup 命中才翻 compiled，先备份，验幂等）。

---

## 八、记忆/记录维护

- **防静默覆盖巡检** `.tools/memory_guard.py`（只读）：体量跌 >20% 或行数减 ≥5 报警；基线只能人工刷新（压缩后须 `baseline` 重置，否则次日误报）。
- **追加式文件永不覆盖**：`log.md`、每日 memory 用 `>>`，**禁 `>`**（10-11 已踩）。

---

_Last updated: 2026-10-31（压缩去重，铁律全保留）_
