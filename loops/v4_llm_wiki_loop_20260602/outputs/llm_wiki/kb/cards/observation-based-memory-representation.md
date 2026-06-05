---
id: observation-based-memory-representation
title: 观察断言式记忆表示优于原始对话检索
status: accepted
card_type: mechanism
tags: [observation, memory-representation, RAG, agent-memory, retrieval-unit]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
justification: ../justification/observation-based-memory-representation.md
canonical_concept: observation-based-memory-representation
aliases: [observation-based memory, 观察式记忆, 断言式记忆表示]
summary: >-
  observation-based-memory-representation（observation-based memory, 观察式记忆, 断言式记忆表示）将对话轮次转化为关于说话者的断言式陈述（observations）作为检索单元，在 LoCoMo QA 中以 top-5 获得最佳 F1=41.4，优于原始对话 31.7 和摘要 29.9，因为消除了共指和对话噪声
related: [episodic-semantic-memory-duality, locomo-benchmark, memory-extraction-update-pipeline, memory-value-granularity-tradeoff, retrieval-snr-tradeoff]
---

LoCoMo 论文中提出的"观察"（observation）是一种将对话轮次转化为关于说话者的断言式陈述的记忆表示方法[^src-1]。每个对话轮次 $h_{k_j}$ 被转化为一个观察 $o_{k_j}$（平均 18.2 tokens），存入长期记忆 $\mathcal{H}_l$[^src-2]。观察本质上是关于说话者人设和生活的断言式声明，例如从"我刚领养了一只小狗"的对话中提取出"Nate 领养了一只新的小狗"。

在 RAG 实验中，以观察作为检索单元的效果显著优于原始对话和会话摘要。观察 top-5 的整体 QA F1=41.4，而原始对话 top-5 仅 31.7，不使用检索的基线为 22.4[^src-3]。观察在时序推理类问题上的优势尤为突出（41.9 vs. 对话 21.3 vs. 摘要 26.9）[^src-4]。

会话摘要虽然检索召回率最高（top-10 达 90.7%），但 QA 性能最低（32.5），说明摘要过程中的信息损失反而降低了答题精度[^src-5]。这表明记忆表示的语义密度和检索精度比检索召回更重要。Zep 的情景-语义双存储设计从理论层面解释了为何这种提取有效——它对应人类记忆中从情景记忆到语义记忆的自然转化[^card-1]。LongMemEval 的粒度实验提供了对照视角：同样是将对话分解为更细粒度，事实级压缩因信息丢失反而损害性能，唯有跨会话推理受益[^card-2]。两者的差异揭示了关键区分：观察提取是澄清性转化，而非有损压缩。

## Footnotes

[^card-1]: [情景记忆与语义记忆的双存储设计](episodic-semantic-memory-duality.md) -- LoCoMo 的 observation 提取实证验证了 Zep 双存储设计的理论预期：从原始事件（情景记忆）提取断言式陈述（语义记忆）能显著提升检索效果
[^card-2]: [记忆存储粒度权衡](memory-value-granularity-tradeoff.md) -- 本卡展示断言式观察优于原始对话（F1 41.4 vs 31.7），该卡展示轮次级存储优于会话级但事实级压缩反而损害性能，共同揭示记忆粒度的最优点取决于转化方式是否保留信息

[^src-1]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 3.3" -- "a single turn of the conversation h_{k_j} is transformed into an observation o_{k_j} and then stored in the long-term memory"
[^src-2]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table dataset_statistics" -- "Avg. # tokens. observation o_{k_j} of turn j in session k: 18.2"
[^src-3]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.1" -- "There is a noticeable 5% improvement with gpt-3.5-turbo when the input is top 5 relevant observations instead of pure conversation logs"
[^src-4]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Table 3" -- "Observation top-5: Temporal=41.9 vs Dialog top-5: Temporal=21.3"
[^src-5]: `data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` -- "Section 6.1" -- "using session summaries as context does not significantly improve the performance despite high recall accuracies, likely due to loss of information during the conversion of dialogs to summaries"
