---
schema: draft_card_provenance.v3
draft_card: ../cards/ragas-wikieval-dataset.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:200-231` —— WikiEval 段完整描述。
2. `agent_source_bundle.txt:201` —— "we first selected 50 Wikipedia pages covering events that have happened since the start of 2022"。
3. `agent_source_bundle.txt:204-211` —— ChatGPT 出题 prompt 全文。
4. `agent_source_bundle.txt:218` —— 标注者一致率数字。
5. `agent_source_bundle.txt:220-229` —— 三维度"低质量对照样本"的构造方法。
6. `agent_source_bundle.txt:297-352` —— Tables 5/6/7 样本示例。

## 卡片范围是否成立

- 卡片范围限定在 WikiEval 数据集本身（构造 / 标注 / 设计巧思 / 对后续研究者的指导），不与指标卡或框架卡重复。
- "想做 reference-free 指标研究就需要 pairwise 对照集" 是基于 WikiEval 范式的合理方法论建议。
- "改变生成过程造对照样本比从错例里挑更好" 是基于三种构造手法的归纳总结，论文未直接论述但与做法一致。

## 发表门控结果

本轮未运行。

## 备注

- 本卡 card_type 选 `example_pattern`：WikiEval 是一个具体可复用的数据集 + 构造模式，适合后续被新的 RAG 指标论文引用作为 baseline。
