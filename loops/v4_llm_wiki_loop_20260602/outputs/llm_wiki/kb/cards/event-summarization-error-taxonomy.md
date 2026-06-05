---
id: event-summarization-error-taxonomy
title: LLM 事件摘要的五类错误分类
status: accepted
card_type: distinction
tags: [error-taxonomy, event-summarization, hallucination, speaker-attribution, agent-memory]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/event-summarization-error-taxonomy.md
canonical_concept: event-summarization-error-taxonomy
aliases: [事件摘要错误分类, LLM event summarization errors]
summary: >-
  event-summarization-error-taxonomy（事件摘要错误分类, LLM event summarization errors）LoCoMo 对 LLM 事件摘要的手动分析识别出五类主要错误：信息缺失（时序/因果连接失败）、幻觉（填充无关细节）、对话线索误读（如幽默当真）、说话者归属错误、显著性判断错误（将无关寒暄识别为重要事件）
related: [locomo-benchmark, long-context-comprehension-illusion]
---

LoCoMo 论文通过对 LLM 生成的事件摘要进行手动分析，识别出五类主要错误模式[^src-1]：

1. **信息缺失**（missing information）：模型未能建立跨长对话的时序和/或因果连接，导致关键事件细节被遗漏。例如，ground truth 为"Joanna 向电影竞赛提交了关于失去、身份和联系的第三部剧本"，模型仅输出"Joanna 向电影竞赛提交了她最近的剧本"[^src-2]。

2. **幻觉**（hallucination）：模型在事件上填充了不存在的细节或来自同一会话中不同事件的信息。例如，将"下次还想再来"的游戏派对评价与同会话的"做了素食冰淇淋"混淆为"Nate 的素食冰淇淋大受欢迎，人们下个月还想再做"[^src-3]。

3. **对话线索误读**（misunderstanding of dialog cues）：模型将幽默、讽刺等非字面表达误读为认真陈述。例如，一个说话者开玩笑说"也许我也该写剧本"，被模型当作真实意图记录[^src-4]。

4. **说话者归属错误**（speaker attribution）：事件被归属到错误的说话者。例如，Nate 邀请 Joanna 品尝无乳糖冰淇淋被反转为 Joanna 邀请 Nate[^src-5]。

5. **显著性判断错误**（saliency）：模型将无关紧要的对话（如寒暄"最近怎么样"）误判为重要生活事件[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.2" -- "we identify five broad categories of event summarization errors made by LLMs"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Missing information: Key details about event are omitted... 'Joanna submits her third screenplay on loss, identity, and connection' -> 'Joanna submits her recent screenplay'"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Hallucination: Non-existent details... 'gaming party was a great success' + 'made vegan ice cream' -> 'Nate's vegan ice cream is a huge success and people want to do it again'"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Misunderstanding of dialog cues: model confuses a light-hearted statement... 'Maybe I'll start to think of a drama myself' -> 'Nate considers writing his own drama screenplay'"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Speaker attribution: Event is attributed to the wrong speaker... 'Nate invites Joanna' -> 'Joanna invites Nate'"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table summary_errors" -- "Saliency: Unimportant interactions... 'Hey Joanna, what's been up' considered significant"
