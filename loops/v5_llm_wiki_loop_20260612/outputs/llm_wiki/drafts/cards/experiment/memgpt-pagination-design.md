---
id: memgpt-pagination-design
title: MemGPT 分页检索防溢出机制
status: draft
card_type: mechanism
tags: [memgpt, pagination, token-constraint, retrieval-overflow, context-aware]
created_time: 2026-06-12T10:27:00+08:00
edited_time: 2026-06-12T10:27:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
evidence_basis: peer-reviewed
justification: ../justification/experiment/memgpt-pagination-design.md
canonical_concept: pagination-overflow-prevention
aliases: [分页检索, pagination, retrieval pagination, context-aware retrieval]
summary: >-
  MemGPT pagination-overflow-prevention 的检索机制感知 token 约束并实现分页，防止单次检索结果溢出上下文窗口；LLM 可通过 function chaining 翻页浏览后续结果，但翻页决策由 LLM 自主做出。
related: [memgpt-function-chaining, memgpt-document-qa-pagination, memgpt-premature-stopping]
---

MemGPT 的内存检索机制被设计为感知 token 约束（context-aware），通过 pagination 防止单次检索溢出上下文窗口：

**设计原理**：检索调用不会一次性返回所有匹配结果，而是返回分页后的有限结果集，确保追加到 FIFO queue 后不会超出上下文容量。LLM 可通过 function chaining（带 request_heartbeat=true）请求下一页结果。[^src-1]

**Figure 2 示例**：论文展示了 MemGPT 对 archival storage 执行多次搜索查询，每次获得分页结果，直到找到回答问题所需的信息。[^src-2]

**与 Document QA 的关联**：在 Document QA 任务中，MemGPT 理论上可以通过不断翻页浏览 embedding retriever 的全部排名结果——即使 gold document 排在第 20、50 甚至 100 位也能被找到。这使得 MemGPT 的有效上下文不受单次 retriever 返回数量限制。[^src-2]

然而，pagination 的设计将"是否翻页"的决策权交给了 LLM——这直接导致了 premature stopping 问题。系统没有确定性的"搜索直到找到或穷尽"逻辑，全靠 LLM 判断当前结果是否足够。此外，每次翻页需要一次完整的 LLM 推理调用，多层翻页的延迟和成本可能在实际部署中成为瓶颈。[^src-1]

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Section: Function executor -- "our memory retrieval mechanisms are designed to be cognizant of these token constraints and implement pagination to prevent retrieval calls from overflowing the context window"
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- Figure: example-docqa / Section: Multi-document QA -- "MemGPT actively retrieves documents from its archival storage (and can iteratively page through results)"
[^card-1]: -> memgpt-premature-stopping -- 本卡描述 pagination 的设计意图，该卡分析 LLM 不愿继续翻页的失败模式
[^card-2]: -> memgpt-function-chaining -- 本卡展示 pagination 依赖 function chaining 实现翻页，该卡描述 function chaining 的通用机制
