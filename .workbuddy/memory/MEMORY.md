# WKB-OB 项目长期记忆

_跨会话有效的方法论铁律与项目约定。日常流水记 `.workbuddy/memory/YYYY-MM-DD.md`。本文件保持精简，超限会被注入截断。_

---

## 一、自动化治理

1. **接管既有自动化 → 原地改造，禁「删除+新建」。** 条目携带执行记忆（`.workbuddy/memory/automations/<id>/memory.md`），删建=切断血脉+可能双条冲突；仅职责真正消失才暂停/删除。
2. **文档修改 ≠ 配置修改。** 凡涉及自动化/配置的变更，**交付时必须同步给出实况核验证据**（如 `automation_update list` 状态），不能只凭文档描述。
3. **自动化真实行为的唯一硬证据 = DB 表 `automation_runs`**（`~/.workbuddy/workbuddy.db`；`runs_json.conversationId` 可回溯会话全文）。调度器日志 `.workbuddy/logs/automation.log`。**无「立即运行」字段** → 手动触发只能等 `next_run_at`。
4. **脱管条目识别：** `automation_update list` ≠ DB ACTIVE 清单。**UUID 型 ID 工具够不着；`automation-*` 型才可管**。成因：`workspaceScope: workspace` + cwds 指向已删目录；风险=零，仅噪音；清理须先备份整库。
5. **会话「被劫持」：** 自动化会话可被人工接管续聊（40KB→4.5MB）——查历史任务窗口时以此为**首要排除项**。

---

## 二、数据一致性（血泪教训）

1. **判重权威源唯一 = `.tools/wkb_dedup.py scan`**，禁手写脚本另算。（旧 101/415/518/480 均错误口径，禁引）
2. **三层架构（不可破）：** `RAW/`=IMA 插件维护的只读原始层（唯一事实锚+唯一判重锚，**绝不写入**）；`RAW_FULL/`=AI 回填正文镜像（含 `extract_status`）；`WIKI/`=编译后知识层。`source_path` 一律指 `RAW/`，禁以 `RAW_FULL/` 作判重锚。
3. **判重 3 登记形态**（缺一必漏）：单值 `source_path` / 多值 `source_paths` / 跨条目合并页。**正则铁律**：禁 `\s*`，一律 `[ \t]*`。**脚本铁律**：扫描后先自证覆盖率再下结论。
4. **merged 指针页：** `status: merged` 页保留原 `source_path` → 必现「一条 RAW 被 2 页登记」。判重工具须把 merged 页**留在已编译索引内**、**从重复告警剔除**。
5. **缓存字段降格命名：** 抄自权威源的缓存须带 `hint` 标识 + 顶部 `_warning` + 一致性校验（不一致只提示不自动改）。
6. **IMA 同步层坑：** ① `enumerate` 只写 `kb_path` 不写 `raw_path` → R 阶段假「漏登」，治具 `_rebind_raw_path.py`；② 全量枚举 **kb_path 重建不可靠**（深层 `parent_folder_id` 常空）→ 只喂新增条目，绝不回灌路径；③ 账本 `kb_path` 口径 = `ima_sync/个人知识库/WKB/<链>`（不带 `RAW/`），须经 `norm_kb_path()` 归一；④ note 条目 MCP fetch 永久失败=`code:220030`（条目级，标后不重试），区别于 `200005`（日配额，次日可试）。
7. **抽取式批量编译（清积压）：** `_compile_extractive.py` —— `source_path` 逐字等于 plan `raw_path`；`key_claims: []` 留空不臆造；正文原文抽取+截断标注；幂等。

---

## 三、front matter 字段口径（铁律）

**凡 front matter 字段，三处必须一致：AGENTS §2 示例 + `TEMPLATES/*.md` + 生成器代码；改字段须三处同改。** 已三踩：生成器漏写 `knowledge_update_status`（483 页缺，10-12 回填 `pending`）；`_compile_p0b02_20261011.py` 自造字段名（`source_credibility`/`compiled_at`/`related`，应 `credibility`/`date_processed`/`pages_linked`）。**新编译脚本先对齐字段名，禁自定义同义字段。** 该字段不可废弃（服务 §5 防重复标记 + §7 journal 扫描闭环）。

---

## 四、concept 库治理（2026-10-12）

- **新建 concept 前必须先在库内做语义检索（读定义，不只看页名）**——凭名字直觉建页=制造重复；「看起来该建页」的目标多数已有对应页（首次应用：20 条优先 SEED 中 11 条实为库内重复）。
- **domain 分类已治：** 133 变体 → **13**（活跃 11，全为 MOC 域），含 114 页「待归类」逐条读定义细分（裁定表 `_unclassified_assign_20261012.json`）；合并 5 组重复（另 17 个 merged 指针页为 09-30 已治）。
- **幂等铁律：** 分类/归一化脚本的输入必须取自「不随自身输出改变」的源（如重构前原始 domain 快照 `_concept_index_20261012.json`），否则永不幂等。
- **人工裁定表须作「最高优先级覆盖表」接入自动化**（`ASSIGN.get(name) or classify(...)`），否则每次自动归类都会冲掉人工成果。
- 重建器：`_rebuild_concept_domains_20261012.py`（新概念入库后跑；数据依赖见上）。

---

## 五、断链治理工具（2026-10-12）

- 唯一入口 **`.tools/wkb_link_guard.py`**：`check`/`plan`/`apply [--mode=redirect|seed|all]`/`report`。白名单 `.tools/link_guard_curated.json`（ast 机械提取，禁手工誊抄）。旧 11 脚本归档 `.tools/_legacy_link_scripts/`，勿再运行。
- **纪律：** 改指只允许「同名变体」（白名单命中+目标页存在）；语义近似一律 SEED；`BLOCK` 强制 SEED（防上位→下位窄化）；**seed 只出清单**（`apply` 默认只改指，建页须显式 `--mode=seed/all`）；apply 前自动备份。比第 2 代更保守：containment 命中一律进 REVIEW，仅「归一化精确相等」才自动改指。
- **成果：** 断链 129 → **0**（全库清零，WIKI 2244 页）；front matter 2244/2244；index 对齐 2244/2244。
- 校验器口径已修：`verify_wiki.py` 加 `MOC_TYPES={'moc'}` 豁免；`rebuild_index.py` 收 `WIKI/MOC/`。**修工具，不改页面迁就工具。**
- **「断链 0」≠「图谱无孤立点」**（正交）：孤立点来自**非知识层文件**（`RAW_FULL/` 1030 + `TEMPLATES/` 5，无 wikilink）→ 图谱过滤须含 `-path:RAW_FULL -path:TEMPLATES`。WIKI 层靠 index.md 连住。
- **知识层语义建链（已做）**：源页补 `## 关联页面` + 概念/实体页补 `## Related Sources` → 完全孤立 **485 → 139**（余者正文无任何概念标题逐字出现，按「不臆造」不链接）。脚本 `_link_layer_build/backfill2/dedup_20261012.py`（均幂等）。**铁律**：① 含拉丁字母的候选**必须词边界**（`cti` 会命中 `practice`）；② 存在性比对**不剥 `.md` 后缀**（有页面名本身以 `.md` 结尾，剥了就永不幂等）。

---

## 六、IMA 双 ID（不可混用）

| 视角 | KB ID |
|---|---|
| MCP / trpc | `001a693ee6c0644e` |
| REST / OpenAPI | `F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI=` |

全量枚举走 MCP（limit ≤ 50）、REST 仅只读兜底。**取正文首选 MCP `fetch_media_content`**（不受 REST 日配额限制）。枚举能力差异：MCP `file_number` 有值（可剪枝）、REST 为 null（只能全量递归）→ **日更管道必须走 MCP**。REST `200001`=频率超限（隔 8~10s 重试）、`200005`=日配额耗尽（当日停止）。

**遗留坑（2026-10-14 实测）：**
- **REST 全量递归会把 folder 条目塞进 `items`**（`media_type=99`、`kb_path` 空）→ 合并前必须剔除，否则 `discovered` 虚增（本次 4→140）；folder 只应存账本 `folders` 字典。治具 `_ledger_cleanup_20261014.py`。**2026-10-15 起已在枚举脚本源头过滤（`_ima_enum_rest_<date>.py`）。**
- **自写 urllib 直调 note 端点返回 HTTP 403，官方 `ima_api.cjs` 返回业务码 `200005`** → 判配额/业务错误**一律以 `ima_api.cjs` 为准，403 不可作依据**。
- **REST 短窗口限频 `200001`（2026-10-15 实测）**：urllib 侧表征为 **HTTP 403**，在 `get_knowledge_list` **长递归**中 0.3s 间隔必被打断（枚举半途崩）。**治具：请求间隔 ≥2.5s + 单次失败 sleep 12s 退避**；47 目录全量递归约 6m15s 跑通。区分：`200001`=频率（可退避重试）、`200005`=日配额（当日停止不重试）。
- **录音原件可下载**：`get_media_info` 对 `soundrecording_`（type 15）返回真实签名 URL（audio/mp4，本次 10.8MB）；`note_` 仅返回 `chrome://note?...` 不可下载。
- **`word_` 原件可下载（2026-10-15 实测）**：`get_media_info` 返回真实签名 URL（`pkb.ima.myqcloud.com/.../*.docx`，带 `X-IMA-Sign` 等 headers）→ 下载后 `zipfile` 抽 `word/document.xml` 即得文本层。通道 B 有效。
- **插件偶发写入笔记完整正文**（非占位壳）→ plan 前先查 RAW 正文长度，可直接镜像，省一次配额调用。
- **`get_doc_content` 日配额极小**：2026-10-15 仅成功 1 次即 `200005`，隔 6 分钟复探不恢复 → 明确为日配额耗尽。**5 条笔记因此自 10-13 起连续 3 日被卡**；唯一无配额通道 = MCP `fetch_media_content`（需会话内有 IMA connector）。疑似 ima-copilot-sync 插件每日耗尽该配额。

**新增（2026-10-16 实测）：**
- **`markdown_` / `html` 类条目可经 `get_media_info` 直下原件（无配额）** → media_type=7 返回 `pkb.ima.myqcloud.com/.../<hash>.md` 签名 URL（`response-content-type: text/markdown`）。**这是无配额的第三条正文通道**（① MCP `fetch_media_content`；② 录音/word 原件；③ markdown/html 原件）。`ima_fetch_originals.py` 的 `DL_PREFIXES` 目前**未含 markdown**，需 Agent 侧手工下载或扩白名单。
- **REST 无 `fetch_media_content` 端点**（直调返回空）——该接口为 MCP 专有，勿在 REST 兜底链路上指望它。
- **`kb_sync_handler.py plan` 盲区**：`if not rp: continue` → **`raw_path` 为空的新条目不进 plan**（新发现条目常因插件未落地 RAW 而无 raw_path）。须 Agent 侧手工写 `RAW_FULL/<kb_path>.md` + 登记账本 `raw_path`/`stage=synced`。要自动化须先修 plan 空值处理。
- **「编译成功」的正确判据**：dedup 的「已编译」按 **RAW 文件覆盖率**计；新条目 RAW 锚点未落地时，新增编译**不改变未编译数**。**判定编译成功看「登记路径去重总数」与「WIKI 页面总数」是否 +1，不能只看未编译数。**
- **枚举合并的「移动 N 条」是噪音**：REST 枚举的 kb_path（标题可能带 `...` 截断、无 `.md` 后缀）与插件侧 kb_path 不一致 → 每次合并报大量 moved。**须复核 `raw_path` 改动数 = 0** 才可认定无污染。

---

## 七、知识管道自动化

| ID | 名称 | 频率 | 职责 |
|---|---|---|---|
| `bcaf361b-...` | 日更 IMA→Obsidian | 每日 18:00 | A/B/C/E（增量） |
| `808e9058-...` | 周度全量对账 | 每周日 09:00 | A/B/C/R/E（全量校准） |
| `5700cc40-...` | 记忆防覆盖巡检 | 每日 08:45 | `memory_guard.py check` |
| `8523233b-...` | IMA 正文回填巡检 | PAUSED | 已被 `bcaf361b` 覆盖 |

- 模型均为 **deepseek-v4.1-flash**；`bcaf361b` prompt 已接线 `kb_daily_pipeline.py run`。
- **架构定案：高频增量 + 低频全量 双轨**（增量靠剪枝提速会累积漂移；全量强制递归整库打平）。职责错开，非重复。
- **脚本矩阵：** `ima_sync_state.py`(init/enumerate/status) · `kb_sync_handler.py`(plan/apply/gaps/status) · `kb_compiler.py`(plan/apply/stub/verify/status) · `kb_daily_pipeline.py`(run/stage/status)。
- **中继铁律：** MCP 调用一律在 Agent 会话内完成，脚本只做合并/落盘。**幂等：** `archive_staging()` 把 B/C 暂存搬 `_done/<date>/`；重复跑正常表现是 `PARTIAL` 非 `FAIL`。**状态：** `OK`/`PARTIAL`(正常态)/`SKIP`/`WARN`(R 漂移)/`FAIL`(真错)。
- 阶段 R（全量对账）**只读不改**：`wkb_dedup.py scan` + 账本三口径校验 + 逐条黑账核对；口径差异（+22）非 bug，只报偏差不判错。

---

## 八、记忆/记录维护

- **防静默覆盖巡检**：`.tools/memory_guard.py`（只读），判据体量跌幅>20% 或行数减≥5；基线只能人工刷新。
- **追加式文件永不覆盖**：`log.md`、每日 memory 用 `>>`，**禁 `>`**（教训：2026-10-11 被覆盖丢失数节）。

---

_Last updated: 2026-10-12_
