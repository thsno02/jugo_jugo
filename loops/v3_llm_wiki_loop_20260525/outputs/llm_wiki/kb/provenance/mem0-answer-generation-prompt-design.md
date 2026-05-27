---
schema: accepted_card_provenance.v3
card: ../cards/mem0-answer-generation-prompt-design.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
draft_card: ../../drafts/cards/mem0-answer-generation-prompt-design.md
draft_provenance: ../../drafts/provenance/mem0-answer-generation-prompt-design.md
similarity_result: ../../drafts/similarity/mem0-answer-generation-prompt-design.json
comparison_provenance: ../../drafts/comparison/mem0-answer-generation-prompt-design.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:45:00+08:00
  gate_notes: 6/6 项通过；六条硬约束 + APPROACH 七步 + Mem0g 差异 + 操作含义齐备。
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-27T11:45:00+08:00
edited_entity: llm
---

## 源证据

1. `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` 第 765–769 行（appendix Results Generation prompt 头部）：

> "You are an intelligent memory assistant tasked with retrieving accurate information from conversation memories. ... You have access to memories from two speakers in a conversation. These memories contain timestamped information that may be relevant to answering the question."

2. 同文件第 774–793 行（六条指令段 + 答案长度约束），关键引文：

> "2. Pay special attention to the timestamps to determine the answer"
> "4. If the memories contain contradictory information, prioritize the most recent memory"
> "5. If there is a question about time references (like 'last year', 'two months ago', etc.), calculate the actual date based on the memory timestamp. For example, if a memory from 4 May 2022 mentions 'went to India last year,' then the trip occurred in 2021."
> "8. The answer should be less than 5-6 words."

3. 同文件第 832–882 行（Mem0g 版 prompt）：模板首行直接写 "(same as previous)"，正文只新增一步 "5. Analyze the knowledge graph relations to understand the user's knowledge context"，并在底部加入 `{speaker_1_graph_memories}` / `{speaker_2_graph_memories}` 字段。

4. 同文件第 711 行（LLM judge prompt 头）：

> "In developing our LLM-as-a-Judge prompt, we adapt elements from the prompt released by [MemGPT]."

—— 表明 Mem0 不只是借用 MemGPT 的 judge prompt，并且自己设计了独立的 Results Generation prompt（即本卡讨论对象）。

5. 同文件第 1212 行（result.tex 对 OpenAI temporal 失败的归因，证明"时间戳显式利用"对 temporal J 的关键性）：

> "OpenAI notably underperforms, with scores below 15%, primarily due to missing timestamps in most generated memories despite explicit prompting in the OpenAI ChatGPT to extract memories with timestamps."

## 卡片范围是否成立

本卡聚焦"答案生成阶段的 prompt 设计"，与已有 `mem0-extract-update-pipeline`（讲提取与更新）、`mem0-locomo-benchmark-evaluation`（讲结果数字）、`mem0-tool-call-add-update-delete-noop`（讲 update 阶段的 LLM 决策）都不重叠。本卡的核心主张是：

- Mem0 的 results-generation prompt 是**显式的、模板化的、强制 LLM 做时间换算与最近优先冲突仲裁**——这一点直接由附录中的 prompt 全文佐证。
- "最近优先" 的去冲突策略与 Mem0g "标记 invalid 保留时序" 的策略形成对照——这是本卡引申，但有 §3.1 update 阶段与 §3.2 conflict resolution 的对比作为依据。
- "答案 ≤ 5–6 词"是 LOCOMO-specific 的约束（直接来自 prompt 文本），用以解释为何 LOCOMO 报告下的 Mem0 答案分布偏短。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:45:00+08:00
- 检查要点：
  - operational_rule 卡列出 prompt 六硬约束 + 七步 APPROACH + Mem0g 差异，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-mem0`，正文锚到附录 762-883 行 / 1212 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 4 张相关卡。

## 备注

- 与 v2 已有卡片不重叠（v2 中 Mem0 类卡片以"两层记忆"为主，未涉及 results-generation prompt）。
- 若未来需要做 prompt-vs-architecture 消融，可与 MemGPT 的 K/V agent persona prompt 合并到 "prompt 起调度作用" 这一更高层 distinction。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/mem0-answer-generation-prompt-design.md`
- draft provenance: `../../drafts/provenance/mem0-answer-generation-prompt-design.md`
- similarity: `../../drafts/similarity/mem0-answer-generation-prompt-design.json`
- comparison provenance: `../../drafts/comparison/mem0-answer-generation-prompt-design.md`
