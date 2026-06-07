---
id: memory-extraction-update-pipeline
title: 记忆提取-更新双阶段管线
status: accepted
card_type: mechanism
tags: [agent_memory, pipeline, incremental_processing, Mem0]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/memory-extraction-update-pipeline.md
canonical_concept: memory-extraction-update-pipeline
aliases: [提取-更新管线, extraction-update pipeline, Mem0 pipeline]
summary: >-
  memory-extraction-update-pipeline（提取-更新管线 / extraction-update pipeline）Mem0 提出的增量式记忆管理架构：提取阶段将新消息对与上下文摘要合并后由 LLM 抽取候选事实；更新阶段将候选事实与已有记忆做语义比对并由 LLM 通过 tool call 决定执行 ADD/UPDATE/DELETE/NOOP 操作
related: [cross-session-continuity, extract-then-read-memory-strategy, ingest-operation, memory-crud-operation-taxonomy, memory-overwrite-vs-omission-failure, raw-vs-consolidated-memory-vulnerability]
---

Mem0 的核心架构遵循增量处理范式（incremental processing paradigm），由两个顺序阶段组成 [^src-1]：

**提取阶段（Extraction Phase）**：系统接收新消息对 $(m_{t-1}, m_t)$（通常为用户消息与助手回复），并结合两类互补上下文进行记忆抽取：(1) 数据库中的对话摘要 $S$，概括整段对话的语义内容；(2) 最近 $m$ 条消息序列，提供细粒度时间上下文。一个异步摘要生成模块独立于主管线运行，定期刷新对话摘要以避免引入处理延迟。提取函数 $\phi(P)$ 从新交换中抽取一组显著记忆（候选事实）$\Omega = \{\omega_1, \omega_2, ..., \omega_n\}$ [^src-2]。

**更新阶段（Update Phase）**：对每个候选事实 $\omega_i$，系统通过向量嵌入从数据库检索前 $s$ 条语义相似的已有记忆，然后将候选事实与检索到的记忆一起呈现给 LLM。LLM 通过函数调用（tool call）接口自行决定执行四种操作之一：ADD（新增）、UPDATE（更新）、DELETE（删除）或 NOOP（无操作）。关键设计：不使用单独的分类器，而是利用 LLM 自身的推理能力来选择合适的操作 [^src-3]。这四种操作的详细语义和判定条件见 CRUD 分类法卡[^card-2]。

实验配置中，系统使用 $m=10$ 条历史消息作为上下文参考，$s=10$ 条相似记忆用于比较分析，所有语言模型操作使用 GPT-4o-mini [^src-4]。LongMemEval 对商业系统的评估揭示了该管线要解决的两个核心失败模式——压缩覆写和间接信息遗漏[^card-1]。值得注意的是，本卡聚焦记忆的写入侧（提取与存储），而记忆系统的读取侧同样需要专门优化——先提取后阅读策略在检索后的阅读阶段带来显著收益[^card-3]。从安全视角看，提取阶段对原始文本语义的保留使管线对环境注入攻击存在脆弱性——原始轨迹记忆因完整保留观察文本（含恶意指令）而尤为脆弱，提取函数可能将恶意载荷识别为合法候选事实[^card-4]。

## Footnotes

[^card-1]: [记忆覆写与遗漏两种失败模式](memory-overwrite-vs-omission-failure.md) -- LongMemEval 诊断的覆写（ChatGPT 压缩时丢失已记录信息）和遗漏（Coze 未记录间接信息）正是 Mem0 提取-更新管线要在架构层面解决的问题
[^card-2]: [记忆 CRUD 操作分类法](memory-crud-operation-taxonomy.md) -- 本卡描述提取-更新双阶段架构，该卡详细展开更新阶段中 LLM 自主选择的四种具体操作（ADD/UPDATE/DELETE/NOOP）的语义与判定条件
[^card-3]: [先提取后阅读的记忆读取策略](extract-then-read-memory-strategy.md) -- 本卡聚焦记忆的写入侧（提取与更新管线），该卡聚焦记忆的读取侧（检索后的 CoN+JSON 阅读策略优化），两者构成记忆系统完整生命周期的互补视角
[^card-4]: [原始轨迹记忆与整合记忆的脆弱性差异](raw-vs-consolidated-memory-vulnerability.md) -- 本卡描述提取管线如何从新消息抽取候选事实，该卡揭示原始轨迹记忆因保留精确环境文本而对注入攻击更脆弱，表明提取阶段需要额外的恶意内容过滤机制

[^src-1]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "Our architecture follows an incremental processing paradigm, enabling it to operate seamlessly within ongoing conversations."
[^src-2]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "The function φ(P) then extracts a set of salient memories Ω = {ω1, ω2, ..., ωn} specifically from the new exchange while maintaining awareness of the conversation's broader context"
[^src-3]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories."
[^src-4]: `data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "we configured the system with 'm' = 10 previous messages for contextual reference and 's' = 10 similar memories for comparative analysis"
