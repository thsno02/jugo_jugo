---
id: long-context-recall-vs-safety-alignment
title: 长上下文召回能力与安全对齐的区分诊断
status: draft
card_type: diagnostic-method
tags: [long-context, needle-in-haystack, safety-alignment, recall-test, agent-security]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
evidence_basis: experimental_paper
justification: ../justification/long-context-recall-vs-safety-alignment.md
canonical_concept: long-context-recall-vs-safety-alignment
aliases: [long context recall test, 长上下文召回测试, recall vs alignment diagnostic, needle-in-haystack diagnostic]
summary: >-
  eTAMP 论文设计长上下文召回测试以区分模型对注入攻击的"免疫"是源于安全对齐还是上下文处理限制。直接要求模型从完整 Task A 轨迹中提取隐藏恶意 URL。结果：GPT-5.2/Qwen3-VL-32B 100% 召回、Qwen2.5-VL-72B 98.9%——这些模型的攻击抵抗可归因于安全对齐。GPT-OSS-120B 仅 6.7%、GPT-5-mini 42.5%——其免疫部分为 needle-in-haystack 失败（偶然性防御）。低 ASR+低召回=偶然免疫；低 ASR+高召回=有意抵抗。
related: []
---

为解释为何某些模型对 eTAMP 免疫，论文设计了长上下文召回诊断测试：直接要求模型在完整 Task A 轨迹（含毒观察）中定位并提取隐藏的恶意 URL。[^src-1] [^card-1]

诊断结果揭示三档能力：
- **高召回(>=98.9%)**: GPT-5.2(100%)、Qwen3-VL-32B(100%)、Qwen2.5-VL-72B(98.9%)——能可靠定位隐藏指令，其攻击抵抗可更确信地归因于安全对齐
- **中召回(42.5%)**: GPT-5-mini——部分上下文处理限制，攻击失败混合了召回失败和潜在安全行为
- **极低召回(6.7%)**: GPT-OSS-120B——严重 needle-in-haystack 失败，其似乎的"免疫"主要是偶然性的（incidental），源于无法处理长上下文而非鲁棒对齐

核心诊断原则：低 ASR_B + 低召回 = 偶然防御（上下文限制）；低 ASR_B + 高召回 = 有意抵抗（安全对齐）。[^src-2]

[^src-1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Long Context Recall Test" P1 -- "To diagnose whether a model's immunity to prompt injection stems from inability to recall the injected instruction versus refusal to follow it"
[^src-2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` -- "Appendix: Long Context Recall Interpretation" P3 -- "a low ASR_B combined with low recall suggests the defense is incidental... while low ASR_B with high recall suggests intentional resistance"

[^card-1]: -> model-capability-security-disconnect
