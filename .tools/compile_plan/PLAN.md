# 非书类欠账编译计划（341 条）

生成时间：2026-10-11　源脚本：`.tools/_make_nonbook_plan_20261011.py`（只读）

## 总量

原始 341 条 − 垃圾件 5 条 = **336 条待编译**

| 层级 | 条数 | 正文就绪 | 处置 |
|---|---:|---:|---|
| P0 | 46 | 46 | 立即编译 |
| P1 | 148 | 148 | 立即编译 |
| P2 | 7 | 0 | 补源或走通道 B 取原件 |
| P3 | 135 | 0 | 先回填正文（无镜像） |
| **合计** | **336** | **194** | |
| 垃圾件 | 5 | — | 不编译，待裁定 |

## 批次表

| 批次 | 层 | 一级区 | 二级区 | 条数 | 正文就绪 |
|---|---|---|---|---:|---|
| [P0-B01](P0-B01_Meeting_Minutes.md) | P0 | Areas | Meeting Minutes | 26 | 26/26 |
| [P0-B02](P0-B02_IP.md) | P0 | Areas | IP | 15 | 15/15 |
| [P0-B03](P0-B03_Supply_Base.md) | P0 | Areas | Supply Base | 4 | 4/4 |
| [P0-B04](P0-B04_Test_Method.md) | P0 | Areas | Test Method | 1 | 1/1 |
| [P1-B05](P1-B05_Training.md) | P1 | Resources | Training | 65 | 65/65 |
| [P1-B06](P1-B06_Open_Innovation.md) | P1 | Resources | Open Innovation | 39 | 39/39 |
| [P1-B07](P1-B07_WKB根级.md) | P1 | Z_其他 | WKB根级 | 32 | 32/32 |
| [P1-B08](P1-B08_Market_Insight.md) | P1 | Areas | Market Insight | 12 | 12/12 |
| [P1-B09](P1-B09_Test_Method.md) | P1 | Areas | Test Method | 3 | 3/3 |
| [P1-B10](P1-B10_Pulp_World.md) | P1 | Resources | Pulp World | 1 | 1/1 |

## 执行顺序建议

1. **P0 优先**：Areas/IP（专利）、Areas/Meeting Minutes（供应商与内部评审纪要）、Areas/Supply Base（供应商资料）——直接支撑研发决策与供应商管理
2. **P1 次之**：Resources/Training（芯体与裤型培训）、Resources/Open Innovation（材料/性能/仿真）
3. **P2/P3 挂起**：P2 走通道 B 取原件；P3 先跑正文回填（MCP `fetch_media_content` 优先，不受 200005 配额限制）
4. 每批编译完跑 `rebuild_index.py` + 追加 `log.md`，并回写各批次文件的「已编译」列
