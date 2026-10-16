# WKB-OB 断链治理收敛方案 · `wkb_link_guard.py`

**日期**：2026-10-12　**状态**：待王总确认（**本文件为方案，未执行任何改动**）
**提出背景**：断链修复能力目前碎片化为 7 个一次性脚本，改指规则散落各处，每次编译都要重写。

---

## 一、结论先行

把 7 个碎片脚本收敛成**单个常驻脚本** `.tools/wkb_link_guard.py`，四子命令 `check / plan / apply / report`，改指白名单**外置为集中 JSON**，判定逻辑沿用第 2 代已标定的纪律（人工白名单 + 语义近似建页 + 禁止自动窄化）。

**预期效果**：编译收尾从「临时写脚本」变成「跑一条命令」；跨批次可重复、幂等、可审计。

---

## 二、现状盘点

### 2.1 现有 7 个脚本（三代演进）

| 代 | 脚本 | 职责 | 处置建议 |
|---|---|---|---|
| 1（09-29） | `fix_broken_links.py` | 归一化匹配改指 | **废弃**（逻辑已被取代，见下） |
| 1 | `final_link_fix.py` | 手工 REWRITE 表 + seed 建页 | **白名单并入**集中表，脚本废弃 |
| 1 | `_fix_wires_links.py` / `_fix_wires_ext.py` | Wires 两页单点修复 | **归档**（已完成，一次性） |
| 1 | `_check_wires.py` / `_test_links.py` | 诊断 | 归档 |
| 2（09-30） | `_link_triage.py` / `_link_triage2.py` | 断链三级分级 | **逻辑吸收**进 `plan` |
| 2 | `_fix_links_all.py` | 三段式执行体（302→0） | **逻辑吸收**进 `apply` |
| 3（10-11） | `_links_p0b02*.py` / `_fixlinks_p0b02.py` | 批次登记 + 定向改指 | **逻辑吸收**进 `check`/`apply` |
| 常驻 | `verify_wiki.py` | 断链 + front matter + index 三校验 | **并入 `check`**（保留原文件作对照） |

### 2.2 当前实况基线（2026-10-12 只读扫描）

| 校验项 | 当前值 | 判读 |
|---|---|---|
| **断链目标** | **127 种** | ⚠️ 10-11 批次编译后新增的派生目标（Daehyoon / Nichidai / Insilico / Niso / 三叶草截面纤维 / ES纤维 …），尚未处理 |
| **front matter** | 缺字段 **481 页 / 1387**（其中 **474 页 = 10-11 抽取式编译批次**） | ✅ 已核实：**字段未过时**，根因是生成器漏写 + AGENTS §2.3 示例漏列（详见 §六） |
| **index.md 对齐** | 实际 2153 / 收录 2140，缺 13 页 | ⚠️ 缺的全是 **MOC 页**（`rebuild_index.py` 只扫四类目录、不扫 MOC） |

### 2.3 断链样本分类（127 种的构成）

| 类别 | 样本 | 判定倾向 |
|---|---|---|
| 供应商/机构实体 | Daehyoon、Nichidai、Niso、Insilico、Huayi集团、Kigami | 建 entity seed（或按第 3 代纪律出清单人工裁决） |
| 材料/工艺概念 | ES纤维、PVA、TPU、PTMEG、SIS 嵌段共聚物、SMS无纺布、三叶草截面纤维 | 建 concept seed |
| 缩写/内部术语 | 320D、IEL、OI、T-channel、RTC工艺、Pinhole 开孔、BM管理 | **需人工裁定**（可能是内部代号，不宜建公开页） |
| 专利/标准/文件 | EP0820747A1…、US 7,195,621 B2、STM-01078…docx | 改指到既有页 或 建 source 页 |

> ⚠️ 上面的分类只是**抽样印象**，`plan` 会用规则重算，不靠肉眼。

---

## 三、方案设计

### 3.1 脚本定位与边界

**做**：wikilink 连通性治理（断链检测 → 分级 → 改指 → 建 seed → 报告）。
**不做**（边界，防止职责重叠）：

- ❌ **不碰判重**——`source_path` 一致性、重复副本判定是 `wkb_dedup.py` 的唯一权威，guard 只读不写。
- ❌ **不碰 `RAW/`**——原始层永不可写（AGENTS 红线）。
- ❌ **不自动晋升 status / 不改正文内容**——只改 `[[...]]` 链接文本与新建 seed 占位页。
- ❌ **不做语义近似改指**——沿用第 2 代铁律，语义近似一律建 seed。

### 3.2 CLI 设计

```
python .tools/wkb_link_guard.py check              # 只读诊断，零改动
python .tools/wkb_link_guard.py plan               # 产出分级计划（JSON + MD 清单），零改动
python .tools/wkb_link_guard.py apply [--mode=M]   # 执行；默认先自动备份
python .tools/wkb_link_guard.py report             # 汇总最新一次 plan/apply 结果
```

| 子命令 | 动作 | 写盘 |
|---|---|---|
| `check` | ① 断链扫描（剥 `\|别名` 与 `#锚`，剥行内代码）② front matter 必填校验 ③ index.md 对齐（**含 MOC**） | 无 |
| `plan` | 把断链分三级：**REDIRECT**（白名单命中且目标存在）/ **REVIEW**（多候选待裁决）/ **SEED**（真缺失） | `.tools/link_guard_reports/<date>_plan.{json,md}` |
| `apply` | `--mode=redirect`（只改指，最保守）/ `--mode=seed`（只建页）/ `--mode=all` | 改 WIKI + 备份 |
| `report` | 汇总 + 残留断链 | `.tools/link_guard_reports/<date>_report.md` |

**为什么分 `--mode`**：第 3 代纪律明确「改指与建页是两个独立批次」。分模式可先改指（零风险）、再单独审建页清单，符合人工裁决习惯。

### 3.3 白名单外置（核心改进）

把历代硬编码表合并为一个集中文件 `.tools/link_guard_curated.json`：

```json
{
  "_warning": "本表非权威源，仅登记『同名变体』改指规则；语义近似一律建 seed。目标页必须已存在。",
  "redirects": { "SAP": "SAP（高吸水树脂）", "...": "..." },
  "groups": { "Nonwoven 非织造布": ["非织造布 Nonwoven", "无纺布 Nonwoven"] },
  "block": ["热熔胶 Hot Melt", "非织造布 Nonwoven", "..."],
  "plain_text": { "log": null, "wikilink": null }
}
```

**合并来源**：`_fix_links_all.py` 的 `CURATED`(≈55) + `GROUPS`(9 组) + `final_link_fix.py` 的 `REWRITE`(≈45) + `_fixlinks_p0b02.py` 的 6 条。
**去重要点**：`final_link_fix.py` 的 `REWRITE` 里有多条是「含 `/` 的文件名转义」（`GB/T…` → `GB-T…`），这类属**文件名规范化**而非语义改指，须单独归入 `filename_sanitize` 组。

### 3.4 判定流水线（沿用已标定纪律）

```
收集链接 → 目标不存在?
  ├─ 在白名单 redirects 且目标页存在 ──→ REDIRECT
  ├─ 属 groups 变体 ────────────────→ 定向 canonical
  ├─ 归一化唯一命中（去括号/空格/标点）→ REDIRECT（⚠️ 仅当唯一且长度≥6）
  ├─ 多候选 ───────────────────────→ REVIEW（人工裁决）
  └─ 无候选 ───────────────────────→ SEED（建占位页）
```

**兜底铁律（不可省）**：

1. `BLOCK` 集合：命中者**强制**走 SEED，禁止任何自动改指（防「上位→下位」窄化）。
2. 归一化匹配**仅用于同名变体**，候选唯一且长度 ≥6 才采信（第 1 代 `norm()` 太松，是错误来源）。
3. seed 页正文**只登记引用来源 + 待补维度，禁止编造任何数据**。

### 3.5 与 AGENTS 铁律的对应

| AGENTS 铁律 | 本脚本落实 |
|---|---|
| §1.1.2-1 正则禁 `\s*`，用 `[ \t]*` | 所有链接/字段正则一律 `[ \t]*` |
| §1.1.2-2 先自证覆盖率 | **每条子命令首行输出**「扫到 N 页 / 提取 M 链接 / N 与 M 之和对账」 |
| §1.1.4 删页前必须备份 | `apply` 前自动建 `.tools/_link_guard_backup_<ts>/` |
| §4.2 改完连跑两次验幂等 | 交付验收：连跑 `check` 两次，第二次断链数应稳定；`apply` 重跑应为「改指 0 / 新建 0」 |
| §1.1.1 三种登记形态 | 本脚本**不涉及** source_path 判定，无需处理（边界清晰） |

### 3.6 交付物

| 文件 | 说明 |
|---|---|
| `.tools/wkb_link_guard.py` | 主脚本（含 `check/plan/apply/report`） |
| `.tools/link_guard_curated.json` | 集中白名单 |
| `.tools/link_guard_reports/*` | 每次运行的 plan/report 产物 |
| `.tools/_link_guard_backup_<ts>/` | apply 前自动备份 |
| 旧 7 脚本 | 移入 `.tools/_legacy_link_scripts/` 归档（**不删**，保留追溯） |

### 3.7 验收标准

1. `check` 输出的断链数 = `verify_wiki.py` 口径（交叉验证一致）。
2. `check` 能额外报出 index 漏收 MOC、front matter 缺失两类问题。
3. `plan` 对待裁决项给出候选与理由。
4. `apply --mode=redirect` 后断链数下降，且**零误改**（人工抽检 10 条）。
5. 连跑两次 `check` 结果一致（幂等）。
6. 全程 `RAW/` 与 `source_path` 零改动（可用 `git status` 或文件 mtime 核验）。

---

## 四、待王总裁决的 3 个问题

> **✅ 2026-10-12 已裁决并落地**：① **seed 只出清单**（`apply` 默认不建页，须显式 `--mode=seed/all`）；② **先建工具**、断链另开批次；③ 已核实并修复（见 §六）。落地报告见 `LINK_GUARD_REPORT_2026-10-12.md`。

1. **seed 建页纪律**：沿用第 2 代「自动建 seed」，还是第 3 代「只出清单、人工裁决后建」？（我倾向：**默认只出清单**，`apply --mode=seed` 需显式指定才建。）
2. **127 条现存断链**：本次是否一并处理？还是先只建工具、断链另行开批次？
3. **front matter FAIL —— ✅ 已核实完毕（见 §六）**：`knowledge_update_status` **不是过时字段**，`verify_wiki.py` 口径正确。根因是**生成器漏写**（`kb_compiler.py` / `_compile_extractive.py`）+ **AGENTS §2.3 示例漏列**。待裁决：**补齐** 还是 **废弃**。

---

## 五、不做什么（明确边界）

- 不重构 `wkb_dedup.py` / `kb_compiler.py` / `kb_daily_pipeline.py`。
- 不把 guard 挂进日更自动化（等工具稳定、王总确认后再议）。
- 不改任何 `RAW/` 文件、不改 `source_path`、不动 `status` 字段。

---

## 六、问题 3 核实记录（2026-10-12 完成）

> **结论：`knowledge_update_status` 不是废弃字段，`verify_wiki.py` 的校验口径正确。**
> 481 页缺字段的根因是「**生成器漏写 + AGENTS §2.3 示例漏列**」双重失守，与字段本身无关。

### 6.1 字段确在服役（三处文档 + 906 页实证）

| 出处 | 内容 |
|---|---|
| AGENTS §5（行 263） | 「所有批量任务使用 `knowledge_update_status`（pending/done/manual_review）标记，已处理的资料不再重复编译」 |
| AGENTS §7.2（行 304） | 「对 `raw/journal/` 中每篇 `knowledge_update_status ≠ done` 的日志执行…」 |
| AGENTS §7.5（行 340） | 「判重依据：源摘要页 `source_path` + `knowledge_update_status`」 |
| `TEMPLATES/source.md` 行 10 | 模板**明确列出** `knowledge_update_status: pending \| done \| manual_review` |
| `TEMPLATES/book_index.md` 行 15 | 固定 `knowledge_update_status: done` |

**实况**：906 页有该字段，值规范（`done` 892 / `manual_review` 14）→ **在用，非僵尸字段**。

### 6.2 缺字段 481 页的分布（定位根因）

| date_processed | 页数 | 判读 |
|---|---|---|
| 2026-10-11 | **474** | 🎯 `_compile_extractive.py` 抽取式批量编译产物的集中表现 |
| 2026-10-12 | 5 | 同族 |
| 2026-09-29 | 2 | 早期个案 |

### 6.3 两个失守点（根因）

1. **生成器漏写字段**：
   - `kb_compiler.py:build_front_matter()`（行 177–189）字段清单**无**该字段
   - `_compile_extractive.py:build_front_matter()`（行 33–45）同样**无**
2. **AGENTS §2.3 示例漏列**：行 179–196 的 front matter 示例里**没有**该字段 → 与 `TEMPLATES/source.md` **自相矛盾**（正是 §2.3 多源一致性铁律所指的病）。

**旁证（同批 10-11 编译口径分叉）**：`_compile_p0b01_20261011.py`(行 506)、`_compile_p0b02_20261011.py`(行 557) **有写**该字段；`patch_frontmatter.py`、`_repair_id_frontmatter.py` 亦在处理它 → **有的脚本记得、有的忘了**。

### 6.4 实际危害（如实评估，不夸大）

- ❌ **不会导致重复编译**——现代判重走 `wkb_dedup.py` 的 `source_path` 口径，**不依赖**此字段。
- ⚠️ **影响 §7 journal 日志扫描闭环**——该闭环按「`≠ done` 的日志」判定，缺字段会造成判定异常/漏判。
- ⚠️ **§5 通用标记语义失真**——「已处理不再重复」失去依据。

### 6.5 待裁决：补齐 还是 废弃？

| 方案 | 动作 | 成本 |
|---|---|---|
| **A·补齐（建议）** | ① 两个生成器补写字段（默认 `pending`）；② AGENTS §2.3 示例补列；③ 回填 481 存量页 | 中，改 3 处 |
| **B·废弃** | 须同步改 AGENTS §5/§7.2/§7.5 + `TEMPLATES/source.md` + `book_index.md` + `verify_wiki.py` REQ 表 | 高，**六改**且打断 §7 闭环 |

> ⚠️ 若选 A，回填的**值语义**需另行裁定：474 页为「抽取式编译」（已落盘但声明待深度编译）→ 记 `done`（处理已完成）还是 `pending`（待深度编译）？

---

_方案版本：v1.1（2026-10-12 更新：§四问题 3 已核实落地）。确认后进入实现。_
