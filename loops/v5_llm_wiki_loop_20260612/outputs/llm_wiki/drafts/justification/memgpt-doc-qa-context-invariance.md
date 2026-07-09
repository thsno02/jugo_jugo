## Justification: memgpt-doc-qa-context-invariance

**为何提取此卡**: 文档 QA 实验是论文在 document analysis 领域的核心验证，展示了"上下文长度不变性"这一关键特性。与 DMR（对话领域）互补，共同构成论文的实验主张。截断策略导致衰减 vs MemGPT 保持不变的对比是直观有力的结果。

**原子性判断**: 与嵌套 KV（合成任务/multi-hop）和 DMR（对话一致性）在领域和测试目标上均不同。此卡聚焦文档分析场景中的上下文扩展能力。

**Evidence basis**: experimental_paper -- 标准检索-阅读实验框架，定量结果。
