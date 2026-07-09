---
id: llm-wiki-model-quality-risk
title: LLM Wiki 模型质量风险
status: accepted
card_type: risk-factor
tags:
- llm-wiki
- model-quality
- error-propagation
- human-review
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- anthemcreation-en-guide
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-model-quality-risk.md
canonical_concept: llm-wiki-model-quality-risk
aliases:
- model quality risk
- error propagation
- weak model risk
summary: LLM wiki 模型质量风险 model-quality-risk：系统完全依赖模型质量来管理来源间矛盾。弱模型可能无标记地传播错误 (propagate errors without flagging)。缓解措施：对关键页面进行定期人工审查，尤其在前几周；agents.md 质量直接决定可靠性。
related:
- agents-md-instruction-file
- llm-wiki-scale-limitations
- llm-wiki-vs-rag-boundary
---
LLM wiki 的可靠性完全依赖于所用模型的质量 [^src-1]。

**核心风险**：弱模型 (weak model) 可能在不标记的情况下传播错误——即将来源间的矛盾信息未经识别便写入 wiki，导致错误在后续 ingestion 中累积。

**缓解建议**：
- 对关键页面进行定期人工审查 (periodic human review)
- 尤其在使用初期的前几周加强审查
- 确保 agents.md 指令文件的质量 [^card-1]

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Warning" -- "The LLM wiki relies entirely on the model's quality to manage contradictions between sources. A weak model can propagate errors without flagging them."
[^card-1]: 参见 [[agents-md-instruction-file]] 关于 agents.md 质量与系统可靠性的关系
