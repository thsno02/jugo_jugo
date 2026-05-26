---
schema: draft_card_provenance.v3
draft_card: ../cards/locomo-observation-rag-beats-summary-rag.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
created_time: 2026-05-26T14:15:00+08:00
edited_time: 2026-05-26T14:15:00+08:00
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

本轮未运行。

## 备注

- 与 LongMemEval 卡片 `longmemeval-round-better-than-session` 互补：LongMemEval 的等价结论是"round > session > fact"——与 LoCoMo 的"observation > dialog > summary"在结构上一致，但 LongMemEval 使用更强 reader（GPT-4o），后续 comparison_provenance 可统一作"RAG value granularity 一般规律"。
