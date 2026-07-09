---
id: llm-wiki-compiled-artifact-analogy
title: LLM Wiki 编译产物类比
status: draft
card_type: conceptual-model
tags: [llm-wiki, analogy, knowledge-compilation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-compiled-artifact-analogy.md
canonical_concept: llm-wiki-compiled-artifact-analogy
aliases: [compiled artifact, compiled executable analogy, source code vs executable]
summary: >-
  LLM wiki 编译产物类比 compiled-artifact-analogy：Karpathy 将 raw sources 比作源代码，LLM wiki 比作编译后的可执行文件。不必每次查询都重新编译——wiki 保持 canonical、alive，并随每次新源 ingestion 而改善。与 RAG 的 re-derivation 形成对比。
related: [llm-wiki-three-layer-architecture, llm-wiki-vs-rag-reasoning-depth]
---

Karpathy 用编程类比阐释 LLM wiki 的核心价值主张 [^src-1]：

- **Raw sources = 源代码 (source code)**
- **LLM wiki = 编译后的可执行文件 (compiled executable)**

正如你不会每次运行程序都重新编译，LLM wiki 也不需要每次查询时重新从原始文档推导答案。Wiki 保持 canonical（权威）、alive（活跃更新），并随每次新源 ingestion 而持续改善。

这一类比区分了 LLM wiki（编译一次、多次运行）和 RAG（每次查询都重新推导）的根本哲学差异 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "What Karpathy's LLM wiki is" -- "raw sources are like source code, and the LLM wiki is the compiled executable. You don't recompile every time you run a program."
[^card-1]: 参见 [[llm-wiki-vs-rag-reasoning-depth]] 对推理深度差异的展开论述
