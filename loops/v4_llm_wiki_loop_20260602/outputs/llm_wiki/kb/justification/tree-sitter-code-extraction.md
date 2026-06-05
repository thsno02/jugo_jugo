---
schema: justification_journal.v1
card: ../cards/tree-sitter-code-extraction.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/pypi/pypi-my-llm-wiki/text.txt`
源证据：
- L108 — "Tree-sitter AST: classes, functions, typed extends / implements , function signatures, doc comments (Javadoc / JSDoc / GoDoc / /// ), call graph."
- L108 — "Code (19 languages) — Python, TypeScript/JavaScript, Go, Rust, Java, C/C++, Ruby, C#, and more"
范围论证：Tree-sitter AST 提取是代码知识图谱构建中的一个独立机制，与 LLM 驱动的文本/文档知识提取在技术路径上截然不同（确定性 AST 解析 vs. 概率性语言模型推理）。将其单独建卡有助于区分知识提取的两条技术路径，也为未来出现的其他 AST 工具（如基于 LSP 的提取）提供对比基准。该卡不重复 my-llm-wiki-implementation 卡中的工具全貌描述，仅聚焦于代码提取这一原子机制。
