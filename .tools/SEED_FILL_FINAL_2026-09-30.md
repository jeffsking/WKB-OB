# WKB-OB Seed 页补齐 · 收官报告 2026-09-30

## 🎉 结论：seed 页全部清零（447 → 0）

| 指标 | 值 |
|---|---|
| WIKI 页数 | **1589**（sources 836 / concepts 530 / entities 143 / comparisons 80） |
| **断链** | **0** ✅ |
| front matter | **1589 / 1589 通过** |
| index.md 对齐 | **1589 / 1589** |
| **`status: seed` 剩余** | **0** ✅ |

---

## 全天总账（447 个 seed 页）

| 处置 | 页数 | 说明 |
|---|---|---|
| **补齐真实内容** | **278** | 23 批代理 × 每批 8 页；每页 Definition / Key Parameters（逐值带 `（源：[[…]]）`）/ Mechanism / Hygiene Relevance / Open Questions / Related Sources |
| 改标 `status: growing` | 161 | S1–S7 收官批遗留 —— **正文完整只是 status 没改** |
| 合并为指针页 | 8 | 命名变体重复；入链改写 + stub 转 `status: merged`；**未删页** |
| **合计** | **447** | |

## 高价值页面成果（节选）

| 页面 | 内容规模 |
|---|---|
| **回渗 Rewet** | 11 行带源数据：加液压力跨方法 0–0.53 psi、单亲 vs 多亲面层 3.89–6.17 vs 0.84–1.32 g、AD 面层互换 0.51→0.15 g、五项目实测 |
| **吸收芯体** | QB/T 三参数、≤40/≤50 s、12.5×、VV 10 kPa |
| **光致变色 Photochromic** | 四族/五家族/五性质、CTI>20 专利·35 技术·60 国、Matsui 1911、Intellego 2.17 亿 SEK |
| **机械变色 Mechanochromic** | ≥40,000 psi→20–150 kPa、市场 $1.2B→$4.1B、0.09¢/pant、127 nm、30,000 循环 |
| **达西定律 Darcy's Law** | q=−K·∇P、K=k/μ、p_c=2γcosθ/r、x_v∝t^(1/2) |
| **湿感指示条 Wetness Indicator** | 8 来源、含 US5197958/US5389093/US20070270773A1 专利族关联 |
| **渗透率 Permeability** | Kozeny-Carman、凝胶阻塞、ADL/Core k 值 |

## 可复用工具链

```
_seed_inventory.py      盘点 seed + 引用频次
_seed_classify2.py      精确测内容量（rich / 半成品 / 真空白）
_gen_seed_digests.py    为每页生成原文摘录 -> .tools/_seed_ctx/（447 份）
_seed_fill_plan.py      剩余 seed 分批（每批 8 页）
_seed_dupes.py          检测重复 seed（Jaccard + 子集）
_seed_intra_dupes.py    待补集合内部查重
_consolidate_seed_dupes.py / _merge_seed_dupes2.py   合并
verify_wiki.py + rebuild_index.py                    收尾校验
```

## 记录在案的三个教训（已写入 skill 与长期记忆）

1. **`status: seed` ≠ 没有内容** —— 收官批常把已有完整正文的页面留成 seed。必须先测内容量。实测 447 个里有 161 个是"假 seed"。
2. **测内容量绝不可剔除表格行（`|`）与列表项（`-`）** —— 首版脚本删了 `^[#>|\-*]` 行，把表格密集型 legacy 页误判空白，虚报 355 vs 实际 174。
3. **代理报错 ≠ 没干活** —— 限流 429 前代理往往已落盘一部分（实测 seed 174→53 后才断）。报错后先查磁盘再重派，只补真缺的。

另：digest 关键词匹配会跑偏（`过滤材料` 命中液晶/热电摘录）—— 代理须回 cited-by 来源页核对原文。

## 待人工裁决（manual_review 类，不影响断链/索引）

**重复标题**（8 组）：
- `稀释便液 BM simulant A` ↔ `BM Simulant A`
- `粘胶 Rayon` ↔ `粘胶纤维 Viscose Fiber`
- `胶乳 Latex` ↔ `胶乳胶黏剂 Latex`
- `干燥角质化 Hornification` ↔ `角化 Hornification`
- `纺粘熔喷 Spunbond-Meltblown` ↔ `SMS 纺粘熔喷复合` ↔ `SMS复合结构`
- `热风无纺布` / `热风粘合无纺布` / `热粘合热风无纺布 Airlaid` / `热风非织造 Hot-Air Bonded Nonwoven`（4 标题同物）
- `东丽` / `舒美` 挂在 concepts/（应为 entities/）

**口径冲突**（未裁决，各页已并列保留）：
- PP 表面能 23 vs 29–31 mN/m
- PNIPAAM LCST 28 / 32 / 34.9 °C
- 脱挥发分须 T>Tg vs SAP 末段干燥须 T<Tg
- Stimuli-Responsive PCM 光学（GST/VO₂）与热管理（微胶囊）两个口径并存

**定义缺口**：大量页面标 `定义待补` —— 库内来源多为功能性口径，词典式定义需回原书补。

## 其他遗留

- P0 工业干燥 40 章未编译（A 原理 4 / B 设备 13 / C 物料 17 / D 系统 4 / E 经济 2）
- 261 条 manual_review 待集中裁决
- OI 编号两套混用的 24 页核对
