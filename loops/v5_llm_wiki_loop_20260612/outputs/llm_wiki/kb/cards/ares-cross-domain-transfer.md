---
id: ares-cross-domain-transfer
title: ARES 跨域迁移能力与边界
status: accepted
card_type: experimental-finding
tags:
- cross-domain
- transfer-learning
- generalizability
- rag-evaluation
- domain-shift
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-ares
evidence_basis: experimental_paper
justification: ../justification/ares-cross-domain-transfer.md
canonical_concept: ares-cross-domain-transfer
aliases:
- ARES cross-domain
- cross-domain LLM judge
- ARES generalizability
summary: ARES fine-tuned judge 在同语言同模态内跨域有效：换 query 类型（NQ→FEVER）、换文档类型（NQ→MultiRC）、或两者都换（NQ→ReCoRD）时
  Kendall's tau 维持 0.78-1.0。PPI 使用 300 标注即可在跨域场景中缓解 judge 精度下降。但跨语言（NQ→XGLUE tau=0.33）、跨模态（文本→代码
  tau=0.28）、跨任务类型（QA→实体抽取 tau=0.38）时严重退化，表明迁移边界在语言/模态边界。
related:
- ares-llm-judge-finetuning
- ares-human-preference-validation-set
- ares-real-rag-system-evaluation
---

ARES 测试了三种域迁移：换 query 类型、换文档类型、两者都换。[^src-1]

同语言同模态内迁移成功：NQ→FEVER、FEVER→NQ、NQ→MultiRC 等所有配置 Kendall's tau 维持 0.78-1.0。PPI 仅用 300 标注即可有效校正。[^src-2]

即使 judge 精度在跨域时下降，PPI 仍能缓解排序退化（如 NQ→FEVER 的 A.R. judge 精度显著下降但 PPI 维持了可用的 tau）。[^src-3]

迁移边界明确：跨语言（英语→XGLUE 多语言，tau=0.33）、跨模态（文本→代码 CodeSearchNet，tau=0.28）、跨任务类型（QA→实体抽取 T-Rex，tau=0.38）均严重失败。[^src-4]

结论：每次跨域迁移需要新的领域内段落和 few-shot 示例重新配置 ARES judge。[^src-5]

[^card-1]: [^ref→ares-llm-judge-finetuning] judge 泛化能力
[^card-2]: [^ref→prediction-powered-inference-for-rag-ranking] PPI 缓解跨域退化

[^src-1]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P887 -- "three domain shifts: change in query type...change in document type...change in both"
[^src-2]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "Tables/Cross_Domain.tex" P91-93 -- Kendall's tau 0.78-1.0 across all in-domain transfers
[^src-3]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P895-896 -- "even when the LLM judge's accuracy suffered...PPI helped mitigate the loss in accuracy"
[^src-4]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P900-903 -- "XGLUE...0.33...CodeSearchNet...0.28...T-Rex...0.38"
[^src-5]: `data/raw/arxiv/arxiv-ares/agent_source_bundle.txt` -- "results.tex" P904 -- "Each cross-domain shift requires in-domain passages and few-shot query examples for reconfiguring ARES judges"
