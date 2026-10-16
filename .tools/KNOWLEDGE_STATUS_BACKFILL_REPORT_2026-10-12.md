# knowledge_update_status 补齐行动报告

**日期**：2026-10-12　**依据**：`.tools/LINK_GUARD_DESIGN_2026-10-12.md` §六 · 方案 A
**决策**：王总 2026-10-12「走 A，然后 474 页先 pending」

---

## 一、结论

**方案 A 执行完毕，target 字段的校验 FAIL 已清零（483 → 0）。**

| 指标 | 执行前 | 执行后 |
|---|---|---|
| sources 缺 `knowledge_update_status` | **483 页** | **0 页** ✅ |
| 该字段覆盖率 | 906 / 1389（65%） | **1389 / 1389（100%）** |
| 生成器是否写该字段 | ❌ 两个都漏 | ✅ 都写（默认 `pending`） |
| AGENTS §2.3 示例 | ❌ 漏列 | ✅ 已补列 |

---

## 二、改动清单（4 处）

### 2.1 存量回填（483 页）

| 项 | 内容 |
|---|---|
| 脚本 | `.tools/_backfill_knowledge_status_20261012.py`（新增，幂等，dry-run 默认） |
| 动作 | 在 front matter 的 `credibility:` 行后插入 `knowledge_update_status: pending` |
| 范围 | 483 页全部命中（**覆盖率自证**：匹配 906 / 缺失 483 / 合计 1389） |
| 插入位置 | 与 `TEMPLATES/source.md` 顺序一致（`credibility` → `knowledge_update_status` → `key_claims`） |
| 备份 | `.tools/_knowledge_status_backfill_backup_20261012/sources/`（483 文件全量副本） |
| 清单 | `.tools/_knowledge_status_backfill_20261012.json`（受影响页全清单，供回滚） |

### 2.2 生成器修复（3 个脚本）

| 文件 | 位置 | 改动 |
|---|---|---|
| `.tools/kb_compiler.py` | `build_front_matter()` 行 187 | 新增 `"knowledge_update_status: pending"` |
| `.tools/_compile_extractive.py` | `build_front_matter()` 行 44 | 同上 |
| `.tools/patch_frontmatter.py` | `DEFAULTS` 行 18 | 默认值 `done` → **`pending`**（口径统一） |

> 实测（`py_compile` 通过 + 实际调用）：两个生成器新产出的 front matter 均含该字段，位置正确。

### 2.3 AGENTS.md 修正（2 处）

| 位置 | 改动 |
|---|---|
| §2.3 行 193 | **补列** `knowledge_update_status: pending \| done \| manual_review`（此前示例漏列 → 与 `TEMPLATES/source.md` 矛盾） |
| 顶部行 5 | 「最后更新」改为 2026-10-12，原 09-30 说明降为「前次更新」（保留历史） |

---

## 三、验证证据

| 验证项 | 方法 | 结果 |
|---|---|---|
| 字段缺失清零 | `verify_wiki.py` 重跑 | ✅ 该字段 FAIL **0** |
| **幂等** | 回填脚本连跑两次 | ✅ 第二次「缺字段 **0**」 |
| 生成器有效性 | 实际调用两个 `build_front_matter()` | ✅ 均输出 `pending` |
| 语法 | `py_compile` ×3 | ✅ OK |
| 插入位置 | 抽查 `1780441413046.jpg.md` | ✅ `credibility` 后、`key_claims` 前 |

---

## 四、顺带发现（**既有问题，不在本次范围，待裁决**）

本次校验重跑暴露 3 项**与 knowledge_update_status 无关**的既有问题：

| # | 问题 | 数量 | 性质 |
|---|---|---|---|
| 1 | **8 页缺 `date_processed/credibility/key_claims/pages_linked`** | 8 | 10-11 **P0-B02 批次**手工页字段不全（BLOCLO 盛色、Insilico×2、JMP 16、US 2007-0203469、US 5266394、CN 111134966、松井色素）——**恰好是 `_fixlinks_p0b02.py` 处理的那 8 个文件** |
| 2 | **`type 非法: moc`** | 13 | `verify_wiki.py` 的 REQ 表**不含 `moc` 类型** → 13 个 MOC 页被误报。AGENTS §1 明确「MOC 不参与 status 治理」→ **校验器口径缺陷** |
| 3 | **index.md 漏收 MOC** | 13 | `rebuild_index.py` 只扫四类目录，不扫 `WIKI/MOC/` |
| 4 | 断链目标 | 129 | 与本次无关，属 `wkb_link_guard.py` 方案的职责 |

> 建议下一批处理：问题 2+3 一起修（校验器加 `moc` 类型豁免 + `rebuild_index.py` 收 MOC）；问题 1 按 §1.1 纪律补字段；问题 4 待 guard 方案落地。

---

## 五、回滚方式（如需）

```bash
# 全量回滚 483 页
cp .tools/_knowledge_status_backfill_backup_20261012/sources/*.md WIKI/sources/
```

生成器与 AGENTS 的改动可用 git diff 单独回退。

---

## 六、边界说明（未做的事）

- ❌ 未动 `RAW/`、未改任何 `source_path`、未动 `status` 字段。
- ❌ 未处理上述 4 项顺带发现（等王总裁决）。
- ❌ 未挂接自动化（等 guard 工具稳定后再议）。

---

_报告版本：v1（2026-10-12）。_
