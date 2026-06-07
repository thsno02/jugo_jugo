---
id: memgpt-memory-hierarchy
title: MemGPT 两级内存层次结构
status: accepted
card_type: mechanism
tags: [LLM, memory_hierarchy, main_context, external_context, MemGPT]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt]
justification: ../justification/memgpt-memory-hierarchy.md
canonical_concept: memgpt-memory-hierarchy
aliases: [MemGPT内存层次, main context vs external context, 主上下文与外部上下文]
summary: >-
  memgpt-memory-hierarchy（MemGPT内存层次, main context vs external context）将 LLM 存储分为 main context（prompt tokens = RAM，LLM 可直接访问）和 external context（recall storage + archival storage = 磁盘，需通过函数调用显式移入），实现分层管理
related: [agent-memory-persistent-attack-surface, ai-memory-operating-system, episodic-semantic-memory-duality, lightmem-three-stage-memory, memgpt-main-context-structure, memgpt-self-directed-memory, virtual-context-management]
---

MemGPT 的 OS 类比式多层内存架构将存储分为两个主要层级 [^src-1]：

**主上下文（main context）**：对应操作系统中的主内存/物理内存/RAM。主上下文由 LLM 的 prompt tokens 构成，其中的所有信息被视为"in-context"，在 LLM 推理时可直接访问 [^src-2]。

**外部上下文（external context）**：对应操作系统中的磁盘存储。包含两种存储：
- **recall storage**（回忆存储）：消息数据库，存储所有历史消息记录
- **archival storage**（档案存储）：读写数据库，存储任意长度的文本对象

外部上下文中的数据被视为"out-of-context"，必须通过函数调用显式移入主上下文才能在推理中被访问 [^src-3]。MemGPT 通过提供函数调用接口让 LLM 处理器在不需要用户干预的情况下自主管理自己的内存 [^src-4]。LightMem 从认知心理学的 Atkinson-Shiffrin 模型出发提出了类似的分层设计，将层级细分为感觉/短期/长期三阶段，侧重效率优化而非自主管理[^card-1]。在 AI 记忆操作系统的宏观框架中，MemGPT 的设计可被视为一种具体的 OS 类比落地[^card-2]。值得注意的是，MemGPT 的分层标准是**访问距离**（in-context vs out-of-context），而 Zep 的情景-语义双存储则按**认知内容类型**划分层次，两者体现了记忆分层的不同维度[^dist-1]。从安全角度看，两级内存层次的持久化特性也创造了攻击面——投毒内容一旦写入 archival storage 即获得跨会话永久驻留能力，且 LLM 的自主函数调用检索机制使恶意载荷无需用户干预即可被激活[^card-3]。

## Footnotes

[^card-1]: [LightMem 三阶段记忆架构](lightmem-three-stage-memory.md) -- MemGPT 从 OS 类比（主内存 vs 磁盘）出发，LightMem 从 Atkinson-Shiffrin 认知模型（感觉/短期/长期）出发，构成分层记忆架构的互补设计路径
[^card-2]: [AI 记忆操作系统框架](ai-memory-operating-system.md) -- 本卡将 OS 类比用于具体的两级内存机制设计，该卡将 OS 概念提升为宏观的记忆架构分类框架
[^dist-1]: [情景记忆与语义记忆的双存储设计](episodic-semantic-memory-duality.md) -- 本卡按访问距离（in-context vs out-of-context）划分记忆层次，该卡按认知功能（情景 vs 语义）划分，两种分层标准正交互补
[^card-3]: [Agent 记忆作为持久性攻击面](agent-memory-persistent-attack-surface.md) -- 本卡描述两级内存层次的功能设计，该卡揭示该持久化架构创造的安全隐患：archival storage 的跨会话驻留 + LLM 自主检索 = 投毒内容可在未来任意相关任务中被无干预激活

[^src-1]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "MemGPT's OS-inspired multi-level memory architecture delineates between two primary memory types: main context (analogous to main memory/physical memory/RAM) and external context (analogous to disk memory/disk storage)."
[^src-2]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "Main context consists of the LLM prompt tokens---anything in main context is considered in-context and can be accessed by the LLM processor during inference."
[^src-3]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "External context refers to any information that is held outside of the LLMs fixed context window. This out-of-context data must always be explicitly moved into main context in order for it to be passed to the LLM processor during inference."
[^src-4]: `data/raw/arxiv/arxiv-memgpt/agent_source_bundle.txt` -- sections/method_rewrite.tex -- "MemGPT provides function calls that the LLM processor to manage its own memory without any user intervention."
