# WKB-OB 项目长期记忆

_本项目跨会话有效的方法论铁律与项目约定。日常流水记 `.workbuddy/memory/YYYY-MM-DD.md`。_

---

## 一、自动化治理铁律（2026-10-11 立）

### 1.1 接管既有自动化 → 原地改造，禁止「删除+新建」

**当一个新方案要接管某个既有自动化时，默认应「原地改造既有条目」，而非「删除旧的 + 新建一个」。**

理由：自动化条目携带**执行记忆**（`.workbuddy/memory/automations/<id>/memory.md`，累积的历史执行上下文）。删除重建 = 切断这条血脉，且可能造成两个同职责自动化并存冲突。

**仅当职责真正消失时**才暂停/删除。

**实证**：2026-10-11 王总纠正 —— v2 方案曾写「删除 `bcaf361b` 日志扫描 + 新建」，实为错误。`bcaf361b` 记忆首行即「每日日志扫描（18:00）」，时间本就对齐，只需改 prompt 挂接账本 + PAUSED→ACTIVE。

### 1.2 文档修改 ≠ 配置修改（2026-10-11 立）

**方案类工作必须区分「纸面计划」与「已落地配置」两个状态。**

改写设计文档中的自动化方案，**不等于**实际自动化配置已变更。交付时必须明确告知：哪些是"文档已写"，哪些是"配置已改"。

**实证**：2026-10-11 —— v2 §6.6 写"原地改造 `bcaf361b`"，但只改了文档，实际条目仍停在 PAUSED。王总追问「还是没看到自动化任务」才暴露。

**执行铁律**：凡涉及自动化/配置的变更，**交付时同步给出实况核验证据**（如 `automation_update list` 输出的状态），而非仅凭文档描述。

### 1.3 验证自动化真实行为的唯一硬证据 = `automation_runs` 表（2026-10-11 立）

看 prompt 文本、看文档描述**都不算验证**。真实运行内容在：

```
C:\Users\Chris Wang\.workbuddy\workbuddy.db  →  表 automation_runs
  thread_id / automation_id / status / thread_title(输出正文) / runs_json
```

- `runs_json` 内含 `conversationId` → 可回溯到 `projects/e-WKB-OB/<id>.jsonl` 会话全文
- `automation_runtime_state` 记 `last_run_at` / `running`
- 调度器日志：`.workbuddy/logs/automation.log`（按 `[LocalAutomationScheduler]` 行）
- **无「立即运行」字段** → 手动触发只能等 `next_run_at`，或人工代跑该 prompt 的动作序列

**实证**：`bcaf361b` 历史 9 次运行（10-02~10-09）全部输出「无未处理日志」，**9 次空转**。10-10/10-11 无记录（调度器未 tick）。

### 1.4 会话「被劫持」现象（2026-10-11 发现）

自动化会话（如 `1bd2c8fa`，10-07 18:00 触发）**可被人工接管继续对话**，从 40KB 膨胀到 4.5MB。此时它不再是"丢失的会话"，而是"被劫持的自动化会话"。查找历史任务窗口时应以此为首要排除项。

---

## 二、数据一致性铁律（2026-10-11 立，血泪教训）

### 2.1 判重权威源唯一

- **判定「是否已编译」一律走 `.tools/wkb_dedup.py scan`**，禁止手写脚本另算。
- 权威基线（2026-10-11）：WIKI 1675 页 / 已编译 **911** / 未编译 **471** / RAW 条目 1382。
- 此前所有 101 / 415 / 518 / 480 均为错误口径产物，**禁止再引用**。

### 2.2 缓存字段必须降格命名 + 一致性校验

- 任何「从权威源抄来的缓存」字段，命名必须带 `hint` 等降格标识（如 `source_page_hint`），**禁止用权威式命名**（如 `source_page`）。
- 缓存必须在容器顶部加 `_warning` 声明非权威。
- 必须配**一致性校验**：权威源更新时比对缓存，不一致只提示、不自动改。

理由：缓存会过期 → 成为错误信息源 → 与权威源互相打脸（与当日"假欠账"同款病）。

### 2.3 交付前必须做全文档一致性扫描

写方案/文档时，**多源描述同一件事（字段名、数字、架构图）必须交叉核对**。2026-10-11 的 v2 方案自身犯了此病：§3.4 字段名与 §3.6.1 定案矛盾、§2 架构图与 §6.6 频率定案矛盾。

**做法**：交付前 `grep` 关键字段名 + 数字，而非只改局部。

### 2.4 三层架构铁律（不可破）

| 层 | 角色 | AI 权限 |
|---|---|---|
| `RAW/` | IMA 插件维护的**只读原始层**（唯一事实锚点 + 唯一判重锚） | **绝不写入** |
| `RAW_FULL/` | AI 回填的正文镜像层（含 `extract_status`） | 读写 |
| `WIKI/` | 编译后的知识层 | 读写 |

- `source_path` 一律指 `RAW/`，**禁止 `RAW_FULL/` 路径作判重锚**（否则双路径漏判 → 重复编译）。

### 2.5 判重的 3 种登记形态（缺一必漏判）

1. 单值 `source_path`（常规）
2. 多值 `source_paths`（重复副本 / 专利同族 / 版本迭代）
3. 跨条目合并页（一页覆盖不同资料的多个条目）

**正则铁律**：禁用 `\s*`，一律 `[ \t]*`（`\s*` 贪婪吞换行 → 全库一条都匹配不到）。

**脚本铁律**：扫描后**必须先自证覆盖率**（打印「匹配 N 条 / 缺失 M 条」），再看结论。

### 2.6 已治理重复页的识别

- `status: merged` 的指针页**保留原 `source_path`** 作合并存档线索 → 必然呈现"一条 RAW 被 2 页登记"。
- 判重工具须把 merged 页**留在已编译索引内**（防误报未编译），但**从重复告警剔除**。
- 只看「多页登记 RAW」而不看页面状态，会得出「重复永远治不完」的假象。

### 2.7 `enumerate` 不绑定 raw_path → R 阶段假"漏登"（2026-10-11 周度对账实证）

- `ima_sync_state.py enumerate` 对新条目只写 `kb_path`，**不写 `raw_path`**（`raw_path: null`）。
- 而阶段 R 的「账本 vs RAW」比对是**按 `raw_path` 做的**（`_recon_raw_vs_ledger`）→ 新枚举条目虽已入账本，仍被判为 `only_in_raw`（**假漏登**）。
- **治具**：`.tools/_rebind_raw_path.py` —— 按 `media_id` 匹配 `RAW/**/*.md` 占位符的 front matter，回绑 `raw_path`。回绑后 R 阶段即转 OK。

### 2.8 全量枚举的 kb_path 重建不可靠 → 合并只喂「新增条目」（2026-10-11 立）

- MCP `get_knowledge_list` 的**深层文件夹 `folder_info.parent_folder_id` 常为空字符串**（已知 IMA quirk，与「深入子层后 folder_info 为 null」同源）。
- 仅凭各文件夹列表响应**无法还原真实路径**：会把 `Adhesive`/`chapters`/`Regulation&PSC` 等深层文件夹误判为顶层（实测 45 个"顶层"里只有 5 个是真 PRA 根）。
- **铁律**：账本里已有权威 `kb_path`（历次正确枚举累积）→ 全量枚举合并时**只喂 `media_id` 不在账本中的新增条目**，**绝不回灌重建路径**（否则制造海量假 `moves`）。
- 权威路径来源 = MCP 响应的 `current_path` 字段（本会话分片未采集，故弃用重建路径）。

### 2.9 IMA note 类型条目 MCP fetch 永久失败 = `code:220030`（2026-10-11 立）

- `fetch_media_content` 对部分 IMA 笔记返 `code:220030 该文件获取失败，请至ima内查看处理`。
- 与 `200005`（日配额耗尽，次日可重试）**不同**：`220030` 是**条目级永久失败** → 标记后不再重试，页以 minimal stub 收尾。

### 2.10 抽取式批量编译（2026-10-11 立，清积压专用）

- 大积压（数百条）无法逐条 LLM 精编时，用 `.tools/_compile_extractive.py`：
  - front matter 的 `source_path` **逐字等于** plan 的 `raw_path`（`kb_compiler.py apply` 强校验）；
  - `key_claims: []` **留空不臆造**；正文用「原文抽取 + 截断标注」，可后续深度编译补全；
  - 幂等：页已存在即跳（apply 也会 `skip-exists`）。
- 残余未编译（dedup 口径）用一次性脚本补齐（front matter 精确匹配后写入 `WIKI/sources/<page_name>.md`）。

---

## 三、记忆/记录维护

### 3.1 防静默覆盖巡检

- 工具：`.tools/memory_guard.py`（只读），守护 `log.md` / `index.md` / `AGENTS.md` + `.workbuddy/memory/*.md`
- 判据：体量跌幅 > 20% 或行数减少 ≥ 5 → 报警
- 自动化：每日 **08:45**（`5700cc40-400d-47ee-b3f1-52d993bb9110`）
- **基线只能人工刷新**（`memory_guard.py baseline`），工具不自动更新基线

### 3.2 追加式文件永不覆盖

`log.md`、每日 memory 均为**追加式**（`>>`），**禁止用 `>` 覆盖**。历史教训：2026-10-11 memory 文件 17:41 被 `>` 覆盖，丢失追加一~六。

---

## 四、IMA 知识库双 ID 体系（不可混用）

| 视角 | KB ID |
|---|---|
| MCP / trpc | `001a693ee6c0644e` |
| REST / OpenAPI | `F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI=` |

- 全量枚举：MCP `get_knowledge_list` 用 `001a693...`，limit ≤ 50
- REST 端点：`openapi/wiki/v1/get_knowledge_list` 用 `F8Dbmy...`
- `get_doc_content` 有日配额（`200005`），命中即当日放弃，**禁止循环重试**
- 取正文首选 MCP `fetch_media_content`（**不受 REST 日配额限制**）

### 4.1 枚举能力差异（2026-10-11 实测，决定架构选型）

| 通道 | `folder_info.file_number` | 能否剪枝 |
|---|---|---|
| MCP `get_knowledge_list` | **有值** | ✅ 可剪枝（§4.2 方案的前提） |
| REST `openapi/wiki/v1/get_knowledge_list` | **null** | ❌ 不可剪枝，只能全量递归 |

→ **日更管道必须走 MCP**；REST 仅作只读兜底。

- REST `code 200001` = **请求频率超限**（连续调用过密），非权限问题 → 间隔 8~10s 重试
- REST `code 200005` = `get_doc_content` 日配额耗尽 → 当日停止

### 4.2 账本 kb_path 口径归一（2026-10-11 血泪）

同步层账本 `.tools/_ima_sync_state.json` 的 `kb_path` **统一口径为 `ima_sync/个人知识库/WKB/<链>`（不带 `RAW/`）**。

Agent 侧 MCP 枚举给的常是「文件夹链+文件名」相对名 → 直接比对会把全部条目误报为「移动」并污染 `moves`。**必须经 `norm_kb_path()` 归一**（剥 `RAW/` → 补 `MIRROR_PREFIX`）。

移动判定收紧为「相对容器的尾巴真变化才记」——防标题标点/后缀差异误报。

**验收铁律**：脚本改完必须**连跑两次验证幂等**（第二次应为「新增 0 · 移动 0」），再交自动化无人值守。

---

## 五、知识管道自动化登记

| 自动化 ID | 名称 | 频率 | 模型 | 职责 |
|---|---|---|---|---|
| `bcaf361b-...` | WKB-OB 知识管道 · IMA→Obsidian 日更 | 每日 18:00 | **deepseek-v4.1-flash** | 阶段 A/B/C/E（增量执行体） |
| `808e9058-...` | WKB-OB 知识管道 · 周度全量对账 | 每周日 09:00 | **deepseek-v4.1-flash** | 阶段 A/B/C/R/E（**全量校准器**） |
| `5700cc40-...` | WKB-OB 记忆防覆盖巡检 | 每日 08:45 | — | `memory_guard.py check` |
| `8523233b-...` | IMA 条目正文回填巡检 | PAUSED | — | 旧机制，已被 `bcaf361b` 覆盖 |

**架构定案（2026-10-11）：高频增量 + 低频全量 双轨**
- 日更增量靠文件夹剪枝提速 → 长期会累积漂移（漏枚举/重复件/口径分叉）
- 周度全量强制递归整库 + 黑账核对 → 打平漂移
- 两者职责错开（增量 vs 全量），**不构成 §1.1 意义的同职责重复**

- `RAW/journal/` 保留（阶段 D 独立跑），**但已不是知识进化的唯一入口**——知识更新多数在 IMA 发起。
- **`bcaf361b` 的 prompt 已于 2026-10-11 20:50 接线到四脚本**（1805→2884 字节）：总入口 `kb_daily_pipeline.py run`，各阶段调 `ima_sync_state.py` / `kb_sync_handler.py` / `kb_compiler.py`。旧 prompt 备份 `~/.workbuddy/workbuddy.db.bak-prompt-20261011`。

### 5.1 自动化治理铁律补充：脱管条目识别（2026-10-11 实证）

- **`automation_update list` 的可管理清单 ≠ DB `automations` 表的 ACTIVE 清单**。
- **判据**：**UUID 型 ID（如 `1b59fd84-...`）工具够不着；`automation-*` 型（如 `automation-1780616679654`）才可管**。
- **脱管成因**：`workspaceScope: workspace` 且 cwds 指向已删项目目录的历史条目。
- **脱管风险 = 零**（不在调度清单 = 无 tick 触发），唯一危害是 ACTIVE 假象造成排查噪音。
- **处置**：授权后可改 DB 状态位（先备份整库）。2026-10-11 清理 12 条，ACTIVE 20→8。

---

## 六、日更管道脚本矩阵（2026-10-11 四批 + 第 5 批全部落地）

| 批次 | 脚本 | 子命令 |
|---|---|---|
| 1 | `.tools/ima_sync_state.py` | `init` / `enumerate --input <json>` / `status` |
| 2 | `.tools/kb_sync_handler.py` | `plan` / `apply --bodies-dir <dir>` / `gaps` / `status` |
| 3 | `.tools/kb_compiler.py` | `plan` / `apply` / `stub` / `verify` / `status` |
| 4+5 | `.tools/kb_daily_pipeline.py` | `run [--stage A\|B\|C\|R\|E] [--full]` / `status` |

### 6.0 两种运行模式（第 5 批新增）

| 模式 | 阶段链 | 调用者 | 报告 |
|---|---|---|---|
| 增量（默认） | A→B→C→E | `bcaf361b` 每日 18:00 | `<date>_pipeline.md` |
| **全量 `--full`** | **A→B→C→R→E** | `808e9058` 周日 09:00 | `<date>_full.md` |

**阶段 R（全量对账）铁律 —— 只读不改**：
- `wkb_dedup.py scan`（唯一权威判重入口）+ 账本三口径校验
- **逐条黑账核对**：RAW 实体文件 vs 账本 `raw_path` 双边差集
- 漂移告警：`only_in_raw`（账本漏登）/ `only_in_ledger`（账本多登）/ `dup_live`（重复编译）
- 产物 `.tools/kb_pipeline_recon/<date>_recon.json`
- **口径差异非 bug**：账本 compiled 按 media_id 一对一；dedup 按 source 页计（含 merged 指针页）→ 差 +22 属预期，**只报偏差不判错**
- 状态可为 `WARN`（有漂移）——区别于 `FAIL`（真错误）

### 6.1 中继模式（Relay）铁律

**MCP 调用一律在 Agent 会话内完成；脚本只做合并/落盘**。三处中继：
- `ima_sync_state.py enumerate --input <json>` ← Agent 侧 MCP 枚举结果
- `kb_sync_handler.py apply --bodies-dir <dir>` ← Agent 侧 `_kb_sync_bodies/<media_id>.md` 抓取正文
- `kb_compiler.py apply` ← Agent 侧 `_kb_compile_pages/<page_name>.md` 提炼页面

### 6.2 幂等铁律 —— `archive_staging()`

编排器在 B/C 落盘后把暂存目录文件搬到 `.tools/_done/<date>/`。
**根治"假失败"**：曾把「上次已处理、本次已不在新 plan 里」的暂存文件误计为 `failed`（曾报"失败 12 / 失败 1"）。
配套：`kb_sync_handler.py` / `kb_compiler.py` 的 `not-in-plan` 分支改判 `already-done-or-unplanned`（计入 skipped）。

→ **重复跑的正常表现是 B/C 报 `PARTIAL`（脚本侧完成、Agent 侧待会话），不是 `FAIL`。**

### 6.3 阶段状态语义

| 状态 | 含义 |
|---|---|
| `OK` | 脚本侧 + Agent 侧都完成 |
| `PARTIAL` | 脚本侧完成，Agent 侧抓取/提炼待会话执行（**正常态**） |
| `SKIP` | 前置缺失（如 MCP 枚举需 Agent 输入），如实标注 |
| `WARN` | 对账发现漂移（仅阶段 R），需人工裁定 |
| `FAIL` | 真错误（异常/timeout），报告含 stderr |

---

_Last updated: 2026-10-11_
