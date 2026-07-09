## Justification for memgpt-memory-hierarchy

**Why this card**: 内存层级架构是 MemGPT 系统的核心结构设计，独立于虚拟上下文管理的概念层抽象，描述的是具体的二分结构和 OS 映射。

**Evidence quality**: method_rewrite.tex 开篇即明确定义两层结构及其 OS 类比。

**Atomicity check**: 本卡聚焦于 main context vs external context 的二分定义和 OS 类比关系，不展开各层内部的具体子组件。
