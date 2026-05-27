---
schema: accepted_card_provenance.v3
card: ../cards/ragas-wikieval-dataset.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragas-wikieval-dataset.md
draft_provenance: ../../drafts/provenance/ragas-wikieval-dataset.md
similarity_result: ../../drafts/similarity/ragas-wikieval-dataset.json
comparison_provenance: ../../drafts/comparison/ragas-wikieval-dataset.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；WikiEval 构造、6 条出题规则、三维度对照样本生成手法、95/90% 一致率全部回到 L200–231 与 Tables 5–7。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文给出动机、构造流程、三维度对照样本巧妙之处、与 SQuAD 区分、操作含义。
  - 知识密度：数据 + 流程 + 设计巧思 + 边界 + 给后续研究者的建议。
  - 源支撑：source_ids 含 arxiv-ragas；L201 / L204–211 / L218 / L220–229 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：6 张 Ragas / GraphRAG / ARES 相邻卡。

## 备注

- 本卡 card_type 选 `example_pattern`：WikiEval 是一个具体可复用的数据集 + 构造模式，适合后续被新的 RAG 指标论文引用作为 baseline。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragas-wikieval-dataset.md`
- draft provenance: `../../drafts/provenance/ragas-wikieval-dataset.md`
- similarity: `../../drafts/similarity/ragas-wikieval-dataset.json`
- comparison provenance: `../../drafts/comparison/ragas-wikieval-dataset.md`
