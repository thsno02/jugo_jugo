---
id: targeted-diagnosis-vs-generic-pinning
title: 定向诊断优于泛化固定
status: accepted
card_type: distinction
tags: [llm-wiki, wicer, ablation, diagnosis, compilation-quality]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-wicer]
justification: ../justification/targeted-diagnosis-vs-generic-pinning.md
canonical_concept: targeted-diagnosis-vs-generic-pinning
aliases: [定向诊断vs泛化固定, targeted diagnosis vs generic pinning, 诊断驱动精炼]
summary: >-
  targeted-diagnosis-vs-generic-pinning（定向诊断vs泛化固定 / targeted diagnosis vs generic
  pinning）是 WiCER 消融实验在 17 个主题上的关键发现：定向诊断（识别具体丢失事实）带来 +0.95 的
  质量提升，而泛化固定（不加区分地保留信息）仅贡献 +0.16
related: [compilation-gap, wicer-iterative-refinement]
---

WiCER 论文的消融实验（ablation）在全部 17 个主题上揭示了一个关键区分：**定向诊断（targeted diagnosis）** 是 WiCER 质量提升的主要驱动力，而非**泛化固定（generic pinning）**[^src-1]。

具体数据显示，定向诊断带来了 **+0.95** 的质量分提升，而泛化固定仅贡献了 **+0.16**[^src-2]。这意味着在迭代编译中，**识别具体被丢弃的事实**比**不加区分地试图保留所有信息**有效近 6 倍。

这一发现具有方法论意义：在 wiki 编译的质量保障中，精确的诊断探针（diagnostic probes）——能够指出"哪些特定事实被丢失了"——是不可替代的。仅仅要求 LLM "保留更多细节"或"不要丢弃信息"这类泛化指令，几乎不能改善编译质量。质量提升必须建立在对**具体丢失事实的识别**之上。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- Abstract -- "An ablation across all 17 topics confirms that targeted diagnosis (+0.95), not generic pinning (+0.16), drives the gains."
[^src-2]: `data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt` -- Abstract -- "targeted diagnosis (+0.95), not generic pinning (+0.16)"
