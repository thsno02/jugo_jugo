---
id: tree-sitter-code-extraction
title: Tree-sitter AST 代码知识提取
status: accepted
card_type: mechanism
tags: [tree-sitter, ast, code-analysis, knowledge-extraction, multi-language]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
justification: ../justification/tree-sitter-code-extraction.md
canonical_concept: tree-sitter-code-extraction
aliases: [Tree-sitter代码提取, AST代码知识提取, Tree-sitter AST extraction]
summary: >-
  tree-sitter-code-extraction（Tree-sitter代码提取 / AST代码知识提取）是一种通过 Tree-sitter
  增量解析器对源代码进行 AST 级结构化知识提取的机制：从 19 种语言中提取类、函数、类型继承、
  函数签名、文档注释和调用图，无需 LLM 参与即可生成知识图谱的代码层节点
related:
  - my-llm-wiki-implementation
  - ingest-operation
  - three-layer-architecture
---

Tree-sitter AST 代码知识提取是一种将源代码转化为知识图谱节点的机制。my-llm-wiki 使用 Tree-sitter 增量解析器对 19 种编程语言进行 AST（抽象语法树）分析，提取六类结构化信息[^src-1]：

1. **类**（classes）——代码的组织单元
2. **函数**（functions）——可调用的行为单元
3. **类型继承**（typed extends/implements）——类之间的层次关系
4. **函数签名**（function signatures）——参数和返回类型
5. **文档注释**（doc comments）——Javadoc、JSDoc、GoDoc、`///` 等格式
6. **调用图**（call graph）——函数之间的调用关系

覆盖的语言包括 Python、TypeScript/JavaScript、Go、Rust、Java、C/C++、Ruby、C# 等共 19 种[^src-2]。

这一机制的意义在于：代码知识提取在 AST 层面完成，是确定性的结构分析而非 LLM 推理，因此提取结果可复现且不消耗 token。提取出的结构化节点（类、函数、继承关系、调用链）构成知识图谱中代码层的骨架，为后续的跨引用和 wiki 编译提供输入。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L108 -- "Tree-sitter AST: classes, functions, typed extends / implements , function signatures, doc comments (Javadoc / JSDoc / GoDoc / /// ), call graph."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L108 -- "Code (19 languages) — Python, TypeScript/JavaScript, Go, Rust, Java, C/C++, Ruby, C#, and more ( full list )."
