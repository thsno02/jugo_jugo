---
id: memory-crud-operation-taxonomy
title: 记忆 CRUD 操作分类法
status: accepted
card_type: mechanism
tags: [agent_memory, CRUD, memory_management, tool_calling, Mem0]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-mem0]
justification: ../justification/memory-crud-operation-taxonomy.md
canonical_concept: memory-crud-operation-taxonomy
aliases: [记忆操作四分类, ADD/UPDATE/DELETE/NOOP, memory update operations]
summary: >-
  memory-crud-operation-taxonomy（记忆操作四分类 / ADD/UPDATE/DELETE/NOOP）Mem0 将记忆更新分类为四种操作：ADD（无语义等价记忆时新增）、UPDATE（增强已有记忆的信息内容）、DELETE（删除被新事实矛盾的记忆）、NOOP（事实已存在或不相关），由 LLM 通过 tool call 自主判断而非使用独立分类器
related: [memory-extraction-update-pipeline, ingest-operation, lint-operation, contradiction-state-machine]
---

Mem0 的记忆更新阶段将每个候选事实的处理归类为四种互斥操作，由 LLM 通过函数调用接口自主决定 [^src-1]：

1. **ADD**：当候选事实与已有记忆库中没有语义相似的内容时，生成唯一标识符并将事实作为新记忆加入 [^src-2]。

2. **UPDATE**：当候选事实增强（augments）已有记忆时，系统找到相关记忆 $m_i$，仅当新事实的信息内容（InformationContent）大于已有记忆时才执行替换——即用更丰富的信息取代旧版本 [^src-3]。

3. **DELETE**：当候选事实与已有记忆产生矛盾（contradicts）时，找到被矛盾的记忆并将其移除 [^src-4]。

4. **NOOP**：当候选事实已经存在于记忆库中或与当前知识库不相关时，不执行任何操作 [^src-5]。

该分类法的关键设计决策是：不使用独立的分类器模型，而是直接利用 LLM 的推理能力，通过函数调用（tool call）机制根据候选事实与已有记忆之间的语义关系来选择合适的操作。这种方式让操作分类具备了语义理解能力，而非仅依赖简单的相似度阈值 [^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "The LLM itself determines which of four distinct operations to execute"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/appendix.tex Algorithm 1 -- "ADD for creation of new memories when no semantically equivalent memory exists"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/appendix.tex Algorithm 1 -- "If InformationContent(f) > InformationContent(m_i) then M ← (M \ {m_i}) ∪ {(id_i, f, 'UPDATE')}"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/appendix.tex Algorithm 1 -- "DELETE for removal of memories contradicted by new information"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/appendix.tex Algorithm 1 -- "NOOP when the candidate fact requires no modification to the knowledge base"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` -- sections/proposed_work.tex -- "Rather than using a separate classifier, we leverage the LLM's reasoning capabilities to directly select the appropriate operation based on the semantic relationship between the candidate fact and existing memories."
