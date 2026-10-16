# 断链治理工具落地报告 · 2026-10-12

**依据**：王总 2026-10-12 裁决 —— ① seed 只出清单（不自动建）；② 先建工具、按方案收敛断链修复脚本，同步修 MOC 口径问题（2+3）。断链本身另开批次。

---

## 一、结论

**工具落地完成。** 三代共 11 个碎片化断链脚本收敛为单一入口 `.tools/wkb_link_guard.py`（check / plan / apply / report）；MOC 口径问题（2+3）已修并验证。断链 129 种**未处理**（按指示另开批次）。

---

## 二、交付物

| 文件 | 说明 |
|---|---|
| `.tools/wkb_link_guard.py` | **主工具**（check / plan / apply / report） |
| `.tools/link_guard_curated.json` | **白名单**（109 条，机械提取） |
| `.tools/_build_link_curated_20261012.py` | 白名单提取器（ast 解析，可复跑，禁手工誊抄） |
| `.tools/link_guard_reports/` | 运行产物（`<date>_plan.{json,md}` / `<date>_report.md`） |
| `.tools/_legacy_link_scripts/` | 旧 **11 脚本 + 3 产物 + README**（归档，不删） |

---

## 三、白名单规模（109 条）

| 类别 | 条数 | 用途 |
|---|---|---|
| `redirects` | 60 | 同名变体改指（目标页须存在） |
| `groups` | 9 组 / 11 变体 | 变体族 → canonical |
| `block` | 23 | **强制走 SEED**，禁止自动改指 |
| `plain_text` | 2 | 占位符/行文链接 → 纯文本 |
| `filename_sanitize` | 13 | 含 `/` 的文件名安全化 |
| **合计** | **109** | |

来源：`_fix_links_all.py`(CURATED/GROUPS/BLOCK) + `final_link_fix.py`(REWRITE) + `_fixlinks_p0b02.py`(FIX)。**机械提取，零手工誊抄。**

---

## 四、运行结果（2026-10-12 基线）

| 项 | 值 |
|---|---|
| 扫描页 | 2157（WIKI 2155 + index/log 2） |
| **断链目标** | **129 种 / 157 处** —— 与 `verify_wiki.py` **完全一致**（交叉验证 ✅） |
| REDIRECT | **6 种**（同名变体，可直接改指） |
| REVIEW | **11 种**（多候选，待人工裁决） |
| SEED | **112 种**（真缺失，**只出清单**） |
| 畸形链接 `[[[X]]]` | 1 种 |

报表：`.tools/link_guard_reports/2026-10-12_plan.{json,md}`

---

## 五、MOC 口径修复（问题 2+3）

| # | 问题 | 修法 | 证据 |
|---|---|---|---|
| 2 | `verify_wiki.py` 误报 `type 非法: moc`（13 页） | REQ 表加 `MOC_TYPES={'moc'}` 豁免（AGENTS §1：MOC 不参与 status 治理） | 复检**该误报清零**；通过 **2147/2155** |
| 3 | `rebuild_index.py` 不扫 `WIKI/MOC/` → index 漏收 13 页 | 加 MOC 区 + 头部统计含 MOC | index 对齐 **2155 / 2155 / 漏收 0**；index.md 新增「导航层 `WIKI/MOC/`」区（行 2191） |

备份：`.tools/_index_backup_before_moc_20261012.md`

---

## 六、验证

| 项 | 方法 | 结果 |
|---|---|---|
| 语法 | `py_compile` ×4 | ✅ OK |
| **交叉验证** | guard `check` vs `verify_wiki.py` | ✅ 断链 **129 = 129** |
| **幂等** | guard `plan` 连跑两次 | ✅ REDIRECT 6 / REVIEW 11 / SEED 112 恒定 |
| MOC 误报 | `verify_wiki.py` 复检 | ✅ 清零 |
| index 漏收 | guard `check` 复检 | ✅ 0 |

---

## 七、纪律固化（已写进 guard 代码 + 归档 README）

1. **改指只允许「同名变体」**——白名单命中且目标页已存在；语义近似一律走 SEED。
2. **`BLOCK` 名单强制 SEED**——禁止自动改指，防「上位→下位」窄化。
3. **seed 只出清单**——`apply` 默认只做改指；建页须显式 `--mode=seed/all`（人工裁决后）。
4. **apply 前自动备份**——受影响页全量副本落 `.tools/_link_guard_backup_<ts>/`。
5. **guard 比第 2 代更保守**：containment 命中一律进 REVIEW，仅「归一化**精确相等**」才自动改指。
6. 承 AGENTS §1.1 铁律：正则 `[ \t]*`、每子命令首行自证覆盖率。

---

## 八、未做的事（按指示）

- ❌ 未修 129 种断链（另开批次）
- ❌ 未自动建任何 seed 页（纪律：只出清单）
- ❌ 未挂接自动化（等工具稳定后再议）
- ⚠️ 遗留：**8 页 P0-B02 批次**仍缺 `date_processed/credibility/key_claims/pages_linked`（既有问题，未处理）

---

## 九、下一步建议

1. **人工裁决 REVIEW 11 种**（`<date>_plan.md` 已列候选）→ 追加 `link_guard_curated.json` → `apply --mode=redirect`
2. **裁决 SEED 112 种**：区分「建页 / 改指 / 忽略」→ `apply --mode=seed`
3. 补 8 页 P0-B02 缺失字段

---

_报告版本：v1（2026-10-12）。_
