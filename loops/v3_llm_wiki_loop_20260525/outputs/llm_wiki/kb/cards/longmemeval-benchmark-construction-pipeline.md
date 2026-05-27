---
id: longmemeval-benchmark-construction-pipeline
title: LongMemEval 的"persona 属性 → 自对话 → 大海捞针拼装"构造管线
status: accepted
card_type: mechanism
tags: [#benchmark-construction, #long-term-memory, #needle-in-haystack, #synthetic-data]
created_time: 2026-05-26T15:20:00+08:00
edited_time: 2026-05-27T11:12:00+08:00
edited_entity: llm
source_ids: [arxiv-longmemeval]
provenance_card: ../provenance/longmemeval-benchmark-construction-pipeline.md
aliases: ["LongMemEval construction", "LongMemEval-S vs -M"]
related: [longmemeval-five-core-memory-abilities, longmemeval-commercial-system-failure-modes, locomo-persona-event-graph-pipeline, locomo-very-long-term-dialogue-dataset]
---

LongMemEval 之所以能在 500 道题里同时覆盖五类记忆能力，是因为它把"题目"与"对话历史"解耦：题目和 evidence 是人工撰写的、对话历史是用一个**大海捞针式（needle-in-a-haystack）拼装器**临时合成的。理解这条管线，就能理解为什么它的难度可以"自由放大"到 1.5M token。

**步骤 1：属性本体(attribute ontology)。**

人工搭建 164 个属性，分 5 大类——demographic、lifestyle、situational context、life events、belongings。lifestyle 下还有 shopping / media consumption / social media / daily routine / travel 等 8 个二级子类。这套本体覆盖"用户在 chat assistant 里实际会提到的话题"。

**步骤 2：背景生成(user background)。**

对每个属性，用 Llama 3 70B Instruct 生成一段聚焦该属性的"用户背景段落"——含多个跨日 / 周 / 月的"近期个人事实"。背景纯零样本 prompt 生成。

**步骤 3：种子题构造与人工筛改。**

LLM 基于背景段落生成若干 `(question, answer)` 候选；专家手工筛选改写——粗略**1000 题候选 → 50 题最终保留(5% 通过率)**。专家再把 answer 拆成 1 或多条"evidence statements"，若涉及时间则在此阶段绑定时间戳。

**步骤 4：evidence session(证据会话)合成。**

每条 evidence statement 用 self-chat 跑成一个独立的任务型 user-assistant 对话——关键技巧：让 user LLM **间接** 把 evidence 表达出来(不要说"我上个月买了车"，而要"帮我查查车保险"并附带提到这一事实)。约 **70% 的 session 被人工二次编辑** 以确保：
- evidence 真的出现在会话里；
- 不会泄漏其他题的 evidence；
- 时间表达自然口语化(LLM 默认偏正式)；
- 会话以自然方式结尾。

**步骤 5：大海捞针历史拼装。**

测试时把上述 evidence session **散落地塞进**一段更长的、无关的 user-AI 对话流里：
- 25% 抽自 ShareGPT，25% 抽自 UltraChat，50% 来自其他属性的 simulated session；
- 这些 distractor 与 evidence 共同 shuffle，再按顺序分配 plausible 时间戳——若 evidence 已有时间锚，则 distractor 时间戳被它约束。
- 提供两个标准长度：**LongMemEval-S ≈ 115k token / 题**，**LongMemEval-M = 500 session ≈ 1.5M token / 题**。
- 因为是合成拼装，**history 可以无限拉长**——这是它和 LoCoMo(固定 9K token)最大的差异。

**步骤 6：evidence 位置在 session 内被人工**多样化分布**——以避免"信息永远在 session 开头"导致检索作弊。论文 `fig:benchmark-basic-stats` 显示 evidence 位置在 session 中均匀分布。

**为什么这套设计能成立**：

- **题与历史解耦** 让难度可控：换 distractor 数量 / 时间跨度 / 检索模型，都不必重新出题。
- **evidence 间接表达** + **70% 人工编辑** 让数据无法靠"模式匹配关键词"过关，必须真的看懂语义。
- **拒答题(abstention)** 是从其他类型修改成 "false premise"——不是单独写的，所以分布与正常题贴近，不会让 abstention 检测器靠"题型识别"作弊。

**边界**：

- 来源混合(合成 + ShareGPT / UltraChat)使分布与真实用户行为略偏；论文 ethics 自己承认这是"研究人员所能拿到的最接近真实长对话的合成数据"。
- abstention 只有 30 道，样本小，置信区间宽。
- LongMemEval-S/M 的 115K 与 1.5M 是 fixed 提供的两个 setting，未来若需要 5M / 10M token 上限，原算法可继续扩展，但**至今没有发布**。

## References

- §3.2 Benchmark Curation 全章节：`data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt` 行 1357–1392。
- 属性本体 164 项：行 887–921(`tables/attribute_ontology.tex`)。
- evidence session 间接表达与 70% 人工编辑：行 1375–1377。
- 大海捞针拼装混合源(25/25/50)：行 1594–1599。
- LongMemEval-S/M 标准设置：行 1391("$\sim$115k tokens/question" / "500 sessions, $\sim$1.5M tokens")。
- evidence 位置均匀分布：行 944–953(`fig:benchmark-basic-stats` subfig1)。

## Footnotes

- 属性五大类："demographic information, lifestyle, situational context, life events, and belongings"(行 1570)。
- 5% 通过率："In total, approximately 1000 questions were generated for each question type, and the final yield rate is about 5\%."(行 1580)
- 间接 evidence："The user LLM is instructed to convey the evidence statement indirectly, e.g., instead of stating ``I bought a new car last month,'' it might instead ask for help about car insurance and reveal the information incidentally."(行 1375)
- 70% 人工编辑："In total, roughly 70\% of the sessions are human edited."(行 1586)
- 大海捞针类比："Our approach is analogous to the needle-in-a-haystack test (kamradt2023needle), which asks a model to retrieve brief information (the ``needle") embedded in a long document (the ``haystack")."(行 1391)
- distractor 混合："we always use the following mixture: 25\% ShareGPT, 25\% UltraChat, and 50\% simulated sessions"(行 1597)。
