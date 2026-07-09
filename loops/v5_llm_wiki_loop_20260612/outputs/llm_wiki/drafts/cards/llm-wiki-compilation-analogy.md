---
id: llm-wiki-compilation-analogy
title: LLM Wiki 编译类比
status: draft
card_type: design_philosophy
tags: [llm-wiki, analogy, knowledge-compilation]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-compilation-analogy.md
canonical_concept: llm-wiki-compilation-analogy
aliases: [source code / executable analogy, code source / exécutable, 源码与可执行文件类比, knowledge compilation]
summary: >-
  Karpathy 将 LLM wiki 类比为编译过程：源文档如源码（code source），wiki 如可执行文件（exécutable compilé）。知识预编译一次后反复查询，无需每次从原始材料重新推导。wiki 是活的编译产物，随新源增量更新，实现知识复合增长（compound）。
related: [llm-wiki-three-layer-architecture, llm-wiki-vs-rag-boundary]
---

Karpathy 用编译类比阐述 LLM wiki 的核心设计哲学 [^src-1]：源文档相当于源代码，LLM wiki 相当于编译后的可执行文件。正如程序不会每次运行时重新编译，wiki 也不应在每次查询时从源文档重新推导答案。

这一类比传达的设计原则：
- 知识应被**预编译**为结构化形式，而非每次使用时即席生成
- Wiki 是"活的"（vivante）编译产物，随新源文档加入而增量更新 [^src-2]
- 复合增长（compound）是系统的核心价值——每份新文档不仅增加自身知识，还通过交叉链接丰富已有知识 [^card-1]

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "Qu'est-ce que le LLM wiki selon Karpathy" P10 -- "les sources brutes sont comme du code source, et la wiki LLM est l'exécutable compilé. Vous ne re-compilez pas à chaque fois que vous lancez un programme."
[^src-2]: `data/raw/webpage/anthemcreation-fr-guide/markdown.md` -- "Qu'est-ce que le LLM wiki selon Karpathy" P10 -- "La wiki reste canonique, vivante, et s'améliore à chaque nouvelle source ingérée."
[^card-1]: [[llm-wiki-three-layer-architecture]] — wiki 层的增量更新机制
