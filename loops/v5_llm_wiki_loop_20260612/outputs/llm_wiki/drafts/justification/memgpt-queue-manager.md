## Justification for memgpt-queue-manager

**Why this card**: 队列管理器是 MemGPT 内存管理的执行核心，其两阶段驱逐策略（warning + flush）是系统能持续运行而不溢出的关键机制。

**Evidence quality**: method_rewrite.tex 中有专门的 "Queue Manager" subsection，给出了具体的百分比阈值示例和完整的流程描述。

**Atomicity check**: 本卡聚焦于 queue manager 的职责和驱逐策略，不涉及函数执行器或控制流机制。
