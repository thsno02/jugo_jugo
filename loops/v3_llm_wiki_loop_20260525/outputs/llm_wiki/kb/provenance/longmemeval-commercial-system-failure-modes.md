---
schema: accepted_card_provenance.v3
card: ../cards/longmemeval-commercial-system-failure-modes.md
material_id: arxiv-longmemeval
digest_id: digest_arxiv-longmemeval
source_paths:
  - data/raw/arxiv/arxiv-longmemeval/agent_source_bundle.txt
draft_card: ../../drafts/cards/longmemeval-commercial-system-failure-modes.md
draft_provenance: ../../drafts/provenance/longmemeval-commercial-system-failure-modes.md
similarity_result: ../../drafts/similarity/longmemeval-commercial-system-failure-modes.json
comparison_provenance: ../../drafts/comparison/longmemeval-commercial-system-failure-modes.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:22:00+08:00
  gate_notes: 6/6 项通过；商业系统数字、ChatGPT KU 失败 + Coze IE 失败两个模式、长上下文 30-60% 掉幅、人工评分齐备。
created_time: 2026-05-26T15:21:00+08:00
edited_time: 2026-05-27T11:22:00+08:00
edited_entity: llm
---

## 源证据

- 行 156–166（`figures/proof_of_difficulty.tex` 第一个 subfigure，商业系统准确率表）：
  - Offline Reading + GPT-4o = 0.9184
  - ChatGPT + GPT-4o = 0.5773；ChatGPT + GPT-4o-mini = 0.7113
  - Coze + GPT-4o = 0.3299；Coze + GPT-3.5-turbo = 0.2474
  - Caption："ChatGPT and Coze instantiated with GPT-4o exhibits 37\% and 64\% performance drop, respectively."

- 行 175–195（`figures/proof_of_difficulty.tex` 第二个 subfigure，长上下文 LLM 表）：GPT-4o oracle 0.870 vs LongMemEval-S 0.606（-30.3%）；Llama 70B oracle 0.744 vs 0.334（-55.1%）；Phi-3 14B oracle 0.702 vs 0.380（-45.9%）等。CoN 版本类似。

- 行 1402–1412（§3.4 LongMemEval represents a significant challenge）：
  - "we randomly selected 97 questions and created a short chat history of 3-6 sessions (approximately 10x shorter than \BENCHMARK\textsubscript{\textsc{S}})."（行 1407）
  - "we found ChatGPT tended to overwrite crucial information as the chat continues, while Coze often failed to record indirectly provided user information."（行 1407）
  - "this result highlights the \textbf{gap between building a seemingly personalized chat assistant by recalling isolated facts and demonstrating a genuinely strong memory ability}."（行 1407）
  - "these LLMs showed a 30\% to 60\% performance decline when tasked with reading the entire \BENCHMARK\textsubscript{\textsc{S}} history"（行 1412）

- 行 1622–1651（Appendix B "A Human Study on Commercial Memory Chatbots" + `tab:commercial-system-detailed`）：
  - "ChatGPT generally records the evidence statements immediately after it has been presented in the evidence session. However, as the interaction proceeds, ChatGPT often modify this information when it compresses the history, resulting in information loss."（行 1629）
  - 表中按能力的细分数字（IE / MR / KU / TR）。

## 卡片范围是否成立

- 所有数字（37% / 64% / 30-60% drop，五能力分项准确率）逐字摘自论文表。
- 两类失败模式（ChatGPT 覆盖、Coze 漏抽）直接来自论文叙述。
- 把失败模式归到 KU / IE 是合理对应（KU 定义在 `longmemeval-five-core-memory-abilities`，论文未明文做"failure mode → ability"映射），属于设计解读，已在卡片标注为"对应 5 类能力里：KU/IE 失败"。
- "用 GPT-4o-mini 反而比 GPT-4o 高" 是从表数字直接看出，标为观察。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:22:00+08:00
- 检查要点：
  - source_claim 卡给出商业系统具体数字 + 两种失败模式叙述 + 长上下文对照，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-longmemeval`，正文锚到行 156-195 / 1402-1412 / 1622-1651。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 5 张相关卡。

## 备注

- 与 `longmemeval-five-core-memory-abilities` 卡互补：那张定义五能力，本卡给出两个商业系统在各能力上的失败画像。
- 与 `longmemeval-benchmark-construction-pipeline` 互补：构造卡解释了"为什么间接表达 evidence 能戳穿 Coze"。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/longmemeval-commercial-system-failure-modes.md`
- draft provenance: `../../drafts/provenance/longmemeval-commercial-system-failure-modes.md`
- similarity: `../../drafts/similarity/longmemeval-commercial-system-failure-modes.json`
- comparison provenance: `../../drafts/comparison/longmemeval-commercial-system-failure-modes.md`
