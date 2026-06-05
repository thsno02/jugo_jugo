# Justification: comparison-runtime-paging-vs-lifecycle-archiving

## 为什么这张卡值得独立存在

virtual-context-management 和 archive-lifecycle 都将 OS 分层存储隐喻应用于 AI 系统，但它们在粒度（消息 vs 主题）、触发方式（自动 vs 意图）、保真度（有损摘要 vs 无损保存）三个维度上的差异构成了一个独立的原子洞察：同一 OS 洞察在不同系统层面必然产生不同机制，因为运行时约束（token 压力、实时性）与生命周期约束（长期价值评估、完整性需求）根本不同。

## 来源卡片

- virtual-context-management (arxiv-memgpt): MemGPT 的 OS 虚拟内存分页机制
- memgpt-queue-eviction-policy (arxiv-memgpt): 运行时分页的具体驱逐策略
- archive-lifecycle (llm-wiki-net): LLM Wiki 的主题归档生命周期

## 区分类型

结构性对比（structural comparison）：两种机制共享"保留但静默"的设计原则，但在粒度、触发方式、保真度三个维度上系统性地不同。
