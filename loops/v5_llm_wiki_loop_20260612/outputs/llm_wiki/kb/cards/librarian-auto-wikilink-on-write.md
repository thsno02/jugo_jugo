---
id: librarian-auto-wikilink-on-write
title: Librarian 写入时自动检测并插入 wikilinks
status: accepted
card_type: mechanism
tags:
- wikilinks
- auto-linking
- obsidian-compatible
- markdown
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-ngmeyer-librarian-mcp
evidence_basis: code_implementation
justification: ../justification/librarian-auto-wikilink-on-write.md
canonical_concept: librarian-auto-wikilink
aliases:
- auto-wikilinks
- auto-linking
- library_write auto-link
- library_suggest_links
summary: Librarian 的 library_write 工具在写入文件时自动扫描已有笔记标题及 frontmatter aliases，将匹配文本包裹为
  [[wikilinks]]。仅在显式写入时触发，从不修改用户未要求写入的文件。跳过代码块、行内代码、URL、已有 wikilinks。链接使用规范文件名以在大小写敏感文件系统上正确解析。支持
  [[Note Name|alias]] 格式。librarian auto-wikilink auto-linking library_write。
related:
- librarian-mcp-as-llm-wiki-productization
- typed-wikilinks
---

Librarian 的自动链接机制在 Claude 通过 `library_write` 工具写入文件时激活[^src-1]：

1. **扫描范围** — 检测 vault 中所有已有笔记的标题，以及 frontmatter 中声明的 aliases（如 `aliases: [ML, machine learning]`）
2. **包裹为 wikilinks** — 匹配的文本被包裹为 `[[wikilinks]]`；alias 匹配使用 `[[Note Name|ML]]` 格式
3. **安全跳过** — 代码块、行内代码、URL、已有 wikilinks 不会被错误修改[^src-2]
4. **仅显式写入** — Librarian 从不自动修改用户未通过 library_write 要求写入的文件
5. **规范文件名** — 链接使用 canonical file names，确保在大小写敏感文件系统上和 Obsidian 图视图中正确解析

此外 `library_suggest_links` 工具可找到未链接的已有笔记提及（包括 aliases），供用户决定是否补充链接[^src-3]。

[^card-1]: [[librarian-mcp-as-llm-wiki-productization]] — Librarian 整体架构
[^src-1]: `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` -- "Auto-linking" P1 -- "When Claude writes files via library_write, Librarian scans for mentions of existing note titles and wraps them in [[wikilinks]]"
[^src-2]: `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` -- "Auto-linking" P3 -- "Auto-linking skips code blocks, inline code, URLs, and existing wikilinks to avoid corrupting content"
[^src-3]: `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md` -- "Tools" P1 -- "library_suggest_links: Find unlinked mentions of existing notes (including aliases)"
