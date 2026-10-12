# WKB-OB 占位符正文提取 · 波次报告 W6–W11

_最后更新：2026-09-27 23:10 · 通道 A（IMA MCP `fetch_media_content`）_

## 一、本轮结果

| 波次 | 范围 | 分值档 | 派发 | 成功 | 源侧无正文 | 失败 | 清洗降级死链 |
|---|---|---|---|---|---|---|---|
| **W6** | Market Insight 6 + 根层级 LMP-PP 簇 8 + Archives 8 | 74 / 55 / 40 | 22 | **22** | 0 | 0 | 66 张 |
| **W7** | Areas/IP 专利 30 | 66（档头） | 30 | **26** | **4** | 0 | 125 张 |
| **W8** | Areas/IP 专利 30（CN/EP/US/JP/KR/WO） | 66（续） | 30 | **30** | 0 | 0 | 244 张 |
| **W9** | Test Method 主流 + IP 余量 + Areas 散件 | 66（续） | 60 | **60** | 0 | 0 | 409 张 |
| **W10** | Test Method 成品 NJ/TJ 56 + Areas 根层级散件 7 | 66（收官） | 63 | **63** | 0 | 0 | 613 张 |
| **W11** | Resources/Ebook 为主（含整本 PDF 书籍） | 30（首批） | 90 | **90** | 0 | 0 | 267 张 |
| 合计 | | | 295 | **291** | 4 | 0 | 1724 张 |

- 参数：**10 份/子代理、并发 3**。W9「6 批分两轮」、W10「7 批分三轮」、W11「9 批分三轮（30+30+30）」，均满命中
- W8 开跑前曾遇连接器掉线（22:12），用户重连后补跑成功；其余各波波前均做三步在线探针
- **`score=66` 档已清空**（179 done + 4 源侧空 = 183）
- 全部通过 `verify_extracted.py`（0 空文件、0 残留死链）

## 二、W7 关键发现：PDF 也会「源侧无正文」

4 份 PDF 的 `fetch_media_content` 返回 **空字符串 `{"content":""}`**（注意：**不是** session/soundrecording 那种「只回标题」）。**主会话对同一 media_id 直接复测仍为空** → 判定为 IMA 端**未从该 PDF 解析出文字层**（影印专利 / 扫描件），**非连接器掉线、非提取失败，重试无益**。

| 文件名 | 专利号 |
|---|---|
| 01_模块一：SMMS_US20070203469A1_Disposable_garment… | US20070203469A1 |
| 01_模块一：SMMS_纺粘-熔喷-熔喷-纺粘无纺布_US20070203469A1… | US20070203469A1 |
| 16_模块三：聚烯烃类热熔胶_US5266394A_Hot_melt_adhesive_compositions_(嵌段共聚物) | US5266394A |
| 18_模块四：氨纶橡筋_弹性纤维_CN111134966A_一种具有防漏尿功能的裤型纸尿裤 | CN111134966A |

**处理（已执行）**
1. 4 份空壳文件（仅 front matter）**移入 `.tools/_empty_body/` 隔离**（可逆，未删），保持 `RAW_FULL/` 只放有正文的文件
2. dst 追加进 `.tools/_extract_no_content.json`（台账据此标 `skipped_no_text`）
3. 新建 `.tools/_extract_source_empty.json` 记录 `{dst, media_id, name, reason, remedy}`，**remedy = 通道 B 下载原件 + 本地 OCR**（待办）

> **W8/W9 反证**：同为 IP 区，W8 的 30 份与 W9 的 IP 余量**零源侧空** → 源侧无正文是**个别文件属性**，不是批次性问题，无需调整策略。

## 三、本轮修掉的两个工程缺陷

| # | 缺陷 | 影响 | 修复 |
|---|---|---|---|
| 1 | `build_ledger.py` 按**原始字节 >200** 判 `done` | 空壳只有 front matter 也有 300+ 字节 → **源侧无正文件会被误计为 done**，虚增进度 | 改为按**净正文长度**判定（去 front matter/标题后 ≥50 字），新增 `empty_body` 状态 |
| 2 | 子代理提示词把 `_extract_no_content.json` 写成 **dict 列表** | 脚本用 `q['dst'] in no_content` 判定 → **格式不符会静默失效**，条目永久滞留 pending | 统一为**路径字符串数组**，固化进 `ima-media-extract` 技能（升 v1.6.0） |

另：`make_wave.py` 增补能力 —— 第 4 参支持**分值列表**（如 `74,55,40`），可跳过中间档只清指定档。

**运维注意（W11 新增）**：子代理会在 `.tools/pilot/` 遗留辅助脚本（累计 9 个）→ 提示词已加「辅助脚本写系统临时目录」；每波收尾巡检并归档到 `.tools/pilot/_scratch/`（不删，可逆）。

## 四、超限转存（通道 A）实测口径

- 单份正文超工具返回上限时，系统**自动转存临时文件**；子代理须从该文件解析正文（单行 JSON `content` 或纯文本）再落盘，**不得判失败**
- **阈值按 token 计而非字符**：W5 见 >19 万字符触发，**W8 见 11.1 万字符即触发**；长专利 / 标准全文 PDF / 整本书是高发类型
- **单份体量纪录刷新：126 万字符**（W11 `29_Principles_of_polymerization.pdf.md`，前纪录 48.3 万）
- W9 实测：**超限临时文件不一定位于工作目录内**，Read 可能被拒 → 改用命令行提取即可
- 工具：`.tools/_dump_oversize.py`（已入技能 §7）。**W11 单批含 3 个百万级书籍 PDF 仍全成功** → 旧「每批不宜含 2 个以上超大体量项」口径已放宽

## 五、累计进度（W11 后）

- RAW_FULL：**509 份 / 15.64 M 字符**；清洗累计降级死链 **3280 张**
- 台账：**509 done ｜ 602 pending ｜ 6 skipped_no_text ｜ 34 排除**（队列 1117）
- **八档全部清空 → score ≥ 40 已全清**：100(57) · 92(47) · 88(63) · 78(51) · 74(6) · 66(179) · 55(8) · 40(8)
- 剩余：**仅 `30` 602 份**（Resources/Ebook 余量 + Open Innovation 188 + Training 66 + 散件）
- 完成度 **509 / 1117 = 45.6%**

## 六、下一波建议

**W12**：继续 `score=30`，一轮 90 份（9 批 ×10、分三轮各并发 3），约 6–7 波清完 602 份。

## 七、高价值命中样本

**W9**：`STM-00429 VOID VOLUME AS A FUNCTION OF SATURATION`｜`TTM-00038 Pore Space Modulus to Void Volume 换算逻辑`｜`STM-00429 Void Volume Template.xlsx`｜`SAM 吸收量 / 保水量 / 通液速度 / 加压吸收 / 密度 / 水分测定` 系列｜`GB/T 28004 纸尿裤国标吸收性能测试` 系列｜`BM simulant A 配方 & BM gun 操作`｜`WI-60236 REL 拼接拉断测试`｜`CoCo Product-REL Width, SAM Width in REL`｜`REL 芯体专利族（一~七 系列）`

**W10**：`STM-00034 FIFE`｜`STM-00033 滞留能力`｜`STM-00060 导流性能`｜`STM-00240 / 00232 Loop 粘连强度`｜`STM-1001 平面扩散` / `STM-1002 U型扩散`｜`TTM-00623 高低压反渗`｜`WI-63848 / 63849 Static / Motion mannequin`｜`STM-00040 厚度` / `00069 重量` / `00048 SAM含量` / `00070/00440 皮筋张力`｜`STM-00078 端封强度` / `00090 腰围密封强度` / `00075 剥离`｜`TTM-00512 绒毛完整性`｜`TTM-00302 面层干爽性`｜`质量成品标准测试方法-TJ`（6.7 万字）｜`BCC成品STM-南京南厂`（12.2 万字）｜`拉力松紧可视化技术评估报告`｜`高吸水纤维的生产工艺`｜`纳米纤维素纤维技术及应用深度研究报告` + `供应商拜访计划 V3`

**W11**：`29_Principles_of_polymerization`（126 万字符）｜`Absorbent-technology-textile-science-and-technology`（125 万）｜`Cosmetic_Formulation_of_Skin_Care_Produc`（116 万）｜`Barel_Paye_Maibach_Handbook_of_Cosmetic`（115 万）｜`Chromic_Phenomena_The_Technological_Appl`（74 万）｜`A review on superabsorbent polymers`｜整书拆解系列：`Absorbent Technology_ch01–ch12`｜`Ebewole Polymer Science Technology_ch01–ch15`｜`Chromic_Phenomena_Ch1–Ch5_解析` + `深度拆书报告`｜`Handbook of Adhesive Technology_Part1–3`｜`Cosmetic Science and Technology_深度拆书报告`｜`Handbook of Adhesion 书评`｜ES 纤维亲水/驻极系列
