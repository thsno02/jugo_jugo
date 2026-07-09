---
id: llm-wiki-dual-link-obsidian
title: 双链格式与 Obsidian 兼容
status: superseded
superseded_by: dual-link-obsidian-agent-compatibility
card_type: design-pattern
tags: [llm-wiki, obsidian, wikilinks, markdown-links, dual-link]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
evidence_basis: documentation
justification: ../justification/llm-wiki-dual-link-obsidian.md
canonical_concept: dual-link-obsidian-compatibility
aliases: [dual-link format, wikilinks, Obsidian compatibility, 双链格式]
summary: >-
  dual-link-obsidian-compatibility 设计：文章使用 [[wikilink]] 加标准 markdown link 双格式，Obsidian 读取 wikilink 用于图谱视图和反向链接，其他工具（Claude Code GitHub 纯文本编辑器）跟随 markdown link，每个 topic wiki 含 .obsidian/ vault config 可独立打开为 vault
related: [llm-wiki-compilation-process, llm-wiki-topic-wiki-isolation]
---

llm-wiki 采用双链格式确保跨工具兼容：每个链接同时以 [[wikilink]] 和标准 markdown link 呈现。例如：`[[gut-brain-axis|Gut-Brain Axis]] ([Gut-Brain Axis](../concepts/gut-brain-axis.md))`。[^src-1]

Obsidian 读取 wikilink 以提供图谱视图（graph view）和反向链接（backlinks）；其他工具（Claude Code、GitHub、纯文本编辑器）跟随标准 markdown link。[^src-2]

每个 topic wiki 自带 .obsidian/ vault 配置，可直接作为独立 vault 打开（如 `open ~/wiki/topics/nutrition/`）。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Obsidian" P302 -- "[[gut-brain-axis|Gut-Brain Axis]] ([Gut-Brain Axis](../concepts/gut-brain-axis.md))"
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Obsidian" P302 -- "Obsidian reads the wikilink for graph view and backlinks; everything else (Claude Code, GitHub, plain text editors) follows the standard markdown link."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Obsidian" P300-301 -- "Each topic wiki ships with its own .obsidian/ vault config and can be opened as an independent vault"
