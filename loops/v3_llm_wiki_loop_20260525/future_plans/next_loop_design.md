---
status: future_plan
stage: discussion_only
created: 2026-05-29
loop_id: v3_llm_wiki_loop_20260525
topic: next_loop_design
note: 下一个 loop 的最终形态设计，逐环节敲定中。仅讨论，未执行。evolve 环节细节见同目录 fusion_and_governance.md。
---

# Future Plan：下一个 loop 的最终形态（可复用 0→1 流程）

## 0. 整体认知（先于逐环节设计）

期望：整个流程是一个**完整、可复用、增量**的 loop——

```
数据收集 collect → 数据抽取 extract → 入库 ingest → 进化迭代 evolve
```

在未来**添加任意一个新材料**时都可直接走通。

### 不变量（让"完整 + 可复用"成立）

1. **以"单个材料"为单位定义流水线**（关键）：一个材料走 collect→extract→ingest→evolve。init KB = N 个材料**并行**跑 + 一次 evolve；后续新增 = 1 个材料 + 一次 **scoped** evolve。**同一套 per-material 契约**，只是 evolve 的节奏不同。→ 这正是"批处理 vs 增量"的统一：批就是"许多 per-material 并行"，所以"加单个新材料"天然可行，不需要另设一套流程。
2. **每个 stage 有明确 I/O 契约**：可组合、可独立运行 / 重跑 / 测试。
3. **源忠实 + 可溯源 + 永不删除**：每卡可溯源到材料；storage/view 分离；不 hard-delete（见 fusion_and_governance.md §4）。
4. **loop 独立**：语料只用本 loop 自己，不跨 loop。
5. **ai-native + best-effort**：agent 驱动；grep-only 召回；让问题更简单而非全解。
6. **增量成本**：加一个材料 ≈ 该材料的 extract+ingest + 一次 scoped evolve（grep 召回有界），不是 O(N)。

## 1. 各环节（逐一敲定）

### 1.0 数据收集 collect —— 暂不动 + TODO
- 现状保留。
- **TODO**：加一环——按指定 source spec（URL / repo / paper id）**获取新数据源**，把"加新材料"从手动落盘变成从 spec 抓取。（本轮不展开。）

### 1.1 数据抽取 extract（分解材料）—— 颗粒度已敲定

**I/O**：In = 一个完整 raw material（一次性全读，不防御性截断）；Out = N 张源忠实 draft 卡 + provenance。

**颗粒度 = Zettelkasten 原子卡**（从 v3 抽象而来；v3 颗粒度是可接受 baseline）：一张卡 = 一个**原子 idea**——有界、自足、可独立理解与链接、知识密集（讲出标题之外的东西）、有源证据支撑。
- **下界（别太碎）**：不复述标题；不"拆到每张卡都失去信息量"；只有和兄弟卡捆在一起才成立 → 太碎。
- **上界（别太大）**：一张卡一个有界 idea；跨多贡献 / 多机制 / 多主题 → 沿 idea 接缝拆开。
- **不做 taxonomy**：**不设预定义、互斥的分类体系**——exclusive taxonomy 是灾难，类别本就无法干净划界，且没人维护就失去意义。`card_type` 保持 v3 那样的**自由描述词**（可选、非受控网格）；六个 lens（concept / mechanism / distinction / operational_rule / source_claim / example_pattern）只是"发现不同 idea 的直觉提示"，**不是分类系统**。
- **best-effort + 治理兜底**：颗粒度在 extract 只求**大致原子**；过碎/过粗交给 evolve 治理 merge（v1 不做 split，过粗只标记待议），所以出生不必完美。
- **保证 = 把 material「耗尽（exhaust）」，不设体量校准**：知识的信息量难以量化，更不能按量化指标去拆——所以**不给数量/体量目标**。唯一要求：这份 material 承载的不同 idea 被**抽尽**（不多造、不漏抽）。「exhaust」本身是模糊概念，到此为止、**交给 agent 智能判断**——这是该技术决策背后的 assumption。

**目的性 = 面向"未来检索"的启发原则**（借鉴 deep research，适配无 query 场景；机制为提议，待确认）：
- deep research（含 STORM）抽取是 **query-conditioned**——有具体 topic/question 当 salience 函数，所以有目的性；wiki ingestion **无 query**，salience 欠定，纯自由发挥不好。
- 解法：注入**最宽口径的目的——anticipated future retrieval**，把 deep research 逻辑**反过来跑（bottom-up）**：建卡前 agent 先问"这份 material 回答了哪些、未来读者/agent 会问的问题？"，每个**值得存**的答案 = 一张原子卡。
- 收益：(1) 给方向又**不收窄**（目的是"会被问"这种宽口径，化解"目的性 vs 泛化"张力）；(2) **锐化 exhaust**——material 被耗尽 = 它有意义地回答的**每个问题都成了卡**（比"agent 觉得够了"可操作，仍由 agent 判断"哪些问题有意义"）。
- **启发原则（给原则，不给 few-shot 卡内容）**：① 目的=未来检索；② exhaust=覆盖所有有意义的潜在问题；③ 卡值得存的过滤=答案非显然/耐久/自足/有据；④ 原子性=一卡≈一问之答。
- **不用 few-shot 卡内容**：会造成领域强偏好、降低 exploration、伤泛化。若确需示例，用**跨领域**且只给"拆分形状/标题"，不给完整卡内容。

**其余 extract 机制**（unified-footnote 出生、源忠实、中文、extract 不做去重、`canonical_concept` 复用时机）见后续逐一敲定。

### 1.2 入库 ingest —— 待敲定
> 占位。

### 1.3 进化迭代 evolve —— 已单独成文
fusion + 治理 + storage/view；grep-only、best-effort、永不删除。详见 `fusion_and_governance.md`。
