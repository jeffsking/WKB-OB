# WKB-OB · IMA → Obsidian 统一知识管道 设计方案

**日期**：2026-10-11
**状态**：待王总确认（确认后按 §6 步骤分批实施）
**关联**：`IMA_NOTE_SYNC_ROOTCAUSE_2026-10-10.md`、`IMA_NOTE_BACKFILL_RUNBOOK.md`、`AGENTS.md` §2/§3/§7

---

## 0. 现状核对（今日实测，非推测）

| 事实 | 实测值 | 来源 |
|---|---|---|
| IMA 知识库名 | `WKB`（"Chris的知识库"主体库） | MCP `get_knowledge_base_list` |
| MCP 视角 KB ID | `001a693ee6c0644e` | MCP `get_knowledge_list` |
| REST 视角 KB ID | `F8DbmyEF1G8cO-4woYjmlpOs1dETfSgd8-mu6PSsPOI=` | REST `get_knowledge_list` |
| IMA 条目总数 | **1378**（含文件夹节点） | `knowledge_total_size` |
| 根层级文件夹 | 5（Areas / Projects / Inbox / Archives / Resources） | 根层枚举 |
| 本地镜像文件夹数 | **244**（递归 `WKB/` 下，含各 `attachments/`） | `find RAW/ima_sync/... -type d` |
| 本地 `RAW/ima_sync` md 文件 | **1766**（含占位壳） | `find` |
| 本地 `RAW_FULL` md 文件 | **459** | `find` |
| WIKI 源摘要页 | **876**（其中 874 带 `knowledge_update_status`） | `WIKI/sources/` |
| **同名文件跨路径重复** | **11 组** | `find + uniq -d` |

### 0.1 关键结论：现有脚本解决不了"新增发现问题"

`.tools/ima_note_backfill.py` 的 `collect()` 是**从本地 `RAW/` 向上遍历**，找"RAW 侧是占位符、RAW_FULL 侧没正文"的缺口。

> **它只能修「已落盘但没正文」的条目，永远看不见「IMA 里有、vault 里根本没有」的条目。**

这就是当前自动化体系的唯一结构性缺口：**没有 discovery（发现）环节，只有 repair（修复）环节。**

---

## 1. 用户提的"两类路径"——精确定义

今日 MCP 枚举确认，IMA 侧同一 KB 内条目确实分处两处，本地镜像一一对应：

| 类别 | IMA 侧特征 | 本地落点 | 当前数量 |
|---|---|---|---|
| **A. 根目录条目** | `parent_folder_id == "001a693ee6c0644e"` 且 `folder_info == null` | `RAW/ima_sync/个人知识库/WKB/<标题>.md` | 本地 52 个文件 |
| **B. 已归档条目** | `parent_folder_id == "folder_xxx"`（在文件夹内，可多层嵌套） | `RAW/ima_sync/个人知识库/WKB/<Folder链>/<标题>.md` | Areas 769 / Resources 2076 / Projects 158 / Inbox 15 / Archives 15 |

**关键机制**：IMA 的归档不是"复制"而是"移动"——同一条目（同一 `media_id`）今天在根目录，明天可能被自动归档进 `Areas/IP/`。**`media_id` 不变，路径变。** 这是整个去重设计必须处理的核心场景（见 §3.3）。

---

## 2. 方案总览

把现有零散的自动化整合为**一条日更管道**，五个阶段串行：

```
阶段 A枚举Discovery → 阶段 B 落地 Sync → 阶段 C 编译 Compile → 阶段 D 日志 Journal → 阶段 E 收尾 Finalize
IMA KB├─ 根层枚举        MCP fetch_media_content      RAW →WIKI/sources      RAW/journal 未处理日志    rebuild_index.py
        └─ 文件夹递归      REST get_media_info 原件     → concepts/entities    §7 四类沉淀             log.md 追加
           (244 目录)     ↓                                                     ↓                       状态快照落盘
                    RAW_FULL/ 同相对路径                                     追加式写 WIKI
```

**统一状态账本**：`.tools/_ima_sync_state.json` —— 全流程唯一判重真相源。

---

## 3. 判重与状态机制（本方案的核心）

### 3.1 三级判重键

| 级别 | 键 | 作用 | 防的是 |
|---|---|---|---|
| **主键** | `media_id` | 唯一身份，跨路径跨改名恒定 | 同一条目被重复入库 |
| **次键** | `kb_path`（文件夹链 + 文件名） | ledger 丢失后可从本地反查恢复 | 账本损坏导致的漏判 |
| **指纹** | `sha1(标题 + file_size)` 或正文 sha1 | 同物改名 / 异名同物 | 标题变更导致的重复编译 |

> **为什么不能用"路径 + 文件名"当唯一键**：实测本地有 **11 组同名文件分布在不同路径**（如 `README.md` 两份、`变色油墨供应商综合技术联系表.xlsx.md` 两份）。它们是不同的条目，不是重复。**必须以 `media_id` 为准。**

### 3.2 五态状态机（与 `knowledge_update_status` 正交）

`knowledge_update_status`（pending/done/manual_review）管的是**编译层**。同步层需要独立的一套：

| 状态 | 含义 | 进入条件 | 下一步 |
|---|---|---|---|
| `discovered` | 已枚举到，本地无正文 | ledger 无记录 | 进 B |
| `synced` | `RAW_FULL` 已有正文 | `extract_status: ok\|empty\|original-only` | 进 C |
| `compiled` | WIKI 源摘要页已建且 `done` | source 页存在 | 终态 |
| `manual_review` | 敏感/ 冲突 / 无法处理 | 命中 §5 边界 | 等人工 |
| `absent` | IMA 侧已删除 | 枚举时本地有、IMA 无 | 记档**不删本地** |

### 3.3 移动检测（用户关切点）

```
枚举得media_id + 当前 kb_path
        ↓
   ledger 命中？
   ├── 否 → 新增 → discovered
   └── 是 → 比对 kb_path
            ├── 相同 → 已处理，跳过
            └── 不同 → **移动**
                 ├─ 记 moves[]: {from, to, date}
                 ├─ 更新 kb_path（账本跟随）
                 ├─ 编译层：更新 source 页 source_path（元数据修正，记 log）
                 └─ **不移动本地文件**（保RAW ↔ RAW_FULL 1:1 镜像不破）
                    提供 `--apply-moves` 开关，人工决定是否真搬
```

**为什么默认不搬文件**：`RAW/` 是插件维护的只读层（AGENTS.md §0 红线），AI 搬 `RAW_FULL` 会立刻破坏 1:1 镜像，插件下轮同步又会按旧路径重新生成，陷入拉锯。**记映射、不搬文件**是唯一稳定解。

另外产出 `_orphans_report.json`：`RAW/` 里有、但账本 kb_path 对不上的残影（插件 `if (a.has(i.media_id)) continue` 冻结产物），列出来供人工判断，不自动删。

### 3.4 账本文件格式

`.tools/_ima_sync_state.json`：

```json
{
  "version": 2,
  "kb_id_mcp": "001a693ee6c0644e",
  "last_full_scan": "2026-10-11T08:44:00+08:00",
  "folders": {
    "folder_7446577501179608": {
      "path": "Areas", "file_number": 16, "folder_number": 8,
      "last_checked": "2026-10-11", "pruned": false
    }
  },
  "items": {
    "note_3867e2b60070d7dc3f413086d0b0036e_7514128608427948": {
      "title": "会议纪要：OI 十月供应商考察与项目推进安排",
      "media_type": 11,
      "kb_path": "Areas/Meeting Minutes/会议纪要：OI 十月供应商考察与项目推进安排.md",
      "create_ts": 1791507913336,
      "first_seen": "2026-10-11",
      "last_seen": "2026-10-11",
      "stage": "discovered",
      "raw_path": null,
      "full_path": "RAW_FULL/ima_sync/个人知识库/WKB/Areas/Meeting Minutes/会议纪要：OI 十月供应商考察与项目推进安排.md",
      "source_page": null,
      "moves": [
        { "from": "会议纪要：OI 十月供应商考察与项目推进安排.md",
          "to": "Areas/Meeting Minutes/会议纪要：OI 十月供应商考察与项目推进安排.md",
          "date": "2026-10-11" }
      ]
    }
  }
}
```

---

## 4. 枚举器设计（阶段 A）——含成本控制

### 4.1 全量递归的真实成本

244 个文件夹 + 1378 条目，按 MCP `limit ≤ 50` 分页：

```
约 245 次目录调用 + 约 28 次翻页 ≈ 273 次 MCP 调用 / 全量扫描
```

每日全量不现实。**剪枝策略**：

### 4.2 `file_number` 变化检测（关键优化）

MCP 返回的文件夹对象自带 `folder_info.file_number`（直属文件数）与 `folder_number`（子文件夹数）——这是一个**免费的廉价变更信号**。

```
枚举根层 → 拿到 5 个顶层文件夹
    ↓
逐个比对账本里的 file_number + folder_number
    ├── 与上次一致 → **不进入该目录**（省下一次调用）
    └── 有变化 → 进入枚举，并更新账本
    ↓
对进入的目录，只取 create_time ≥ 水位 的条目；更早的只核对存在性
```

**典型日增量**：5 次根层 + 少数变动目录 ≈ **8~15 次调用**（vs 全量 273）。
**兜底**：每周一次强制全量递归对账，防止剪枝漏判。

### 4.3 只取已解析完成的条目

枚举时带 `filters: [{filter_type: MEDIA_TYPE_FILTER_TYPE, media_state_filter: {media_states: [MEDIA_PARSE_SUCCESS]}}]`，跳过 `MEDIA_PARSING` 的半成品，避免拉到空壳。

---

## 5. 落地器设计（阶段 B）——通道分级沿用已验证结论

根因报告已实测确认的三通道，直接复用，不重新发明：

| 通道 | 手段 | 配额 | 适用 |
|---|---|---|---|
| **A** | MCP `fetch_media_content` | **无日配额** | 笔记 / 录音 / session / 网页（`media_type ∈ {11,12,15,20,2}`） |
| **B** | REST `get_media_info` → 签名 URL → GET | 宽松 | 无文字层原件（图纸图片 / 扫描件 PDF / Office / CSV） |
| **C** | REST `get_doc_content` | **受日配额（200005）** | 仅兜底，命中即当日放弃，**禁止循环重试** |

**落盘铁律**（沿用已固化结论）：
1. 正文一律写 `RAW_FULL/<同相对路径>`，**绝不写 `RAW/`**（只读红线）
2. 原件落`RAW_FULL/<条目目录>/attachments/<原始文件名>`，用回原名（Obsidian 可直接 `![](attachments/x.jpg)`）
3. 原件扩展名按 **Content-Type → 魔数 → 前缀** 三级判定
4. `extract_status ∈ {ok, empty, original-only}` 即视为终态，**不再重跑**

---

## 6. 实施步骤（分 5 批，每批可独立验收）

### 第 1 批 · 账本与枚举器（半天）
- 新建 `.tools/ima_sync_state.py`
  - `init` — 扫描本地 `RAW/` 建初始账本（从 876 个 source 页的 `source_path` + RAW front matter 反推 `media_id ↔ 路径` 映射）
  - `enumerate` — 递归枚举 + `file_number` 剪枝 + 移动检测 → 写账本
  - `status` — 一行摘要
- 验收：`enumerate` 跑完，`items` 数与 IMA 侧条数（1378 −文件夹数）对得上，`moves` 有实际样本

### 第 2 批 · 落地器接线（半天）
- 在 `ima_sync_state.py` 加 `sync` 子命令，对 `stage=discovered` 的条目按 §5 通道分级落`RAW_FULL`
- 复用 `ima_note_backfill.py --slices` 的子代理切片机制（正文可达数百 KB，不能在主会话逐条拉）
- 验收：新增条目全部 `synced`，`extract_status` 分布合理

### 第 3 批 · 编译器接线（1天）
- `compile` 子命令：`RAW` 有、`WIKI/sources` 无 source_path 的条目 → 生成源摘要页
- 严格照 AGENTS.md §3：先源摘要页 → 再概念/实体页 → 全部 `[[wikilink]]` 互链
- **英文为主 + 中文对照**（§2.0）
- 数字必须来自源摘要页，无来源判断标 `[待验证]`
- 命中 §5 四条人工边界 → `manual_review`，不自动裁决
- 验收：跑 `rebuild_index.py`，`index.md` 四区对齐，无新增断链

### 第 4 批 · 统一编排器（半天）
- 新建 `.tools/kb_daily_pipeline.py`：一条命令跑完 A→B→C→D→E
- 任一阶段失败**不中断后续**，产出部分结果 + 失败清单（符合"进程被 kill 也要返回已有结果"的要求）
- 报告落 `.tools/kb_pipeline_daily/YYYY-MM-DD.md`

### 第 5 批 · 自动化整合（半小时）
- 新建自动化「**WKB-OB 知识管道 · 日更**」：每日 09:30，cwd = `E:/WKB-OB`
- 暂停/删除：
  - `8523233b` IMA 条目正文回填巡检（ACTIVE）→ 其能力被阶段 B 吸收
  - `bcaf361b` WKB-OB 日志扫描（**当前 PAUSED**）→ 其能力被阶段 D 吸收
- 新增每周任务「全量对账 + §5 健康检查」：周日 09:00

### 首日全量对账（并入第 5 批执行）
IMA 1378 条（含约 245 文件夹节点 → 实际文档约 1130 条）对本地已编译 876 页，**预估 200~300 条历史欠账**待编译。首日跑完 `--force-full` 后出准确数字。

---

## 7. 与现有日志扫描（§7）的整合方式

阶段 D **完全复用**现有 §7 规则，不改逻辑，只换执行位置：

| §7 能力 | 保留在阶段 D | 变化 |
|---|---|---|
| 判重`source_path` + `knowledge_update_status` | ✅ | 不变 |
| 四类判断（验证/实体动态/新概念实体/教训） | ✅ | 不变 |
| `RAW/journal/` 只读 | ✅ | 不变 |
| 追加式写入，不改既有结论 | ✅ | 不变 |
| `manual_review` 标记 + log.md 说明 | ✅ | 不变 |
| **执行频率** | 18:00 → **并入 09:30 统一管道** | 一次跑完 A~E |

> **是否合并的取舍**：合成一条的好处是状态账本统一、报告一份；坏处是日志扫描被 IMA 枚举的耗时拖累。建议 **09:30 跑 A/B/C/E，18:00 单独跑 D**（D 极轻，秒级），两者共享同一账本。我倾向这个拆法——除非王总坚持要单条。

---

## 8. 风险与边界

| 风险 | 缓解 |
|---|---|
| 枚举调用量超限触发限频 | `file_number` 剪枝（§4.2）+ 每轮调用间延迟 + 命中限频即停并保留进度 |
| REST `get_doc_content` 200005 | 通道 A 优先；命中 C 即当日放弃，**禁止循环重试**（已实测 12 轮重试零产出） |
| 移动后本地文件分裂| 默认**只记映射不搬文件**（§3.3），`--apply-moves` 人工触发 |
| 编译出无来源的数字 | 强制走源摘要页；无来源标 `[待验证]` |
| 商务敏感信息页面化 | 命中即 `manual_review`（§5 边界，AI 不得自动执行） |
| 账本损坏 | `init` 可从本地 1766 个文件 + 876 个 source 页**完全重建** |
| `RAW/ima_sync/notes/飞书.md` 含明文密钥 | 建议移出 vault 或改 `.env` 引用（**遗留项，非本方案引入**） |

---

## 9. 每日管道输出示例

```
=== WKB-OB 知识管道 · 2026-10-11 ===

[A枚举] 根层 5 文件夹 → 剪枝后进入 3 个 → 新增 12 / 移动 4 / 已知 1089
       media_state=PARSING 跳过 2
[B 落地] discovered 12 → ok 9 / empty 2 / original-only 1
       通道A(MCP) 9 · 通道B(原件) 1 · 通道C 未触发
[C 编译] 12 条 → sources 新建 12 · concepts 新建 3 · entities 更新 5
       manual_review 1（疑似商务敏感：报价单）
[D 日志] RAW/journal/ 空 → 零动作
[E收尾] rebuild_index.py 完成 · index.md 876 → 888 页
       log.md 已追加 · 账本已保存 · 孤儿残影 3 个（待人工）

⏱ 耗时 6m12s · 报告 .tools/kb_pipeline_daily/2026-10-11.md
```

---

## 10. 待确认事项

1. **09:30 单条 vs 09:30+18:00 拆两条**（§7 末段建议拆两条）
2. **首日全量对账是否立即跑**（会一次性编译 200~300 条历史欠账，耗时可能 1~2 小时）
3. 阶段 B 遇`media_type=15`（录音，20 MB）时，是否默认只取转写文本、跳过原件下载