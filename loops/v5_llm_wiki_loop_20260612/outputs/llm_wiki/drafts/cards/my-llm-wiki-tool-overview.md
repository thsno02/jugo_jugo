---
id: my-llm-wiki-tool-overview
title: my-llm-wiki 工具概览
status: draft
card_type: tool
tags: [my-llm-wiki, knowledge-graph, tree-sitter, obsidian, docling, python-tool]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
evidence_basis: documentation
justification: ../justification/my-llm-wiki-tool-overview.md
canonical_concept: my-llm-wiki-tool-overview
aliases: [my-llm-wiki, llm-wiki CLI, my_llm_wiki]
summary: >-
  my-llm-wiki 是一个 Python 包（pip install my-llm-wiki），实现 Karpathy LLM Wiki 三层架构，将任意文件夹转为可查询知识图谱。使用 Tree-sitter AST 提取 19 种编程语言的结构信息，Docling 处理 PDF/DOCX/PPTX/HTML/EPUB，输出为 Obsidian vault。SHA256 cache 实现增量更新。作者 phuc-nt，MIT 许可，Python >=3.10，v0.9.0 Beta。
related: []
---

my-llm-wiki 是一个 Python 包，实现了 Karpathy 的 LLM Wiki 三层架构 [^card-1]，将任意文件夹转为可查询的知识图谱 [^src-1]。

## 核心能力

- **代码提取**：通过 Tree-sitter AST 支持 19 种编程语言（Python, TypeScript/JavaScript, Go, Rust, Java, C/C++, Ruby, C# 等），提取 classes、functions、typed extends/implements、function signatures、doc comments、call graph [^src-2]
- **文档提取**：Markdown（headings/definitions/wikilinks/cross-document references）；PDF/DOCX/PPTX/HTML/EPUB 通过 Docling 实现 layout-aware extraction，scanned PDFs auto-OCR，EPUB 经 stdlib zipfile 解包后走 Docling HTML pipeline [^src-3]
- **图像处理**：HEIC/PNG/JPG 通过 Claude Code agent mode 进行 vision OCR
- **输出格式**：wiki-out/vault/ 为即开即用的 Obsidian vault
- **增量更新**：SHA256 cache 跳过未修改文件

## 使用方式

```
pip install my-llm-wiki
cd your-project && llm-wiki .
```

## 项目元数据

作者 phuc-nt，MIT 许可，Python >=3.10，Development Status 4-Beta，v0.9.0（2026-04-28 发布），从 v0.1.0 到 v0.9.0 在 2026 年 4 月内快速迭代 [^src-4]。

[^src-1]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Project description" P34 -- "Turn any folder into a queryable knowledge graph"
[^src-2]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Supported file types" P108 -- "Tree-sitter AST: classes, functions, typed extends / implements, function signatures, doc comments"
[^src-3]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Supported file types" P112 -- "layout-aware extraction via Docling... Scanned PDFs auto-OCR. EPUB unpacked via stdlib zipfile"
[^src-4]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Release history" P178-180 -- "0.9.0 Apr 28, 2026"
[^card-1]: karpathy-llm-wiki-three-layer-architecture
