---
schema: accepted_card_provenance.v3
card: ../cards/locomo-observation-rag-beats-summary-rag.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
draft_card: ../../drafts/cards/locomo-observation-rag-beats-summary-rag.md
draft_provenance: ../../drafts/provenance/locomo-observation-rag-beats-summary-rag.md
similarity_result: ../../drafts/similarity/locomo-observation-rag-beats-summary-rag.json
comparison_provenance: ../../drafts/comparison/locomo-observation-rag-beats-summary-rag.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:57:00+08:00
  gate_notes: 6/6 项通过；三粒度对比表 + SNR 解读 + 4 条操作含义 + 模型/索引成本边界齐备。
created_time: 2026-05-26T14:15:00+08:00
edited_time: 2026-05-27T10:57:00+08:00
edited_entity: llm
---

## 源证据

- 第 407-423 行（表 2，三种检索单元 × top-k 的 F1 与 recall@k）。关键数字：
  - Dialog top-25：F1 35.8 / recall 79.9
  - Observation top-5：F1 **41.4** / recall 49.6（最高 F1）
  - Observation top-50：F1 37.8（k 变大反而降）
  - Summary top-5：F1 32.5 / recall 75.1
  - Summary top-10：recall 90.7 但 F1 仅 31.5
- 第 445 行解读句（observation 优于 dialog 约 5%；summary 即使 recall 高，F1 也低）。
- 第 346 行（observation 定义为"assertions about each speaker"）。
- 第 583 行 appendix（"the model is also instructed to indicate the turn IDs that directly contribute to each observation"）。

## 卡片范围是否成立

- 三粒度的 F1/recall 数字、最优 k、"SNR ratio"解读全部直接来自表 2 与 §6.1 正文，没有跨文献综合。
- "GPT-4o 等更强 reader 曲线可能不同"是合理边界提示，论文确实只跑了 `gpt-3.5-turbo-16k` 一种 reader 在 RAG 上。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:57:00+08:00
- 检查要点：
  - operational_rule 卡给出明确规则、表格、原因与边界，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-locomo`，正文锚回 agent_source_bundle.txt 行 407-423 / 445 / 346。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 4 张相关卡。

## 备注

- 与 LongMemEval 卡片 `longmemeval-round-better-than-session` 互补：LongMemEval 的等价结论是"round > session > fact"——与 LoCoMo 的"observation > dialog > summary"在结构上一致。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/locomo-observation-rag-beats-summary-rag.md`
- draft provenance: `../../drafts/provenance/locomo-observation-rag-beats-summary-rag.md`
- similarity: `../../drafts/similarity/locomo-observation-rag-beats-summary-rag.json`
- comparison provenance: `../../drafts/comparison/locomo-observation-rag-beats-summary-rag.md`
