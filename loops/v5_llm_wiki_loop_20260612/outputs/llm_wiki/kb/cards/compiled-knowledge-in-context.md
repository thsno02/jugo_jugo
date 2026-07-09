---
id: compiled-knowledge-in-context
title: 编译知识装入 Context 的性能声明
status: accepted
card_type: claim
tags:
- llm-wiki
- context-window
- performance
- rag-comparison
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- aillm-wiki-directory
evidence_basis: documentation
justification: ../justification/compiled-knowledge-in-context.md
canonical_concept: compiled-knowledge-in-context
aliases:
- compiled knowledge fits in context
- 编译知识入上下文
- context-fit wiki
summary: 据 AILLM Wiki Directory 声明，一个 400K-word LLM Wiki 对中小知识库（small-to-mid knowledge
  bases）在延迟和准确率上优于 RAG 管道，且跨会话跨设备一致。该声明明确限定规模范围，暗示大规模知识库可能不适用。
related:
- llm-wiki-vs-rag
- llm-wiki-pattern-definition
- fc-kv-cache-latency-advantage
---

AILLM Wiki Directory 提出一项性能声明：编译后的 LLM Wiki 知识可装入模型 context window，对中小知识库（small-to-mid knowledge bases）在延迟和准确率上优于 RAG 管道。[^src-1]

具体而言，材料以 "400K-word wiki" 作为示例规模。[^src-2] 该声明同时指出跨会话跨设备的一致性优势——编译后的 wiki 作为静态文本无需在线检索基础设施。

**规模限定**：材料明确使用 "small-to-mid knowledge bases" 限定词，暗示大规模知识库（似乎超出单次 context window 容量时）该优势不再成立。[^card-1]

[^card-1]: 参见 [[llm-wiki-vs-rag]] LLM Wiki 与 RAG 对比的完整分析
[^src-1]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Value Props" P8 -- "A 400K-word wiki beats RAG on small-to-mid knowledge bases for both latency and accuracy"
[^src-2]: `data/raw/webpage/aillm-wiki-directory/markdown.md` -- "Value Props" P8 -- "For most personal knowledge bases a compiled LLM Wiki answers faster than a RAG pipeline and stays consistent between sessions and devices"
