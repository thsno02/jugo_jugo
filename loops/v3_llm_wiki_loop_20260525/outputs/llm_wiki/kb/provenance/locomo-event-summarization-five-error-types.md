---
schema: accepted_card_provenance.v3
card: ../cards/locomo-event-summarization-five-error-types.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
draft_card: ../../drafts/cards/locomo-event-summarization-five-error-types.md
draft_provenance: ../../drafts/provenance/locomo-event-summarization-five-error-types.md
similarity_result: ../../drafts/similarity/locomo-event-summarization-five-error-types.json
comparison_provenance: ../../drafts/comparison/locomo-event-summarization-five-error-types.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:46:00+08:00
  gate_notes: 6/6 项通过；五类错误定义 + GPT-3.5 例子 + long-context 互证 + 边界齐备。
created_time: 2026-05-26T15:31:00+08:00
edited_time: 2026-05-27T10:46:00+08:00
edited_entity: llm
---

## 源证据

- 行 493（§6.2 Event Summarization Task）：
  - "From a manual analysis of predicted summaries, we identify five broad categories of event summarization errors made by LLMs: (1) \textbf{missing information} in events because the model fails to make temporal and/or causal connections over a lengthy conversation; (2) \textbf{hallucinations} i.e., models pad extra details that are either not present in the conversation or are part of a different event in the same session; (3) errors from \textbf{misunderstanding of dialog cues} such as humor or sarcasm is a distinctive issue with comprehension of dialogs; (4) inaccurate \textbf{speaker attributions}; and (5) insignificant dialogs that are wrongly considered as \textbf{salient} events. See examples in Table~\ref{tab:summary_errors} in the Appendix."

- 行 754–774（Appendix D `tab:summary_errors`）：完整 5 行例子表，每行有"Error Type / Explanation / Ground truth event 或 relevant dialogs / Predicted event"四列。所有引用的例子（Joanna screenplay、Nate vegan ice cream、guitar party "haha"、Nate→Joanna ice cream attribution、"how's it been since we last chatted"）均逐字摘自此表。

- 行 491（同节正文）：
  - "$\texttt{gpt-3.5-turbo-16k}$ exhibits a decline in both precision (by 3.0\%) and recall (by 8.7\%) compared to $\texttt{gpt-3.5-turbo}$ which has a 4K context window. This suggests that \textbf{long-context models may not be proficient at utilizing their context appropriately}"

- 行 444（§6.1 QA 结果解读，提供 speaker attribution 跨任务佐证）：
  - "they are especially prone to misassigning dialogs or events to the wrong speaker"

## 卡片范围是否成立

- 5 类错误的命名、释义、例子完全来自论文 §6.2 + Appendix D。
- "为什么这套分类比单一分数有用" 是合理设计解读，给出针对每类错误的修复方向——这部分是引申，没有声称是论文断言。
- "与 long-context LLM 现象互证" 把 §6.1 与 §6.2 串起来，引用都是论文显式段落。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:46:00+08:00
- 检查要点：
  - 五类错误一一列出且各配例子，非标题复述。
  - 知识密度合格：分类 + 例子 + 工程解读 + 长上下文互证 + 边界。
  - source_ids 含 `arxiv-locomo`，正文锚回 agent_source_bundle.txt 行 493 / 754-774 / 491 / 444。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 4 张相关卡。

## 备注

- 与 `locomo-long-context-adversarial-collapse` 卡可互相引用：speaker attribution 错的同一根因在两张卡里都被点出。
- 与 `locomo-three-task-evaluation-framework` 卡互补：那张卡说"用 FactScore 替代 ROUGE"，本卡说"FactScore 之上还要划分 5 类失败模式"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/locomo-event-summarization-five-error-types.md`
- draft provenance: `../../drafts/provenance/locomo-event-summarization-five-error-types.md`
- similarity: `../../drafts/similarity/locomo-event-summarization-five-error-types.json`
- comparison provenance: `../../drafts/comparison/locomo-event-summarization-five-error-types.md`
