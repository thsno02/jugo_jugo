---
schema: accepted_card_provenance.v3
card: ../cards/ragas-reference-free-rag-evaluation.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragas-reference-free-rag-evaluation.md
draft_provenance: ../../drafts/provenance/ragas-reference-free-rag-evaluation.md
similarity_result: ../../drafts/similarity/ragas-reference-free-rag-evaluation.json
comparison_provenance: ../../drafts/comparison/ragas-reference-free-rag-evaluation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；reference-free 动机、三维度定义、judge LLM 风险、长 context 上 CR 弱等论述均回到 L87 / L119–120 / L238–244 / L271。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:87-90` —— Abstract："we put forward a suite of metrics which can be used to evaluate these different dimensions without having to rely on ground truth human annotations."
2. `agent_source_bundle.txt:98` —— LlamaIndex / Langchain 集成声明。
3. `agent_source_bundle.txt:119-120` —— 三指标的直观定义。
4. `agent_source_bundle.txt:238-244` —— Table 1 三指标 accuracy 数字：Ragas 0.95 / 0.78 / 0.70；GPT Score 0.72 / 0.52 / 0.63；GPT Ranking 0.54 / 0.40 / 0.52。

## 卡片范围是否成立

- 卡片定位为"框架级"概念卡，三个指标卡片（faithfulness / answer relevance / context relevance）单独成片，避免本卡过载。
- "judge LLM hallucination 会传染" 与 "AR 高且 F 低则可能完整但错" 是基于指标定义的合理风险声明，论文未直接列出但属合理边界。
- "Context Relevance 在长 context 上是最弱维度" 直接来自论文实验讨论 line 271。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文给出框架定位、动机、三维度、关键设计选择、边界，多段 substantive。
  - 知识密度：概念 + 设计 + 数字 + 边界全覆盖。
  - 源支撑：source_ids 含 arxiv-ragas；L87 / L119 / L238 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：7 张同源 / 跨论文姊妹卡。

## 备注

- 与 v2 现有卡片无强重叠，但与 `auto-index-replaces-rag-at-small-scale` 在"RAG 系统应该如何评估"语义上相邻；可在 comparison_provenance 阶段考虑互链。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragas-reference-free-rag-evaluation.md`
- draft provenance: `../../drafts/provenance/ragas-reference-free-rag-evaluation.md`
- similarity: `../../drafts/similarity/ragas-reference-free-rag-evaluation.json`
- comparison provenance: `../../drafts/comparison/ragas-reference-free-rag-evaluation.md`
