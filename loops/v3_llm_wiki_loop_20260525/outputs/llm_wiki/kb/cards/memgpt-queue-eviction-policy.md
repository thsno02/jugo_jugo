---
id: memgpt-queue-eviction-policy
title: MemGPT 用"警告水位—溢出—递归摘要"三段策略管 FIFO 队列驱逐
status: accepted
card_type: operational_rule
tags: [#memgpt, #queue-manager, #context-overflow, #recursive-summarization]
created_time: 2026-05-26T11:30:00+08:00
edited_time: 2026-05-28T11:04:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
provenance_card: ../provenance/memgpt-queue-eviction-policy.md
aliases: [memory pressure warning, queue flush, recursive summary system message]
related: [memgpt-main-vs-external-context, memgpt-function-chaining-heartbeat, memgpt-virtual-context-os-analogy, lightmem-light2-topic-aware-stm, memory-as-metabolism-five-operations]
---

MemGPT 把"上下文要溢出怎么办"做成一条**显式的、双水位、对 LLM 可见**的驱逐策略，由 queue manager 执行[^src1]：

1. **正常态**：每来一条消息，queue manager 把它 append 到 FIFO 队尾，并**同时写入 recall storage** 一份永久副本；触发 LLM inference，把生成的输出也写进 recall。
2. **warning token count 水位（论文示例 ≈ 70% 上下文）**：queue manager 向队列**插入一条系统消息**告诉 LLM "memory pressure"[^src2] ——这是"主动告警"，让 LLM 有机会先调函数把 FIFO 里它认为重要的事实搬到 working context 或 archival storage[^v3-1]。这一步关键：驱逐前 LLM 有机会"自救"。
3. **flush token count 水位（论文示例 ≈ 100% 上下文）**：queue manager 真正驱逐——按"一次驱多少"（论文示例 50% 上下文）取出一批 FIFO 消息，**结合现有 recursive summary 与被驱逐消息生成新的 recursive summary**[^src3]，写回到 FIFO 第一条系统消息槽位。被驱逐消息仍在 recall storage 里随时可被函数检索回来[^src4]。

为什么这样设计：
- **两段式水位**避免"突然失忆"：LLM 在 warning 水位还有窗口主动把"用户的口味偏好"这类高价值事实搬到 working context（prompt-resident），不至于在 flush 后等到下次再 retrieve；
- **递归摘要而非丢弃**：第一条永远是当前所有历史的 lossy 摘要，保证 LLM 即使没主动 retrieve 也能看到大致脉络；
- **recall storage 是无损副本**：flush 不会真的丢消息，只是从 in-context 退到 out-of-context，仍可寻回。
- 这条"按 token 阈值触发批量整合"的思路与 LightMem Light2 的 STM 阈值 `th` 在动机上一致[^v3-2]；与 memory-as-metabolism 的 CONSOLIDATE 周期化处理也是同类[^v3-3]。

操作含义/工程提示：
- 警告水位的具体百分比是可调的；论文给的"70% / 100%"是默认；
- 一次 flush 的驱逐数量也是可调（50% 上下文是一个折中：驱多了 lossy 摘要过粗，驱少了短期内反复触发 flush）；
- "递归摘要"使用 LLM 调用本身——意味着 flush 是一次额外推理，有延迟代价；
- 这个机制是 MemGPT 之所以能让对话"无限延展"的工程基础——不是模型变了，而是**驱逐是有警告、有摘要、有备份**的。

边界与误用：
- 警告水位若设得过高（接近 flush），LLM 来不及反应就被强制 flush；若过低，频繁告警污染 prompt；
- recursive summary 是 lossy 的，长时间运行后**会产生"摘要漂移"**——这是 MemGPT 设计中明确接受的代价，靠 working context 与 archival 双兜底。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — method 行 1644–1648（§Queue Manager）— 队列管理器、警告水位、flush 与递归摘要的完整描述。
[^src2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — 行 1648 — "When the prompt tokens exceed the 'warning token count' of the underlying LLM's context window (e.g. 70% of the context window), the queue manager inserts a system message into the queue warning the LLM of an impending queue eviction (a 'memory pressure' warning) to allow the LLM to use MemGPT functions to store important information contained in the FIFO queue to working context or archival storage."
[^src3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — 行 1648 — "When the prompt tokens exceed the 'flush token count' (e.g. 100% of the context window), the queue manager flushes the queue ... evicts a specific count of messages (e.g. 50% of the context window), generates a new recursive summary using the existing recursive summary and evicted messages."
[^src4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` — 行 1648 — "the evicted messages are no longer in-context and immediately viewable to the LLM, however they are stored indefinitely in recall storage and readable via MemGPT function calls."
[^v3-1]: [memgpt-main-vs-external-context](memgpt-main-vs-external-context.md) — working context 与 archival storage 是 LLM 自救的两个目标位置。
[^v3-2]: [lightmem-light2-topic-aware-stm](lightmem-light2-topic-aware-stm.md) — LightMem STM 阈值 th 是同类"缓冲触发"思路。
[^v3-3]: [memory-as-metabolism-five-operations](memory-as-metabolism-five-operations.md) — CONSOLIDATE 把整合周期化的同类设计。
