---
id: comparison-runtime-paging-vs-lifecycle-archiving
title: 运行时分页 vs 生命周期归档：OS 分层存储隐喻的两种落地
status: accepted
card_type: distinction
tags: [OS_analogy, tiered_storage, runtime_paging, lifecycle_archiving, MemGPT, llm-wiki]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memgpt, llm-wiki-net]
justification: ../justification/comparison-runtime-paging-vs-lifecycle-archiving.md
canonical_concept: comparison-runtime-paging-vs-lifecycle-archiving
aliases: [运行时分页vs生命周期归档, runtime paging vs lifecycle archiving]
summary: >-
  comparison-runtime-paging-vs-lifecycle-archiving（运行时分页vs生命周期归档）同一 OS 分层存储洞察在不同系统层面产生截然不同的机制：
  MemGPT 在运行时自动按 token 压力驱逐消息并生成摘要，LLM Wiki 在生命周期层面按用户意图归档整个主题并完整保留，
  区别在于粒度（消息 vs 主题）、触发方式（自动 vs 意图）、保真度（有损摘要 vs 无损保存）
related: [archive-lifecycle, memgpt-queue-eviction-policy, virtual-context-management]
  - virtual-context-management
  - archive-lifecycle
  - memgpt-queue-eviction-policy
  - ai-memory-operating-system
---

OS 分层存储（热/冷分离、按需调回）是 AI 记忆系统中反复出现的隐喻，但同一洞察在不同系统层面的落地方式存在结构性差异：

**运行时分页（MemGPT）**：虚拟上下文管理在 LLM 推理过程中实时运作[^card-1]。当 prompt tokens 达到阈值时，队列管理器自动驱逐旧消息并生成递归摘要[^card-2]。其特征为：
- **粒度**：单条消息级别
- **触发方式**：自动，由 token 压力（内存压力警告）触发
- **保真度**：有损——被驱逐消息被递归摘要压缩
- **检索方式**：通过函数调用从 recall storage 读取

**生命周期归档（LLM Wiki）**：归档生命周期作用于知识库管理的长期维度[^card-3]。用户主动将不再活跃的主题 wiki 移至冷存储。其特征为：
- **粒度**：整个主题 wiki 级别
- **触发方式**：意图驱动，由用户判断主题活跃度后决定
- **保真度**：无损——来源、文章、日志全部保留
- **检索方式**：通过显式 `--include-archived` 标记读取

这一区分揭示了 OS 类比的适用边界：在运行时上下文管理中，自动化和压缩是必要的（LLM 无法等待人工决策）；在知识库管理中，人类判断和完整保留更为重要（知识的长期价值难以自动评估）。两者的共同点——「保留但静默」的设计原则——证明 OS 分层存储的核心洞察跨层面有效，但具体机制必须因层面而异。

## Footnotes

[^card-1]: [虚拟上下文管理](virtual-context-management.md) -- 运行时分页的上层概念：借鉴 OS 虚拟内存在 LLM 上下文窗口与外部存储之间分页数据
[^card-2]: [MemGPT 队列驱逐与内存压力机制](memgpt-queue-eviction-policy.md) -- 运行时分页的具体实现：两阶段驱逐（内存压力警告 → 队列刷新 + 递归摘要）
[^card-3]: [主题归档生命周期](archive-lifecycle.md) -- 生命周期归档的具体实现：整个 topic wiki 移至 .archive/，保留但默认静默
