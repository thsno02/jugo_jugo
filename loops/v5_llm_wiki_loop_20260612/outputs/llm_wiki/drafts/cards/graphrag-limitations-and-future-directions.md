---
id: graphrag-limitations-and-future-directions
title: GraphRAG 局限性与未来方向
status: draft
card_type: limitations-and-outlook
tags: [graphrag, limitations, future-work, hybrid-rag, hallucination, drill-down, roll-up]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-graphrag]
evidence_basis: experimental_paper
justification: ../justification/graphrag-limitations-and-future-directions.md
canonical_concept: graphrag-limitations-and-future-directions
aliases: [GraphRAG limitations, GraphRAG future work, hybrid RAG, drill-down mechanism, roll-up approach]
summary: >-
  GraphRAG graphrag-limitations-and-future-directions 论文承认的局限性：仅在两个约 1M token 语料评估需更多领域验证；未比较幻觉率如 SelfCheckGPT；empowerment 混合表明抽取可能丢失引用细节。未来方向包括 hybrid RAG（embedding 匹配 + 即时社区报告生成）、roll-up 跨层级聚合、drill-down 按信息气味探索低层社区、微调 relationship extraction 保留更多细节。论文讨论 broader impacts 指出如全局答案不准确代表源数据则影响下游决策。
related: [graphrag-vs-vector-rag-results, graphrag-global-sensemaking]
---

**已知局限**:
1. **评估范围有限**: 仅在两个约 1M token 的语料上测试，需更多领域/规模的验证
2. **未评估幻觉率**: 未使用如 SelfCheckGPT 等方法比较不同条件的 fabrication rate
3. **Empowerment 薄弱**: 图索引抽取过程似乎丢失了具体引用、例证和引语——这些对帮助读者做出知情判断至关重要

**未来方向**:
1. **Hybrid RAG**: 结合 embedding-based 匹配（局部）+ just-in-time community report 生成（全局），在查询时动态生成社区报告后使用 map-reduce
2. **Roll-up**: 跨多个社区层级向上聚合信息
3. **Drill-down**: 按高层级社区摘要中的"信息气味"（information scent）向下探索低层级细节
4. **抽取 prompt 优化**: 微调实体/关系抽取 prompt 以保留更多细粒度信息

**Broader Impacts**:
- 如果生成的全局答案不能准确反映源数据，则存在误导下游 sensemaking 和决策的风险
- 系统使用应附带 AI 使用声明和输出可能存在错误的明确提示
- 相比 vector RAG，GraphRAG 实际上据材料推测能减轻这类风险：vector RAG 可能用检索到的局部事实样本虚假地呈现为全局总结

[^src-1]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Discussion" (Section 5) -- "More work is needed to understand how performance generalizes to datasets from various domains"
[^src-2]: `data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt` -- "Future work" (Section 5.2) -- "we see potential in hybrid RAG schemes that combine embedding-based matching with just-in-time community report generation"
[^card-1]: [graphrag-vs-vector-rag-results] 局限性部分回应实验结果中的不足
[^card-2]: [graphrag-global-sensemaking] 未来方向扩展核心 sensemaking 能力
