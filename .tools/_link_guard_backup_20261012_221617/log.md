# 操作日志（log.md）

> 本文件由 AI 依《AGENTS.md》§3.6 / §7.5 自动维护，**追加式，永不改写历史记录**。
> 每条记录格式：日期 + 动作 + 涉及文件。索引见 [[index]]。

---

## 2026-09-27 · 知识库基础设施初始化 + 首批样例编译

**执行人：** AI（WorkBuddy）
**触发方式：** 用户指令「读取 raw/ 中新增文件，按 AGENTS.md 编译到 wiki/，并更新 index.md 与 log.md」
**执行范围：** 经用户确认——**先搭基础设施，再试编译 5 份样例校准格式**（编译深度：完整四类页面）

### 1. 基础设施新建（此前全部不存在）

| 产出 | 说明 |
|---|---|
| `TEMPLATES/source.md` | 源摘要页模板（含 source_path / key_claims / knowledge_update_status 字段） |
| `TEMPLATES/concept.md` | 概念页模板（含「禁止无来源参数」提示与验证记录区） |
| `TEMPLATES/entity.md` | 实体页模板（含商务敏感信息处理约定 + real_name_hint） |
| `TEMPLATES/comparison.md` | 对比页模板（强制含「成本」「供应链风险」两列） |
| `WIKI/concepts/`、`WIKI/entities/`、`WIKI/sources/`、`WIKI/comparisons/` | 四个 wiki 子目录（此前为空） |
| `index.md` | 目录索引骨架，按四区建立（新增） |
| `log.md` | 本文件（新增） |
| `.tools/verify_wiki.py` | 断链 / front matter / 索引对齐 三合一校验脚本（供 §5 每周健康检查复用；置于点目录，Obsidian 不索引） |

### 2. 样例编译（5 份 raw → 20 个 Wiki 页面）

**源摘要页（5）**

| 源摘要页 | 源 raw 文件 | 原始发布日期 |
|---|---|---|
| [[无纺布-五大工艺论剑]] | `raw/ima_sync/WKB/Areas/Nonwoven/无纺布 - 五大工艺论剑.md` | 2026-08-23 |
| [[热风与针刺无纺布]] | `raw/ima_sync/WKB/Areas/Nonwoven/热风与针刺无纺布.md` | 2026-08-20 |
| [[低熔点共聚酯及皮芯复合纤维技术突破]] | `raw/ima_sync/WKB/Areas/Nonwoven/全链自主创新，低熔点共聚酯及皮芯复合纤维制备技术实现关键突破.md` | 2026-08-15 |
| [[卫生用品认证体系完全指南]] | `raw/ima_sync/WKB/Areas/Regulation&PSC/卫生用品认证体系 完全指南.md` | 2026-07-01 |
| [[天丝为什么突然这么难买]] | `raw/ima_sync/WKB/Areas/Supply Base/天丝为什么突然这么难买，国产的又能不能替.md` | 2026-09-18 |

**概念页（6，全部新建）**

- [[热风粘合无纺布]]（由 [[热风与针刺无纺布]]、[[无纺布-五大工艺论剑]] 建立）
- [[皮芯复合纤维]]（由 [[热风与针刺无纺布]]、[[低熔点共聚酯及皮芯复合纤维技术突破]] 建立）
- [[原纤化]]（由 [[天丝为什么突然这么难买]] 建立）
- [[SMS复合结构]]（由 [[无纺布-五大工艺论剑]] 建立）
- [[认证与法规的区别]]（由 [[卫生用品认证体系完全指南]] 建立）
- [[亲水-疏水梯度设计]]（由 [[热风与针刺无纺布]] 建立）

**实体页（6，全部新建）**

- [[福建闽瑞新合纤]]、[[东华大学]]（由 [[低熔点共聚酯及皮芯复合纤维技术突破]] 建立）
- [[兰精集团]]、[[赛得利]]（由 [[天丝为什么突然这么难买]] 建立）
- [[OEKO-TEX]]、[[bluesign]]（由 [[卫生用品认证体系完全指南]] 建立）

**对比页（3，全部新建）**

- [[无纺布五大工艺对比]]（依据 [[无纺布-五大工艺论剑]] + [[热风与针刺无纺布]]）
- [[兰精莱赛尔与国产莱赛尔对比]]（依据 [[天丝为什么突然这么难买]]）
- [[卫生用品五大认证体系对比]]（依据 [[卫生用品认证体系完全指南]]）

**质量校验**

- 断链检查：扫描全部 20 页的 Obsidian 双链（wikilinks），**断链 0 条**。
- 溯源校验：对比页所有数字均已在表格尾注标明来源源摘要页；无来源参数一律标 `[待验证]`。

### 3. 人工确认边界（manual_review）标记

| 条目 | 位置 | 原因 |
|---|---|---|
| A100 明年停产、LF 年底停产 | [[兰精集团]] | 属**传闻非公告**，检索不到任何公开来源（兰精官网无公告）。依 AGENTS.md §5「人工确认边界」，AI 只记录不裁决，不据以下判断 |
| 国产常规纱 vs 兰精 A100 每公斤价差 ≥10 元 | [[兰精集团]]、[[兰精莱赛尔与国产莱赛尔对比]] | 属具体报价类**商务敏感信息**页面化，须人工确认；且原文已声明口径不同、不构成同质对比 |

> 上述 2 条已在对应页面以 🔴 标注，**未计入自动结论**。当前 manual_review 积压 2 条（< 5 条阈值，无需集中处理提醒）。

### 4. 未处理范围（如实记录）

- `raw/` 下共 **1716 份 .md**（含 `Areas/` 414、`Resources/` 1189、`Projects/` 77、`Archives/` 14、`Inbox/` 2、根层级 19）。本次仅编译 5 份，**其余 1711 份未编译**。
- 原因：WIKI 层此前为空，按 §3 判新规则全部属「新增」；1716 份无法单轮完成。经用户确认采用「先搭基础设施 + 样例校准」策略，后续按批次推进。
- 已识别的下一批高优先级对象见 [[index]] 第五节「待办与缺口」。

### 5. 后续建议

1. 用户先审阅本次 5 份样例的格式（尤其模板字段、对比页列结构、manual_review 标注方式），确认后再放量。
2. 放量时建议按 `Areas/` → `Projects/` → 根层级 LMP-PP 群 → `Resources/` 的顺序分批（`Resources/` 体量最大且多为拆书/训练材料，可最后处理）。
3. 每批完成后按 §3.5/§3.6 追加本索引与本日志，批内的 `knowledge_update_status` 统一置 done 以便判重。

---

## 2026-09-27 · 批次 1「研发核心层」编译（放量启动）

**执行人：** AI（WorkBuddy）
**触发方式：** 用户指令「没问题，开始按批次放量吧」
**执行范围：** `raw/ima_sync/WKB/` 根层级 LMP-PP 项目群（9 份）→ 产出 9 源摘要 + 15 概念 + 14 实体 + 4 对比

### 0. 前置盘存（本轮新增的关键事实）

对 `raw/` 全部 1716 份 .md 做正文净长度判定（去 front matter / 标题 / 自引用后 <150 字视为空壳），得到**二分盘存**：

| 类别 | 份数 | 说明 |
|---|---|---|
| **可编译**（净正文 ≥150 字） | **565** | 有实质内容，可正常编译 |
| **占位符**（净正文 <150 字） | **1151** | 仅含 `media_id` + 标题 + 自引用链接，**零正文**；IMA 同步时未提取附件正文（.pdf 311 / .pptx 143 / .docx 109 / .xlsx 48 / .csv 28 / .doc 18 / other 494） |

> 盘存清单落盘 `.tools/_inventory.json`；批次规划脚本 `.tools/plan_batches.py`、`.tools/list_batch1.py`。
> **结论**：原「1716 份待编译」的口径应修正为「**565 份可编译 + 1151 份待回源提取**」。占位符须回 IMA 提取正文后才能编译，否则只能登记索引。

### 1. 本批源摘要页（9 份，全部新建）

| 源摘要页 | 源 raw 文件 | 类型 |
|---|---|---|
| [[低熔点PP的冲突地图]] | `低熔点PP的冲突地图.md` | 内部笔记 |
| [[LMP-PP方案C技术论证]] | `王总，先说结论：知识库里没有专门讲_低熔点PP粒子（Low.md` | 内部笔记 |
| [[低温PP纺粘与TBCW低成本方案]] | `低温PP相关的纺粘布讨论主要集中在TBCW低成本方案.md` | 录音纪要 |
| [[2026年上半年国内茂金属催化剂突破]] | `2026年上半年是国内茂金属催化剂密集突破的半年.md` | 内部笔记 |
| [[PP纤维级树脂技术综述]] | `Polypropylene Fiber Grade_ Adv.md` | 专利情报 |
| [[成纤聚合物的判据]] | `为什么能做成纤维的聚合物，就那么几种？.md` | 公众号 |
| [[聚酯水解与水分控制]] | `聚酯为什么要控制水分：水解机理、动力学方程与纺丝后果.md` | 公众号 |
| [[OI项目清单与优先级]] | `好，资料已经齐了。根据知识库中最新（2026-09-18）的.md` | 内部会议 |
| [[智能尿裤功能层专利地图]] | `智能尿裤功能层专利地图.md` | 内部专利调研 |

### 2. 本批概念页（15，全部新建）

- LMP-PP / 纤维主题：[[低熔点聚丙烯]]、[[茂金属聚丙烯]]、[[熔融指数与化学降解]]、[[应力诱导取向与结晶]]、[[成纤性判据]]、[[聚酯水解与水分控制]]
- 结构 / 项目主题：[[TBCW结构]]、[[REL增强层]]、[[COCO芯体平台]]、[[分区密度设计]]、[[SAP错峰膨胀]]
- 智能功能化主题：[[细菌纳米纤维素]]、[[智能尿裤功能层]]、[[变色油墨]]、[[Mechanochromic变色纤维]]

### 3. 本批实体页（14，全部新建）

- 树脂 / 催化剂端：[[中石化]]、[[中石油石化研究院]]、[[广州石化]]、[[仪征化纤]]、[[上海德福伦]]
- 海外对标：[[TotalEnergies]]、[[利安德巴塞尔]]、[[Sabic]]
- 项目供应方：[[海南拜瑞科]]、[[中科依兰]]、[[皖维高新]]、[[汉高]]
- 异议方 / 竞品：[[福建兴泰]]、[[Ontex]]

### 4. 本批对比页（4，全部新建，均含「成本」「供应链风险」两列）

- [[低熔点PP技术路线对比]]（RCP / 立构调控 / 共混 / 皮芯）
- [[PP基皮芯与PET基皮芯对比]]（PE/PP vs PP/PP vs 共聚酯）
- [[国产mPP与进口mPP对比]]
- [[BNC功能层嫁接可行性对比]]（四功能层，源自 [[智能尿裤功能层专利地图]]）

### 5. 质量校验

- 断链检查：全库 **断链 0 条**（初检 1 条 `[[福建闽瑞]]` 已修正为 `[[福建闽瑞新合纤]]`）。
- front matter 必填字段：**62/62 通过**（source / concept / entity / comparison 四类分别校验）。
- `index.md` 索引覆盖：本轮新增 41 页**已全部收录**（四区表 + 规模统计 + 批次进度表同步更新）。

### 6. 人工确认边界（manual_review）新增 2 条

| 条目 | 位置 | 原因 |
|---|---|---|
| OI-02 PVA 配方与成本增量（+RMB 1,400/吨） | [[REL增强层]]、[[皖维高新]] | 配方比例与成本属产品开发敏感信息，对外引用前须人工确认 |
| BNC 成本量级（RMB 50,000/t） | [[海南拜瑞科]]、[[细菌纳米纤维素]] | 供应商成本信息，商务敏感；单一口径未交叉验证 |

> manual_review 累计 4 条（含既有 2 条）。

### 7. 未处理范围（如实记录）

- 本批仅处理根层级 **9 份**；根层级另有 2 份待处理（`【深度分析】柔性压力传感器的技术路线.md`、`花了五六千积分…PPT 工作流.md`，前者可补 [[智能尿裤功能层]]，后者属工具类非知识内容）。
- `Projects/` 可编译 19 份**本批未做**，顺延至批次 21。
- 剩余可编译 **556 份**（565 − 9）按 index 第五节批次表推进。
- 占位符 **1151 份**需回 IMA 提取附件正文，属**独立工程**（非编译任务），建议单独立项处理。

### 8. 本批沉淀的可复用资产

- `.tools/_inventory.json`：可编译 / 占位符二分清单（长期复用）
- `.tools/plan_batches.py`：按目录细分组统计
- `.tools/list_batch1.py`：批次清单抽取
- `.tools/verify_wiki.py`：断链 / front matter / 索引对齐三合一（沿用）

## 2026-09-28 · IMA 占位符正文提取（W15R 残量 + W16 全波 + W17 启动）

> 本条目为 2026-09-29 补记。9/28 全天执行的是**正文提取**（回填 `RAW_FULL/`），不是 WIKI 编译，故当日未在此日志建条目——提取进度只记在 `.tools/_extract_ledger.json` 台账里。现按磁盘与台账实测回填，避免日志出现日期断档。

### 1. 产出（磁盘实测）

`RAW_FULL` 文件按落盘日期：9-27 共 599 份 / **9-28 共 294 份** / 9-29（00:xx）147 份。
台账状态：**797 done → 950 done**（pending 311 → 154）。

### 2. 波次轨迹

- **W16（90 份 / 9 批）全波收口**：87 项落盘 + 3 项源侧无正文 + 1 项 IMA 侧持续 `code 220030`（`2025.03.26 - Learning Cycle Update.pptx`，留 pending 待重试）
- **W17（90 份）启动**：batch3 一次 10/10；多数批次落入「代理冻结 → 按真缺失清单重派」循环
- **W15R 残量**（限流前遗留）并入本轮清完

### 3. 源侧无正文登记（no_content 9 → 13 条）

新增 4 条全部为 `soundrecording` 类型（`fetch_media_content` 返回 `{"content":""}`），另补登 W16 batch2 的 `BUFF BABY DOE - January 2024`。均为源侧确无正文，非提取失败，重试无益。

### 4. 本日确立的三条作业规范（后续波次沿用）

1. **单次 Write 不得超 ~8,000 字符**——超限会被**自身单条 tool-call 参数上限**截断（非 Write 工具限制）。解法：分块写 5–7k 到 `.tools/pilot/_scratch/`，再用 python 合并。该问题在 `2025.03.04 - Rewet - Josie update.pptx`（约 25k 字符）上连败 3 次后定位。
2. **子代理「中途冻结」**：无返回、无报错、落盘数长期不变。判据 = 间隔复查数字不动；处置 = 按 `not os.path.exists(dst)` 拉真缺失清单，改用**定点小组（5–7 项/代理，明确批次文件 + 1-based 序号）**重派。
3. **超大正文自动转存临时文件**：用命令行解析该文件取 `content` 直接写 dst，**不要 Read**（临时文件常在 cwd 之外，会被权限拒绝）。

### 5. 未处理范围

- W17 剩余批次、W18 全部（62 份）顺延至 9-29
- `Learning Cycle Update.pptx` 因 IMA 源侧未解析完成（220030）保持 pending

## 2026-09-29 · RAW_FULL 追溯字段修复 + 图谱过滤（维护性操作）

**触发**：用户发现「已解析文件多数没有链接」。

**诊断结论（三层，均非故障）**：
1. `raw`/`RAW_FULL` 层按 AGENTS.md 定位是「唯一事实锚点，AI 只读」，**不参与知识图谱**；`RAW/` 中 1175 份的 `[[...]]` 是 IMA 同步器生成的**自引用链接**（指向自己），在图谱中是自环。
2. 真正的链接层是 `WIKI/`（62 页 100% 含 wikilink）；编译目前只覆盖「基础设施样例 + 批次 1」，**900+ 份已提取正文尚未编译成 source 页** → 无入链 → 图谱孤岛。
3. `.obsidian/graph.json` 原为 `showOrphans: true` + 空 search，全库节点全画，放大观感。

**已执行修复（2 项）**：
- **RAW_FULL 追溯字段回填**：108 份提取时被 Write 覆盖掉骨架 front matter（丢 `media_id` / `original_path` / `extract_method`）。脚本 `.tools/fix_raw_full_frontmatter.py` 从台账 `_extract_ledger.json` 取权威字段回填 **107 份**；另 2 份路径错位（少一段目录）的游魂文件由 `.tools/fix_stray_raw_full.py` 归位并回填。**全部逐份 MD5 校验正文未改动**，备份在 `.tools/_fm_repair_backup/`。
  - 现状：RAW_FULL **1002 份 / 0 游魂 / 0 缺 front matter**
- **图谱过滤**：`.obsidian/graph.json` 的 `search` 设为 `-path:RAW -path:.tools`（`RAW_FULL` 含 `RAW` 子串，一并排除），图谱只显示 WIKI 层。

**遗留待办**：
- **994 份重名**：`RAW/` 与 `RAW_FULL/` 存在 994 个同名文件，`[[文件名]]` 无法唯一解析（Obsidian 任取其一）。若后续要在 raw 层建链，须先解决重名（如 RAW_FULL 改后缀）。
- **路径非 1:1**：`RAW/` 为 `ima_sync/个人知识库/WKB/…`，`RAW_FULL/` 为 `ima_sync/WKB/…`（少一段），镜像路径并不等价。
- 900+ 份已提取正文的 WIKI 编译尚未开始（方案 A）。
- **W18 波次暂停**：用户 2026-09-29 00:47 指令暂停 W18（62 份）。暂停时已落盘 **0/62**，无半成品。暂停标记见 `.tools/_W18_PAUSED.md`；批次文件 `W18_batch_1..9.json` 保留可直接复用。台账中这 62 份会持续显示 `pending`（属正常，非遗漏）。

## 2026-09-29 · 路径布局对齐为真 1:1（A 元数据 + B 物理对齐）

### 1. 根因（查实）

`RAW/ima_sync/个人知识库` 的 **ctime = 2026-09-28 05:32:35** —— **IMA 同步程序于 9/28 凌晨在 RAW 侧插入了一层 `个人知识库/`**（原为 `RAW/ima_sync/WKB/…`）。而库存清单、台账 `src`、`RAW_FULL` 布局均为 9/27 按旧布局生成 → 三类路径字段 **100% 指向不存在的路径**：

| 检查项 | 修复前 | 修复后 |
|---|---|---|
| 两侧布局 | RAW 长 / RAW_FULL 短 | **完全一致** |
| 台账 `src` 有效 | 0 / 1117 | **1117 / 1117** |
| `RAW_FULL.original_path` 有效 | 0 / 1040 | **1040 / 1040** |
| `WIKI/sources.source_path` 有效 | 0 / 14 | **14 / 14** |

**实质损害**：AGENTS.md §3 的判新依赖 `source_path` 比对 → 路径系统性错误使比对永不命中，**编译将重复建页**；「优先 RAW_FULL、缺失回退 RAW」的回退链同时失效。此前 1014 份文件被代理误搬的事故，本质是同一次错位引发。

### 2. 执行（脚本 `.tools/_align_rawfull_to_raw.py`，dry-run 默认、全量备份、幂等）

- **B 物理对齐**：`RAW_FULL/ima_sync/WKB` → `RAW_FULL/ima_sync/个人知识库/WKB`（1040 份）
- **A 元数据**：JSON 路径字段 **8768 处**｜`original_path` **1040 份**（其中 91 份原为残缺相对路径，改用「从文件自身位置反推」修正）｜WIKI `source_path` **14 页**（小写 `raw/` 归一为 `RAW/`）
- 备份：`.tools/_path_migration_backup/`
- **副产品**：换前缀公式 `dst = 'RAW_FULL/' + src[4:]` 重新成立，**全管线不再需要路径映射**

### 3. 新增/治理的资产

- `.tools/audit_path_consistency.py` —— 五项审计（物理布局 / 台账 src / original_path / source_path / 重名）。**每次动过目录或做过 IMA 同步后应跑一次**（IMA 随时可能再改 RAW 结构）
- `list_batch1.py`、`plan_batches.py` 布局无关化（先剥离 `ima_sync/<库>/WKB/` 前缀，不再用固定段位索引）
- 停用 `.DISABLED`：`_restore_rawfull_layout.py`（会把布局搬回旧样子）、`fix_stray_raw_full.py`（硬编码旧路径）

### 4. 遗留

跨层同名文件 **1031 个**（RAW 与 RAW_FULL 各一份）—— 只要不在 raw 层建 `wikilink` 即无影响。

> 📌 **阅读说明（2026-09-29 追加，不改写历史）**：本文件 **2026-09-27 及更早**条目中出现的
> `raw/ima_sync/WKB/…` 是当时的真实布局。2026-09-28 05:32 IMA 同步在 RAW 侧插入 `个人知识库/` 层后，
> 该路径**现已不存在**；查阅旧条目时请按 `raw/ima_sync/个人知识库/WKB/…` 理解。
> 历史条目按 AGENTS.md「日志追加式、永不改写历史」保持原样，此处仅作说明。

## 2026-09-29 · 编译层恢复：样板批（S1 Projects/REL · CoPET 簇）

- 用户拍板：编译从 **S1+S2** 开始；概念/实体页采用**建页门槛**（本批内被 ≥2 份来源提及，或属核心参数/机理/供应商/项目）；**Ebook 暂跳过**；先跑 1 批做样板。
- 批次清单已生成：`.tools/make_compile_batches.py` → `.tools/compile_batches/`（**79 批**：S1 13 / S2 17 / S3 17 / S4 23 / S5 5 / S7 4，Ebook 已跳过），索引 `.tools/_compile_batch_index.json`
- **样板批产出**：`S1_Projects_REL_01`（CoPET 簇 10 份）→ 新建 sources 10 / concepts 8 / entities 11 / comparisons 2，另**追加**更新既有页 4 个（[[皮芯复合纤维]]、[[REL增强层]]、[[热风粘合无纺布]]、[[福建闽瑞新合纤]]，只追加注日期）
  - WIKI 规模 **62 → 93 页**（sources 24 / concepts 29 / entities 31 / comparisons 9）
  - 校验：**断链 0**、front matter **93/93**、索引覆盖 **93/93**
  - manual_review 新增 5 条（本批配方工艺参数、报价点位、采购指令/合同条款、26 家企业联系方式、优彩环保 C 层判定跨来源矛盾）→ **累计 9 条，已超 §5 的 5 条阈值，待集中处理**
- **顺带修复（维护项）**：源摘要页 `聚酯水解与水分控制` 与概念页同名（09-27 遗留）→ 按「文件名 = 标题」约定改名为 `聚酯为什么要控制水分：水解机理、动力学与纺丝后果`，消除 wikilink 歧义（现 WIKI 内**跨目录重名 0**）；并修正 WIKI 正文与 `index.md` 中残留的旧短路径（62 个页面 + index 14 处）。脚本：`.tools/fix_wiki_naming_and_paths.py`
- 未处理：S1 其余 12 批 47 份、S2–S5+S7 全部；Ebook 432 份按约定暂跳过

## 2026-09-29 · 规则修订：WIKI 语言规范改为「英文为主 + 中文对照」

- **变更依据**：用户 2026-09-29 指示「后续编译的输出默认都是英文」；经确认口径为 **双语（英文为主 + 中文对照）**，并**授权同步修订 AGENTS.md**。
- **AGENTS.md 改动**：
  - 头部「最后更新」→ 2026-09-29（注明语言规范修订）
  - **新增 §2.0 语言规范**（适用于四类页面）：正文主体英文撰写；小节标题 / 关键结论 / 表格表头附中文对照；术语首次出现附中文；**页面标题 / 文件名 / wikilink 文本英文优先**（中文专名可用「中文名」或「English Name（中文名）」，同一对象全库一致）；中文源资料需翻译但保留中文对照与数字口径；`key_claims` 同样英文为主。
  - **§3 写入规范**原「中文为主，专业术语首次出现附英文原文」→ 改为「英文为主 + 中文对照（详见 §2.0）」
- **追溯范围**：2026-09-27 ~ 09-29 期间产出的中文页面**不强制回溯改写**，后续编辑时逐步补齐英文。
- **生效范围**：自本条目之后派发的编译批次一律按 §2.0 执行。

## 2026-09-29 · 编译波次 S1（并发推进中）

- 首批并发派发 3 批：`S1_Projects_BNC_01`（10 份）、`S1_Projects_COCO_01`（6 份）、`S1_Projects_PPC_01`（10 份）
- 架构调整：**并发代理不再直接改 `index.md` / `log.md`**（会互相覆盖），改为各批写回执到 `.tools/compile_batches/_done/<批名>.json`，由主会话统一汇总索引与日志
- 截至本条目：WIKI **93 → 142 页**（sources 46 / concepts 44 / entities 38 / comparisons 14）；已收到回执 1 份（PPC_01）
- ⚠️ 本轮产出为**中文页面**（语言规范修订前派发），按 §2.0 的追溯范围不强制回溯

## 2026-09-29 · 编译波次 S1 第二轮（双语规范首轮）+ 质量修复

### 1. 批次产出

- 派发 3 组、覆盖 7 个批次共 19 份：
  `S1_Projects_BNC_02` / `Film_01` / `Active Hygiene_01`（一组 5 份）、
  `S1_Projects_Liner_01` / `Thermal Comfort_01`（一组 8 份）、
  `S1_Projects_Mechanochromic_01` / `BM_01`（一组 6 份）
- **全部按 AGENTS.md §2.0 新规范产出**：正文英文、小节标题双语、表头与关键结论附中文对照
- WIKI 规模 **93 → 219 页**（sources 65 / concepts 80 / entities 48 / comparisons 26）

### 2. S1 阶段进度

`S1` 共 13 批 57 份，**已编译 51 份（89.5%）**；剩 `Projects/(直属文件)_01`（1 份，139 KB）与 `(直属文件)_02`（5 份，221 KB）。
完成度判据 = 源摘要页 `source_path` 是否覆盖批次 `src`（脚本 `.tools/compile_status.py`）——
**不依赖子代理回执**（实测有 3 批页面已产出但代理中途死掉没写回执）。

### 3. 质量修复（本轮发现并处理）

| 问题 | 规模 | 处置 |
|---|---|---|
| **断链** | 101 处 | 归一化匹配修复 + **补建 2 个"代理计划但未创建"的对比页**（`BNC 卫品应用路线对比（A–F 六赛道）` 被引 20 次、`BNC 与绒毛浆和 SAP 定位对比` 被引 17 次），以 **seed 页**形式建立（登记待补维度 + 引用来源，**不编造数据**）→ 断链 **0** |
| **title 与文件名不一致** | 74 页 | 违反库内约定「文件名 = 页面标题 = wikilink 文本」；统一为 `title := 文件名`，原长写法存入 `aliases`（Obsidian 仍可用旧写法解析）。脚本 `.tools/normalize_titles.py` |
| **库内无 SAP 通识页** | 1 页 | 按 AGENTS.md §2.1 补建 seed 页 `SAP（高吸水树脂）`，只写定义与入口链接、不填数字，全库 `[[SAP]]` 改指该页 |
| **并发同实体多页** | 2 组 | `CTI` 3 种命名变体、`福地（Fudi）` / `Fudi（福地）` 各一份（两个代理各建一页）→ 已收敛为「正页 + 别名页」，**删除待人工确认**（AGENTS.md §5） |

### 4. 索引自动化（新增资产）

- **`.tools/rebuild_index.py`** —— 以 WIKI 实际文件为唯一事实来源重建 `index.md` 一~四区表格与头部统计（幂等，可反复运行）；链接文本一律用文件名，确保解析
- `.tools/compile_status.py` —— 批次完成度状态（按 source_path 覆盖）
- `.tools/fix_broken_links.py` / `.tools/normalize_titles.py` —— 断链解析与 title 归一化

### 5. 校验结果（收尾）

- **断链 0**｜front matter **219 / 219**｜索引覆盖 **219 / 219**
- ⚠️ **manual_review 积压：本轮批次回执合计 40 条 + 历史 9 条**，远超 AGENTS.md §5 的 5 条阈值，**须集中处理**

### 6. 未处理范围

- S1 剩 2 批 6 份；S2–S5、S7 全部未开始；`Resources/Ebook` 432 份按用户决定暂跳过

## 2026-09-29 · S1 阶段收官（57/57）+ 并发事故登记

### 1. 收尾批次

- `S1_Projects_(直属文件)_01`（1 份 / 139 KB）→ sources 1 / concepts 3 / entities 2 / comparisons 2
- `S1_Projects_(直属文件)_02`（5 份 / 221 KB）→ sources 5 / concepts 6 / entities 7 / comparisons 2，另**追加**既有页 18 个
- **S1 阶段 13 批 57 份全部编译完成（100%）**

### 2. 当前规模与校验

| 项 | 数值 |
|---|---|
| WIKI 页面 | **246 页**（sources 71 / concepts 89 / entities 56 / comparisons 30） |
| 断链 | **0** |
| front matter 校验 | **246 / 246 通过** |
| 索引覆盖 | **246 / 246** |

### 3. ⚠️ 并发事故登记（须人工复核）

1. **页面被并发覆盖**：`WIKI/entities/Guoke Haina（国科海纳）.md` 被两个批次（`(直属文件)_01` 与 `_02`）在数秒内先后创建，后者 Write 返回 `overwrote`，**前者的内容已被覆盖、无法回滚**。处置：内容结构完整（基本盘/性能/路径/供货历史/商务要点/来源），**请人工复核取舍**。
2. **并发造成的重复主题页**（未合并未删除，依 AGENTS.md §5 待人工确认）：`CTI` 系列 3 种命名变体、`福地（Fudi）` / `Fudi（福地）` 两页；另 `(直属文件)_01` 与 `_02` 就同一份年度汇报大纲分别建了概念/对比页各一组（`OI Portfolio（开放创新组合）`、`Technology Roadmap 2026-2029`、`Material Safety Control（材料安全双轨管控）`、`REL Variant C vs Option B Dual-Layer`、`Degradable SAP Routes`），已交叉链接但**需确认是否合并**。
3. **口径冲突（未裁决）**：OI 组合存在四份清单（23 项 / 25 项 / 19 项重构 / 8 条台账），项目数与状态口径不一；已记矛盾记录，**须人工指定汇报基准**。

### 4. 工程结论：并发编译的安全边界

本轮实测确认——**同一份资料被两个批次同时编译时，会产出同主题重复页，甚至发生页面覆盖**。
后续派发原则：**同一主题簇的批次不并发**（按 block 串行），不同 block 之间方可并发；或并发前先划定互斥的文件命名空间。

### 5. manual_review 积压

回执合计 **49 条**（本轮批次新增 40 + 历史 9），**远超 AGENTS.md §5 的 5 条阈值**，须集中处理。

## 2026-09-29 · 重复页收敛（人工确认）：福地

- **人工裁决**：用户指示「以 `福地（Fudi）` 为准」（解决并发编译造成的同实体双页问题）。
- **执行**：
  1. 全库 `[[Fudi（福地）]]` → `[[福地（Fudi）]]` 改指（2 个文件）
  2. 正页补 `aliases: ["Fudi（福地）", "Fudy"]` —— 旧写法与英文拼写仍可解析
  3. **删除重复页** `WIKI/entities/Fudi（福地）.md`（内容此前已全部并入正页，**零信息损失**）；备份于 `.tools/_page_backup/Fudi（福地）.md.20260929`
  4. 正页内过期的「页面卫生提示」替换为「命名收敛记录」
- **复核**：WIKI **245 页**（sources 71 / concepts 89 / entities 55 / comparisons 30）｜**断链 0**｜front matter 245/245｜索引 245/245
- **遗留同类问题**：`CTI` 仍有 2 页（`CTI (Chromatic Technologies)` 被引 11 处 / 10.5 KB，`CTI（Chromatic Technologies Inc.）` 被引 6 处 / 2.9 KB）——**待人工指定正页**后同样收敛。
- **面积更大的重复组**：`(直属文件)_01` 与 `_02` 两个批次就同一份年度汇报大纲各建了一组概念/对比页（`OI Portfolio（开放创新组合）`、`Technology Roadmap 2026-2029`、`Material Safety Control（材料安全双轨管控）`、`REL Variant C vs Option B Dual-Layer`、`Degradable SAP Routes`）——已交叉链接，**待人工确认是否合并**。

## 2026-09-29 · 重复页收敛（人工裁决）：CTI 与 OI Portfolio

### 1. CTI —— 人工裁决「两者均保留、不合并」

- 库内 `CTI (Chromatic Technologies)`（10.5 KB / 被引 11 处）与 `CTI（Chromatic Technologies Inc.）`（2.9 KB / 被引 6 处）两页。
- **人工指示：两页没有关系、都要保留**。处置：
  1. **不删除、不合并**，两页均保留；
  2. 后一页原自称「别名页 / 待合并」的表述**已改为独立页表述**（tags 加入 `独立页`、`实体同一性待核`，移除 `别名页`/`待合并`）；
  3. 两页**各自添加命名提示**，互相指向并注明「人工指示两页均保留、不合并；实体关系待核，核实前勿混用数据」；
  4. ⚠️ **如实登记的待核事项**：后一页来源 [[Active Hygiene Roadmap（力致变色材料商业化路线图）]] 把该对象写作 "CTI (Chromatic Technologies Inc.)"，与前一页名称高度相似，**两页是否为同一实体尚无定论**——按人工裁决先按独立对象处理，标 `manual_review`。

### 2. OI Portfolio —— 人工裁决「合并」

- 两页：`IPC BCC OI Portfolio（开放创新项目组合）`（8.2 KB / 被引 11 处，含四份清单口径对照表）与 `OI Portfolio（开放创新组合）`（5.2 KB / 被引 4 处，含平台矩阵与优先级规范）。
- 处置：**以 `IPC BCC OI Portfolio（开放创新项目组合）` 为准**：
  1. 后者的独有内容（**5 平台 × 25 项目矩阵**、**优先级三档规范与一致性校验**）并入正页新增的「平台矩阵与优先级规范」一节，原结论未改动；
  2. 全库引用改指（4 个文件）；正页补 `aliases: ["OI Portfolio（开放创新组合）", "OI Portfolio", "Open Innovation Portfolio"]`；
  3. **删除** `OI Portfolio（开放创新组合）`（备份 `.tools/_page_backup/`）；正页内过期的「重复页提示」替换为「重复页收敛记录」。

### 3. 经核查**判定为不重复、予以保留**（未合并）

- `Degradable SAP Routes（可降解 SAP 四路线对比）`（4 条 SAP 路线专项）与 `可降解材料路线对比（PPC-P+PBAT vs PDA vs 淀粉基 SAP）`（基材/吸水体/低成本三个层级）——**范围与层级不同**，属互补对比页，且已互相交叉引用，**保留两页**。
- `Biodegradable SAP（可降解高吸水树脂）`（概念页）与上述两对比页——页面类型不同（概念 vs 对比），按 AGENTS.md §2 分列保留。
- `Technology Roadmap 2026-2029（技术路线图）`、`Material Safety Control（材料安全双轨管控）`、`REL Variant C vs Option B Dual-Layer（成本·性能·供应链）`——经查在另一批次中**无同主题对应页**，非重复页。

### 4. 复核

WIKI **244 页**（sources 71 / concepts 88 / entities 55 / comparisons 30）｜**断链 0**｜front matter **244 / 244**｜索引 **244 / 244**。
删除页备份：`.tools/_page_backup/`（可回滚）。

## 2026-09-29 · OI 编号口径裁决（人工）：以「重构版 E」为默认基准

### 1. 裁决内容

- **人工指定**：本库 OI 编号与项目数的**默认基准 = `IPC BCC OI Project List 2026-09-18（重构版·19 项）`**（重构版 E，2026-09-18，**19 项**，编号 `OI-1` ~ `OI-19`）。
- **引用纪律（自本日生效）**：
  1. 本库任何页面提到 `OI-xx`，**默认按重构版 E 的编号解释**；
  2. 引用其他清单（官方 v2 / 大纲 v7 / 供应商台账）的编号时，**必须注明出自哪一份与日期**；
  3. 其他三份清单保留为「历史口径」，差异如实并列、不删不覆盖。
- **落地位置**：`WIKI/concepts/IPC BCC OI Portfolio（开放创新项目组合）.md` 新增「Baseline for reporting 汇报基准」节；`index.md` §六、维护说明 写入引用纪律；此前登记的 manual_review「OI 组合口径未裁决」**结案**。

### 2. ⚠️ 裁决带出的清理待办（新发现，已量化）

审计脚本 `.tools/audit_oi_numbers.py` 扫描结果——**45 个页面引用 OI 编号，其中 24 页在两套编号之间混用**：

| 类别 | 页数 | 含义 |
|---|---|---|
| 符合基准（仅不补零 `OI-x`） | 15 | 与重构版 E 口径一致 |
| 旧口径（仅补零 `OI-0x`） | 6 | 出自官方 v2 / 大纲 v7，引用须注明 |
| ⚠️ **两套混用** | **24** | 同一页既有 `OI-08` 又有 `OI-8`，**列为清理待办** |

**处置口径：不自动转换。** 编号语义需逐条核对原文与 old→new 对照表（例：大纲 v7 的 `OI-04` = PVA/PTT REL，而重构版 E 的 `OI-4` = Biomass PP/PET，**同号不同项**，机械换算会引入错误）。后续编辑这些页面时逐条补注出处，或按对照表换算。

## 2026-09-29 · 批次 S1_Projects_REL_01 编译（CoPET 项目簇 · 10 份）

**范围**：`Projects/REL` 的 10 份 CoPET 资料（样板批），`read` 源为 `RAW_FULL/ima_sync/个人知识库/WKB/Projects/REL/`。批次文件 `.tools/compile_batches/S1_Projects_REL_01.json`。

**动作**：按 AGENTS.md §2/§3 编译 —— 先建源摘要页，再派生概念/实体/对比页，全部与源摘要页 `[[wikilinks]]` 互链。

**新建源摘要页（10）**：
[[CoPET 供应基盘背调汇总（26 家企业·联系方式版）]]、[[CoPET 供应基盘背调汇总（布局核实精简版）]]、[[CoPET 双组份热粘合纤维市场与供应商（供应链分层·明细表）]]、[[CoPET 双组份热粘合纤维市场与供应商（供应链分层·文档版）]]、[[CoPET-PET 与 PE-PET 成本结构深度拆解报告]]、[[CoPET 与 PET 成本差异对比（2026 年 7 月）]]、[[CoPET-PET 与 PE-PET ES 纤维 ADL 影响模拟（英文详版）]]、[[CoPET ADL 转型蓝图（皮层聚合物替代评估）]]、[[CoPET 采购蓝图：成本拆解与供应分层]]、[[优化 REL 五纤维配方与穿透热风粘合工艺模拟]]

**新建概念页（8）**：[[CoPET（低熔点共聚酯）]]、[[PET（聚酯）]]、[[ADL（导流层）]]、[[IPA（间苯二甲酸）]]、[[无锑聚酯]]、[[亲水整理耐久性]]、[[毛细梯度设计]]、[[并列复合自卷曲纤维]]

**新建实体页（11）**：[[厦门翔鹭]]、[[盐城市中联]]、[[嘉兴新丰]]、[[汇维仕]]、[[优彩环保]]、[[桐昆集团]]、[[江南高纤]]、[[三房巷]]、[[天津石化]]、[[恒逸]]、[[宁波大发]]

**新建对比页（2）**：[[CoPET 与 PET 成本对比]]、[[CoPET-PET 与 PE-PET 皮芯纤维对比]]（均含「成本」「供应链风险」两列）

**追加更新的既有页（只追加、注日期、未改既有结论）**：
- [[皮芯复合纤维]] —— 追加「CoPET 皮芯（4080 型）的判据与工程条件」小节（4080 判据、并列复合构型、本批成本/良率参数、验证记录）
- [[REL增强层]] —— 追加「REL 五纤维配方与穿透热风粘合工艺」小节（配方、性能预测、TAB 窗口、验证记录）
- [[热风粘合无纺布]] —— 追加「CoPET 项目批的热风工艺参数」（Zone 1/2 温度、风速、急冷、粘合下限、验证记录）
- [[福建闽瑞新合纤]] —— 追加「CoPET 项目批的定位记录」（D 层 ES 龙头 / CoPET 替代对象、0.8D 细旦竞争、追加来源）

**索引**：`index.md` 四区已按 sources/concepts/entities/comparisons 追加条目，规模 62 → **93 页**，「最后编译」更新为 2026-09-29；批次进度表新增「批次 S1 已完成」。

**manual_review 标记（本批新增 5 条，累计 9 条 → 已超 §5 的 5 条阈值，须集中处理）**：
1. CoPET/REL 配方比例与工艺参数（产品开发敏感）—— [[优化 REL 五纤维配方与穿透热风粘合工艺模拟]] 等
2. CoPET 具体报价点位（页面只留区间与相对价差）—— [[CoPET 与 PET 成本对比]] 及 5 个实体页
3. 采购指令与合同条款（RFQ 限 A 层、Sb 检测限写入技术协议、谈判目标价）—— [[CoPET 采购蓝图：成本拆解与供应分层]] 等
4. 26 家企业联系方式与联系人信息（**完全不页面化**，仅留原文）—— [[CoPET 供应基盘背调汇总（26 家企业·联系方式版）]]
5. ⚠️ **跨来源矛盾**：优彩环保产品层级（公司自述「皮芯结构复合涤纶短纤」vs 第三方采购文档判为 C 层「非双组份」）—— 依 §5「矛盾检测」在 [[优彩环保]] 页登记矛盾、**不擅自裁决**，待人工确认

**未建页说明（依用户门槛：本批 ≥2 份来源提及，或属核心参数/机理/供应商/项目）**：供应基盘背调中另有 15 家企业（天富龙、南亚塑胶、东丽 TAK/世韩、泰光、江阴宏凯、河北金友、江苏中石、宁波天诚、湖北博韬、可隆、兴辉、三菱、晓星、杜邦、Radici、FiberVisions、FIT 等）**仅在附录级清单中出现**，为避免碎片页污染图谱**未单独建实体页**，其事实已在对应源摘要页留存，后续如需可作为独立实体页素材。

**治理备注**：本次仅新增/追加，未移动、未重命名、未删除任何已有文件；`RAW/`、`RAW_FULL/`、`AGENTS.md` 均未改动。中途曾因路径笔误在 `E:/` 下误建 `WIKI-OB/placeholder.md`，已即时删除并移除该空目录（非知识库文件，不影响本库）。

---

## 2026-09-29 午后 · Wave A/B 编译推进 + 收尾治理（主会话汇总）

**编译推进（S1–S7 总盘 605 份 → 已编译 537，88.8%；WIKI 1012 页：sources 551 / concepts 253 / entities 127 / comparisons 78）**

- **Wave A（3 代理并发，全成）**：S5 Meeting Minutes_04/05 收尾 → **S5 清零 47/47**；S2 Test Method_07/08/09（19 份）→ TM 全部完成；S3 Regulation&PSC_05/06/07（25 份，4 概念 + 2 对比页：GB/T 28004 新旧版对比、离型纸 vs 离型原纸）。
- **Wave B（2 代理并发，全成）**：S2 IP_07/08 整批 + IP_01/03/04/05 查重核验 → **S2 156/167**；S3 Supply Base_04~08（33 份，含 Cabot/天富龙/中弘芯/三洋化成 SDP/盛色 BLOCLO 等实体）→ **S3 122/123**。
- **剩余 68 份**：S2 IP 大文件尾 11（IP_01 剩 2 份共 983 KB / IP_03 2 / IP_04 2 / IP_05 5，多为 US/JP/CN 专利扫描件）；S3 Supply Base_05 尾 1（天富龙-扬州富威尔简介）；S4 全部 56（OI_03/16~20 + Training/FEI/Pulp World）→ 待 Wave C。

**收尾治理（本轮）**：
1. 28 页 `title ≠ 文件名`（新代理又违Naming规）→ `normalize_titles.py --apply` 归一，原 title 存 aliases
2. 断链 76 → 自动修复 62 处（33 文件）；**剩 60 条真实断链（59 个缺失目标）**，均为代理写了 `[[计划页]]` 未建页（Top：粘扣强度对比 16 处、Rewet 口径对比 13 处、化妆品限用体系 11 处、温变湿变微胶囊 10 处、共挤弹性膜 10 处…）——**与 S1 收官同类，待 Wave C 后统一补 seed 页**
3. 清理 Wave B 误建的尾随空格垃圾目录 `WIKI/entities/Sanyo Chemical /`（内容已备份 `.tools/_page_backup/`；**教训：Windows 删不掉尾随空格目录，先 `mv` 改名摘掉空格再删**）
4. `index.md` 重建对齐（1009/1009）
5. 新增 `.tools/remaining.py`（剩余统计；**再次验证 bash heredoc 会间歇性把正则 `\s` 替换成 `/`——统计类正则一律写 .py 执行，本次内联脚本两度误报"全部剩余 605 份"即此因**）

**回执 manual_review 累计 146 条**（S2 IP 专利批贡献 26 条：FTO 边界、法律状态待验证；Supply Base 商务敏感 9 条）——持续积压，待集中处理。

**下一步**：Wave C（S4 剩余 56 份 + S2 IP 尾 11 + S3 尾 1）→ 补 seed 页修 60 条断链 → 最终 verify + Ebook 432 份维持跳过。

---

## 2026-09-29 午后 · Wave C + 全库收官（S1–S5、S7 全部 100%）

**Wave C（2 代理并发）**：
- S4 Open Innovation_03/16~20 + Training/FEI/Pulp World：全部落盘。**OI_17~20 曾被误判"代理虚报"——实为那批页面 `source_path` 写成 `RAW_FULL/` 前缀（批单为 `RAW/`）导致查重落空**，第二个代理核实 33 页内容完整（22–114 行/页无 stub）、校正 source_path 登记、重写回执。
- S2 IP 尾 11 份：**实际早已完成**——族页用多值 `source_paths:` 列表登记，单行判重脚本识别不到；补做 front matter 登记后清零。
- S3 尾 1（天富龙-扬州富威尔）：建正名页 `天富龙集团与扬州富威尔公司简介（Tinfulong／Fuweier 2025-05-10）`。

**断链终修（233 处引用 → 0 断链）**：
1. `.tools/seed_missing.py` 全量枚举 63 缺失目标：11 个别名改指（`/`→`_` 文件名变体）+ 2 近标题 + 50 待补
2. `.tools/final_link_fix.py --apply`：改指 33 项 + 高频目标补 **22 个 seed 页**（对比 3 / 实体 8 / 概念 11；只登引用来源与待补维度，**不编造数据**）
3. 清理占位符 `wikilink`/`log` 行文误用 2 处
4. **`.tools/rebuild_index.py` 修复一个隐蔽 bug**：`parse_front_matter` 按逗号切分内联列表，`Antimony, Sb` 这类含逗号值被拆散重组出假链接 → 改为引号感知切分
5. `.tools/patch_frontmatter.py`：49 页缺字段补全（seed 页漏 title、旧代理页缺 domain/status/subjects）

**终态**：S1–S5、S7 共 605 份 **全部编译完成**（Ebook 432 份按用户决定跳过）｜WIKI **1104 页**（sources 607 / concepts 280 / entities 137 / comparisons 80）｜**断链 0**｜front matter **1104/1104**｜索引 **1104/1104**｜manual_review 回执累计 **147 条**待集中裁决。

**新增工具**：`.tools/remaining.py`（支持 source_paths 多值判重）、`.tools/diag_missing.py`、`.tools/seed_missing.py`、`.tools/final_link_fix.py`、`.tools/patch_frontmatter.py`。

---

## 2026-09-29 深夜 · Ebook P0/P1/P2 状态盘点 + 干燥章 front matter 修复

**front matter 修复（14 页 → 0 缺陷）**：
- Wave 2 新编译的 **13 篇 Industrial Drying 章节页**缺 AGENTS.md §2.0 六个必填字段（`date_published` / `date_processed` / `credibility` / `knowledge_update_status` / `key_claims` / `pages_linked`），`verify_wiki.py` 报 14 FAIL。
- 用 `.tools/_id_digest.py` 逐页抽 H2/H3 + 原文金句 + 数值，据此**逐条写实** `key_claims`（不编造）；`pages_linked` 从各页「Related Sources」段抽真实链接 + 补 `[[Handbook of Industrial Drying]]`。
- `.tools/_repair_id_frontmatter.py` 批量回写（备份先落 `.tools/_page_backup/`，共 21 份）。
- 顺带修 `Handbook of Adhesive Technology Full Report.md`（P0 胶黏剂手册，旧页同样缺 6 字段；`related:` 字段改写为标准 `pages_linked:`）。
- **终态：front matter 1218/1218 通过；索引 1218/1218；WIKI 共 1218 页（sources 721 / concepts 280 / entities 137 / comparisons 80）**。

**P0/P1/P2 状态盘点（权威判据 = source_path 登记，非 mtime 非文件名）**：
- 新增 `.tools/_ebook_coverage_check.py`（覆盖率）与 `.tools/_ebook_status_report.py`（分级报告 + 工业干燥板块归类）。
- **P0：17 本有效条目，15 本全书完成，章节 83/127**
  - `Handbook_of_Industrial_Drying` 13/53 —— **40 章待编译**（A 原理 4 / B 设备 13 / C 物料 17 / D 系统 4 / E 经济 2）
  - `Absorbent Technology` 12/16 —— 4 项「待编译」经 `.tools/_ab_dupe_diff.py` 逐行 diff 证实为 **IMA 重同步的内容完全重复件**（差异仅 media_id / source_file / original_path / H1 四行元数据，正文零差异）→ **实质 16/16 完成**
  - → **P0 真实缺口 = 40 章（全部来自工业干燥手册）**
- **P1：清单中不存在**（manifest `scope: P0 + P2(index_only)`，40 本书中无 P1 条目）
- **P2：4 本全部 `compile_as: index_only`，4/4 索引页已建**（含 `Cosmetic Science and Technology.md` CRC 2009 15 章轻量索引）→ **按其契约已完成**；15 章正文是刻意不编译，非遗漏

**待用户裁决**：工业干燥 40 章是否继续编译。若只取卫材高价值，建议 C 板块 `Ch36`（唯一剩下带★的纤维/纸浆/聚合物轴线章）+ A 板块 `Ch02/Ch03`（结合水/自由水二分、特征干燥曲线——已被全书红线引用两次）；B 板块 13 章设备类、E 板块 Ch51/Ch52（结晶、油炸）对卫材价值最低。

**新增工具**：`.tools/_ebook_coverage_check.py`、`.tools/_ebook_status_report.py`、`.tools/_id_digest.py`、`.tools/_ab_dupe_diff.py`、`.tools/_repair_id_frontmatter.py`。

---

## 2026-09-30 凌晨 · P1 分级清单建立 + P1 全量编译收官

**P1 从"不存在"到落地——澄清一个误判**：`_gen_ebook_manifest.py` 第 137 行有 `if pri not in ("P0","P2"): continue  # P1 deferred`，即**P1 书真实存在（43 本）但被显式排除在 P0+P2 manifest 之外**。新建 `.tools/_gen_p1_manifest.py` 复用同一套书籍合并 / 优先级打标 / 分章筛选逻辑，产出 `.tools/ebook_p1_manifest.json`（43 本，P0/P1/P2 全量分布 = 36/43/4，共 83 本）。

**用户裁决的两条规则**：
1. P1 **全量 43 本按章编译**
2. root 正文 **> 800,000 字符**的大部头 → **只建索引页**，不逐章编译

**规模修正（重要）**：首轮 P1 排期只统计了「章节正文」，漏算 root 正文 → 误估 1.68M 字符；补齐后 **P1 可用正文 = 11,489,967 字符**（约 1150 万），量级远超 P0 剩余。分组结果：逐章编译 12 本 / 80 章；仅建索引页 31 本（其中 2 本无 root 文件、源侧无内容 → 跳过）。

**新增工具**：`.tools/_gen_p1_manifest.py`、`.tools/_gen_p1_batches.py`（50 批次）、`.tools/_p1_triage.py`（四级相关性分级 + 正文可用性）、`.tools/_p1_coverage_check.py`、`.tools/_ebook_status_all.py`（P0/P1/P2 统一盘点）。

**执行结果（Wave 3–8，共 8 波）**：
- **章页 80/80 落盘**（12 本全章完成）：
  Manufactured Fibre Technology 20 ｜ Seymour Polymer Chemistry 18 ｜ Ebewole Polymer Science 15 ｜ Smart Polymers 14 ｜ US Patents 智能织物传感 6 ｜ 其余 7 本单卷本各 1
- **索引页 35/35 落盘**（含 8 本 >800k 大部头 + 27 本无分章文件）
- 高价值提前项：`US_Patents_智能织物传感_拆解` 实为 **P&G/Howell 湿态指示专利族**（US20070270773A1 热变色、US5197958 / US5389093 Howell 母案与续案、US8273939、US10905605、**US11013641 = 金佰利自家**），已优先编译并逐条标注法律状态待核。

**终态**：WIKI **1333 页**（sources 836 / concepts 280 / entities 137 / comparisons 80）｜front matter **1333/1333 通过**｜索引 **1333/1333**｜断链 302（全部为 P1 之前的存量 seed 缺口；P1 新增页引入的 2 处已修：`01_PLA_PPC_可降解材料研究报告.md.md`、`06_SSMMS无纺布技术研究报告.md.md` 双 `.md` 后缀未写全）｜P1 manual_review 回执 **61 条**（源侧 OCR 乱码 / 出版年缺失 / 内部数字打架 / 专利法律状态）。

**限流踩坑（本次实测）**：3 个 lite 代理并发 → 全部 429（重置时间 09-30 08:00）；降为 **2 并发仍半数 429**；**单代理串行 → 连续成功（idx-retry-a 5 项、idx-final 11 项）**。→ 再次确认：**可控变量是并发数，单代理最稳**，与既有记忆一致。

**待办**：P0 工业干燥 40 章（按板块 A 4 / B 13 / C 17 / D 4 / E 2）；P1 大部头 45 章（按规则刻意不编译）；302 处存量断链补 seed 页。

---

## 2026-09-30 晨 · 断链清零（302 → 0）

**背景**：P1 编译收官后 `verify_wiki.py` 报 **302 处断链**（累计自 S1–S7 收官后的存量 seed 缺口 + Wave 2/3 新页引入）。

**三段式修复（新增 `.tools/_fix_links_all.py`，幂等、可 dry-run）**：
1. **改指（46 种 / 182 处引用）** —— 只做**同名变体**（同一实体的写法差异），绝不做语义窄化：
   - 归一化命中：`SAP`→`SAP（高吸水树脂）`(45)｜`导流层 ADL`→`ADL（导流层）`(22)｜`绒毛浆 Fluff Pulp`→`绒毛浆（Fluff Pulp）`(17)｜`面层 Topsheet`→`Topsheet（面层）`(7)｜`Kimberly-Clark`→`Kimberly-Clark（金佰利）`｜`HG Chem/SNF` 等
   - SAP 家族收敛：`SAP Superabsorbent Polymer` / `Superabsorbent Polymer 高吸水树脂` / `Synthetic Superabsorbent Polymers` / `SAP Composites` → 统一指向 `SAP（高吸水树脂）`
   - 胶黏剂手册分册改名：`Part 2 Adhesion Science`→`Part 2 Fundamental Aspects`；`Part 3 Polymer Chemistry`→`Part 3 Adhesive Classes`
   - 温致变色收敛：`热致变色 Thermochromic` / `温致变色 Thermochromic` → 既有 `热致变色`
   - 同义组合并（9 组）：`非织造布/非织造材料/无纺布 Nonwoven` → `Nonwoven 非织造布`；`双组分纤维 Bicomponent Fiber`→`双组分纤维 Bicomponent`；`水刺 Spunlace`→`水刺 Hydroentanglement`；`热熔胶 Hot Melt`→`热熔胶 Hot Melt Adhesive`；`气流成网 Airlaid`→`气铺 Airlaid`；`交联密度 Cross-link Density`→`Crosslink Density`；`光致变色 Photochromism`→`Photochromic`；`保水值 WRV`→`WRV 水保留值`；`刺激响应材料`→`刺激响应聚合物 Stimuli-Responsive Polymer`
2. **建 seed 页（256 个）** —— 概念 247 / 实体 9（后修正 3 个误判）。模板固定：`status: seed` + 引用来源清单（去重、≤12 条）+ 待补维度，**明写「未填任何数据、须回来源核对、禁止编造」**。高频：吸收芯体 23 / 光致变色 14 / 回渗 Rewet 13 / 机械变色 13 / 达西定律 10 / 热致变色 9 / Fick 定律 9。
3. **手工收尾 2 处**：`Handbook of Adhesive Technology Full Report.md` 的 `pages_linked` YAML 缺引号（写成 `[[[X]]` 畸形）→ 修正为合法引号列表；`[[每克厚度 T/W]]` 的半角 `/` 无法做文件名 → 页面落地为全角 `每克厚度 T／W.md`，改写源页链接匹配。

**⚠️ 重要教训（新增铁律）**：**token-overlap 自动改指会犯语义错误** —— 首轮尝试用「token 重合度」自动匹配，产出 `光致变色 Photochromic`→某供应商调研报告、`BASF`→某产品页、`Sun Chemical`→`Chemical bonding`、`热熔胶 Hot Melt`→`Polyolefin Hot Melt Adhesive` 等**把上位概念窄化到下位页**的错误改指。→ **改指只允许「同名变体」，语义近似一律建 seed 页**，宁可多建占位页也不做错误合并。

**终态**：WIKI **1589 页**（sources 836 / concepts 530 / entities 143 / comparisons 80）｜**断链 0**｜front matter **1589/1589 通过**｜索引 **1589/1589**。备份：`.tools/_wiki_backup_20260930/`（修复前全量 WIKI）。

**新增工具**：`.tools/_link_triage.py`、`_link_triage2.py`（分级 + 候选评分）、`_fix_links_all.py`（改指 + seed 生成，支持 `--apply`）、`_link_fix_plan.json` / `_link_fix_result.json`（计划与结果留痕）。

**待办不变**：P0 工业干燥 40 章；**530 个 seed 页待按引用来源补齐真实内容**（其中吸收芯体、回渗、达西定律、Fick 定律等属核心概念，建议优先）。

---

## 2026-09-30 上午 · Seed 页补齐（第一轮：核心层 + 存量重标）

**背景**：断链清零时建了 256 个 seed 占位页，加上 S1–S7 收官时的存量 seed，`status: seed` 共 447 页。

**⚠️ 首要发现（修正一个长期误判）**：**`status: seed` 不等于"没有内容"**。S1–S7 收官批建的 161 页里，大量页面**已有完整正文**（如 `Residual Fluid & Pore Stranding` 9 条机理、`Changeover Four-Layer Architecture` 四层表、`Repitch` 定义表），只是 status 仍标 `seed`。→ 批量改标 `status: growing`（**161 页**），未动任何正文。
  - 另一个坑：**统计"内容量"时不能剔除表格行与列表项** —— 首版脚本把 `^[#>|\-*]` 行全删，导致表格密集型 legacy 页被误判"空白"（1175→240 的假缺口）。改版保留表格/列表只去掉 seed 横幅与纯链接行后，真空白仅 **174 页**。

**补齐执行（10 批代理，严格"只引库内实证、禁编造"）**：
- **按引用频次排序，引用 ≥2 的 92 页 100% 补齐**（吸收芯体 23 引、光致变色 14、回渗 13、机械变色 13、刺激响应聚合物 11、达西定律 10 …）
- 额外补齐引用=1 的高价值 12 页（Polyolefin Absorbent Materials、变色材料、过滤材料、聚合物刷、植物基材料、中空纤维、爆裂纤维、鸡毛纤维、自由体积、导电无纺布、热风非织造、Nonwoven Lamination）
- **合计填充 104 页**；每页结构：Definition / Key Parameters（逐值带 `（源：[[…]]）`）/ Mechanism / Hygiene Relevance / Open Questions / Related Sources
- **工具链**：`.tools/_seed_inventory.py`（盘点）→ `_gen_seed_digests.py`（为每页生成原文摘录 digest，447 份 → `.tools/_seed_ctx/`）→ 代理读 digest 写页 → `verify_wiki.py`

**重复页处理**（`.tools/_seed_dupes.py` + `_consolidate_seed_dupes.py`）：
- **合并 6 对**（一方为真 stub）：`热致变色`→`热致变色 Thermochromic`｜`Contact Angle`→`接触角 Contact Angle`｜`Hot Melt Adhesive`→`热熔胶 Hot Melt Adhesive`｜`毛细管压力 Capillary Pressure`→`毛细压力 Capillary Pressure`｜`2025.06.25 Learning Cycle`→`GRIFFIN Learning Cycle Check In`｜`SymDeo™ XPP`→`Symrise SymDeo™ XPP（中文版）`
  - 做法：全库入链改写为 canonical（19 个文件）→ stub 转**指针页**（`status: merged`）+ `manual_review` 提示，**未删除**（AGENTS.md §5）
- **标记 2 对双方均有内容的重复**（不强并，交人工）：`Changeover Four-Layer Architecture` vs `83 Changeover …`；`Repitch` vs `82 鼓距…repitch 选型`

**⚠️ digest 局限（写进流程注意）**：关键词匹配生成的 digest 会**跑偏**（如 `过滤材料` 命中液晶/热电、`爆裂纤维` 命中通用纤维表征）。→ 已要求代理**回 cited-by 来源页原文核对**，跑偏摘录一律弃用；但**根本对策是给 digest 加主题词白名单**。

**终态**：WIKI **1589 页**｜**断链 0**｜front matter **1589/1589**｜索引 **1589/1589**｜**剩余真 seed 176 页**（174 空白 + 2 半成品）。

**新增工具**：`.tools/_seed_inventory.py`、`_seed_context.py`/`_seed_context2.py`（正文检索）、`_gen_seed_digests.py`、`_seed_classify.py`/`_seed_classify2.py`、`_relabel_seeds.py`/`_relabel_seeds2.py`、`_seed_dupes.py`、`_consolidate_seed_dupes.py`。备份 `.tools/_page_backup_dupes/`。

**待办**：剩余 176 个真 seed 页按 `_seed_ctx/` digest 继续补齐（按 digest 内容丰富度排序即可）；4 页重复待人工裁决。

---

## 2026-09-30 下午 · Seed 页全部清零（447 → 0）

**收尾结果**：`_seed_classify2.py` 报 **`status: seed` 页面 0**。WIKI **1589 页**｜**断链 0**｜front matter **1589/1589**｜索引 **1589/1589**。

**本日 seed 处理总账（447 页）**：
| 处置 | 页数 | 说明 |
|---|---|---|
| 改标 `status: growing` | 161 | S1–S7 收官批遗留，正文完整只是 status 没改 |
| 合并为指针页（`status: merged`） | 8 | 命名变体重复（热致变色/Contact Angle/Hot Melt Adhesive/毛细管压力/Learning Cycle/SymDeo™/有限差分法/Silane Coupling Agent），入链已改写，**未删页** |
| 补齐真实内容 | **278** | 每页 Definition / Key Parameters（逐值带 `（源：[[…]]）`）/ Mechanism / Hygiene Relevance / Open Questions / Related Sources |

**执行方式**：`_gen_seed_digests.py` 为每页生成原文摘录 digest（447 份 → `.tools/_seed_ctx/`），代理按 `_seed_fill_plan.json` 分 23 批（每批 8 页）读 digest 写页。共约 23 次代理派发。

**⚠️ 限流又双叒来了（第 4 次实测，加深认知）**：
- 09-30 15:0x 三并发派批 17/18/19 → **全部 429**（报重置 10-01 06:20）
- 但**三个代理实际各写了一部分页面才断**（seed 从 174 掉到 53）→ 第 2 次证实「**代理报错 ≠ 没干活，只信磁盘**」
- 17:0x 重派 → 2 并发一次成功；随后 3 并发也成功 → **限流窗口会自己过去，重试即可，不必等"重置时间"**

**已知遗留（manual_review 类，不影响断链/索引）**：
1. **重复标题待人工裁决**：`稀释便液 BM simulant A` ↔ `BM Simulant A`、`粘胶 Rayon` ↔ `粘胶纤维 Viscose Fiber`、`胶乳 Latex` ↔ `胶乳胶黏剂 Latex`、`干燥角质化` ↔ `角化`、`纺粘熔喷` ↔ `SMS 纺粘熔喷复合` ↔ `SMS复合结构`、`热风无纺布` 系 4 标题、`东丽`/`舒美` 挂在 concepts（应为 entities）
2. **口径冲突未裁决**：PP 表面能 23 vs 29–31 mN/m；PNIPAAM LCST 28/32/34.9 °C；脱挥发分 T>Tg vs 末段干燥 T<Tg；Stimuli-Responsive PCM 光学/热管理两义
3. **大量页面定义标注 `定义待补`** —— 库内来源多为功能性口径，词典式定义需回原书
4. **`东丽`/`舒美` 等实体页在 concepts/ 目录**，分类待人工纠正

**工具链（本轮新增/完善）**：`_seed_fill_plan.py`（剩余 seed 分批）、`_seed_intra_dupes.py`（待补集合内部查重）、`_seed_context2.py`（全库正文检索）、`_merge_seed_dupes2.py`。

---

## 2026-09-30 傍晚 · 工业干燥 40 章收官 —— P0 全部完成

**执行**：`_gen_id_batches.py` 把 40 章待编译清单按 5 章/批分 8 批（含源文件 `# Chapter N — Title` 标题抽取），8 个代理派发，**一次通过、零 429**。

**结果**：`Handbook_of_Industrial_Drying` **53/53 章**全部落盘（此前 13 + 本轮 40）。
- 高价值章：**Ch36 Drying of Wood**（角化分子机理 p.830 氢键逐字引证、FSP、各向异性渗透——直通绒毛浆）、Ch19 SSD、Ch20 Table 20.1 非织造基准、Ch8/Ch10（SAP 喷雾制粉/微胶囊）、Ch44（SAP 计量给料）
- 低相关章（Ch11 冷冻干燥、Ch22 鱼、Ch52 油炸）已**如实降级**，页面从简，未强行关联

**书目索引页** `Handbook of Industrial Drying.md` 已更新：新增「Compiled Chapters 已编译章节（全 53 章）」按 A–E 板块分组（★标注卫材关键轴），`pages_linked` 扩到 54 项。

**终态**：WIKI **1629 页**（sources 876 / concepts 530 / entities 143 / comparisons 80）｜**断链 0**｜front matter **1629/1629**｜索引 **1629/1629**。
**P0 状态**：**16/17 本书全书完成，章节 123/127** —— 唯一"未完成"的 `Absorbent Technology` 4 项已证实为 IMA 重同步重复件，**实质 16/16**。**P0 收官。**

**工具新增**：`.tools/_gen_id_batches.py`、`_update_id_book_index.py`、`_id_batch_index.json`。

---

## 2026-09-30 晚 · 判重锚统一 + 积压账目重建（Reconciliation 第一步，用户授权执行）

**背景**：会话只读对账（`WKB-OB-Architecture-Reconciliation-2026-09-30.md`，存 WorkBuddy 会话目录）发现 P1 三项，用户拍板执行第一步（工具侧零风险项）。

**1. 判重锚统一（P1-1）**
- 269 个源摘要页 `source_path` 由 `RAW_FULL/` 改写为对应 `RAW/` 路径（改前 269/269 逐一验证 RAW 侧文件存在，零缺失）；同页正文旧路径引用一并替换 113 处。
- 改后全库 RAW_FULL 锚 **0**；统一锚碰撞检查发现 **2 组真实重复页（4 页）**：`Cross-linked Cellulose and Derivatives` ↔ `Cross-linked Cellulose and Its Derivatives`、`Liquid Flow in Porous Structures` ↔ `Porous Structure and Liquid Flow Models`（同章双页，已登记 `.tools/_anchor_collision_report.json`，**待人工裁决合并**）。
- 备份：`.tools/_anchor_unify_backup_20260930/`（269 页 + index/AGENTS/backlog）。脚本 `.tools/_unify_anchor_20260930.py`。

**2. 积压账目重建（P1-2）**
- 旧 `_compile_backlog.json`（1037 条，25% 陈旧）作废，按统一锚重算：RAW md 1720 = **compiled 866** + backlog 854（其中无正文登记 14 → 净 840，含空壳件 209 建议不派发）。**真实可派发待编译 ≈ 631 条**。
- 8 个 book-index 元数据锚指向 RAW_FULL 提取工件属良性特例（`.tools/_compile_reconcile_20260930.json`）。脚本 `.tools/_rebuild_compile_backlog_20260930.py`。

**3. AGENTS.md 规范修订（P1-3 + stable 判据）**
- §1 目录对齐实况：注明无 raw/pdfs/；`RAW/journal/` 标注**规划中未启用**（§7 章首加横幅，启用前不执行）；补 `.tools/` 条目。
- §1 新增强制规则：**source_path 一律指 RAW/，RAW_FULL 仅作编译输入不作判重锚**。
- §2.1 新增 **stable 判据**（≥2 独立来源或 1 高可信源 + 无未决矛盾 + 治理检查无修正 + 三要素齐备）与晋升机制（脚本出候选、人工确认晋升）。
- §2.3 source_path 注释、§3 判新依据、§8 编译指令同步更新。

**4. stable 晋升候选（只读）**
- `.tools/_stable_candidates_20260930.py` 扫描 521 个 growing 页：**候选 21 页（全 concept）**；卡点分布：待补/待验证标记 ~430 页、未决矛盾 42 页（与已知 4 项口径冲突吻合）。**未改任何页面 status，晋升待人工确认。**

**遗留（待授权/待裁决）**：①2 组重复页合并；②42 页矛盾页裁决；③21 候选页晋升确认；④journal 闭环启用决策；⑤东丽/舒美迁 entities。

---

## 2026-09-30 晚（二） · 重复页治理 + 口径裁决 + manual_review 裁决单（Reconciliation 第二步，用户授权执行）

**1. 重复页合并（11 组 → 10 组合并 + 1 歧义拆分，全部转 status: merged 指针页，未删页，原文存档保留）**
- 合并 10 组：稀释便液 BM simulant A→BM Simulant A；粘胶 Rayon→粘胶纤维 Viscose Fiber；胶乳胶黏剂 Latex→胶乳 Latex；角化→干燥角质化 Hornification；SMS 纺粘熔喷复合、SMS 复合无纺布→SMS复合结构；热风无纺布、热风非织造 Hot-Air Bonded Nonwoven→热风粘合无纺布；Cross-linked Cellulose and Derivatives→…and Its Derivatives（sources 同章双编译）；Liquid Flow in Porous Structures→Porous Structure and Liquid Flow Models（sources 同章双编译）。
- 歧义拆分：热粘合热风无纺布 Airlaid（页面自证混淆两个概念）→ 双指向 [[热风粘合无纺布]] + [[气铺 Airlaid]]。
- 入链改写 155 处 / 55 文件；canonical 页均追加带日期合并注记。备份 `.tools/_merge_dupes_backup_20260930/`。脚本 `.tools/_merge_dupes_governance_20260930.py`。
- **裁决保留不合并**：合金粘胶 Alloy Rayon（特种纤维，非普通粘胶变体）；纺粘熔喷 Spunbond-Meltblown（spunmelt 工艺家族页，SMS 仅为其标准型）。

**2. 东丽/舒美迁移**：concepts/ → entities/（type: entity、category: 供应商、relationship: 信息源）。索引现为 concepts 528 / entities 145。备份 `.tools/_entity_move_backup_20260930/`。

**3. 口径冲突 4 项裁决（追加式注记，原结论未动）**
- PP 表面能：**≈29–31 mN/m 为库内主口径**（ScienceDirect iPP=30.1/30.2 mN/m 等外部一致）；23 mN/m（Chemical bonding）判为来源专属离群值。涉事页：亲水整理、等离子处理。
- PNIPAAM LCST：**≈32 °C 为主口径**（三源一致 + 教科书值）；34.9/28 °C 判为体系依赖变体（共聚/刷结构/端基敏感），摘 [待验证]。
- SAP 干燥 T>Tg vs T<Tg：判为**分段工艺窗口关系，非事实矛盾**（前中段驱动扩散 / 末段冻结网络保溶胀，与 hornification 同机理方向）。
- PCM 两义：判为**同缩写两类材料（光学 GST/VO₂ vs 热管理微胶囊），非冲突**，两页分立 + 全称消歧，关闭两义标记。

**4. manual_review 24 条**：机械闭环 2 条（变色油墨联系表（1）→ merged、ASTM E2149-20 平行备份 → merged，脚本 `_mr_dedupe_20260930.py`，备份 `.tools/_manual_review_dedupe_backup_20260930/`）；余 22 条出**裁决单** `.tools/_manual_review_triage_20260930.md`（B 商务敏感 5 / C 对外释放 2 / D 源侧问题 4 / E 建议批量转 done 10 / F 域外 1）。Shin-Etsu 两条经核验为不同公告、非重复。

**5. 定义待补显式清单**：`.tools/_def_pending_20260930.json` —— 631 页含待补标记（定义待补 169 处、[待补]/[待验证] 1958 处；concepts 482 / entities 102 / comparisons 47）。

**终态**：WIKI **1629 页**（sources 876 / concepts 528 / entities 145 / comparisons 80）｜status：growing 512 / merged 21 / seed 2 / stable 1｜断链无新增（残留旧名仅存在于 canonical 合并注记与指针页存档，属设计内）。

**待王总决策**：①journal 闭环启用与否；②JackywineV 库处置；③裁决单 B/C/F 类 8 条逐条拍板、D/E 类 14 条批量确认。

---

## 2026-09-30 晚（三） · 用户三项决策落地

1. **journal 闭环启用**：`RAW/journal/` 已建立；AGENTS §1/§7 改为「已启用（2026-09-30）」；WorkBuddy 每日自动化（18:00）已配置，按 §7.2/§7.4/§7.5 执行扫描沉淀（目录空或全部已处理则零动作）。
2. **manual_review D+E 类 14 条批量转 done**（frontmatter `knowledge_update_status`，备份 `.tools/_mr_flip_done_backup_20260930/`）。余 **8 条**：B 商务敏感 5（报价单/成本表/联系表×2/甄选报告/生产商清单）+ C 对外释放 2（ADT POV、Henkel 议题）+ F 域外 1（投研圆桌报告），逐条拍板见 `.tools/_manual_review_triage_20260930.md`。
3. **JackywineV 第二库**：确认保持现状（旧测试库），WKB-OB 为唯一主库。

---

## 2026-09-30 晚（四） · MOC 导航层试运行（用户授权：首页 + 2 热域）

**产出**（`WIKI/MOC/`，type: moc，不参与 status 治理）：
- `00 总览 MOC.md` — 知识地图首页（已建域 MOC + 7 个规划域 + 横向入口）。
- `MOC - REL增强层与纤维.md` — 成员 86 页（孤儿 0），核心页 REL增强层(93 入链)/皮芯复合纤维(89)/COCO芯体平台(73) 等。
- `MOC - 无纺布工艺.md` — 成员 36 页（孤儿 2），核心页 热风粘合无纺布(123)/SMS复合结构(39)/水刺/熔喷/纺粘 等。
- 生成器 `.tools/_rebuild_moc.py`（幂等；域成员按标题关键词归集，改 DOMAINS 表重跑；域只收知识页，sources 不进 MOC）。
- AGENTS §1 已新增 `WIKI/MOC/` 层定义。

**⚠️ 统计更正（重要）**：本轮发现此前链接解析 bug——wikilink 被按全角「（」截断，标题含括号的页面（数量很大）入链全部漏计。更正后真实指标：
- 孤儿率 **4.6%（75/1614）**，此前报告的 51%（825 页）为 bug 虚高值，作废；知识页孤儿 74/735（10.1%）。
- 平均出链 **8.2/页**，此前 3.9 同为 bug 低估。
- 结论修正：库内链接密度本就健康，MOC 的价值是**主题导航与域地图**，而非抢救孤儿页。

**遗留**：7 个规划域 MOC 未建（芯体与吸收/SAP与流体/表面处理与胶黏剂/变色与智能材料/供应商与供应链/书籍知识地图/测试与标准），614 知识页未归域，扩容视试运行反馈。

---

## 2026-09-30 晚（五） · MOC v2 全量扩容（用户授权「继续」）

**产出**（`WIKI/MOC/` 共 14 页，脚本 `_rebuild_moc.py` v2 幂等重建）：
- 11 个域 MOC：REL增强层与纤维(86) / 无纺布工艺(36) / 变色与智能材料(59) / 法规与合规(36) / 功能添加剂与整理(24) / 基础理论与模型(37) / 测试与标准(50) / 芯体与吸收(80) / SAP与流体(38) / 表面处理与胶黏剂(28) / 实体与供应链(125，原「供应商与供应链」扩容改名，旧文件已清理)。
- 书籍知识地图：263 个书籍源页归入 68 本书（组键 book_title > parent_book > Ch 前缀 > 独立书名；Industrial Drying 与 Handbook of Industrial Drying 已按包含合并）。
- 00 总览 MOC 同步为 12 域目录。

**知识页归域覆盖**：644/735（87.6%）；余 137 页为零散化学/物理/工程单条（PET、Bessel 函数、甲醛等），不硬凑域，走 index 检索。

**修正**：v1 dry-run「未归域 19」为报告 bug（误把书籍域 263 sources 从知识页池扣除），真实未归为 281 → 扩域后 137。

AGENTS §1 MOC 条目同步为 v2 口径。

---

## 2026-10-01 晨 · IMA 占位符正文批量回填（171 条） + RAW/RAW_FULL 归因

**复核**：独立脚本 `verify_dual_empty_v2.py`（basename 索引 + 净正文口径）确认双空 **171 条**（旧口径 206 有误），**100% 带 media_id，无死链**。

**回到 IMA 补正文**：`make_backfill_batches.py` 切 18 批 → 21 批 lite 子代理（并发 2–3）→ **145 条成功落盘（3.09 MB）/ 30 条源侧无正文 / 0 失败**。4 个误写空壳经 `clean_empty_shells.py` 隔离至 `.tools/_empty_body/`，登记 `_no_content.json`（26 条）。

**推翻两旧结论**：① **img 类不是空**——`void volume test method.png` 返回完整对照表、`SAP生产工艺流程图.png` 返回六阶段工艺全文（IMA 已做 OCR），32 条 img 全部回填；② 「RAW_FULL 1:1 镜像」措辞作废。

**🔴 RAW vs RAW_FULL 归因**（回答「为何 1040 vs 1720」）：RAW 1720 = 附件类占位符 1213 + AI 派生件 403 + 微信 92 + 原生笔记 10 + weburl 2。**RAW_FULL 只装占位符那一半（1183），是 RAW 的路径子集（额外件 = 0），从设计上就不含自带正文的 507 条** → 差额 537 = 507 + 30。**不是丢数据。**

**可达率更新：98.3%（1690/1720）**，旧记 88.0% 作废。记忆与 `ima-media-extract` skill 已同步修正。

**遗留**：30 条源侧无正文（jpg 无文字层 / 录音未转写 / 扫描件 PDF），如需内容须走通道 B 下载原件 + 本地 OCR。

---

## 2026-10-02 · IMA 笔记区全量对账 + 批量落盘启动（受限中断）

**对账结论**（回答「IMA 笔记是否已同步」）：
- IMA 笔记区共 **127 条**（search_note 多关键词并集枚举；`list_note` 无游标不可翻页）。
- vault 存量 note_ 条目 71 条 = 曾「存入知识库」的笔记，同步工具不带正文（占位符注明不支持），61 条正文为 09-30 人工 MCP 回填。
- **59 条笔记完全未入库**（多为会议纪要、供应商交流、技术分析），已确认缺失。

**落盘动作**：新建 `RAW/ima_sync/notes/`，走 ima-api `get_doc_content`（format 0）批量拉正文。首日即触发 OpenAPI 日报额（200005 请求超量），**仅枚举完成、0 条正文落盘**；已修复响应字段解析（content），脚本幂等待续跑，明晨 09:00 自动化任务继续。存量 71 条路径不变。

## 2026-10-03 09:00 · 自动化续跑第 2 轮（再次 200005）

- 自动化按两级策略启动：A·MCP 优先不可用（自动化会话未挂载 ima MCP 工具，connector-status 仅 agent-mail；凭证 AES-256-GCM 加密无法脚本直调，维持昨日结论）；转 B·REST。
- **REST 首个 `get_doc_content` 即 200005**（09:00:44，全天第 1 次调用）→ 日报额未在零点重置（或额度已被其他调用消耗），按预案立即终止，0 条落盘。
- 对账修正：media_id frontmatter 精确扫描得 vault 已有 **74/127**（昨日口径 68/127 系标题模糊匹配差异），**待拉取实为 53 条**（`missing_to_pull.json` 已落盘 `.tmp_ima_notes/`）。
- `backfill_notes.py` 幂等性验证通过（media_id 扫描跳过已有 74 条）；`TODAY` 改为动态取当日日期。
- 已建 2026-10-04 09:00 一次性自动化第 3 轮续跑；若再 200005 则建议改为「当天分时段重试」策略（疑似配额重置点不在零点/9 点前）。

## 2026-10-04 09:00 · 自动化续跑第 3 轮（第 3 次连续 200005）

- MCP 优先路径不可用（自动化会话仍未挂载 ima MCP 工具，与第 1/2 轮一致），转 B·REST。
- REST 首个 `get_doc_content` 再次 200005（连续第 3 天在 09:00 首调即超量）→ **确认配额重置点不在零点/9 点前**，当日 9 点后额度也已被其他调用耗尽（或重置点更晚）。
- 按预案切换「当天分时段重试」策略：已创建 3 个一次性自动化 **12:00 / 18:00 / 21:00**（名称：IMA笔记续跑-重试1200/1800/2100），任一时段成功即清除其余待执行重试；21:00 兜底轮若仍失败则自动创建次日 09:30 续跑。
- 本轮落盘 0 条，剩余缺口维持 **53 条**（missing_to_pull.json 不变，脚本幂等）。

## 2026-10-04 18:00 · 自动化续跑第 5 轮（部分成功后 200005）

- 对账：IMA 笔记 127 条，vault 已有 74（共 78 条 note 条目），待拉取 53。
- 第 1 条 `get_doc_content` 成功落盘（ok=1），第 2 条即 200005「请求超量」→ 脚本幂等提前终止。
- **落盘 1 条，缺口 53 → 52**（missing_to_pull.json 下一轮自动重对账）。
- 配额判断：18:00 仍有额度但仅够约 1 次调用，当日 OpenAPI 日报额已基本耗尽（12:00 轮应已消耗或重置点不在白天）。
- 「IMA笔记续跑-重试2100」保留待执行（缺口未清零）；21:00 兜底轮若仍失败则按预案建次日 09:30 续跑。

## 2026-10-04 21:00 · 自动化续跑第 6 轮（当日兜底，部分成功后 200005）

- 对账：IMA 笔记 127 条，vault 已有 75（共 79 条 note 条目），待拉取 52。
- 第 1 条成功落盘（ok=1），第 2 条即 200005「请求超量，请明日再试」→ 脚本幂等提前终止。
- **落盘 1 条，缺口 52 → 51**（missing_to_pull.json 下一轮自动重对账）。
- 本轮为当日最后一次（09:00/12:00/18:00/21:00 四时段均未清零），按预案已创建次日一次性自动化「IMA笔记续跑-次日0930」（2026-10-05 09:30）。
- 次日若 09:30 首调仍 200005，建议人工排查 IMA 后台配额详情（重置点/日报额），或改用 ima-mcp 通道。

## 2026-10-05 09:30 · 自动化续跑第 7 轮（首调即 200005，连续第 4 天超量）

- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与昨日 21:00 后缺口一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- **连续第 4 天（10-02 起）在每日各时段均遇配额超量，且跨零点后 09:30 仍未恢复——「明日再试」提示与实际重置行为不符，疑似重置点远晚于零点，或日报额极低/被其他调用持续耗尽。**
- 建议用户人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道（但自动化会话此前多次确认未挂载 ima MCP 工具，需在交互式会话中验证）。
- 按预案已创建当日一次性自动化「IMA笔记续跑-重试1200」（2026-10-05 12:00）。

## 2026-10-05 12:00 · 自动化续跑第 8 轮（首调即 200005，连续第 4 天超量）

- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与 09:30 轮一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- 当日 09:30 与 12:00 首调均即 200005，12:00 仍未恢复，进一步说明配额重置点不在白天（或日报额极低/被其他调用持续耗尽）。
- **建议人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道（需在交互式会话验证 MCP 工具挂载）。**
- 按预案已创建当日一次性自动化「IMA笔记续跑-重试1800」（2026-10-05 18:00）。

## 2026-10-05 18:00 · 自动化续跑第 9 轮（首调即 200005，连续第 4 天超量）

- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与 12:00 轮一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- 当日 09:30 / 12:00 / 18:00 三个时段首调均即 200005，**连续第 4 天超量且当日各时段均未恢复，进一步说明配额重置点不在白天**（或日报额极低/被其他调用持续耗尽）。
- **建议人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道（需在交互式会话验证 MCP 工具挂载）。**
- 按预案已创建当日一次性自动化「IMA笔记续跑-重试2100」（2026-10-05 21:00）；21:00 兜底轮若仍失败则按预案建次日（2026-10-06）09:30 续跑。

## 2026-10-05 21:00 · 自动化续跑（当日兜底轮，首调即 200005，连续第 4 天超量）

- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与 09:30/12:00/18:00 三轮一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- **当日 09:30 / 12:00 / 18:00 / 21:00 四个时段首调均即 200005，连续第 4 天（10-02 起）超量且全天未恢复——进一步说明配额重置点不在白天，或日报额极低/被其他调用持续耗尽。**
- **建议用户人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道（需在交互式会话验证 MCP 工具挂载）。**
- 按预案已创建次日一次性自动化「IMA笔记续跑-次日0930」（2026-10-06 09:30）。

## 2026-10-06 09:30 第 10 轮（重试）
- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与前几轮一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- **2026-10-06 09:30 首调仍 200005，连续第 5 天（10-02 起）超量；各时段全天未恢复。**
- **建议用户人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道。**
- 按预案已创建次日一次性自动化「IMA笔记续跑-次日0930」（2026-10-07 09:30，第 11 轮）。

## 2026-10-07 09:30 第 11 轮（重试）
- 对账：IMA 笔记 127 条，vault 已有 76（共 80 条 note 条目），待拉取 51（与前几轮一致）。
- 首个 `get_doc_content` 即 200005「请求超量，请明日再试」→ 落盘 0 条，缺口维持 51。
- **2026-10-07 09:30 首调仍 200005，连续第 6 天（10-02 起）超量；此前 10-02 至 10-06 各时段首调均失败，全天未恢复过。**
- **建议用户人工排查 IMA 后台配额详情（重置时间点 / OpenAPI 日报额），或改用 ima-mcp 通道（需在交互式会话验证 MCP 工具挂载）。**
- 按预案已创建次日一次性自动化「IMA笔记续跑-次日0930」（2026-10-08 09:30，第 12 轮）。

---

## 2026-10-10 · IMA 笔记同步失败根因定位（代码级 + API 级 + 数据级）

**问题**：多数笔记在 vault 中为「此条目为笔记，暂不支持自动同步内容」占位符，个别（如 `会议纪要 Knight IV`）正文完整。

**根因（已定位到插件源码行）**：`.obsidian/plugins/ima-copilot-sync/main.js` v6.6.0
1. 知识库通道取笔记正文只走 `openapi/note/v1/get_doc_content`，该接口**受当日配额限制**；今日实测连续 4 次均返回 `200005 请求超量，请明日再试`。
2. 插件的可重试错误判定 `Di=new Set([200001,20002,110021,20005])` —— **`20005` 少一位，不匹配 `200005`**；消息正则含 `/超限/` 但不含 `/超量/`、含 `/稍后重试/` 不含 `/明日再试/` → 配额错误被当作**永久失败**，不重试、不中断，逐条写占位符。
3. 知识库主循环 `if (a.has(i.media_id)) continue` → 占位符已含 `media_id`，**下轮直接跳过，永不重试** → 12 轮续跑全部零产出。

**排除项（API 实测）**：成功笔记 `Knight IV` 与失败笔记 `会议纪要一`/`V6产品开发技术研讨会`，`get_media_info` 返回完全同构（media_type=11、`notebook_ext_info.notebook_id` 均存在、同目录、创建时间相差 2~33 分钟）→ **与条目类型/位置/状态无关，纯调用时序/配额问题**。

**落盘实况**：`RAW/ima_sync/` 84 条 note 条目 = 12 条正文 + 72 条占位符；`RAW_FULL/` 61 条 note 全有正文（09-30 人工 MCP 回填）。IMA 笔记区 127 条 → **约 43 条从未入库**。
占位符族另有：类型15录音 41、类型12 session 8、类型20 html 5、网页 3；附件类无提示占位 1109 条。

**关键突破**：实测 MCP `fetch_media_content` **今日可用且返回完整正文**（对占位符笔记与录音均验证通过），**绕开 REST 日配额** → 方案 A 可行。

**产出**：`.tools/IMA_NOTE_SYNC_ROOTCAUSE_2026-10-10.md`（含方案 A/B/C/D、风险、核验命令）。未执行批量回填，待确认。

## 2026-10-10 · 方案 A + C 执行：IMA 正文回填清零 + 自建补库流水线

**方案 A（MCP 通道回填，已完成）**：以 3+3 个子代理分批走 MCP `fetch_media_content`，正文写 `RAW_FULL/` 同相对路径（RAW 只读未动）。
- 「暂不支持」家族 17 条（笔记 10 / 录音 5 / session 2）→ 12 条取到正文
- 附件类缺口 40 条（xlsx/md/pdf/pptx/图片）→ 15 条取到正文
- 合计 57 条处理完毕，27 条落正文、30 条 IMA 侧确无正文（16 图片无文字层 / 7 CSV·JMP 数据文件 / 4 扫描件 PDF / 2 空录音 / 1 `飞书` 报 code 220030）
- **验收：12 个类型全部 0 缺口**；`RAW_FULL` 侧有正文条目 1182 → **1240**

**方案 C（自建补库流水线，已上线）**：
- `.tools/ima_note_backfill.py` — 清单/切片/验收（`--scan` `--slices N` `--verify` `--status` `--kinds`）；幂等判据改为识别 `extract_status: ok|empty`，避免 empty 条目被反复重跑
- `.tools/IMA_NOTE_BACKFILL_RUNBOOK.md` — 运行手册（通道优先级 / 三条命令 / 子代理契约 / 已知错误码边界）
- 自动化「IMA 条目正文回填巡检」— 每日 09:30，缺口>0 时 MCP 优先、REST 兜底，报告落 `.tools/ima_backfill_daily/YYYY-MM-DD.md` 并追加本日志

**遗留**：16 张图纸类图片 + 4 个扫描件 PDF 需走 `get_media_info` 签名 URL 下载原件；约 43 条笔记仍未入库（需先在 IMA 客户端「存入知识库」）；旧一次性重试链（`IMA笔记续跑-*` 12 轮）已被取代可清理；`RAW/ima_sync/notes/飞书.md` 明文密钥待处置。

## 2026-10-10 · 清除旧重试链 + 上线通道 B（原件下载 + 本地识读）

**清理**：删除自动化 `IMA笔记续跑-次日0930`（0b7a190e…）。此前 10-02~10-08 的 12 轮一次性重试链至此全部清空，由「IMA 条目正文回填巡检」取代。

**通道 B 上线**：新增 `.tools/ima_fetch_originals.py` —— 走 REST `openapi/wiki/v1/get_media_info` 取签名 URL 下载原件，落 `RAW_FULL/<原条目目录>/attachments/<原始文件名>`（用回原名便于 Obsidian 直接引用）。子命令：`--list` / `--run` / `--fix-ext`（去 hash 后缀 + 按魔数纠正扩展名）/ `--manifest`（原件↔stub 配对）。幂等：目标名已存在即 SKIP。

**执行结果**：
- 原件下载 **24/24 成功**（4 扫描件 PDF、14 图纸图片、1 pptx、1 docx、4 CSV；约 9.6 MB）；复跑 24 SKIP 验证幂等
- 本地识读 24 条 stub 全部回填：3 份美国专利扫描件识读成功（`US20070203469A1` SMMS / `US5266394A` SBS 热熔胶）、`CN111134966A` 源文件截断已如实标注、`1780441413150.jpg` 幻灯片截图识读约 1100 字、13 张 `Code N.jpg` 确无文字层改为结构描述、4 CSV 内联 400 行、`NOTE.docx` 手写图已识读、`REL_Optimized_PTT_PVA_Composition.pptx` 为 DRM 加密 → `original-only`
- **验收：12 类型 0 缺口**；`extract_status` = ok 1233 / original-only 1 / empty 6；`RAW_FULL` 有正文 1240 条

**文档**：`IMA_NOTE_BACKFILL_RUNBOOK.md` 增补「通道 B」章节（命令、落盘约定、识读流程）；根因报告增 §8 扩展项执行记录。

**工程要点**：① 原件扩展名须按 Content-Type→魔数→前缀三级判定（早期只按前缀写死，导致图片丢扩展名、CSV 被写成 .xlsx）；② 落盘用原名而非 hash 后缀，幂等判据即文件名存在性；③ `url_info.url` 为 `chrome://…` 或空时无法下载，脚本 SKIP。

**已闭环**：`.tools/_pdfpages/`（识读 PDF 生成的 65 张页图 + 3 个诊断文件，约 17 MB）已清除；删前核验 `D_text.txt` 乱码、`D_rebuilt.pdf` 无效修复、原件已存 `attachments/`，无信息损失。

## 2026-10-11 · P0-B01 编译 · Areas/Meeting Minutes 26 条

**背景**：IMA↔WIKI 对齐核查（见 `.tools/ALIGNMENT_MECHANISM_AUDIT_2026-10-11.md`）确认真实欠账 415 条，其中非书类 341 条。生成可执行批次计划 `.tools/compile_plan/`（10 批），本批为 P0-B01。

**动作**：编译 `Areas/Meeting Minutes` 26 条 → `WIKI/sources/` 26 个源摘要页。
- **备份**：`.tools/_backup_compile_20261011/`（WIKI 全量 16M + index.md + log.md）
- **脚本**：`.tools/_compile_p0b01_20261011.py`、`.tools/_digest_p0b01_20261011.py`（只读提取要点）、`.tools/_fix_dates_p0b01_20261011.py`
- **纪律执行**：`source_path` 26/26 指向 `RAW/`（未误指 RAW_FULL）；front matter 六字段 26/26 齐备；全程未写 `RAW/`（核验：RAW 侧 `extract_status` 字段仍为 0）

**新增页面（26）**：
`CO V6 新体机芯体验证实验方案评审` / `Daehyoon 供应商技术来访`×3（主会·技术专场·总结行动项）/ `Huayi 集团创新非织造布技术交流会` / `KC 拜访供应商维盛技术交流` / `KC 与福建兴泰 SMS 无纺布供应商技术交流` / `KC 团队内部技术讨论会（TBCW 在线超声波复合工艺）` / `Liner Trial Request` / `OI（Open Innovation）团队会议纪要` / `TJ 供应商工厂访问与会谈纪要` / `与华峰集团研发及合作会议纪要` / `会议纪要：山东希瑞新材（双色 ES 纤维）` / `会议纪要：松井油墨（水变温变油墨技术分享）` / `会议纪要：FEI & OI 益生菌项目` / `会议纪要：Bryan 1_1 纤维加工工艺验证` / `会议纪要：Q2 Mini BS 创新功能开发脑暴会` / `复合纤维生产工艺及性能探讨（闽瑞纤维）` / `尿裤弹性收紧力不足及 Niso 材料工艺方案` / `日本 Nichidai 丝网工艺技术交流` / `汉高亚太研发中心技术交流会` / `紫华公司与 KC 团队技术交流会议` / `纸尿裤产品设计与材料开发评审会` / 会议纪要图片 ×3

**标`manual_review` 6 条及原因**：
1. `TJ 供应商工厂访问与会谈纪要` —— TBCW 克重原文自记33 gsm 与 30 gsm **两个值且标注「data discrepancy to be verified」**，属材料选型关键参数，须回原始演示文档核实
2. `会议纪要：山东希瑞新材` —— **商务敏感**（现报价 19 元/kg、需方目标价 16 元/kg），按 AGENTS.md §5 待确认是否保留具体数字
3-5. `会议纪要图片` ×3 —— 图片类条目，`RAW_FULL` 侧无可用文本，需多模态读图判断价值
6. `紫华公司与 KC 团队技术交流会议` —— 本批正文提取不完整（仅「会议纪要」「下一步计划」两节），建议走通道 B 重回填

**date_published 口径处理**：原文仅2 份记载会议日期（OI 会议 2026-09-18；TJ 2026-09 未精确到日），其余 24 份**原文未记载**。`RAW_FULL` 的 `extracted: 2026-09-30` 是**正文回填日期，非会议日期**——已全部留空并在 front matter 加注口径说明，避免把回填日期误当会议日期入库。

**索引**：`.tools/rebuild_index.py` → `index.md` 重建，**1655 页**（源摘要 902 / 概念 528 / 实体 145 / 对比 80）；manual_review 回执累计 238 条。

**待办/ 下一步**：P0-B02（Areas/IP 15 条）、P0-B03（Areas/Supply Base 4 条）、P0-B04（Areas/Test Method 1 条）待编译；P1 5 批共 148 条待排。

**⚠️ 遗留断链**：本批 26 页共引用 **96 个尚不存在的概念/实体页**（最高频：`Pinhole 开孔` 8 次、`三叶草截面纤维` 8 次、`Daehyoon` 6 次、`双组分纤维` 6 次）。已导出待建清单 `.tools/compile_plan/_P0B01_断链待建页清单.md`。按 AGENTS.md §3，这些是从源摘要页派生的下游欠账，须另起批次建 seed 级概念/实体页，**不在本批编译范围内**。

---

## 2026-10-11 · P0-B02/B03/B04 编译完成（Areas/IP + Supply Base + Test Method）

**批次**：`P0_Areas_IP_SupplyBase_TestMethod_01`
**范围**：原定 20 条（Areas/IP 15 + Areas/Supply Base 4 + Areas/Test Method/成品/TJ 1）

### 关键发现：判重口径缺陷（全库级，影响此前所有欠账数字）

执行前判重时发现，此前"未编译"判定**只检索单值 `source_path`**，遗漏两类已登记情况：

1. front matter 的 **`source_paths` 多值字段**（全库 8 页在用）
2. **跨专利合并页**（例：`WO2010071584A1 & US9162007...` 页同时登记 CN102245218B / JP5604444B2 / US9162007 等同族条目）

**修正后全库数字**：

| 口径 | 数字 |
|---|---|
| RAW 条目（排除 attachments） | 1382 |
| 旧口径（仅单值 source_path）未登记 | 492 |
|其中**其实已编译** | **12** |
| **真实未编译** | **480**（此前报告 518，高估 38 条） |

本批 20 条中 **11 条属已编译**，按库纪律改为「补登副本说明」而非重复建页。

### 重复件裁定

| 组合 | 裁定 | 依据 |
|---|---|---|
| US9162007.pdf / US9162007 (1).pdf | **重复件，不单独建页** | 正文均90218 字符；difflib 全文档相似度 **0.9996**；首个差异仅 front matter `media_id`（`63a8b2303e` vs `d7cf3bafdc`） |
| CN 101679760 B（4 份命名） | **归并单页** | `CN101679760B` / `09_EDANA引用` / `10_英文引用` / `v3第9项`，专利号出现次数一致，仅引文标注粒度不同 |
| CN 101641398 B vs CN 101679760 B | **明确不合并** | 同优先权日、同日申请、同族，但为不同专利（PCT/EP2008/053172 vs 053169） |
| BLOCLO 官网 HTML vs 产品册 PDF | **分别编译、互链** | 同一公司不同物料（官网简介 vs 产品册），非重复件 |
| US 5266394 A（2 份命名） | **分别编译、互链** | 正文长度与指纹一致，属同一识读结果的重复命名 |

### 新建源摘要页（8 页）

| 页面 | 批次 | status |
|---|---|---|
| US 2007-0203469 A1 熔喷非织造背片（P&G SMMS 背片） | B02 | done |
| US 5266394 A SIS 嵌段共聚物热熔胶（Dow 与 Exxon·多线贴合用） | B02 | done |
| CN 111134966 A 防漏尿裤型纸尿裤（ω 型腿围橡筋·原件损坏） | B02 | **manual_review** |
| BLOCLO 盛色科技（广州盛色）光变与温变动态色彩材料产品册 | B03 | done |
| Insilico 功能性微胶囊产品手册（感温·感光·水致变色·香精·英文版） | B03 | done |
| Insilico 功能性微胶囊（中文产品册·2019） | B03 | done |
| 松井色素 Chromicolor 温变油墨产品册（11 色 × 9 温度类型） | B03 | done |
| JMP 16 软件操作流程（Mannequin 测试数据分析 WI-JMP 第0版） | B04 | done |

### 追加式更新的既有页（5 页，均仅追加不改结论）

`CN 101679760 B` / `CN 101641398 B` / `WO2010071584A1 & US9162007` / `US5266394A Disposable Articles` / `盛色科技官网关于我们` —— 各追加「同源副本与同族登记」段。
改动前已备份至 `.tools/_backup_p0b02_20261011/`。

### manual_review（2 条）

1. **CN 111134966 A**：原件在 **IMA 源侧即损坏**（缺 xref / trailer / `%%EOF`，MD5 `b73eb774790a5f09e47464dc95bde4f3`；重新从 IMA 下载核验字节与 MD5 完全一致）。摘要、权利要求、说明书、16页附图**全部无法辨认**。→ 需向 IMA 索取完好原件或改走 CNIPA 官方渠道调取全文。本专利**不得**用于 FTO 判断或专利地图标注。
2. **US 2007/0203469 A1**：纯扫描件且**权利要求书不在扫描范围内**，页面参数取自说明书段落表述，**不得用作 FTO 结论依据**。

### 日期口径

仅 5 页填真实日期：US 2007-0203469 A1 → `2007-08-30`（扉页）、US 5266394 A → `1993-11-30`（授权日）、CN 111134966 A → `2020-05-12`（公开日）、Insilico 中文册 → `2019`（封面）、JMP → `2024-02-26`（修订日期）。
其余 3 页留空并注明：**RAW_FULL 的 `extracted` 是正文回填日期，不是发布日期**。

### 校验结果

- 8 新页 front matter 六字段齐备 ✓
- `source_path` **100% 指向 RAW**（RAW_FULL 泄漏 0）✓
- RAW 侧 AI 字段（`extract_status` / `date_processed` / `key_claims`）写入数 **0** ✓
- RAW 条目数 **1382 未变** ✓
- 全库 `source_path` 误指向 RAW_FULL 页数 **0** ✓
- 索引：1655 → **1663 页**（源摘要 910 / 概念 528 / 实体 145 / 对比 80）
- 回执 manual_review 合计：238 → **240 条**

### 遗留

- 本批 8 页产生 **30 个派生断链**（概念/实体/专利 seed），清单见 `.tools/compile_plan/_P0B02B03B04_断链待建页清单.md`，须另起 seed 批次，不混入源摘要编译批次。
- P0-B01 的 96 个断链仍未处理。

### 附：P0-B01 同副本重复编译回查（2026-10-11 事后审计）

因P0-B01 在发现 `source_paths` 判重缺陷**之前**执行，故对其做事后回查。

**回查方法（4 个维度）**：

| 维度 | 判据 | 结果 |
|---|---|---|
| 1. 同目录正文完全相同 | sha1（剥离 media_id） | 75 条中仅 2 条相同，且**均为 55 字符空壳**（`录音纪要_260829135725` / `_260920002637`），**不在 P0-B01 的 26 条内** |
| 2. 全库同指纹副本 | sha1（剥离 media_id）跨 1238 条配对条目 | P0-B01 的 26 条**同指纹副本数 = 0** |
| 3. 登记唯一性 | 每条 RAW 被几个 WIKI 页登记 | 26/26 **恰好各 1 页**，无一对多、无一登记零 |
| 4. 近似副本 | difflib两两（词元 Jaccard 粗筛 + ratio），阈值 0.55 / 全目录 0.75 | P0-B01 内部及其与全目录 75 条互比，**近似副本数 = 0** |

**结论：P0-B01 不存在同一文件多个 RAW 副本被重复编译的情况**，无需回滚或合并。

**原因**：Meeting Minutes 目录 78 条中，仅 P0-B02 的 Areas/IP 存在「同一专利多副本」（因专利可按国家阶段/引用标注反复上传），而会议纪要**天然一议一档**，无重复上传动机。

**全目录仅有的 2 对高相似件（均不在 P0-B01 内，且均未编译）**：

| 相似度 | 文件对 | 状态 |
|---|---|---|
| 1.0000 | `录音纪要_260829135725.md` / `录音纪要_260920002637.md` | 均 55 字符空壳，未编译，**不处理** |
| 0.9714 | `TJ工厂访问会前简报_20260907_v3.docx.md` / `_v3.1.docx.md` | 版本迭代（v3 → v3.1），未编译；编译时应以 v3.1 为主件、v3 登记为历史版本 |

**同时发现（P0-B02 遗留）**：`STM-01078OD产品折叠后长度、宽度测量方法.docx` 被拆成两个页——`STM-01078...（成品·NJ）.docx` 与 `STM-01078...（产品折叠长度）.docx`。二者正文指纹完全相同（`e39cab83f1b4`），属**同一测试方法被拆成两页**，须合并。待处理。

### 本轮脚本教训（已入长期记忆）

1. **清单文件名不带 `.md` 后缀** —— 跨目录比对时必须补后缀，否则全部 FileNotFound/静默跳过，**结论会是假的"零重复"**。回查脚本必须先打印"匹配到 N 条 / 缺失 M 条"验证非零。
2. **`r'^source_path:/s*(.+)$'` 的 `\s*` 会吞换行** —— 导致全库 912 个已登记 source_path 一条都匹配不到，误判"全部未编译"。须用 `[ \t]*`。
3. **sha1 不同 ≠ 内容不同** —— 跨文件判重必须用 difflib，不能只靠指纹。

---

## 2026-10-11 · STM-01078 合并 + 「已编译却误判未编译」根因回顾

### 一、STM-01078 重复页合并（完成）

全库扫描发现 `STM-01078 OD产品折叠后长度、宽度测量方法.docx` 被拆成两个页，正文指纹完全相同（`e39cab83f1b4`）：

- 主件：`WIKI/sources/STM-01078 ...（成品·NJ）.docx.md`
- 副页：`WIKI/sources/STM-01078 ...（产品折叠长度）.docx.md`

**处置**：

1. 备份两页至 `.tools/_backup_stm01078_20261011/`
2. 保留 NJ 版为主件（内容更全，多`Elastic Tension & Creep` 关联），用 `source_paths` 并入副本路径
3. 改写全库 2 处引用（`concepts/Folded Product Dimension Test`、`sources/STM-00064 Diaper尺寸`）指向主件
4. 删除副页，主件正文写明合并记录与备份路径

索引 1663 → **1662 页**（源摘要 910 → 909）。残留引用检查：0。

### 二、根因回顾：为什么反复出现「已编译却误判未编译」

**先排除登记侧**：实测 909 个 source 页**100% 有 `source_path`**，无orphan。**问题 100% 在判读侧，不在登记侧。**

#### 根因 1：AGENTS.md 的判重规范本身有缺口（制度问题）

原 §1 只规定「`source_path` 一律指 RAW/」，把它当作**唯一判重锚**。但库里实际存在 **3 种登记形态**：

| 形态 | 写法 | 页数 |
|---|---|---|
| 单值登记 | `source_path: RAW/...` | 899 |
| 多值登记 | `source_paths:` +缩进列表 | 10 |
| 跨条目合并页 | 一个页混装**不同资料**的多条路径 | （含上述） |

规范只描述了第1 种。**任何按规范实现的判重脚本都必然漏判第 2、3 种。** 这不是执行失误，是制度缺口。

#### 根因 2：三条脚本反模式，方向全都是「把已编译报成未编译」

| # | 反模式 | 本日实证后果 |
|---|---|---|
| 1 | 正则用 `\s*` 而非 `[ \t]*` | `\s*` 贪婪吞掉换行与后续多行 → **全库 912 个已登记 source_path 一条都匹配不到** → 误判「全部未编译」 |
| 2 | 扫描后不自证覆盖率 | 回查 P0-B01 时清单文件名**不带 `.md` 后缀**，全部静默跳过 → 得出**假的「零重复」**，重跑才发现 |
| 3 | 跨文件判重只比 sha1 | US9162007 两份 sha1 不同但 difflib **0.9996** → 漏判重复件 |

**共同特征：脚本不报错、输出格式正常、结论方向一致（都是高估未编译量）**。所以每次都能"通过直觉校验"，直到与另一份数据交叉才暴露。

#### 根因 3：数字被反复引用，形成自我强化的错误基线

`log.md` 里「1711 份未编译」（09-27）、「900+ 份未编译」（09-29）被后续多轮报告当作既定事实引用 → 每轮都在错误基线上再做微调 → 修正一次就又出现新的不一致口径（101 → 415 → 518 → 480 → **471**）。

### 三、制度性修复（已完成，不是靠自觉）

**1. `AGENTS.md` 新增 §1.1「判重执行规范」（强制）**

- §1.1.1 明确 3 种登记形态 + 唯一正确的 `collect_paths()` 写法
- §1.1.2 三条脚本铁律（禁 `\s*`、必须自证覆盖率、跨文件必须 difflib）
- §1.1.3 指纹与相似度阈值表（含「0.75~0.98 须人工裁定，禁止自动合并」）
- §1.1.4 重复副本处理纪律（主件 + `source_paths` 并入 + 改引用 + 备份 + 写合并记录）
- §2.0 模板补`source_paths` 字段说明
- §3 步骤 1 补「必须按 §1.1.1 覆盖 3 种形态」

备份：`.tools/_backup_agents_20261011/AGENTS.md`

**2. 新建 `.tools/wkb_dedup.py` —— 判重的唯一合法入口**

把正确判定固化成工具，禁止再手写一次性脚本：

```
python .tools/wkb_dedup.py scan--out backlog.json   # 全库对账（先自证覆盖率再给结论）
python .tools/wkb_dedup.py check<RAW相对路径># 判定单条
```

工具**强制**先输出覆盖率自证（页面总数 / 含登记页数 / 登记路径数 / 单值页数 / 多值页数），匹配为 0 时直接 `sys.exit(1)` 拒绝出结论。

### 四、当前权威数字（以工具为准）

```
RAW 条目（排除 attachments）: 1382
已编译: 911
真实未编译: 471
登记路径去重总数: 921（含多值与合并页）
```

**471 条是截至2026-10-11 的唯一权威未编译数**。此前所有 101 / 415 / 518 / 480 均为错误口径下的产物，**今后引用未编译量必须以 `wkb_dedup.py scan` 输出为准，禁止手写脚本另算。**

### 五、工具首次运行即发现的新问题（2 组，待人工裁定）

工具在扫描时自动检出「一条 RAW 被多个页登记」2 组，**P0 各批次均未发现**：

| RAW 条目 | 登记页 | 两页相似度 |
|---|---|---|
| `Absorbent Technology_ch01_report.md.md` | `Liquid Flow in Porous Structures` / `Porous Structure and Liquid Flow Models` | **0.2496** |
| `Absorbent Technology_ch07_report.md.md` | `Cross-linked Cellulose and Derivatives` / `Cross-linked Cellulose and Its Derivatives` | **0.1689** |

相似度极低（0.25 / 0.17），**判定为「同一章报告按主题拆成两个视角页」，属合理拆分，不是重复编译**。但仍需人工确认这两组是否符合库意图：

- 若认可拆分 → 应把第二页的 `source_path` 改为 `source_paths` 之外的显式「同源不同视角」标注，避免每次扫描都被报警
- 若不认可 → 按 §1.1.4 合并

**未擅自处置，留待王总裁定。**

---

## 2026-10-11 · 判重锚设计意图复核 + 重复登记告警口径修正（用户要求「搜索记忆确认逻辑无问题」）

**用户提问**：`source_path` 作唯一判重锚「是有原因的」，要求检索记忆确认，并验证新判重逻辑（3 形态 + `wkb_dedup.py`）无问题。

### 1. 记忆检索结论 —— 立规原因（证据 `log.md` 2026-09-30 晚 · 判重锚统一 P1-1）
> 会话只读对账发现：同一资料曾因 `RAW/` 与 `RAW_FULL/` **双路径**导致**漏判 → 重同步重复编译**。故 269 个源摘要页 `source_path` 由 `RAW_FULL/` 改写为对应 `RAW/` 路径（改前 269/269 逐一验证 RAW 侧存在，零缺失）；正文旧路径引用替换 113 处。**改后全库 RAW_FULL 锚 = 0。**
> AGENTS §1 同步立规：**source_path 一律指 RAW/，RAW_FULL 仅作编译输入不作判重锚。**

→ **立规目标** = 消灭「同资料双路径 → 漏判 → 重复编译」这一类缺陷。

### 2. 新逻辑与立规原因是否冲突 —— **不冲突**
- §1.1.1 的 3 形态（单值 `source_path` / 多值 `source_paths` / 跨条目合并页）**全部锚定 `RAW/`**，无一条引入 `RAW_FULL/`。
- 故新逻辑是对**登记粒度**的扩展，而非对**锚命名空间**的放宽 → 原设计意图（防双路径漏判）**完好保留**。
- 复核实测：`wkb_dedup.py scan` 报出 921 条登记路径，`RAW_FULL/` 锚 **0 条**，与 09-30 立规完全一致。

### 3. 复核中发现并修正的真实缺陷 —— 告警漏了 `merged` 一层
- `wkb_dedup.py` 此前检出「2 条 RAW 被多页登记」，我上一轮曾误判为「同章按主题拆成两视角页，合理拆分」——**该判断错误，已更正**。
- 真实情况：这 2 组正是 **09-30 晚（二）已治理为 `status: merged` 的指针页**（`Liquid Flow in Porous Structures` / `Cross-linked Cellulose and Derivatives`）。
- 证据：09-30 治理脚本 `_merge_dupes_governance_20260930.py` **grep `source_path` = 0 次** —— 脚本只改 `status`/`updated`/`tags`/正文，**刻意保留原 `source_path` 作合并存档线索**。故指针页必然呈现「一条 RAW 被 2 页登记」。
- 全库统计：`status: merged` 页 **21**，其中仍持有 RAW 侧 `source_path` 的 **4** 页（2 条触发重复告警 + `ASTM E2149-20 平行备份`、`变色油墨供应商综合技术联系表（1）`各 1 条独享路径）。

### 4. 工具修正（`wkb_dedup.py`，已落地）
- `build_index()` 改为返回 `(idx, merged_pages)`：
  - **merged 页保留在 idx 内** —— 否则其 RAW 条目会因「无人登记」被误报为未编译；
  - **merged 页从重复登记告警中剔除**，单列「已被 merged 指针页治理过的登记（非新问题，仅存档线索）」。
- 修正后实测：真实未编译 **471** 不变；真实重复编译 **0**；已治理登记 **2**（全部指向上述 2 组 09-30 已治理页）。**判重账目自洽。**
- 文档同步：AGENTS.md 新增 **§1.1.5 判重锚的唯一性**（立规原因 + 3 形态不冲突说明 + merged 页口径）。

**结论**：新判重逻辑与原设计意图**兼容**，且修正了「把已治理重复页重新报警」的口径漏洞。判重锚体系自洽，无遗留冲突。

---

## 2026-10-11 18:13 · Areas/Personal 孤儿镜像项闭环（王总裁定：无需处理）

**背景**：10-11 判重审计遗留「2 条 `Areas/Personal/` 下 RAW_FULL 孤儿镜像，需人工确认」。

**王总裁定**：RAW 侧条目文件已转移，**此项作废、不用管**。

**复核实况（更正：实为 3 条镜像，非 2 条）**：

| RAW_FULL 镜像 | RAW 侧对应 | 判定 |
|---|---|---|
| `AI核心设定_王总_2026-06-06_v3.pdf.md` | `.md` + `attachments/` 齐备 | 正常配对 |
| `APEV03R08CH-new passport.pdf.md` | 仅剩 `attachments/` 原件，条目 `.md` 已转移 | 半孤儿（保留不动） |
| `检验报告20260708132924.pdf.md` | 仅剩 `attachments/` 原件，条目 `.md` 已转移 | 半孤儿（保留不动） |

**处置**：镜像与附件**均保留原地不动**（RAW 只读红线 + RAW_FULL 不删）。后续判重扫描须**忽略 `Areas/Personal/` 下这 3 条**，不得再报为孤儿或未编译。

**同期另一项闭环**：8 条 18:00 空转自动化会话（10-01~10-09）的清理请求——备份已完成（`.tools/_auto_session_archive_20261011/`），但原文件删除被平台安全规则拦截（`~/.workbuddy/projects/*/*.jsonl` 属受保护路径），王总裁定「不管了」。原文件原样保留，无数据损失。

---

## 2026-10-11 18:20 · 记忆防覆盖巡检上线 + IMA 日更管道方案 v2

### 1. 记忆防覆盖巡检（新建，防"静默覆盖"复发）

**动因**：本日实测两次记录被 `>` 覆盖（`memory/2026-10-11.md` 17:41 丢失追加一~六；`log.md` 早期条目作者不明）。王总 18:15 批准建立防御机制。

**产出**：
- `.tools/memory_guard.py`（只读巡检）— 守护 `log.md` / `index.md` / `AGENTS.md` + `.workbuddy/memory/*.md`，比对体量基线，跌幅 > 20% 或行数 -≥5 即报警
- `.tools/_memory_baseline.json` — 首个基线已建立（守护 7 个文件）
- **自动化「WKB-OB 记忆防覆盖巡检」**（`5700cc40-400d-47ee-b3f1-52d993bb9110`）每日 **08:45**，早于其他管道
- 模拟测试验证通过：基线声称多 50 行 → 工具准确报警「疑似被覆盖/截断」

**设计要点**：只读、绝不改被守护文件；基线仅由人工确认后刷新；无异常时零动作结束。

### 2. IMA 日更管道方案 v2（补丁版，取代 v1）

**背景**：v1（`.tools/IMA_DAILY_PIPELINE_DESIGN_2026-10-11.md`，08:48）的核心数字与判重口径被当日下午的制度改革推翻。

**产出**：`.tools/IMA_DAILY_PIPELINE_DESIGN_v2_2026-10-11.md`

**v2 修订项**：

| 项 | v1（已废） | v2（权威） |
|---|---|---|
| 已编译 / 未编译 | 876 / 预估 200~300 | **911 / 471** |
| 判重口径 | 单值 `source_path` | **3 形态**（AGENTS.md §1.1.1） |
| 判重工具 | 手写脚本 | **`wkb_dedup.py` 唯一法定入口** |
| merged 页 | 未提及 | **新增 §3.5 识别规则** |
| 首日全量 | 跑全量 | **分批 P0→P3，先跑 P0** |
| 频率 | 待定 | **定案拆两条**（09:30 A/B/C/E + 18:00 D） |

**v2 新增章节**：§3.5 merged 页识别规则、§3.6 两个账本的正交关系（同步层 `_ima_sync_state.json` vs 编译层 `wkb_dedup.py scan`）、§6.1 init 后强制交叉验证。

**v1 保留部分**（立论根基，确认成立）：§0.1「只有 repair、没有 discovery」的结构性诊断、五阶段架构、`file_number` 剪枝、通道分级 A/B/C、「只记映射不搬文件」。

**王总三项裁定**：① 出 v2 补丁非重写；② 首日全量分批，先跑 P0；③ 频率拆两条。

**待确认残留**：v2 §10 第 3、4 项（录音原件是否跳过 / 账本是否冗余存 source_path）。

**取证**：`wkb_dedup.py scan` 实时输出已核（1675 页 / 909 登记页 / 911 已编译 / 471 未编译 / 真实重复 0 / merged 登记 2）。

### 3. v2 §10 待确认事项全部关闭（18:26）

**王总两项裁定**：

**① 录音（media_type=15）处理 → 转写文本 + 音频原件双落，设 50MB 阈值**（写入 v2 §5.1）
- < 50MB：转写入正文 + 音频落 `attachments/`
- ≥ 50MB：只落转写，原件记 `original_media_id` + 尺寸供按需单独取
- 理由：转写文本才是知识载体，原件只是溯源凭证；防长期录音让 RAW_FULL 膨胀到 GB 级
- 常量 `AUDIO_ORIGINAL_MAX_MB = 50`，可调

**② 同步层账本冗余存编译线索 → 存，但降格为 hint + 强制一致性校验**（写入 v2 §3.6.1）
- 字段名**必须** `source_page_hint`（**禁止**叫 `source_page`，防后来者误当权威）
- 账本顶部加 `_warning` 声明非权威
- `wkb_dedup.py scan` 跑完顺手比对 hint，不一致则输出 `[hint 过期]` 清单（**只提示不自动改**）
- 对冲的是"缓存当真相"风险 —— 与当日"假欠账"同款病

**结果**：v2 §10 **4/4 关闭**，新增 §11「实施就绪检查」表，方案进入可实施状态。**下一步：第 1 批 · 账本与枚举器**（§6.1）。

### 4. v2 自查修正 4 处（18:30，王总要求"先看一遍完整版"时发现）

**修正项**：

| # | 问题 | 修正 |
|---|---|---|
| 1 | §3.4 账本示例字段名写 `source_page`，与 §3.6.1 刚定的 `source_page_hint` **自相矛盾**（违反刚立的命名铁律） | §3.4 改为 `source_page_hint`，并补 `_warning` 行 |
| 2 | §2 架构图画五阶段**串行一条**，与 §6.6「拆两条」定案矛盾 | 重画为「09:30 主管道 A/B/C/E」+「18:00 独立 D」双块图 |
| 3 | §6.6 写 `bcaf361b`「被阶段 D 吸收 → 保留暂停不复用」**两句打架** | 改为**删除**（D 独立新建，留着会冲突） |
| 4 | §0 现状表 3 个数字是旧快照：RAW_FULL 459 / RAW md 1766 / 文件夹 244 | 实测更正为 **1240 / 1788 / 247**（`find`+`grep -l` 核实） |

**另**：§4.1 的「244」同步改 247；§9 示例里「未编译 471 → 459」的 459 是**合理示例降幅值**，非旧快照，保留。

**教训（与今日主题一脉相承）**：这份 v2 自己犯了它要防的病 —— **多源描述同一件事，一旦不同步就互相打脸**（字段名不一致 / 架构图与定案矛盾）。**交付前必须做一次全文档一致性扫描**（grep 关键字段名 + 数字），而非只改局部。

### 5. 王总纠正：阶段 D 应「原地改造 bcaf361b」而非「删除+新建」（18:33）

**王总指出**：「不是应该替代之前的日志扫描定时任务吗」——**成立**。

**我上一轮的错**：为修 §6.6「两句打架」，矫枉过正写成「删除 `bcaf361b` + 新建日志扫描自动化」。这等于把**同一任务推倒重建**，会：
1. 丢失 `bcaf361b` 连续 8 天执行记忆（`.workbuddy/memory/automations/bcaf361b-.../memory.md`）
2. 可能造成两个同职责自动化并存冲突

**硬证据**：`bcaf361b` 记忆首行即「自动化执行记忆 — 每日日志扫描（18:00）」——**它的时间本就是 18:00，与阶段 D 完全对齐**，根本不需要动时间。

**正确处置**（已改入 v2 §6.6）：
- `bcaf361b` → **原地改造并启用**：保持 18:00；prompt 增补「读写共享账本」；PAUSED → ACTIVE
- `8523233b` → 暂停（职责真被阶段 B 吸收）
- 每周对账 09:00 → 新建（无既有条目可改造）

**一般化教训（重要，写入长期记忆候选）**：
> **当一个新方案要"接管"某个既有自动化时，默认应「原地改造既有条目」，而非「删除旧的 + 新建一个」。** 因为自动化条目携带**执行记忆**（累积的历史上下文），重建会切断这条血脉。仅当职责**真正消失**时才暂停/删除。

**九条自动化最终形态**中，真正的"新建"只有 2 条（09:30 日更管道、周日对账）；1 条改造（bcaf361b）；1 条已建（memory_guard）；1 条暂停（8523233b）。

### 6. 自动化层实际执行（18:37，王总指出「还是没看到自动化任务」）

**王总的观察成立**：此前只改了 v2 文档 §6.6，**实际自动化条目一条没动**。王总要求立即执行（原方案排在"第 5 批"）。

**已执行两项**：

| 自动化 ID | 名称 | 变更 | 结果 |
|---|---|---|---|
| `bcaf361b-...` | WKB-OB 日志扫描（AGENTS §7 知识进化闭环） | PAUSED → **ACTIVE**；prompt 增补「本任务为管道阶段 D，与 09:30 主管道共享账本 `.tools/_ima_sync_state.json`」；时间保持 18:00 | ✅ 已生效，下次运行 2026-10-11 18:00 |
| `8523233b-...` | IMA 条目正文回填巡检 | ACTIVE → **PAUSED**（职责被阶段 B 吸收） | ✅ 已生效 |

**未动**（按方案待后续批次）：
- 09:30「WKB-OB 知识管道 · 日更」—— 需等第 1~4 批代码就绪后新建
- 周日 09:00「全量对账 + 健康检查」—— 同上

**教训**：设计文档的修改**不等于**实际配置的修改。方案类工作必须区分"纸面计划"与"已落地配置"两个状态，并在交付时明确告知实况 —— 本次若王总不追问，会误以为自动化已改造。

---

## 2026-10-11 · 知识管道第 1 批落地（枚举器可用 + 自动化职责真正纠正）

**背景**：王总指出前一轮只改了设计文档、没改自动化配置——"文档改了、配置没改 = 假完成"。本轮落实两件实事。

**一、`bcaf361b` 自动化职责重构（真实配置变更）**
- 名称：`WKB-OB 日志扫描（AGENTS §7 知识进化闭环）` → **`WKB-OB 知识管道 · IMA→Obsidian 日更`**
- prompt：从「只扫 `RAW/journal/`」改为 A/B/C/E 四阶段 15 步，调用 `ima_sync_state.py` / `ima_note_backfill.py` / `ima_fetch_originals.py` / `wkb_dedup.py` / `rebuild_index.py`
- 频率不变 18:00；`8523233b` 维持 PAUSED
- 旧记忆已备份为 `memory.md.bak-20261011`

**二、第 1 批枚举器打通并修 2 个真 bug**
- `ima_sync_state.py enumerate` 首跑暴露：**kb_path 口径不一致** → 18 条全部误报"移动"，污染 `moves` 历史
  - 根因：Agent 侧给的是「文件夹链+文件名」相对名，账本存的是 `ima_sync/个人知识库/WKB/...`
  - 修复：新增 `norm_kb_path()` 归一（剥 `RAW/`、补 `MIRROR_PREFIX`）；移动判定改为「相对容器的尾巴真变化才记」
  - 已回滚 18 条污染记录；修复后重跑两次均为 `新增 0 · 移动 0 · 已知 18`，**幂等**
- 根层枚举实测：5 个顶层文件夹 + 18 条近期条目（10-07~10-11），**全部已在账本中** → 根层真缺口 0
- 账本现 1382 条 / folders 快照 5 个

**三、关键架构结论（REST vs MCP 枚举能力差异）**
- MCP `get_knowledge_list` 的 `folder_info` 含 `file_number`/`folder_number` → **可剪枝**
- REST `openapi/wiki/v1/get_knowledge_list` 的 `folder_info` 为 **null** → **不可剪枝，只能全量递归**
- 故日更管道必须走 MCP；REST 仅作兜底
- REST 侧 `code 200001` = 请求频率超限（连续调用过密触发），非权限问题

**待办**：第 2 批（落地器）/ 第 3 批（编译器）/ 第 4 批（编排器）—— B/C 段目前只能部分自动。

## 2026-10-11 19:16 自动化「WKB-OB 知识管道 · IMA→Obsidian 日更」执行记录
- 阶段 A：今日已由早前会话完成（18:54 全量递归扫描 + 19:11 枚举合并 `ima_sync_state.py enumerate`，`_ima_enum_20261011.json`）。本批无新增增量，未重复枚举。
- 阶段 B：`ima_note_backfill.py --verify` → 缺口 33 条（PDF 17 / PPT 5 / Word 6 / Excel 2 / 笔记 1 / 图片 2）；`ima_fetch_originals.py --run/--fix-ext` 均 0 目标（缺口属既往失败/受限件，非新待下载）；笔记正文通道需 MCP fetch_media_content，本会话 IMA connector 不可用 → 本批未回填。
- 阶段 C：`wkb_dedup.py scan` 对账：WIKI 1675 页 / 已编译 911 / 未编译 471 / RAW 1382，活跃重复登记 0。账本积压：synced 349 + discovered 144（均已在 RAW 落盘，为分类/编译欠账，需 MCP 通道+专项编译会话消化）。
- 阶段 E：`rebuild_index.py` 重建 index.md（1662 页，manual_review 240 条）；本记录与 `.workbuddy/memory/2026-10-11.md`、日报 `.tools/kb_pipeline_daily/2026-10-11.md` 已追加。
- 结论：今日无新增增量；既有积压 493 条待后续批次消化，非本批可无人值守完成。

### 2026-10-11 20:50 · 日更管道四批全部落地 + bcaf361b 接线

- **第 1–4 批交付**：`ima_sync_state.py`（账本/枚举）→ `kb_sync_handler.py`（阶段 B 落地）→ `kb_compiler.py`（阶段 C 编译）→ `kb_daily_pipeline.py`（A→B→C→E 编排器）。
- **验收**：端到端首跑 A/B/C/E 全 OK（阶段 B 写 12 · 跳 0 · 失败 0）；幂等复跑第 2 次起 B/C 稳定 PARTIAL、E OK；`index.md` 1663 页；`memory_guard` 无覆盖。
- **关键修复**：编排器新增 `archive_staging()`，根治"假失败"（暂存目录落盘后归档到 `.tools/_done/<date>/`）；两个处理器把 `not-in-plan` 改判为 skipped。
- **bcaf361b 接线**：prompt 1805→2884 字节，改调四脚本；DB 实况核验 ACTIVE / deepseek-v4.1-flash / FREQ=DAILY;BYHOUR=18。旧 prompt 已备份。
- **积压**：阶段 B 132 条、阶段 C 345 条待 Agent 会话批处理。

### 2026-10-11 21:20 · 第 5 批：自动化治理 + 周度全量对账

- **僵尸清理**：DB 20 条 ACTIVE 中 12 条为脱管一次性任务（UUID 型 ID，cwds 指向已删项目）→ 备份后置 PAUSED，ACTIVE 降至 8 条。
- **编排器加 `--full`**：新增阶段 R（全量对账，**只读不改**）= wkb_dedup scan + 账本三口径校验 + 逐条黑账核对 + 漂移告警。首跑即抓到 2 条账本漏登（NIFO 两份新资料）。
- **周度对账自动化**：`808e9058-3451-44ff-a7fc-8abf3a678a1f`，周日 09:00，deepseek-v4.1-flash。
- **架构定案**：高频增量（bcaf361b 每日 18:00）+ 低频全量（808e9058 周日 09:00）双轨。

## 2026-10-11 · 周度全量对账（首跑，808e9058 校准器）

- **全量枚举**：MCP `get_knowledge_list` 递归整库（knowledge_base_id `001a693ee6c0644e`，跳过剪枝），132 文件夹 / 1384 条目全部访问（+12 条 media_state≠2 未入 items）。产物 `.tools/_ima_enum_full_20261011.json`（root/items/folders/_meta）。分片暂存 `.tools/_enum_work/`（83 文件）。
- **漏登消除**：R 阶段首跑抓到 2 条账本漏登（NIFO 两份新资料），枚举合并后 `新增 2 · 移动 0`；再按 media_id 回绑 raw_path（`.tools/_rebind_raw_path.py`）→ R 阶段转 **OK**，drift 清零。
- **阶段 B 正文回填**：134 条 discovered 全部处理完毕，`synced` 424→493；唯一残留 = `note_7434068337643175`（IMA 笔记，MCP fetch 返 `code:220030`，无法自动获取，如实标注）。
- **阶段 C 编译**：471 条待编译 → 全清。8 条 stub（`kb_compiler.py stub --write`）+ 463 条抽取式源页（`.tools/_compile_extractive.py`，诚实抽取、不臆造 key_claims）+ 3 条 dedup 残余补编（`.tools/_compile_residual3.py` / `_residual1.py`）。账本 `compiled` 890→1353。
- **权威判重终值**：`wkb_dedup scan` → **真实未编译 0 · 已编译 1384 · 重复编译 0 · merged 指针页 4**。
- **口径差异（预期，非 bug）**：账本 compiled=1353 vs dedup compiled=1384，差 +31（dedup 计 merged 指针页/跨条目合并页；账本按 media_id 一对一）。
- **索引重建**：`rebuild_index.py` → index.md 2135 页（源摘要 1382 / 概念 528 / 实体 145 / 对比 80）。
- **记忆巡检**：`memory_guard.py check` → OK（守护 8 文件，无覆盖迹象）。

## 2026-10-12 · 周度全量对账（续跑：会话窗口外新增条目处置）

- **发现**：上一轮对账收尾后，Obsidian 插件于 **2026-10-11 23:57** 新同步 5 条 COCO V6 条目（10.10 版），落入 `RAW/ima_sync/个人知识库/WKB/Projects/COCO/`。账本当时仍登记旧版（20261006/20261007），R 阶段复跑即报 `uncompiled=5`、`only_in_raw=5`。
- **定性**：这 5 条是 **10.07 → 10.10 的版本迭代**（同族资料新版本），非纯漏登。本批含 Code 13–17 新增实测 + 「噪声底体系撤回」重大修订。
- **处置**：MCP 枚举确认 5 条在 IMA 侧存在（COCO 文件夹，`time_wording=23:46`）→ 构造增量 merge（`.tools/_ima_enum_merge_20261011.json`，累计 7 条）→ `ima_sync_state.py enumerate` 合并（账本 1384→1389）→ `.tools/_rebind_raw_path.py` 回绑 raw_path。
- **阶段 B/C 补跑**：`kb_sync_handler` 抓正文（MCP `fetch_media_content`，5 条全部成功，含 mrk/html/excel/img 两图）→ `kb_compiler` 抽取式编译落 `WIKI/sources/`。
- **权威判重终值**：`wkb_dedup scan` → **真实未编译 0 · 已编译 1389 · 重复编译 0 · merged 指针页 4**。
- **R 阶段终态**：账本 1389 = RAW 1389，`only_in_raw=0`、`only_in_ledger=0`、`drift=[]` → **OK**。
- **索引**：`rebuild_index.py` → index.md **2140 页**（源摘要 1387 / 概念 528 / 实体 145 / 对比 80）。
- **口径差异（预期，非 bug）**：账本 compiled=1358 vs dedup compiled=1389，差 +31（dedup 计 merged 指针页/跨条目合并页；账本按 media_id 一对一）。

## 2026-10-12 · 每日增量同步与编译（bcaf361b 日更 · 18:00 调度）

- **阶段 A（枚举，降级通道）**：本会话 **IMA MCP connector 不可用**（无 get_knowledge_list / fetch_media_content）。改用 REST `openapi/wiki/v1/get_knowledge_list` 只读兜底（`knowledge_base_id=F8Dbmy...`，子层参数名实为 `folder_id`，非 `parent_folder_id`）。根层返回 39 条 = 35 文件 + 5 文件夹；与账本比对 → **新增 2 条**。REST 的 `current_path.file_number` 恒为 "0"，**无法剪枝**（与 MEMORY §4.1 一致），故仅做根层 + 5 顶层文件夹浅枚举。
- **新增 2 条**（均落 WKB 根层，由 ima-copilot-sync 插件写入 RAW）：
  1. `wechatarticle_...6467148e...` **芯吸效应：水为什么自己往细缝里钻**（公众号「材料有门道」，含**完整正文** 11.7KB）
  2. `note_...7515332654669274` **会议纪要：2026-10-12**（IMA 笔记，RAW 侧为占位符）
- **账本合并**：构造 `.tools/_ima_enum_20261012.json` → `ima_sync_state.py enumerate` → **新增 2 · 移动 0**，账本 1389→**1391**；`_rebind_raw_path.py` 回绑 raw_path。
- **阶段 B（落地）**：plan 3 条（通道 A 全部）。① 芯吸效应：插件已落全文 → 复制至 RAW_FULL（`extract_status: ok`）；② 会议纪要：**MCP 不可用 → 单次 REST `openapi/note/v1/get_doc_content`（note_id=7515332654669274, format=0）成功**取回 3427 字正文 → RAW_FULL（`ok`）；③ `note_7434068337643175`（ima笔记使用指南，legacy 220030 件）无内容可取，**留积压**。写入 2 · 跳过 1 · 失败 0。
- **阶段 C（编译）**：plan 2 条 → 生成 2 张源摘要页（英文为主 + 中文对照）→ `apply` 落 `WIKI/sources/`（`芯吸效应：水为什么自己往细缝里钻.md`、`会议纪要：2026-10-12.md`），账本 synced→compiled 2 条。
- **权威判重终值**：`wkb_dedup scan` → **真实未编译 0（2→0）· 已编译 1389 · 重复编译 0 · merged 指针页 4**。
- **阶段 E**：`rebuild_index.py` → index.md **2142 页**（源摘要 1389 / 概念 528 / 实体 145 / 对比 80）。
- **遗留**：账本 `synced=30` + `discovered=1` 为**同步层陈旧缓存**——dedup 已确认 0 未编译，权威口径以 dedup 为准（§3.6）。`note_7434068337643175` 待 MCP 可用时回填。
- **口径差异（预期，非 bug）**：账本 compiled=1360 vs dedup compiled=1389，差 +29（dedup 计 merged 指针页/跨条目合并页）。
