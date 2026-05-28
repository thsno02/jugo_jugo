---
id: locomo-event-summarization-five-error-types
title: LoCoMo 给 LLM 事件摘要错误划出五类——失败模式比 ROUGE 分数更可操作
status: accepted
card_type: concept
tags: [#event-summarization, #error-taxonomy, #locomo, #factuality]
created_time: 2026-05-26T15:31:00+08:00
edited_time: 2026-05-28T10:26:00+08:00
edited_entity: llm
source_ids: [arxiv-locomo]
provenance_card: ../provenance/locomo-event-summarization-five-error-types.md
aliases: ["LoCoMo summary error taxonomy", "event summarization error types"]
related: [locomo-three-task-evaluation-framework, locomo-long-context-adversarial-collapse, locomo-very-long-term-dialogue-dataset, longmemeval-commercial-system-failure-modes]
---

LoCoMo 的事件摘要任务（让模型把对话里出现的"个人事件"列出来与 ground-truth 事件图比对）不止给一个 FactScore 分数，论文 §6.2 + Appendix D.1 还人工分类了 LLM 失败模式，得到 5 个稳定的错误类型。这套分类对设计 evaluator / debug 数据集 / 训目标都比单一指标更可操作。

**五类错误（带 GPT-3.5-turbo 真实例子，见论文 `tab:summary_errors`）**：

1. **Missing information（漏信息）**——模型没把跨多 session 的因果或时间连成线，只描述了片段。
   - 例：GT = "Joanna submits her third screenplay on loss, identity, and connection to a film contest"
   - 模型 = "Joanna submits her recent screenplay to a film contest." —— 主题/序号丢了。

2. **Hallucination（幻觉）**——模型补加了对话里不存在的细节、或把另一个 event 的细节挪过来。
   - 例：GT 是"Nate 的 vegan ice cream"加上"游戏 party 大家想再办一次"，模型把两件事缝在一起 → "Nate's vegan ice cream is a huge success and people want to do it again next month."

3. **Misunderstanding of dialog cues（误读对话信号）**——模型分不清玩笑、反讽、礼貌性提议。
   - 例：Joanna 笑着说"Haha, now that would be something! ..."（明显玩笑），模型当真：模型 = "Nate considers writing his own drama screenplay."

4. **Speaker attribution（说话人错配）**——同一事件被记到错误说话人头上。
   - 例：GT = "Nate invites Joanna to try his homemade lactose-free ice cream."
   - 模型 = "Joanna invites Nate to her home to try her dairy-free ice cream recipe." —— 主客倒置。

5. **Saliency（错抓琐事当事件）**——把普通寒暄当成"重要个人事件"列入摘要。
   - 例：N 说 "Hey Joanna, what's been up since we last chatted?" —— 模型 = "Nate asks Joanna how she has been since they last talked." 显然不是 life event。

**为什么这套分类比单一分数有用**：

- ROUGE / BLEU 只衡量字面相似度，对 hallucination 与 saliency 几乎无感（生成顺畅的胡话能拿高 ROUGE）。
- FactScore 解决了"是不是事实"，但不区分"少答 vs 多答 vs 答错人"——而这三种错的修复方式完全不同：
  - missing info → 需要更长程的检索 / 更强的因果建模；
  - hallucination → 需要事实约束（如更严的 atomic-fact 抽取或约束生成）；
  - dialog cue → 需要情感 / 话语标记建模；
  - speaker attribution → 需要把"谁说" 强制结构化（如 in-context 编 ID）；
  - saliency → 需要 "salient event" 的判别器或 in-context demo。

**与 long-context LLM 现象互证**：

- **speaker attribution 错** 这个类与 `locomo-long-context-adversarial-collapse` 卡里 long-context LLM "misassigning dialogs or events to the wrong speaker" 是同一根因——注意力稀释导致 "谁" 这个维度先丢。
- **hallucination** 类与 long-context LLM 在 adversarial 上塌到 2.1% 也是同一机制的不同表现：context 越长，模型越倾向"找一个看起来像答案的句子"。

**边界**：

- 这 5 类是 GPT-3.5-turbo 在 LoCoMo 上的错误分布；换更强模型 (GPT-4 / Claude) 比例会变化，但论文未给细分数字。
- "saliency" 类隐含了"什么算 life event"的主观判断——FactScore 与人工标注都靠 GT 事件图当 oracle，但事件图本身也是 LLM 生成 + 人工编辑的产物，有 bias。

## References

- 五类错误首次列出：`data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt` 行 493。
- 完整 5 类例子表 `tab:summary_errors`：行 754–774。
- "long-context LLM 不擅用 context" 互证：行 491 + 行 444。

## Footnotes

- 五类原始定义："(1) \textbf{missing information} in events because the model fails to make temporal and/or causal connections over a lengthy conversation; (2) \textbf{hallucinations} i.e., models pad extra details that are either not present in the conversation or are part of a different event in the same session; (3) errors from \textbf{misunderstanding of dialog cues} such as humor or sarcasm is a distinctive issue with comprehension of dialogs; (4) inaccurate \textbf{speaker attributions}; and (5) insignificant dialogs that are wrongly considered as \textbf{salient} events."（行 493）
- 长上下文模型在事件摘要上反而比 4K base 差："the \textbf{long-context model does not surpass the base model}, despite its capability for extended-range reasoning facilitated by a larger context window. \texttt{gpt-3.5-turbo-16k} exhibits a decline in both precision (by 3.0\%) and recall (by 8.7\%)"——行 491。
