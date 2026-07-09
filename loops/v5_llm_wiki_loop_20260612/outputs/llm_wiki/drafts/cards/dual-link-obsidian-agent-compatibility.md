---
id: dual-link-obsidian-agent-compatibility
title: 双链接格式——Obsidian 与 Agent 兼容性设计
status: draft
card_type: convention
tags: [llm-wiki, dual-link, obsidian, wikilink, markdown-link, cross-reference]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/dual-link-obsidian-agent-compatibility.md
canonical_concept: dual-link-obsidian-agent-compatibility
aliases: [dual-link format, dual-linking, wikilink + markdown link, Obsidian compatibility, cross-reference format]
summary: >-
  llm-wiki 要求所有交叉引用在同一行使用双链接格式：[[slug|Name]] ([Name](../category/slug.md))。Obsidian 读取 [[wikilink]] 用于图视图和反向链接；Agent 跟随标准 markdown 链接导航；GitHub 渲染标准链接为可点击。系统不锁定于任何工具——纯 markdown 在任何文本编辑器中可读。See Also 链接必须双向（A->B 则 B->A）。
related: [hub-topic-wiki-isolation, llm-as-knowledge-compiler-metaphor]
---

llm-wiki 的交叉引用系统采用双链接格式确保工具无关性：

**格式规范**[^src-1]：
```
[[target-slug|Display Text]] ([Display Text](../category/target-slug.md))
```

**多工具兼容**：
- **Obsidian**：读取 `[[wikilink]]` 驱动图视图、反向链接面板、快速跳转
- **Agent（Claude/Codex）**：跟随标准 markdown `(relative/path.md)` 链接导航
- **GitHub/任意 markdown 查看器**：渲染标准链接为可点击
- **无查看器**：纯 markdown，任何文本编辑器可读[^src-2]

**双向性要求**：
- 所有 "See Also" 链接必须双向：若 A 链接到 B，则 B 必须链接回 A
- Lint (C4) 检查并可自动修复缺失的反向链接

**内联使用**：
```
The [[transformer-architecture|Transformer]] ([Transformer](../concepts/transformer-architecture.md)) uses self-attention...
```

该设计确保 wiki "不锁定于任何工具"——Obsidian 是可选的查看器，Claude Code 是编译器。[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "wiki-structure.md Dual-Link Convention" -- "[[target-slug|Display Text]] ([Display Text](../category/target-slug.md))"
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Linking: Works Everywhere" -- "The wiki is not locked into any tool"
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Obsidian Integration" -- "Claude Code is the compiler. Obsidian is an optional viewer."
