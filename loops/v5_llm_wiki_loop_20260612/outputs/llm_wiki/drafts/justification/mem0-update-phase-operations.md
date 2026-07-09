## Justification: mem0-update-phase-operations

**提取理由**: 更新阶段的四种操作（ADD/UPDATE/DELETE/NOOP）及其通过 LLM tool call 而非独立分类器实现的设计，是 Mem0 知识库维护的核心机制。

**原子性判断**: 本卡聚焦于更新阶段的操作分类逻辑和执行方式，与提取阶段独立。

**Hedge 审查**: 无推测性语言，操作定义和实现方式均来自论文明确描述。
