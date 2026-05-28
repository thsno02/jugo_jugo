---
id: graphrag-global-sensemaking-pipeline
title: GraphRAG 把 RAG 改造成"全局意义建构"的两阶段流水线
status: accepted
card_type: mechanism
tags: [#graphrag, #rag, #knowledge-graph, #sensemaking]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T11:10:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
provenance_card: ../provenance/graphrag-global-sensemaking-pipeline.md
aliases: ["GraphRAG pipeline", "From Local to Global"]
related: [graphrag-self-reflection-gleaning, wikibase-item-property-snak-statement, graphrag-leiden-community-hierarchy, graphrag-context-window-8k-optimal, graphrag-adaptive-benchmark-via-personas, graphrag-root-community-token-efficiency]
---

GraphRAG（Edge et al., Microsoft Research, NeurIPS 2024）针对的是传统 vector RAG 答不出的一类问题——"What are the main themes in the dataset?"这种需要对整个语料做意义建构（sensemaking）的查询[^src1]。论文给出的解法是把流水线拆成**索引时**与**查询时**两个阶段，并在二者之间放一个"分层社群摘要"的中间产物。

**索引阶段（一次性、可离线跑完）：**

1. `Source Documents → Text Chunks`：原文档被切成固定大小的 chunk（论文实验用 600 token），chunk 越小召回越好但 LLM 调用越多。论文用一个 self-reflection gleaning 循环把"大 chunk 省 token"与"小 chunk 高召回"的优势同时拿到[^v3-1]。
2. `Text Chunks → Entities & Relationships`：用 LLM 在每个 chunk 上抽实体（名字、类型、简短描述）、抽关系（源/目标实体 + 关系描述）；可选再抽 *claims*（关于实体的可验证事实陈述）。这套四层抽象与 Wikibase 数据模型的 Item / Property / Snak / Statement 四结构在意图上有可比性[^v3-2]。
3. `Entities & Relationships → Knowledge Graph`：跨 chunk 把同一实体的多次出现合并成单节点；关系出现次数变成边权重；实体匹配在论文里用 exact string，但可换更软的匹配[^src2]。
4. `Knowledge Graph → Communities`：跑分层 Leiden 社群检测（用 graspologic 实现），得到一棵从根（C0，最大、最少）到叶的社群树[^v3-3]。
5. `Communities → Community Summaries`：自底向上为每个社群生成报告式摘要——叶社群按"节点度数优先"把 element 摘要塞进 8k 上下文；高层社群在塞不下时把子社群摘要替换掉其底层 element 摘要。

**查询阶段（map-reduce）：**

- 选定一个社群层级，把该层所有社群摘要**洗牌**后切成等长 chunk（防止信息集中而被"lost in the middle"）[^src3]；
- Map：每个 chunk 并行生成局部答案，并自评 0–100 的"是否回答了问题"分数，0 分被丢弃；
- Reduce：按分数降序把局部答案塞进新上下文，生成最终全局答案。

map-reduce 阶段统一用 8K 上下文窗口（实验确定的全局最优）[^v3-4]；评测协议本身也由论文给出（persona × task × question 自适应基准）[^v3-5]。

边界与误用：GraphRAG 不是为"What is the capital of France?"这类事实型查询设计的——评测里它在 *directness* 指标上输给 vector RAG (SS)。它的强项是 *comprehensiveness* 和 *diversity*：对 ~100 万 token 量级的播客转写和新闻语料，全局方法相对 vector RAG 在两项上的胜率分别是 72–83% 和 62–82%（p<0.001 / 0.01）[^src4]。把根级 C0 当默认索引可以同时拿到这两项胜率与极低 token 成本[^v3-6]。

## Footnotes

[^v3-1]: [graphrag-self-reflection-gleaning](graphrag-self-reflection-gleaning.md) — 索引阶段第 2 步的 chunk size + gleaning 循环细节
[^v3-2]: [wikibase-item-property-snak-statement](wikibase-item-property-snak-statement.md) — Wikibase 用 Item / Property / Snak / Statement 四结构表达实体与关系，可与 GraphRAG 的 entity / relationship / claim 抽取对照
[^v3-3]: [graphrag-leiden-community-hierarchy](graphrag-leiden-community-hierarchy.md) — 第 4–5 步的 Leiden 社群与分层摘要构造规则展开
[^v3-4]: [graphrag-context-window-8k-optimal](graphrag-context-window-8k-optimal.md) — query 阶段 8K 窗口实验与作者据此固化的全局默认
[^v3-5]: [graphrag-adaptive-benchmark-via-personas](graphrag-adaptive-benchmark-via-personas.md) — 用 persona × task × question 自适应生成全局意义建构基准
[^v3-6]: [graphrag-root-community-token-efficiency](graphrag-root-community-token-efficiency.md) — 根级 C0 以 ~2% token 成本接近全局方法效果
[^src1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — Edge et al., "From Local to Global: A GraphRAG Approach to Query-Focused Summarization"，NeurIPS 2024。摘要与 §3.1 Methods（行 671–860）
[^src2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 769、776、808、821、829（索引五步骤的小节标题）
[^src3]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 853–857（查询时 map-reduce 的三步 Prepare/Map/Reduce）；行 854："shuffled and divided into chunks ... ensures relevant information is distributed across chunks, rather than concentrated (and potentially lost) in a single context window"
[^src4]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` — 行 987–989（评测胜率与统计显著性，directness 反向结果）
