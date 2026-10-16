# 断链治理 · 第一批执行报告 · 2026-10-12

**触发**：王总 2026-10-12 21:51「好的，开始」（承接工具落地后的下一步）
**范围**：① 修 guard 判定缺陷 ② 裁定 REVIEW 11 ③ 修 8 页字段分叉 ④ 执行改指

---

## 一、结论

| 指标 | 开始前 | 完成后 |
|---|---|---|
| 断链目标 | 129 种 | **123 种**（−6）✅ |
| REVIEW 待裁决 | 11 种 | **0 种**（全部裁定）✅ |
| front matter 通过 | 2147 / 2155 | **2155 / 2155（100%）** ✅ |
| index 对齐 | 2155 / 2155 | 2155 / 2155 ✅ |

---

## 二、guard 判定缺陷修正（假唯一）

**问题**：`norm()` 去括号归一化会造假唯一。例：`Insilico 功能性微胶囊` 与页面 `Insilico 功能性微胶囊（中文产品册·2019）` 去括号后都归一为 `insilico功能性微胶囊` → 被误判「唯一命中」而自动改指到「中文产品册」（**任意选择**，语义错误）。

**修法**：加「括号变体」检查——若存在**其他**页面的 norm 以 `n` 为前缀，则不自动改指，转 REVIEW。

```python
variants = {b for b in valid if b != tgt and norm(b).startswith(n) and norm(b) != n}
if len(hits) == 1 and not variants and len(n) >= 6:   # ← 加 not variants
    redirect[tgt] = next(iter(hits))
```

**效果**：该条从 REDIRECT 降为 REVIEW → 裁定后归 SEED。

---

## 三、REVIEW 11 条裁定

| # | 目标 | 裁定 | 依据 |
|---|---|---|---|
| 1 | `尿裤（卫生巾）…方案探` | → **redirects** | 与正确页名只差**空格**（真·同名变体） |
| 2 | `Daehyoon`（3 篇纪要） | → **block**（SEED） | 供应商实体，指向任一纪要即窄化 |
| 3 | `Insilico`（2 册） | → **block**（SEED） | 同上 |
| 4 | `Insilico 功能性微胶囊`（泛称） | → **block**（SEED） | 泛称歧义（2 候选） |
| 5 | `Huayi集团` | → **block**（SEED） | 实体 → 纪要，窄化 |
| 6 | `山东希瑞新材` | → **block**（SEED） | 同上 |
| 7 | `水致变色油墨` | → **block**（SEED） | 子类 ⊂ `变色油墨`，指上位即丢语义 |
| 8 | `双组分纤维PE/PET` | → **block**（SEED） | `PET（聚酯）` 是窄化 |
| 9 | `SUPER ABSORBENT RESIN` | → **block**（SEED） | `EP3636698B1…` 是具体专利，非泛称 |
| 10 | `SMMS 纺粘-熔喷-熔喷-纺粘无纺布` | → **block**（SEED） | `纺粘无纺布` 是窄化 |
| 11 | `SAP 表面交联` | → **block**（SEED） | `BNC 基…` 是窄化 |

> **裁定原则**：REVIEW 中绝大多数是「上位概念 → 下位页」的窄化陷阱 → 一律 `block`（强制走 SEED）。
> 判定依据全部来自候选页与引用页的实际内容，非猜测。

白名单变更：`redirects` 60 → **61**；`block` 23 → **34**；新增 `review_decisions` 段留痕。

---

## 四、8 页字段分叉修复（第三次「多源不一致」）

**问题**：`_compile_p0b02_20261011.py`（10-11 P0-B02 批次）生成时用了**非标准字段名**：

| 实际字段 | 应为（AGENTS §2.3） |
|---|---|
| `source_credibility` | `credibility` |
| `compiled_at` | `date_processed` |
| `related` | `pages_linked` |
| （无） | `key_claims` |

**处置**：原地**改名 + 补 `key_claims: []`**（不臆造内容）；`knowledge_area` / `compile_batch` / `subjects` 作为扩展元数据**保留**。

- 脚本：`.tools/_fix_p0b02_frontmatter_20261012.py`（幂等，dry-run 默认）
- 备份：`.tools/_p0b02_fm_backup_20261012/`（保留最早版本，不被二次覆盖）
- 结果：8 页 → **front matter 通过率 2147/2155 → 2155/2155（100%）**

---

## 五、改指执行结果

`python .tools/wkb_link_guard.py apply --mode=redirect`

| 项 | 值 |
|---|---|
| 备份 | `.tools/_link_guard_backup_20261012_215553`（5 文件） |
| 改指 | **6 处** |
| 畸形修复 | 0 |
| seed 新建 | **0**（纪律：只出清单） |
| 断链 | **129 → 123 种** |

---

## 六、验证

| 项 | 结果 |
|---|---|
| 交叉验证 | guard `check` 断链 **123** = `verify_wiki.py` **123** ✅ |
| front matter | **2155 / 2155（100%）** ✅ |
| index 对齐 | **2155 / 2155 漏收 0** ✅ |
| 幂等（字段修复脚本） | 第二次命中 **0 页** ✅ |
| 幂等（plan） | REDIRECT 6 / REVIEW 0 / SEED 123 稳定 ✅ |

---

## 七、剩余 SEED 123 条（待裁决）

- **拟建 concept 119 / entity 4**
- 引用 ≥2 的 20 条（优先）。

| 引用 | 目标 | | 引用 | 目标 |
|---|---|---|---|---|
| 4x | Pinhole 开孔 | | 2x | 水致变色油墨 |
| 4x | 三叶草截面纤维 | | 2x | 感温变色微胶囊 |
| 3x | Daehyoon | | 2x | 感光变色微胶囊 |
| 3x | 微胶囊 | | 2x | TBCW在线超声波复合工艺 |
| 3x | 双组分纤维 | | 2x | 异形纤维 |
| 3x | 图片类条目 | | 2x | 可弃式服装（P&G 专利族） |
| 2x | 温变材料 | | 2x | 热熔胶 |
| 2x | 防漏结构 | | 2x | 底膜 |
| 2x | 绒毛浆 | | 2x | ES纤维 |
| 2x | Insilico | | 2x | 温变油墨 |

> 全 123 条见 `.tools/link_guard_reports/2026-10-12_plan.md`。
> **需裁决**：区分「建页 / 改指到既有页 / 忽略」。裁决后跑 `apply --mode=seed`。

**注**：`图片类条目`（3x）疑似**占位符残留**（非真实概念），建议归「忽略」。

---

## 八、遗留

- ⚠️ `图片类条目` 等疑似占位符（待裁决）
- ⚠️ 123 条 SEED 未建页（按纪律只出清单）
- ⚠️ 畸形链接 1 种未处理（随改指批次）

---

_报告版本：v1（2026-10-12）。_
