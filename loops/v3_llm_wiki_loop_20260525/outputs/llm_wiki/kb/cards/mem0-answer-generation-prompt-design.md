---
id: mem0-answer-generation-prompt-design
title: Mem0 的"答案生成 prompt"把时间换算与冲突仲裁写成显式指令
status: accepted
card_type: operational_rule
tags: [#memory, #mem0, #prompt-engineering, #temporal-reasoning, #llm-instruction]
created_time: 2026-05-26T15:10:00+08:00
edited_time: 2026-05-28T10:58:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
provenance_card: ../provenance/mem0-answer-generation-prompt-design.md
aliases: [Mem0 results prompt, mem0 time normalization prompt, mem0 contradiction policy]
related: [mem0-extract-update-pipeline, mem0-locomo-benchmark-evaluation, mem0-tool-call-add-update-delete-noop, longmemeval-chain-of-note-and-json-reading]
---

## 为什么要单独看"答案生成 prompt"

很多对 Mem0 的描述只讲"检索什么"或"存什么"。但论文附录的 *Prompt Template for Results Generation*[^src1] 显示：决定 Mem0 在 **temporal** 题上能从 21.71（OpenAI）拉到 55.51 J 分的关键[^v3-1]，不只是存了带时间戳的记忆，而是**在生成时强制 LLM 做时间换算 + 冲突仲裁**——这两步本来该模型自己想，被 Mem0 显式写进了 prompt。这一点与 LongMemEval 强调的 reading 阶段 Chain-of-Note 是同质的方法论选择[^v3-2]。

## 上下文结构

每次问答 Mem0 都把：

- 两位说话人的**全部已检索 memories**（按 speaker 分块，每条带时间戳）
- 用户当前问题

按固定模板拼成 prompt 喂给 GPT-4o-mini，并强制 LLM 走一段固定的"思考流程"。

## prompt 的六条硬约束（指令段）

附录列出的指令段实际包含六条带编号的硬性规则：

1. **逐 memory 扫描**：要求模型先逐条分析所有相关记忆，再下结论；
2. **时间戳优先**：明确说"pay special attention to the timestamps to determine the answer"；
3. **直接证据原则**：若问题是事件或事实，必须在 memories 里找到直接证据；
4. **冲突仲裁规则**："If the memories contain contradictory information, **prioritize the most recent memory**" —— 这是 Mem0 base 的去冲突立场（与 Mem0g 的"标记 invalid 保留时序"不同）；
5. **相对时间换算**：对"last year / two months ago"等相对引用，必须**结合 memory 时间戳算出绝对时间再回答**，并显式举例（4 May 2022 的 memory 里说"last year" → 2021）；
6. **角色与用户分离**：明确禁止把"memories 里被提到的人名"与"创建这些 memories 的真实用户"混淆——这是多 speaker 对话场景的典型陷阱。

最后再额外加一条：**答案长度 ≤ 5–6 个词**——把 LLM 拉回 LOCOMO 评测期望的短答案分布。

## "Think step by step" 段

prompt 还附带一段 *APPROACH* 七步链：先找相关 memory → 看时间戳 → 找显式日期/地点/事件 → 若需计算就 *show your work* → 写下精确简洁答案 → 检查答案是否对题 → 确认无模糊时间引用。

这是把 chain-of-thought 锁定到"先时间核算、再回答"上，避免 LLM 直接给一个含糊的相对时间答案。

## Mem0g 版的差异

Mem0g 的答案生成 prompt 复用 Mem0 base 的前 6/7 条，**只多一条**：在第 5 步插入"Analyze the knowledge graph relations to understand the user's knowledge context"[^src3]，并在 prompt 末尾把每个 speaker 的 `{speaker_X_graph_memories}` 关系字段并排放进上下文。其它指令完全一致——这意味着图结构带来的提升来自**额外的关系上下文**，而不是新的推理 protocol。详见 Mem0g 图变体卡[^v3-3]。

## 操作含义

- 若打算复刻 Mem0 的 temporal 指标，**不能省去这两段指令**——只把"带时间戳的 memory"塞给裸 LLM，温度调到 0，也未必有 55.51 J 分。
- "prioritize the most recent memory" 是一条**基于时间戳的去冲突 heuristic**，假设记忆库时间戳可信；若上游存储时间戳缺失（OpenAI ChatGPT 的失败案例），整套机制塌掉——这解释了 OpenAI temporal J 21.71 vs Mem0 55.51 的差距并不全在"会不会存"，而在"生成时能不能用"。
- **答案 ≤ 5–6 词**[^src4] 是 LOCOMO 评测下的特化约束；做开放回答场景需要重新调整这一条，否则会让 LLM 漏掉合理的解释空间。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/appendix.tex` 第 762–828 行（*Prompt Template for Results Generation (Mem0)*）+ 第 720–759 行（*LLM as a Judge prompt* 改编自 MemGPT）。
[^src2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `appendix.tex` 第 783–788 行 — "If there is a question about time references (like 'last year', 'two months ago', etc.), calculate the actual date based on the memory timestamp. For example, if a memory from 4 May 2022 mentions 'went to India last year,' then the trip occurred in 2021."；第 780 行 — "If the memories contain contradictory information, prioritize the most recent memory."；第 790–791 行 — "Focus only on the content of the memories from both speakers. Do not confuse character names mentioned in memories with the actual users who created those memories."
[^src3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `sections/appendix.tex` 第 831–883 行（Mem0g 版 prompt）+ 第 849 行 — "Analyze the knowledge graph relations to understand the user's knowledge context."
[^src4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` — `appendix.tex` 第 793 行 — "The answer should be less than 5-6 words."
[^v3-1]: [mem0-locomo-benchmark-evaluation](mem0-locomo-benchmark-evaluation.md) — temporal 55.51 vs OpenAI 21.71 的整体数字背景。
[^v3-2]: [longmemeval-chain-of-note-and-json-reading](longmemeval-chain-of-note-and-json-reading.md) — 同属"reading 阶段强 prompt"思路。
[^v3-3]: [mem0-graph-memory-variant](mem0-graph-memory-variant.md) — Mem0g 图变体的全部设计。
