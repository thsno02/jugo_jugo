---
id: llm-wiki-thesis-mode
title: Thesis 驱动研究模式
status: draft
card_type: mechanism
tags: [llm-wiki, thesis-mode, claim-verification, confirmation-bias]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-thesis-mode.md
canonical_concept: thesis-driven-research
aliases: [thesis mode, thesis-driven investigation, 论文驱动研究, claim verification mode]
summary: >-
  thesis-driven-research 模式：从特定声明出发，agents 分为 supporting opposing mechanistic meta adjacent 五组平衡设计，无关源被跳过保持 wiki 精简，输出 verdict（supported/partially supported/contradicted/insufficient evidence/mixed），第二轮反确认偏差
related: [llm-wiki-parallel-multi-agent-research, llm-wiki-gap-report-iterative]
---

Thesis 模式（/wiki:research --mode thesis "<claim>"）是 llm-wiki 的声明验证研究路径。它从一个特定声明出发，将该声明用作过滤器。[^src-1]

Agents 被分为五组——supporting（支持）、opposing（反对）、mechanistic（机制）、meta/review（元分析/综述）、adjacent（相邻领域）——设计上确保平衡。与声明变量无关的源被跳过，保持 wiki 精简。[^src-2]

输出不是摘要而是裁决（verdict）：supported、partially supported、contradicted、insufficient evidence 或 mixed。[^src-3]

当使用 --min-time 时，第二轮聚焦于证据较弱的一方——作为反确认偏差的权重。[^src-4]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Thesis Mode" P305 -- "/wiki:research --mode thesis '<claim>' starts from a specific claim and uses it as a filter."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Thesis Mode" P305 -- "Agents are split across supporting, opposing, mechanistic, meta/review, and adjacent — balanced by design."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Thesis Mode" P306 -- "Output is a verdict: supported, partially supported, contradicted, insufficient evidence, or mixed."
[^src-4]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Thesis Mode" P307 -- "With --min-time, round two focuses harder on the weaker side of the evidence — counter-weight against confirmation bias."
