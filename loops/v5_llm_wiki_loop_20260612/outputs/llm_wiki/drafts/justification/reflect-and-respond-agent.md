## Justification for reflect-and-respond-agent

**Why this card**: 双记忆系统（summary + observation）是 LoCoMo 管线的架构创新，且 observation 概念在后续 RAG 实验中被证明是最优检索单元。作为独立方法概念值得记录。

**Evidence quality**: Section 3.3 给出完整架构描述，附录提供 prompt 和输出示例，统计数据（127.4 tokens/summary, 18.2 tokens/observation）来自 Table 2。

**Atomic check**: 本卡片描述 agent 架构的记忆机制和生成流程，不涉及其在评估中的表现。
