## Justification: memgpt-nested-kv-retrieval

**为何提取此卡**: 嵌套 KV 检索是论文独创的评测任务，精确测试了多跳检索能力 -- 这是 MemGPT function chaining 的直接能力验证。实验结果（GPT-4 基线 3 层归零 vs MemGPT 不受影响）是论文对 multi-hop retrieval 能力最清晰的定量证据。

**原子性判断**: 与 DMR（测对话一致性）和 doc QA（测文档分析）在任务类型和所测能力上均不同。嵌套 KV 是合成任务、精确测 multi-hop 能力。

**Evidence basis**: experimental_paper -- 论文设计了合成任务并报告了量化比较。
