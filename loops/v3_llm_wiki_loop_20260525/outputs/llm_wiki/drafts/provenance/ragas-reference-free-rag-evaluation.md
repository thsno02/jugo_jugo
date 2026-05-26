---
schema: draft_card_provenance.v3
draft_card: ../cards/ragas-reference-free-rag-evaluation.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
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

本轮未运行。

## 备注

- 与 v2 现有卡片无强重叠，但与 `auto-index-replaces-rag-at-small-scale` 在"RAG 系统应该如何评估"语义上相邻；可在 comparison_provenance 阶段考虑互链。
