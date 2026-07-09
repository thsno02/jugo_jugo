---
id: wiki-compilation-by-llm
title: LLM 增量编译 Wiki 机制
status: draft
card_type: mechanism
tags: [wiki-compilation, incremental-build, markdown, llm-agent]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
evidence_basis: practitioner_report
justification: ../justification/wiki-compilation-by-llm.md
canonical_concept: wiki-compilation-by-llm
aliases: [wiki compilation, LLM compile wiki, 知识编译, incrementally compile a wiki]
summary: >-
  wiki-compilation-by-llm LLM增量编译wiki机制 LLM将raw/目录中的源文档增量"编译"为结构化markdown wiki，
  包含摘要、反向链接、概念分类、文章生成及互联。类比传统编译器但为有损语义重组而非确定性转换。
  LLM自动维护索引文件和文档摘要。编译过程可反复运行，增量更新。
related: [llm-knowledge-base-workflow, llm-wiki-qa-without-rag]
---

在 Karpathy 的工作流中，"编译"(compile) 指 LLM 将 `raw/` 目录中的源文档转化为结构化 .md wiki 的过程。该编译包含以下操作：

- 为所有 raw 数据生成摘要
- 建立反向链接 (backlinks)
- 将数据分类为概念 (concepts)
- 为每个概念撰写文章
- 将所有文章互相链接

这一比喻映射到传统编译：raw 数据对应源代码，wiki 对应编译产物，LLM 对应编译器。关键差异在于：传统编译是确定性转换，此处是有损的语义重组；输出非可执行代码而是人类可读知识制品；过程为增量式，可反复运行。[^src-1]

LLM 在此过程中自动维护索引文件和简短摘要，使后续查询无需依赖向量检索即可定位相关数据。[^src-2] [^card-1]

[^src-1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "Data ingest" -- "I use an LLM to incrementally \"compile\" a wiki, which is just a collection of .md files in a directory structure"
[^src-2]: `data/raw/webpage/karpathy-x-launch-post/text.txt` -- "Q&A" -- "the LLM has been pretty good about auto-maintaining index files and brief summaries of all the documents"
[^card-1]: 参见 [[llm-wiki-qa-without-rag]] 关于索引替代 RAG 的详细讨论
