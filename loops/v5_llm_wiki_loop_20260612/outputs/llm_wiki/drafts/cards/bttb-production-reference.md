---
id: bttb-production-reference
title: Beyond the Token Bottleneck 生产参考实现
status: draft
card_type: project-instance
tags: [llm-wiki, production-implementation, obsidian, latent-reasoning, latent-communication]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
evidence_basis: practitioner_report
justification: ../justification/bttb-production-reference.md
canonical_concept: bttb-production-reference
aliases: [BTTB, Beyond the Token Bottleneck, CompleteTech wiki]
summary: >-
  Beyond the Token Bottleneck (bttb-production-reference) 是 CompleteTech 团队对 Karpathy LLM Wiki 模式的生产级实现，面向潜空间推理与潜通信前沿。规模：27 源 (26 论文 + 1 开源项目, 2022.12-2026.04)、120+ wiki 页面、1400+ 内部链接、13 研究组档案、9 MoC、9 分析页。可作为 Obsidian vault 打开。分拆许可 Apache 2.0 (code) + CC-BY 4.0 (content)。
related: [llm-wiki-pattern, llm-wiki-three-layer-architecture, llm-wiki-ingest-loop]
---

Beyond the Token Bottleneck (BTTB) 是 CompleteTech-LLC-AI-Research 对 Karpathy LLM Wiki 模式的生产级参考实现，应用于潜空间推理与智能体间潜通信这一单一活跃研究领域。[^src-1]

规模指标：[^src-2]
- 27 个源（26 篇论文 + 1 个开源项目，2022.12–2026.04）
- 120+ wiki 页面
- 1400+ 内部链接
- 13 个研究组实体档案
- 9 个 Maps of Content（导读路径）
- 9 个分析/综合页

工作流层 (workflows/) 包含维护 playbooks：create（ingest/batch-ingest/synthesize）、enrich（enrich/expand）、audit（gap-analysis/verification/lint/plugin-audit/schema-self-audit）、query、meta。[^src-3]

许可：Apache 2.0（代码：workflows/scripts/schema）+ CC-BY 4.0（内容：wiki 本身）。Vault 可在 Obsidian 中直接打开。[^src-4]

[^card-1]: 参见 [llm-wiki-pattern] 了解底层方法论
[^card-2]: 参见 [llm-wiki-three-layer-architecture] 了解架构分层

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Opening" P2 -- "Beyond the Token Bottleneck...is a production implementation of Karpathy's pattern, applied to a single live research domain."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "How Karpathy's pattern shows up in the build" P17 -- "wiki/— 120+ pages...1400+ internal links"
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "How Karpathy's pattern shows up in the build" P19 -- "workflows/— maintainer playbooks: create(ingest, batch-ingest, synthesize), enrich(enrich, expand), audit(gap-analysis, verification, lint, plugin-audit, schema-self-audit), query, meta."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/markdown.md` -- "Licensing" P29 -- "The repo is split-licensed: Apache 2.0 for code (workflows, scripts, schema), CC-BY 4.0 for content (the wiki itself)."
