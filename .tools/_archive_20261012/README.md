# 归档：2026-10-12 一次性脚本

本目录存放 **2026-10-12 断链治理 / concept 库整顿** 期间执行过、**已完成使命**的一次性脚本。
保留供追溯（未删除），**不再运行**。

## 归档清单

| 脚本 | 用途（已完成） |
|---|---|
| `_backfill_knowledge_status_20261012.py` | 回填 483 页 `knowledge_update_status: pending` |
| `_fix_p0b02_frontmatter_20261012.py` | 修 8 页 P0-B02 批次的非标准字段名 |
| `_merge_duplicate_concepts_20261012.py` | 合并 5 组重复 concept（副件转 merged 指针页） |
| `_seed_semantic_probe_20261012.py` | 优先 SEED 语义探测（第一轮） |
| `_seed_semantic_match_20261012.py` | 111 条 SEED 语义匹配（第二轮，含 concept 语义档案构建） |
| `_collect_seed_material_20261012.py` | 抽 seed 页引用素材 |
| `_fill_seed_pages_b1_20261012.py` | 第 1 批 seed 页补内容（28 页） |
| `_fill_seed_pages_b2_20261012.py` | 第 2 批 seed 页补内容（39 页） |

## 未归档（仍在 `.tools/` 根，属管线/可追溯）

| 文件 | 原因 |
|---|---|
| `_rebuild_concept_domains_20261012.py` | **新 concept 入库后仍需运行**（域归类引擎） |
| `_classify_unclassified_20261012.py` | 含 114 条人工裁定逻辑，可追溯/可复跑 |
| `_build_link_curated_20261012.py` | 白名单 `link_guard_curated.json` 的 provenance（guard 报错信息指向它） |
| `_unclassified_assign_20261012.json` | domain 重建器的**人工裁定表数据**（输入） |
| `_concept_index_20261012.json` | domain 重建器的**重构前 domain 快照**（确定性输入） |

> 相关报告：`.tools/SEED_BUILD_REPORT_2026-10-12.md`、`.tools/SEED_FILL_REPORT_2026-10-12.md`、
> `.tools/CONCEPT_MERGE_AND_DOMAIN_REBUILD_2026-10-12.md`、`.tools/UNCLASSIFIED_FIX_REPORT_2026-10-12.md`。
