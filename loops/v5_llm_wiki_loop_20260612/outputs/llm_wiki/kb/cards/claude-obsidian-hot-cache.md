---
id: claude-obsidian-hot-cache
title: claude-obsidian hot cache 跨会话记忆机制
status: accepted
card_type: mechanism
tags:
- hot-cache
- session-memory
- obsidian
- context-persistence
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-agricidaniel-claude-obsidian
evidence_basis: code_implementation
justification: ../justification/claude-obsidian-hot-cache.md
canonical_concept: claude-obsidian-hot-cache
aliases:
- hot cache
- hot.md
- session memory
- recent context cache
summary: claude-obsidian 的 hot cache 机制通过 wiki/hot.md 文件实现跨会话记忆： 每次会话结束时自动更新 hot.md 为最新 context summary（约 500 words）； 下次会话启动时首先读取 hot.md 获得 full recent context，无需 recap。 跨项目引用时也建议优先读取 hot.md。由 hooks.json
  中 SessionStart/Stop hooks 驱动。
related:
- claude-obsidian-knowledge-engine
- claude-obsidian-differentiation
---
claude-obsidian 通过 `wiki/hot.md` 文件实现跨会话记忆持续（session memory）。[^src-1]

机制运作方式：每次会话结束时，Claude 将当前会话的 context 压缩为摘要并写入 hot.md；下次会话启动时首先读取该文件，获得 full recent context，无需人工回顾。[^src-2]

hot.md 约 500 words，定位为 "recent context cache"。[^src-3]

该机制由 `hooks/hooks.json` 中的 SessionStart 和 SessionStop hooks 自动驱动。[^src-4]

跨项目引用 vault 时，官方建议的读取优先级为：hot.md → index.md → domain sub-index → specific wiki pages。[^src-5] [^card-1]

[^src-1]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "What It Does" P4 -- "At the end of every session, Claude updates a hot cache. The next session starts with full recent context, no recap needed."
[^src-2]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Commands" Table -- "update hot cache | Refresh hot.md with latest context summary"
[^src-3]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/CLAUDE.md` -- "Cross-Project Access" -- "Read wiki/hot.md first (recent context, ~500 words)"
[^src-4]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "File Structure" -- "hooks/ └── hooks.json # SessionStart + Stop hot cache hooks"
[^src-5]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Cross-Project Power Move" -- "1. Read wiki/hot.md first (recent context cache) 2. If not enough, read wiki/index.md 3. If you need domain details, read the relevant domain sub-index 4. Only then drill into specific wiki pages"

[^card-1]: 参见 [[claude-obsidian-knowledge-engine]] 了解 hot cache 在 ingest-index-query 闭环中的位置
