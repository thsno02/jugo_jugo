---
id: ragchecker-limitations
title: RAGChecker 框架局限性
status: accepted
card_type: limitation-note
tags:
- limitations
- retriever-metrics
- neutral-contradiction
- multimodal
- multilingual
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ragchecker
evidence_basis: experimental_paper
justification: ../justification/ragchecker-limitations.md
canonical_concept: ragchecker-limitations
aliases:
- RAGChecker limitations
- RAGChecker 局限性
summary: RAGChecker 存在三个已知局限：(1) retriever 诊断指标相比 generator 指标洞察力较弱，未考虑信息密度/多样性/连贯性；(2) 对 RefChecker 的 Neutral 和 Contradiction 结果不做区分，可能导致不完整评估；(3) 基准仅覆盖英文文本单模态，未涉及多语言或多模态（图像/音频）场景。
related:
- ragchecker-framework-overview
- ragchecker-retriever-metrics
- ragchecker-generator-metrics
---

RAGChecker 作者明确指出框架存在三个局限性：[^src-1]

**1. Retriever 指标洞察力有限**：检索指标仅关注 ground truth claims 的 recall 和 context precision，未能充分捕捉检索过程的复杂性。未来可开发考虑信息密度、多样性和连贯性等因素的更精细指标。[^src-1]

**2. 未区分 Neutral 和 Contradiction**：当前指标对 RefChecker 输出的 Neutral（无法判定）和 Contradiction（明确矛盾）结果同等对待。两种类型对最终回答质量的影响可能不同，未来应探索差异化权重或惩罚。[^src-1]

**3. 仅覆盖英文文本单模态**：评估基准基于现有纯文本英文数据集构建，不能完全代表 RAG 系统可应用的多模态（图像/音频）和多语言场景。[^src-1]

[^src-1]: `data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt` -- "sections/appendix_limitation.tex" -- "the diagnostic metrics for the retriever component are less insightful...the metrics proposed do not differentiate between Neutral and Contradiction checking results...the evaluation benchmark is limited to English queries and corpus"

[^card-16]: 参见 [ragchecker-retriever-metrics] 了解当前 retriever 指标的具体定义
