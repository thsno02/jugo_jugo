---
id: compilation-gap
title: 编译鸿沟
status: accepted
card_type: 问题现象
tags:
- knowledge-compilation
- information-loss
- compression-failure
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-wicer
evidence_basis: experimental_paper
justification: ../justification/compilation-gap.md
canonical_concept: compilation-gap
aliases:
- compilation gap
- 编译差距
- knowledge compilation gap
- wiki compilation failure
summary: Compilation gap 指 LLM 编译器将原始文档蒸馏为 wiki 时的质量退化。编译器忽略压缩目标过度压缩(目标75%实际35.4%,
  目标50%实际12.2%, 目标25%实际8.2%)，丢弃关键事实。盲编译 wiki 评分 2.14-2.32 vs FC raw 3.46(17 RepLiQA
  主题, 6800 QA pairs), 灾难性失败率(score-1)达 53-60% vs 17%。根因为 compression compliance failure。
related:
- wicer-algorithm
- knowledge-compilation-paradigm
- cegar-paradigm-in-wicer
---

编译鸿沟（compilation gap）指 LLM 编译器将原始文档蒸馏为结构化 wiki 时发生的灾难性质量退化。[^src-1]

**核心问题——压缩合规失败（compression compliance failure）**：编译器系统性地忽略目标字数限制，实际压缩远超预期：
- 轻度压缩：目标 75% -> 实际 35.4%
- 中度压缩：目标 50% -> 实际 12.2%
- 激进压缩：目标 25% -> 实际 8.2%

在实际达到的压缩比（8-35%）下，编译器丢弃了过多特定事实，模型无法恢复。[^src-2]

**实验证据**（17 个 RepLiQA 主题，每主题 80 文档，6800 QA pairs）：
- Wiki-light: 质量 2.32, score-1 率 52.9%
- Wiki-moderate: 质量 2.25, score-1 率 57.1%
- Wiki-aggressive: 质量 2.14, score-1 率 60.3%
- FC raw 基线: 质量 3.46, score-1 率 17.3%

质量随压缩单调退化，所有 wiki 条件均远低于 FC raw 和 RAG 基线。Score-1 率（53-60% vs 17%）确认答案失败是因为信息"缺失"而非"找不到"。[^src-3]

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Compilation Gap" P696-703 -- "the approach breaks at scale...blind compilation fails catastrophically"
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Compilation Gap / Analysis" P755-763 -- "compression compliance failure: the compiler ignores target word counts, compressing 2x-3x beyond the requested level"
[^src-3]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- "The Compilation Gap / Results" P729-746 -- Table 3 wiki compilation results

[^card-1]: 与 [[llm-wiki-pattern]] 的矛盾：LLM Wiki 模式依赖编译质量，但盲编译系统性失败
