# 断链修复脚本 · 历史归档（_legacy_link_scripts）

**归档日期**：2026-10-12
**归档原因**：三代碎片化断链修复脚本的功能已全部收敛到 **`.tools/wkb_link_guard.py`**（check / plan / apply / report），旧脚本的白名单已机械提取并合并进 **`.tools/link_guard_curated.json`**。

> ⚠️ 本目录脚本**仅供追溯，请勿再运行**。新工作一律走 `wkb_link_guard.py`。

---

## 一、归档清单与替代关系

### 第 1 代（2026-09-29）— 雏形期

| 脚本 | 原职责 | 现由谁取代 |
|---|---|---|
| `fix_broken_links.py` | 归一化匹配改指（去括号/空格/标点后唯一命中） | `guard plan`（归一化分支；**更保守**——containment 只出 REVIEW，不自动改指） |
| `final_link_fix.py` | 手工 REWRITE 表(≈45) 改指 + 占位符清理 + seed 建页 | `guard plan/apply`（REWRITE 表已并入 `curated.redirects`；占位符 → `plain_text`） |
| `_fix_wires_links.py` | Wires 两页改名后回改链接 | `guard apply --mode=redirect`（个案已入白名单） |
| `_fix_wires_ext.py` | 修文件名缺 `.md` 后缀 | 一次性，无需替代 |
| `_check_wires.py` | 诊断（查尾部空格） | `guard check` |
| `_test_links.py` | 诊断（查 Wires 链接命中） | `guard check` |

### 第 2 代（2026-09-30）— 体系化

| 脚本 | 原职责 | 现由谁取代 |
|---|---|---|
| `_link_triage.py` / `_link_triage2.py` | 断链三级分级（REDIRECT / REVIEW / SEED） | `guard plan` |
| `_fix_links_all.py` | 三段式执行体（curated + GROUPS + seed），302 种断链 → 0 | `guard apply`（CURATED/GROUPS/BLOCK 已并入 `link_guard_curated.json`） |

### 第 3 代（2026-10-11）— 批次定向

| 脚本 | 原职责 | 现由谁取代 |
|---|---|---|
| `_links_p0b02_20261011.py` | 扫描 P0-B02 批次 8 页，产出断链待建页清单（只登记不建页） | `guard plan`（同纪律：seed 只出清单） |
| `_fixlinks_p0b02.py` | 按清单定向改指 6 条 | `guard apply --mode=redirect`（6 条已入白名单） |

### 数据产物（一并归档）

| 文件 | 说明 |
|---|---|
| `_link_triage.json` | 第 2 代分级结果 |
| `_link_fix_plan.json` | 第 2 代修复计划 |
| `_link_fix_result.json` | 第 2 代修复结果（新建页清单） |

---

## 二、关键纪律（已固化进 guard）

1. **改指只允许「同名变体」**——白名单命中且目标页已存在；**语义近似一律建 seed**。
2. **`BLOCK` 名单强制走 SEED**——禁止自动改指，防「上位→下位」窄化。
3. **seed 只出清单**——`apply` 默认只做改指；建页须显式 `--mode=seed/all`，人工裁决后执行。
4. **apply 前自动备份**——受影响页全量副本落 `.tools/_link_guard_backup_<ts>/`。

> 第 1 代曾用 token-overlap 自动匹配改指，产出「上位概念窄化到下位页」的错误
> （`非织造布 Nonwoven` → `Meltblown Nonwoven`、`BASF` → 某产品页）。
> 这是引入人工白名单 + BLOCK 兜底的直接动因。

---

_归档人：WorkBuddy · 依据 `.tools/LINK_GUARD_DESIGN_2026-10-12.md`_
