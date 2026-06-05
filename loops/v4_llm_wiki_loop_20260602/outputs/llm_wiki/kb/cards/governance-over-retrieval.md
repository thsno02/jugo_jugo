---
id: governance-over-retrieval
title: 治理优先于检索架构
status: accepted
card_type: source_claim
tags: [governance, rag, llm-wiki, enterprise, data-quality]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [atlan-llm-wiki-vs-rag-dynamic-20260524]
justification: ../justification/governance-over-retrieval.md
canonical_concept: governance-over-retrieval
aliases: [治理优先于检索, governance over retrieval, 治理决定结果]
summary: >-
  governance-over-retrieval（治理优先于检索 / governance over retrieval / 治理决定结果）
  Atlan 文章的核心论点：企业知识库的真正问题不是检索架构（wiki vs RAG），而是上游数据治理——
  访问控制、新鲜度、并发都是治理问题；规模决定架构，治理决定结果
related: []
---

Atlan 文章提出一个核心论点：企业 LLM 知识库的真正问题**不是检索架构问题，而是数据治理问题**[^src-1]。

"访问控制、新鲜度和并发性是治理问题，不是检索架构问题"[^src-2]。无论选择 wiki 还是 RAG，如果上游源数据是过时的、矛盾的或未受治理的，两种方案都会失败。RAG 管线的输出质量完全依赖于上游数据质量——如果源文档陈旧或未受治理，RAG 会检索并放大这些问题[^src-3]。

文章以一句话概括了整个辩论的结论：**"规模决定架构，治理决定结果"**（Scale decides the architecture, governance decides the outcome）[^src-4]。这意味着 wiki vs RAG 的选择由知识库规模决定（小规模用 wiki，大规模用 RAG），但无论选择哪种架构，最终成败取决于数据治理是否到位。

Epsilla 的分析被引述来支撑这一论点："从个人研究 wiki 到企业运营的跳跃才是真正残酷的地方。数千名员工、数百万条记录、跨团队自相矛盾的部落知识。"在未治理的数据之上构建影子 wiki 或原始 RAG 管线不会解决问题——它只是把问题重新组织成了新的格式[^src-5]。

在 agent 治理领域，确定性策略引擎提供了一种将治理原则操作化的具体机制 [^card-1]。框架无关的治理层设计进一步使治理规则可跨 20+ agent 框架统一执行 [^card-2]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L220 -- "Access control, freshness, and concurrency are governance problems, not retrieval architecture problems."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L217 -- "The real enterprise question is not wiki vs RAG: it is whether source data is trustworthy enough for either."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L314 -- "If the source documents are stale, contradictory, or ungoverned, RAG retrieves and amplifies those problems."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L415 -- "The bottom line: scale decides the architecture, governance decides the outcome"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/atlan-llm-wiki-vs-rag-dynamic-20260524/text.txt` -- L392-393 -- "Building a shadow wiki or a raw RAG pipeline on top of ungoverned data does not solve it. It reorganizes the problem into a new format."
[^card-1]: [确定性策略执行](deterministic-policy-enforcement.md) -- Microsoft 工具包通过 OPA/Rego/Cedar 等策略引擎实现确定性治理，是治理优先原则的一种技术落地路径
[^card-2]: [框架无关的治理层](framework-agnostic-governance-layer.md) -- Microsoft 将治理解耦为独立于 agent 框架的层，支持 20+ 框架的统一治理规则执行
