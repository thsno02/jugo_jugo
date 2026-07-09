## Justification: memgpt-deep-memory-retrieval

**为何提取此卡**: DMR 是论文的核心实验贡献之一，是首个专门测试对话 agent "深度记忆一致性"的任务。93.4% vs 35.3% 的巨大性能差距是论文最强实验证据。任务设计本身（基于 MSC + LLM 生成 QA）也是可复现的方法论贡献。

**原子性判断**: DMR 是一个独立的实验设计+结果，与 opener task（测 engagement）和 doc QA（测文档分析）在目标和方法上均独立。

**Evidence basis**: experimental_paper -- 论文设计并执行了该实验，报告了定量结果。
