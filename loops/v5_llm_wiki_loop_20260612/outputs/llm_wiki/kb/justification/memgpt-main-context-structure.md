## Justification for memgpt-main-context-structure

**Why this card**: 主上下文的三段式划分是 MemGPT 区别于普通 prompt engineering 的关键设计，定义了 LLM 处理器实际"看到"的信息的组织方式。

**Evidence quality**: method_rewrite.tex 中以专门的 subsection "Main context (prompt tokens)" 详细描述，给出三段的名称、权限和用途。

**Atomicity check**: 本卡专注于主上下文的内部三段结构定义，不涉及外部上下文或队列驱逐策略。
