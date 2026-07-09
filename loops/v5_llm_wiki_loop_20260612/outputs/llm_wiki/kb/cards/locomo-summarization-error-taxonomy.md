---
id: locomo-summarization-error-taxonomy
title: LLM 事件摘要五类错误模式
status: accepted
card_type: taxonomy
tags:
- error-analysis
- event-summarization
- hallucination
- speaker-attribution
- dialog-cues
created_time: 2026-06-12 16:00:00+08:00
edited_time: 2026-06-12 16:00:00+08:00
edited_entity: llm
source_ids:
- arxiv-locomo
evidence_basis: experimental_paper
justification: ../justification/locomo-summarization-error-taxonomy.md
canonical_concept: llm-event-summarization-error-taxonomy
aliases:
- event summarization error types
- LLM 事件摘要错误分类
- summarization error taxonomy
summary: llm-event-summarization-error-taxonomy LLM 在长期对话事件摘要中的五类错误模式： (1) missing information 关键信息遗漏（未能建立长程因果/时序连接）； (2) hallucination 幻觉（补充不存在或属于不同事件的细节）； (3) misunderstanding of dialog cues 对话语用误读（混淆幽默/讽刺为认真声明）；
  (4) speaker attribution 说话人归因错误； (5) saliency 显著性误判（将闲聊误判为重要事件）。 基于 GPT-3.5-turbo 预测结果的人工分析。
related:
- locomo-event-summarization-degradation
- locomo-evaluation-framework
---

通过对 GPT-3.5-turbo 生成的事件摘要进行人工分析，论文识别出 LLM 在长期对话事件摘要中的五类主要错误模式。[^src-1]

**1. Missing information（信息遗漏）**: 模型未能在冗长对话中建立时间和/或因果连接，导致事件关键细节被遗漏。示例：ground truth 为"Joanna submits her third screenplay on loss, identity, and connection to a film contest"，预测仅为"Joanna submits her recent screenplay to a film contest"。[^src-2]

**2. Hallucination（幻觉）**: 模型补充了对话中不存在的细节，或将同一 session 中不同事件的细节混淆拼接。示例：将"gaming party success"和"made vegan ice cream"两个独立话题混为"vegan ice cream is a huge success and people want to do it again"。[^src-2]

**3. Misunderstanding of dialog cues（对话语用误读）**: 模型将轻松的玩笑或讽刺误判为认真声明。这是对话理解特有的问题，区别于一般文本摘要。[^src-2]

**4. Speaker attribution（说话人归因错误）**: 将事件归因于错误的说话人。示例："Nate invites Joanna"被错误预测为"Joanna invites Nate"。[^src-2]

**5. Saliency（显著性误判）**: 将不重要的日常寒暄（如"Hey, what's been up?"）错误地视为重要事件纳入摘要。[^src-2] [^card-1] [^card-2]

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Event Summarization Results" -- "we identify five broad categories of event summarization errors made by LLMs"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Missing information / Hallucination / Misunderstanding of dialog cues / Speaker attribution / Saliency"

[^card-1]: 与 [locomo-event-summarization-degradation] 关联——错误分类解释了摘要退化的具体机制
[^card-2]: 与 [locomo-evaluation-framework] 关联——错误分析基于事件摘要任务
