---
id: my-llm-wiki-supported-source-types
title: my-llm-wiki 用 Tree-sitter + Docling + 视觉 OCR 覆盖代码/办公文档/图像
status: draft
card_type: source_claim
tags: [#tree-sitter, #docling, #file-ingestion]
created_time: 2026-05-26T14:50:00+08:00
edited_time: 2026-05-26T14:50:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
provenance_card: ../provenance/my-llm-wiki-supported-source-types.md
aliases: [my-llm-wiki file types]
related: [my-llm-wiki-three-layer-implementation]
---

## 三条并行的源抽取管道

`my-llm-wiki` 0.9.0 把"任何文件夹变成可查询知识图"的能力靠三条管道并存：

1. **代码（19 语言）via Tree-sitter AST**——Python / TypeScript / JavaScript / Go / Rust / Java / C / C++ / Ruby / C# 等。抽取的不是简单 token，而是 class、function、`extends`/`implements` 类型继承、function signature、doc comment（Javadoc / JSDoc / GoDoc / `///`），以及 call graph。
2. **办公文档 via Docling**（PDF / DOCX / PPTX / HTML / EPUB），需 `pip install 'my-llm-wiki[docling]'`。保留 heading 与 table；扫描版 PDF 自动走 OCR；EPUB 用 stdlib `zipfile` 拆包后走 Docling 的 HTML pipeline；无 Word heading 样式的文档用"bold-as-heading" fallback。
3. **图像（HEIC / PNG / JPG）via vision OCR**——结构化 pass 时先生成 hub 节点，真正 OCR 通过 Claude Code 的 agent mode 命令 `/wiki .` 完成。

Markdown / 纯文本是 native 一等公民：heading、definition、`[[wikilinks]]`、跨文档引用都直接解析。

## 为什么值得抓住

- **代码不是字符串切片，是 AST**。这意味着图的边来源是"call graph + 类型继承"，而不是字符级相似度——这与 RAG 把代码切 chunk 完全不同。
- **图像 OCR 走 Claude Code agent mode**——工具承认"视觉理解不在 CLI 范围内"，而把这部分 offload 给已在用户机器上跑的 LLM 客户端。这是把"LLM as service"嵌入文件抽取的实用做法，但也意味着该路径无法在无 Claude Code 的环境跑。
- **Docling 是默认推荐的 office 抽取引擎**——而不是自己写 PDF parser；表明 2026 年 Python 生态里 layout-aware extraction 已经稳定足以作 SDK 依赖。

## References

- 三条管道的描述：`data/raw/pypi/pypi-my-llm-wiki/text.txt` 第 108-115 行。
- Provides-Extra 列出 `pdf`、`leiden`、`office`、`docling`、`all`、`dev`：第 65 行。

## Footnotes

- 代码管道："Code (19 languages) — Python, TypeScript/JavaScript, Go, Rust, Java, C/C++, Ruby, C#, and more (full list). Tree-sitter AST: classes, functions, typed extends/implements, function signatures, doc comments (Javadoc / JSDoc / GoDoc / ///), call graph."（第 108 行）
- 办公文档 + EPUB："PDF / DOCX / PPTX / HTML / EPUB — layout-aware extraction via Docling ... Scanned PDFs auto-OCR. EPUB unpacked via stdlib zipfile and routed through Docling's HTML pipeline. Bold-as-heading fallback for documents without Word Heading styles."（第 112 行）
- 图像："Images (HEIC / PNG / JPG) — hub nodes from structural pass; vision OCR via Claude Code agent mode (/wiki .)."（第 114 行）
