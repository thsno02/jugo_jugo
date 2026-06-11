---
id: dual-link-format
title: 双链格式与跨查看器兼容
status: accepted
card_type: mechanism
tags: [llm-wiki, obsidian, markdown, linking, compatibility]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/dual-link-format.md
canonical_concept: dual-link-format
aliases: [双链格式, dual-link format, wikilink+markdown link, 双格式链接]
summary: >-
  dual-link-format（双链格式 / dual-link format / wikilink+markdown link / 双格式链接）
  是 LLM Wiki 的链接策略：每个交叉引用同时以 [[wikilink]] 和标准 markdown link 两种格式写入，
  Obsidian 读取 wikilink 用于图谱视图和反向链接，其他工具（Claude Code/GitHub/纯文本编辑器）
  跟随标准 markdown link
related: [topic-isolation, multi-platform-skill-portability, zero-runtime-dependency]
---

LLM Wiki 的文章采用**双链格式（dual-link format）**处理所有交叉引用[^src-1]。每个链接同时以两种语法写入：

```markdown
[[gut-brain-axis|Gut-Brain Axis]] ([Gut-Brain Axis](../concepts/gut-brain-axis.md))
```

这一设计解决的核心问题是：**同一套 Markdown 文件需要在多种工具中保持可导航性**[^src-2]。

**Obsidian 侧**：读取 `[[wikilink]]` 用于图谱视图（graph view）和反向链接（backlinks）——这是 Obsidian 知识管理体验的核心功能。每个 topic wiki 自带 `.obsidian/` vault 配置，可直接作为独立 vault 打开[^src-3]。

**通用工具侧**：Claude Code、GitHub 渲染器、VS Code、纯文本编辑器跟随标准 `[text](path.md)` 链接——无需任何 Obsidian 特有的解析逻辑[^src-4]。

这一策略是 LLM Wiki 零运行时依赖原则的具体延伸——不强制要求用户安装 Obsidian 或任何特定查看器，纯 Markdown 在所有环境中保持完整语义[^card-1]。同时，双链格式使得主题隔离中的跨主题 peek 和 `--with` 参数能在两种链接生态中都正确解析[^card-2]。多平台可移植性的保障也依赖于链接格式的通用性——如果链接只能在 Obsidian 中工作，AGENTS.md 模式和非 Obsidian 平台的可用性将受损[^card-3]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` L301-302 -- "Cross-references use a dual-link format: [[gut-brain-axis|Gut-Brain Axis]] ([Gut-Brain Axis](../concepts/gut-brain-axis.md)) Obsidian reads the wikilink for graph view and backlinks; everything else (Claude Code, GitHub, plain text editors) follows the standard markdown link."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` L117 -- "[[wikilinks]] for Obsidian plus standard markdown links for everything else. Works in every viewer — including no viewer at all."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` L300 -- "Each topic wiki ships with its own .obsidian/ vault config and can be opened as an independent vault"
[^src-4]: `data/raw/webpage/llm-wiki-net/markdown.md` L302 -- "everything else (Claude Code, GitHub, plain text editors) follows the standard markdown link."
[^card-1]: [零运行时依赖](zero-runtime-dependency.md) -- 双链格式是零依赖原则在链接层的延伸：不强制要求任何特定查看器
[^card-2]: [主题隔离原则](topic-isolation.md) -- 双链格式确保跨主题 peek 和 --with 参数在两种链接生态中都可解析
[^card-3]: [多平台技能可移植性](multi-platform-skill-portability.md) -- 链接格式的通用性是多平台可移植的前提之一
