---
id: claude-obsidian-knowledge-engine
title: claude-obsidian 自主知识引擎架构
status: accepted
card_type: architecture
tags:
- llm-wiki
- obsidian
- knowledge-engine
- ingest
- lint
- multi-agent
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-agricidaniel-claude-obsidian
evidence_basis: code_implementation
justification: ../justification/claude-obsidian-knowledge-engine.md
canonical_concept: claude-obsidian-knowledge-engine
aliases:
- claude-obsidian
- claude obsidian wiki
- LLM Wiki Obsidian implementation
summary: claude-obsidian 是基于 Karpathy LLM Wiki pattern 的 Claude Code 插件 + Obsidian vault， 实现自主知识引擎闭环：ingest 读取源文件产出 8-15 wiki pages 并更新 index/log， query 按 hot.md → index → domain sub-index → pages 优先级综合作答并引用具体
  wiki page， lint 执行 8-category 健康检查（orphans/dead links/gaps/stale claims/missing cross-references）。 11 skills、零手动归档、multi-agent parallel ingestion。 6 种 vault 模式（Website/GitHub/Business/Personal/Research/Book）可组合。
  可选 DragonScale Memory 扩展。支持 Claude/Gemini/Codex/Cursor/Windsurf 多模型。
related:
- claude-obsidian-hot-cache
- claude-obsidian-differentiation
---

claude-obsidian 是一个 Claude Code 插件兼 Obsidian vault 项目，基于 Andrej Karpathy 的 LLM Wiki pattern 实现自主知识引擎。[^src-1]

## 核心循环

1. **Ingest**: 读取源文件 → 提取 entities/concepts → 创建 8-15 wiki pages → 更新 index.md 和 log.md → 建立 cross-references [^src-2]
2. **Query**: 按 hot.md → index.md → domain sub-index → specific pages 的优先级检索，综合作答并引用具体 wiki page（非训练数据）[^src-3]
3. **Lint**: 8-category 健康检查——orphans、dead links、stale claims、missing cross-references 等 [^src-4]

## 工程特性

- 11 skills，零手动归档（Zero manual filing）[^src-1]
- Multi-agent support：batch ingestion 时使用 parallel agents [^src-5]
- 6 种 vault 模式（Website / GitHub / Business / Personal / Research / Book），可组合 [^src-6]
- 跨项目共享：任何 Claude Code 项目通过 CLAUDE.md 指向同一 vault [^src-7]
- 可选 DragonScale Memory 扩展：log folds、deterministic page addresses、semantic tiling lint、boundary-first autoresearch [^src-8]
- 多模型支持：Claude, Gemini, Codex, Cursor, Windsurf [^src-9]

[^src-1]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Header" P2 -- "Based on Andrej Karpathy's LLM Wiki pattern. 11 skills. Zero manual filing. Multi-agent support."
[^src-2]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "What It Does" P2 -- "You drop sources. Claude reads them, extracts entities and concepts, updates cross-references, and files everything into a structured Obsidian vault."
[^src-3]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "What It Does" P3 -- "You ask questions. Claude reads the hot cache (recent context), scans the index, drills into relevant pages, and synthesizes an answer. It cites specific wiki pages, not training data."
[^src-4]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "What It Does" P4 -- "You lint. Claude finds orphans, dead links, stale claims, and missing cross-references."
[^src-5]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Why claude-obsidian?" Table -- "Batch ingestion | Parallel agents for multiple sources"
[^src-6]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Six Wiki Modes" -- "A: Website | B: GitHub | C: Business | D: Personal | E: Research | F: Book/Course ... Modes can be combined."
[^src-7]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Cross-Project Power Move" -- "Point any Claude Code project at this vault."
[^src-8]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Header" P2 -- "Optional DragonScale Memory extension (log folds, deterministic page addresses, semantic tiling lint, boundary-first autoresearch)."
[^src-9]: `data/raw/github_repo/repo-agricidaniel-claude-obsidian/repo/README.md` -- "Why claude-obsidian?" Table -- "Multi-model support | Claude, Gemini, Codex, Cursor, Windsurf"
