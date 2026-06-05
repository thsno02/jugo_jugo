---
schema: justification_journal.v1
card: ../cards/memory-crud-operation-taxonomy.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`
源证据：
- sections/proposed_work.tex — "The LLM itself determines which of four distinct operations to execute: ADD for creation of new memories when no semantically equivalent memory exists; UPDATE for augmentation of existing memories with complementary information; DELETE for removal of memories contradicted by new information; and NOOP when the candidate fact requires no modification to the knowledge base."
- sections/appendix.tex Algorithm 1 — ClassifyOperation function with SemanticallySimilar, Contradicts, Augments checks
范围论证：四种操作构成一个完整的记忆管理原语集，与 wiki 系统中知识条目的 CRUD 操作有直接映射关系。UPDATE 操作中的 InformationContent 比较机制和 DELETE 操作中的矛盾检测尤其值得单独记录为原子概念。
