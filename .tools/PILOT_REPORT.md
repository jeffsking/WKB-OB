# 占位符正文提取 · 压测报告

_日期：2026-09-27 ｜ 范围：`RAW_FULL/` 镜像方案（用户选定 A 方案）_

## 1. 压测设计

| 项 | 设置 |
|---|---|
| 样本量 | 30 份（3 批 × 10） |
| 类型覆盖 | pdf 8 / markdown 6 / ppt 6 / word 4 / excel 3 / soundrecording 2 / html 1 |
| 选取范围 | 队列价值分 ≥ 88 的头部（Projects / Meeting Minutes / Supply Base） |
| 通道 | A：MCP `fetch_media_content` |
| 并发 | 3 个子代理同时跑 |

## 2. 结果：30/30 成功，零失败

- 落盘 30 份，**总 343,184 字符**（清洗后 319,606）
- 单份跨度：649 B ~ 40,187 B（最大 `CI-06 COCO V6 3rd round trial.xlsx`）
- **空文件 0**、**失败 0**、**速率限制未触发**
- 子代理上下文隔离有效：30 份正文全部只写在磁盘，主会话未被污染

**结论：batch size = 10、并发 = 3 可安全放量。**

## 3. 清洗规则（已验证有效）

只做**信息零丢失**的处理，脚本 `.tools/clean_extracted.py`（幂等）。

| 噪声 | 处理 | 依据 |
|---|---|---|
| 图片死链（指向 IMA 内部路径 `2/xxx/tmp_zip_img/*.png`） | 降级为 `[图片: <alt>]`，原路径记入 `.tools/_image_stripped.json` | 本地永久不可达，保留纯噪声；**共降级 156 张** |
| 标题层级塌陷（DOCX 全部压成 H1） | **不处理** | 还原层级属推断，违反"不改原结论"精神；仅记录 |
| HTML 实体（`&lt;` `&amp;` 等，5 处） | **不处理** | Obsidian 渲染器原生兼容，解码反而引入 `<` 被当标签解析的风险 |
| 开头孤立数字（POC 曾见） | 本批未复现 | 无需规则 |
| 原文自身重复标题（PGA 1 处） | **不处理** | 源文档特征，非提取缺陷 |

### 3.1 意外收获：PPTX 的文字层藏在图片 alt 里

`BM_Urine_Indicator_Concept.pptx` 等文件中，IMA 把**整页文字**塞进了图片的 alt 属性：

```
![1 Odour granular added Zeolite / silica / cyclodextrin in the core scavenges
   $NH_{3}$, amines, $H_{2}S$ and volatile fatty acids. 2 Head-space cue disappears ...](2/xxx/tmp_zip_img/xxx.png)
```

这些内容在原始 md 里**只存在于链接属性中，正文不可检索**。降级为 `[图片: ...]` 后变成正文，**可搜索、可被编译引用**——是净收益。这也是坚持"降级而非删除"的直接回报。

## 4. 产物结构（RAW_FULL 1:1 镜像）

```
RAW_FULL/ima_sync/WKB/<与 RAW 完全相同的相对路径>
---
media_id: "<原占位符 media_id>"
source_file: "<原文件名>"
original_path: "RAW/ima_sync/..."      # 回指占位符
extracted: "2026-09-27"
extract_method: "ima-mcp fetch_media_content"
extract_status: "ok"
clean_rules: "dead-image-link -> text (alt preserved)"
processed: "2026-09-27"
---

# <文件名>

<正文原文>
```

**RAW/ 未被触碰**（只读原则完整保留）。

## 5. 台账

`.tools/_extract_ledger.json` —— 全量 1117 条队列，含 `status` / `bytes` / `score`。

| 状态 | 份数 |
|---|---|
| done | **218** |
| pending | 897 |
| skipped_no_text（IMA 无转写/无正文） | 2 |
| skipped（img 32 / 微信图片 1 / 加密件 1） | 34 |

按价值档：`score=100` **57/57** ｜ `92` **47/49**（2 无音转）｜ `88` **63/63** ｜ `78` **51/51** —— **四档全部清完**。剩余：`74` 6 ｜ `66` 183 ｜ `55` 8 ｜ `40` 8 ｜ `30`（Resources）692。

## 6. 工具链（全部可复现）

| 脚本 | 作用 |
|---|---|
| `.tools/plan_extraction.py` | 扫描 → 打分排序 → 排排除项 → 建 RAW_FULL 骨架 → 出队列 |
| `.tools/make_pilot.py` | 按类型配额选择 + 打散成批（改 `N`/`QUOTA` 即可复用） |
| `.tools/verify_extracted.py` | 落盘完整性 / front matter / 规模 / 五类噪声统计 |
| `.tools/clean_extracted.py` | 幂等清洗（死链降级 + 追溯表） |
| `.tools/build_ledger.py` | 生成提取总账 |

## 7. 已知局限

1. **加密件 1 份**（`REL_Optimized_PTT_PVA_Composition.pptx`，MIP/RMS）—— 两通道均无法读明文，需人工解密。
2. **img 类 32 份** —— 返回 `{"content":"8"}`，需独立 OCR/视觉方案，已排除出队列。
3. **微信图文 1 份** —— 正文仅图片链接，同上。
4. **图片本体未归档** —— 本次只降级链接。若要真正拿到图表，需走通道 B（`get_media_info` 下载原件解包）。**注意签名 URL 有时效。**
5. 部分扫描件型 PDF 若 IMA 未做 OCR，正文可能为空壳——本批未遇到，放大后需抽查。

## 8. 放量建议

按价值降序推进，每波 3 子代理 × 10 份：

| 波次 | 范围 | 份数 | 状态 |
|---|---|---|---|
| W1 | `score=100` 剩余（Projects 尾） | 30 | ✅ 完成 30/30 |
| W2 | `score=92` Meeting Minutes | 47 | ✅ 完成 45/47（2 无音转） |
| W3–W4 | `score=88` Supply Base | 63 | ✅ 完成 63/63 |
| W5 | `score=78` Regulation&PSC | 51 | ✅ 完成 51/51 |
| W6 | `score=74` 零散 6 + `score=55` 8 + `score=40` 8 | 22 | ⏳ 下一波 |
| W7–W8 | `score=66` Areas 其余 | 183 | ⏳ |
| … | `score=30` Resources | 692 | ⏳ |

**价值档覆盖：`100`/`92`/`88`/`78` 四档已全部清完（218/1117 = 19.5%）。** 剩余 897 份均为 `score≤74` 的中长尾。

---

# 附：W1 实战（2026-09-27）

**范围**：`score=100` 剩余 30 份（Projects 区收尾）｜**结果 30/30 成功，零失败**

## W1 新发现的噪声 + 清洗 v2

PPT 的**图表刻度被 OCR 成超长重复数字串**，混进图片 alt：

| 文件 | 模式 | 长度 |
|---|---|---|
| `Active_Hygiene_Roadmap` | `10` 重复 | 146 |
| `ATB_topsheet_600mpm_ultrasonic` | `5` 重复 | 208 |
| `Mechanochromic_TechReview` | `1` 重复 | **594** |
| `CoPET_ADL_Strategic_Blueprint` | `1 2` 交替 | 186 |
| `Stretch-Triggered Colour Indicator` | `0` 重复 | 208 |

**处理：压缩而非删除** —— `[重复数据串: <seq> ×N]`，保留 token 与数量（存在性 + 规模不丢），
追溯表 `.tools/_repeat_collapsed.json`。规则 R2 已并入 `clean_extracted.py` v2。

同时收紧幂等判断：原用「80 字符窗口」扫描，会被正文里的 `v2` 误触发（`05_材料合作分析模板_v2_...md` 被漏处理）；
改为**只读 `clean_rules` 字段自身的值**。

## W1 累计战果

- RAW_FULL: **60 份 / 1.4 MB**；清洗累计降级死链 **324 张**、压缩重复串 **11 处**
- **Projects 区 57/57 = 100% 覆盖**（BNC / COCO / REL / Liner / Mechanochromic / PPC / Thermal Comfort / Film / Active Hygiene / BM / PIPC）
- 队列总账：**60 done ｜ 1057 pending ｜ 34 skipped**
- 六大噪声复验：`ima_img 0` `repeat_digits 0` `empty 0` `leading_num 0`；
  保留 `dup_title 1`（PGA 源文档自身重复标题）、`html_entity 14`（渲染兼容，不处理）

## 下一波建议

W2–W3：`score=92` Meeting Minutes 47 份（会议纪要信息密度高，且与已编译的 wiki 概念页关联强）。

---

# 附：W2 实战（2026-09-27）

**范围**：`score=92` 全部 47 份（`Areas/Meeting Minutes`）｜**结果 45/47 成功**，2 份无正文

## 类型构成与并发结论

| 类型 | 份数 | 结果 |
|---|---|---|
| soundrecording（录音转写） | 31 | 全部成功，单份最长 41,889 字符 |
| session（会议会话） | 5 | 3 成功 / **2 无正文** |
| pdf | 5 | 全部成功 |
| word | 5 | 全部成功 |
| markdown | 1 | 成功 |

- **并发 5 一次性跑完 47 份，未触发速率限制** —— 并发上限从压测的 3 提到 5 仍然安全
- 总 745K 字符（清洗后），单份跨度 1.4KB ~ 41.9KB
- 批次切分：5 批（10/10/9/9/9），按类型轮转打散

## 新发现 1：`session` 类型可能无正文（需与提取失败区分）

2 份 `录音纪要_260920002637` / `录音纪要_260829135725` 经**直接重试确认**，IMA 端只返回标题字符串（6 字符），无转写正文。

**性质**：不是通道故障，是 IMA 端该录音**根本没有生成转写**（同场会议的另一轨 `260920002641` 正常拿到 9,956 字符，说明是单条录音本身为空）。

**处理**：新增台账状态 `skipped_no_text`（区别于 `pending` 与 `skipped`），记入 `.tools/_extract_no_content.json`，`build_ledger.py` 已支持。**这类条目不要反复重试**，直接归档为「源侧无内容」。

## 新发现 2：标题层级塌陷从 DOCX 扩散到 PDF

本批 `dup_title` 6 例，其中 5 例是 **PDF**：IMA 把 PDF 的章节标题（`一、` `1.1` 等）全部压成 H1，导致同一文件出现多个同级标题。

**处理：仍不还原** —— 还原层级属推断，违反「不改原结论」原则。已从「DOCX 专属问题」修正为「**IMA 解析器对多类格式的共性行为**」。

## W2 累计战果

- RAW_FULL: **105 份 / 1.67 MB**；死链降级累计 **368 张**
- **Meeting Minutes 区已全部处理**（45 提取 + 2 无正文）
- 队列总账：**105 done ｜ 1010 pending ｜ 2 无正文 ｜ 34 排除**
- 六大噪声复验：`ima_img 0` `repeat_digits 0` `empty 0` `leading_num 0`；
  保留 `dup_title 6`（源文档结构，不修复）、`html_entity 20`（渲染兼容，不解码）

## 下一波建议

W3–W4：`score=88` Supply Base 62 份（供应商侧资料，配合采购线；含已提取 1 份，实际余 62）。

---

# 附：W3 实战（2026-09-27）—— ⚠️ 连接器掉线，半途中断

**范围**：`score=88` Supply Base 62 份（pdf 50 / excel 5 / ppt 3 / html 3 / word 1）｜**结果 30/62 完成，32 份被 `ima-mcp` 连接器掉线卡住**

## 事故经过

并发 5 派 5 个子代理跑 W3（批次 1–5）+ W4（2 批，共 12 份）：

| 批次 | 结果 |
|---|---|
| W3 batch 1 | ✅ 10/10 |
| W3 batch 2 | ✅ 10/10 |
| W3 batch 3 | ⚠️ 4/10（卡死） |
| W3 batch 4 | ⚠️ 4/10（卡死） |
| W3 batch 5 | ⚠️ 2/10（卡死） |
| W4 batch 1–2 | ❌ 未启动（12 份） |

**根因**：`ima-mcp` MCP 连接器在 ~20:15 掉线。子代理调 `fetch_media_content` 报 "tool not found in deferred tools index"，`ToolSearch` 搜不到任何 `mcp__ima-mcp__*`，连接器状态里 ima 消失（只剩 agent-mail / qq-mail / westock-mcp）。

## 已落盘成果（30 份，通道 A 高质量）

- RAW_FULL **135 份 / 2.09 MB**
- 本波 30 份清洗降级死链 **838 张**（Supply Base 的 PDF 数据表图片密度极高——大量产品规格表以图片呈现）、压缩重复串 1 处
- 六噪声复验：`ima_img 0` `repeat_digits 0` `empty 0` `leading_num 0`；保留 `dup_title 18`、`html_entity 29`

## 台账（中断时）

- **135 done ｜ 980 pending ｜ 2 无正文 ｜ 34 排除**
- `score=88` **31/63**（剩 32：20 份补跑 + 12 份 W4）

## 恢复方案（ima 重连后）

1. 用户重连 ima 连接器
2. 用「skip-existed」恢复代理补跑 `.tools/pilot/W3_batch_{3,4,5}.json` + `W4_batch_{1,2}.json` 的缺失项（批次 JSON 都在，不必重新 make_wave）
3. 并发回归 **3**，逐批核对落盘数

## 沉淀的教训（已入技能 v1.4.0）

1. **`ima-mcp` 连接器会中途掉线**——每波开始前先 `ToolSearch` 验证工具在线；发波后核对落盘数
2. **并发 5 有风险**（W2 可行但 W3 触发中断），回归并发 3 基准值
3. **make_wave 加「防重复切批」守卫**——台账未及时更新时重复调用不会重复切批

## ✅ 补跑完成（2026-09-27 20:33，ima 重连后）

用户重连 ima 连接器后，派 **3 个恢复代理（并发 3）**，带「skip-existed」守卫补跑 32 份缺失项：

| 恢复代理 | 覆盖 | 结果 |
|---|---|---|
| recover-A | W3_batch_3 + W3_batch_4 | 新提取 12 / 跳过 8 / 失败 0 |
| recover-B | W3_batch_5 | 新提取 8 / 跳过 2 / 失败 0 |
| recover-C | W4_batch_1 + W4_batch_2 | 新提取 9 / 跳过 3 / 失败 0 |

- **32/32 全部补齐，0 失败**。W3 batch 3/4/5 与 W4 batch 1/2 全部 10/10、6/6 落盘
- 清洗：本波 32 份降级死链 **1024 张**（Supply Base PDF 数据表图片密度极高）
- 台账：**167 done ｜ 948 pending ｜ 2 无正文 ｜ 34 排除**；`score=88` **63/63 = 100%**
- 高价值区（≥88）**全部清完**。下一波 `score=78` Regulation&PSC 51 份

---

# 附：W5 实战（2026-09-27）—— `score=78` Regulation&PSC 51 份

**范围**：`Areas/Regulation&PSC` 全部 51 份（pdf 50 / soundrecording 1）｜**结果 51/51 成功，零失败**

## 执行

- 波次前先做**在线探针**（`ToolSearch` 验证 ima 工具在线）——已验证可加载
- 6 批（9/9/9/8/8/8），**并发 3 分两轮**（batch 1–3，batch 4–6），两轮均满命中
- 内容是国标/行标 + 国际标准 + 行业白皮书：GB/T 卫生用品系列、GB 7918 化妆品微生物、EDANA AHPs 白皮书、CIR/Phenoxyethanol 安全评估、JIS/ASTM 抗菌测试等

## 🆕 新工程细节：超大正文需临时文件转存

本波出现 **5 份超大文档**（>19 万字符），单次工具返回超出上限，被系统**自动转存为临时文件**，子代理需从该文件解析 `content` 字段后再落盘：

| 文档 | 字符数 |
|---|---|
| `CIR Safety Assessment of Butoxyethanol` | 483,478 |
| `Final Opinion on Phenoxyethanol in cosmetic products` | 295,075 |
| `IFRA Category Lookup Tool` | 197,141 |
| `EDANA AHPs Whitepaper 2022` | 195,934 |
| `IFRA Category Lookup Tool（12 大产品类别）` | 195,823 |

**子代理均正确完成了转存路径解析**，落盘完整（首尾已抽查），无截断。**这是目前遇到的单份最大体量（48.3 万字符）**，验证了「超 50K 字符单独成批」的旧建议**不必要**——只要子代理能处理临时文件即可。建议后续保留在同一批内，但**每批不宜含 2 个以上超大体量项**（本波每批恰好 1 个）。

## 结果

- RAW_FULL **218 份 / 5.09M 字符**
- 本波清洗降级死链 **164 张**（法规正文本体文字为主，图片密度低于 Supply Base）
- 六噪声复验：`ima_img 0` `repeat_digits 0` `empty 0` `leading_num 0`；保留 `dup_title 39`、`html_entity 72`（既定不处理）
- 台账：**218 done ｜ 897 pending ｜ 2 无正文 ｜ 34 排除**；`score=78` **51/51 = 100%**
- **价值档 `100`/`92`/`88`/`78` 四档全部清完**。下一波 `score=74`+`55`+`40` 共 22 份


