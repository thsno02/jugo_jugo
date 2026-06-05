---
id: my-llm-wiki-implementation
title: my-llm-wiki PyPI 实现
status: accepted
card_type: example_pattern
tags: [llm-wiki, implementation, pypi, cli, python, tree-sitter, docling]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [pypi-my-llm-wiki]
justification: ../justification/my-llm-wiki-implementation.md
canonical_concept: my-llm-wiki-implementation
aliases: [my-llm-wiki, phuc-nt LLM Wiki]
summary: >-
  my-llm-wiki-implementation（my-llm-wiki / phuc-nt LLM Wiki）是 Karpathy LLM Wiki
  三层架构的 Python CLI 实现：pip 安装后 llm-wiki . 即可将任意文件夹编译为可查询的 Obsidian vault，
  支持 19 语言代码（Tree-sitter AST）、多格式文档（Docling）、SHA256 增量缓存和 CLI 回写
related: [kb-compile-implementation, obsidian-karpathy-wiki-plugin]
  - llm-wiki-pattern
  - three-layer-architecture
  - obsidian-tooling
  - wiki-compounding-artifact
  - obsidian-karpathy-wiki-plugin
  - kb-compile-implementation
  - tree-sitter-code-extraction
  - wiki-write-back-mechanism
---

`my-llm-wiki` 是由开发者 phuc-nt 发布的 Python 包（MIT 许可），实现了 Karpathy LLM Wiki 概念的全部三层架构[^src-1]。该工具以 CLI 形式运行：`pip install my-llm-wiki` 安装后，`llm-wiki .` 即可将当前文件夹编译为知识图谱[^src-2]。

**输出格式**：编译产物 `wiki-out/vault/` 是一个可直接打开的 Obsidian vault，也可通过 CLI 查询[^src-3]。

**支持的文件类型**涵盖四类[^src-4]：
- **代码**（19 种语言）：通过 Tree-sitter AST 提取类、函数、类型继承、函数签名、文档注释和调用图
- **Markdown/文本**：标题、定义、`[[wikilinks]]`、跨文档引用
- **办公/出版文档**（PDF/DOCX/PPTX/HTML/EPUB）：通过 Docling 进行版面感知提取，保留标题和表格，扫描 PDF 自动 OCR
- **图片**（HEIC/PNG/JPG）：结构化遍历生成 hub 节点，通过 Claude Code agent 模式进行视觉 OCR

**增量机制**：重复运行时 SHA256 缓存自动跳过未变更文件[^src-5]。

**回写能力**：`llm-wiki note "<insight>"` 命令可从 Claude Code 会话中将洞察写回知识图谱，使图谱随时间持续增长[^src-6]。

**开发节奏**：从 v0.1.0（2026-04-07）到 v0.9.0（2026-04-28），21 天内发布 15 个版本，状态为 Beta[^src-7]。

与同类实现相比，该工具走 CLI + pip 路线（区别于 Obsidian 插件内运行的 obsidian-karpathy-wiki-plugin，以及 Claude Code 自定义命令形式的 kb-compile[^card-2]），强调代码仓库级别的知识图谱构建能力。Obsidian 社区插件走 GUI 路线提供了互补的交互方式，4 周内发布 27 版达 94/100 评分[^card-1]。

## Footnotes

[^card-1]: [Obsidian 社区插件 Karpathy LLM Wiki](obsidian-karpathy-wiki-plugin.md) -- my-llm-wiki 走 CLI+pip 路线强调代码仓库级知识图谱，Obsidian 插件走 GUI 路线强调笔记本级交互体验，两者是同一三层架构模式在不同工具生态中的独立实现
[^card-2]: [kb-compile 实现模式](kb-compile-implementation.md) -- 本卡是独立 pip 包（Tree-sitter + Docling + SHA256 缓存），kb-compile 是 Claude Code 自定义命令叠加于 Mem0+pgvector 向量检索层之上，体现独立工具 vs 嵌入已有基础设施的两种落地策略

[^src-1]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L100 -- "Andrej Karpathy shared a concept he called LLM Wiki — a personal knowledge system with three layers: raw files (never modified), a compiled wiki with cross-references, and a schema that tells the LLM how to maintain it"
[^src-2]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L103-104 -- "pip install my-llm-wiki cd your-project && llm-wiki ."
[^src-3]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L104 -- "The output wiki-out/vault/ is a drop-in Obsidian vault — open it directly, or query from CLI."
[^src-4]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L108-114 -- "Code (19 languages)... Markdown / text... PDF / DOCX / PPTX / HTML / EPUB... Images (HEIC / PNG / JPG)"
[^src-5]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L104 -- "Re-run anytime; SHA256 cache skips unchanged files."
[^src-6]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L104 -- "llm-wiki note \"<insight>\" writes back from your Claude Code sessions so the graph compounds over time."
[^src-7]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- L68-69, L178-236 -- "Development Status 4 - Beta" + release history from 0.1.0 (Apr 7) to 0.9.0 (Apr 28)
