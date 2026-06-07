---
id: fuzzy-intent-router
title: 模糊意图路由器
status: accepted
card_type: mechanism
tags: [llm-wiki, router, intent-detection, natural-language, command-dispatch]
created_time: 2026-06-08T10:00:00+08:00
edited_time: 2026-06-08T10:00:00+08:00
edited_entity: llm
source_ids: [repo-nvk-llm-wiki]
justification: ../justification/fuzzy-intent-router.md
canonical_concept: fuzzy-intent-router
aliases: [模糊路由, fuzzy router, 意图路由, intent router, wiki 自然语言路由]
summary: >-
  fuzzy-intent-router（模糊路由 / fuzzy router / 意图路由 / intent router / wiki 自然语言路由）
  是 llm-wiki 的自然语言入口：用户输入经 20 级优先级规则匹配意图，
  高置信度直接路由并说明理由，低置信度展示 2-3 候选让用户选择
related: [llm-wiki-pattern, hub-resolution-algorithm, ask-first-retrieve-loop]
---

llm-wiki 的 `/wiki` 命令不要求用户记住子命令名称——它作为**模糊意图路由器（fuzzy intent router）**接受自然语言输入，自动匹配并分发到正确的子命令[^src-1]。

**路由优先级表**包含 20 级意图（priority 0-19），按「首次匹配胜出」规则依次检查[^src-2]：

| Priority | Intent | 典型信号 |
|----------|--------|----------|
| 0 | Collection Ingest | "import wiki", dump.xml, github.com 含 "all" |
| 1 | Inventory | "inventory", "queue", "backlog", "track this" |
| 2 | Dataset | "dataset", "large data", "too big for wiki" |
| 3 | Ingest | URL、文件路径、"add"、"save" |
| 4 | Resume | "where was I", "continue", "resume" |
| 5 | Audit | "audit", "can I trust", "provenance" |
| 6 | Query | what/why/how 开头、含 "?"、"explain" |
| 7 | Research | "research", "investigate", "deep dive" |
| ... | ... | ... |
| 19 | Topic Archive | "archive wiki", "restore topic" |

**置信度分流**是路由器的核心交互设计[^src-3]：

- **高置信度**（强单一信号：URL 存在、问号、精确关键词）→ 直接路由，并向用户说明检测到的意图：`"Detected: ingest (found URL). Routing to /wiki:ingest."`
- **低置信度**（模糊输入可能匹配多个意图）→ 展示前 2-3 个候选为编号列表，等待用户选择
- **无匹配** → 显示 wiki 状态和可用子命令列表

**关键规则**[^src-4]：
- 歧义时不猜测——快速菜单比撤消错误操作更快
- Inventory/dataset 信号的优先级高于通用 URL 检测（避免 "track this URL as a candidate" 被误路由到 ingest）
- Project archive 与 topic archive 通过是否出现 "project" 一词区分
- 路由到目标命令时去除信号词（如 "add https://example.com" 只传递 URL）

**输入检测三分法**（research 命令专用）[^src-5]：
- Topic（名词/短语）→ 标准研究
- Question（what/why/how 开头或含 "?"）→ 问题模式分解
- Thesis（含 "prove that"/"is it true"/"verify"）→ 论点模式

该路由器使 llm-wiki 能通过单一入口 `/wiki` 服务所有操作——用户不需要学习 20+ 子命令的名称和参数。这与 ask-first-retrieve-loop 模式共享「先理解用户意图再行动」的设计哲学[^card-1]。

## Footnotes

[^card-1]: [先问后检索循环](ask-first-retrieve-loop.md) -- 模糊路由器与 ask-first-retrieve-loop 共享「先理解意图/需求再执行操作」的交互哲学

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "The user typed something that isn't a known keyword. Detect their intent and route to the right subcommand."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "Check these patterns in order — first match wins" (priority table from 0 to 19)
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "High confidence — a single strong signal... Route directly. Tell the user what you detected... Low confidence — ambiguous input... Present the top 2-3 matching options as a numbered list"
[^src-4]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/wiki.md -- "Never guess when ambiguous. A quick menu is faster than undoing the wrong action."
[^src-5]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- FILE: claude-plugin/commands/research.md -- "Input Detection: Topic vs Question vs Thesis — Before starting research, detect the input mode"
