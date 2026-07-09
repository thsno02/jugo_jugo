---
id: karpathy-llm-wiki-pattern-automation
title: Karpathy LLM Wiki 模式的产品化实现
status: accepted
card_type: design-pattern
tags:
- karpathy
- llm-wiki-pattern
- automation
- source-types
- detail-level
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-ndjordjevic-pin-llm-wiki
evidence_basis: code_implementation
justification: ../justification/karpathy-llm-wiki-pattern-automation.md
canonical_concept: karpathy-llm-wiki-pattern-automation
aliases:
- Karpathy LLM Wiki pattern
- LLM wiki pattern
- pin-llm-wiki ingest pipeline
summary: 'pin-llm-wiki 将 Karpathy 提出的"给 LLM 建本地 wiki"理念产品化: 自动 ingest URL->raw capture->wiki page->cross-link->agent可读。 三种源类型(GitHub/YouTube/Web)各有专用fetch工具(gh/yt-dlp/crawler), detail level(brief/standard/deep)控制抓取深度,
  deep模式支持 companion repo发现和多产品站点拆分。支持 Claude Code/Cursor/GitHub Copilot。'
related:
- pin-llm-wiki-architecture
- pin-llm-wiki-agent-consumption-protocol
- karpathy-llm-wiki-pattern
- llm-compilation-paradigm
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-pattern-overview
- llm-wiki-persistent-knowledge-compilation
- llmwiki-compile-first-architecture
- obsidian-wiki-compile-not-retrieve-pattern
---

pin-llm-wiki 将 Karpathy 提出的"给 LLM 建本地 wiki"理念（源自其公开 gist）自动化为多编辑器 skill [^src-1]。核心流程为：URL 投入 → raw capture → wiki page 生成 → wikilink 交叉引用 → agent 可查阅。

**三种源类型的 detail-aware fetch 策略** [^src-2]：

| 源类型 | 工具 | 策略 |
|--------|------|------|
| GitHub repo | `gh` CLI | metadata + README + repo layout；deep 模式抓更多 docs/，可选 clone |
| YouTube | `yt-dlp` | description + chapters + cleaned transcript（或 no-transcript 标记） |
| Web page | crawler | landing + docs + llms.txt/sitemap；deep 模式可拆分多产品站点为 hub + 子页 |

detail level 分三档（brief / standard / deep），控制 fetch 广度与深度。Web 类型的 deep 模式支持 companion GitHub repo 自动发现并合并为统一页面 [^src-3]。

该 skill 支持三编辑器统一工作流：Claude Code（slash commands）、Cursor、GitHub Copilot，均使用同一 SKILL.md [^card-1]。

[^src-1]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Title" P1-3 -- "A multi-editor skill that automates the Karpathy LLM Wiki pattern: drop in URLs, get a local, citable, cross-referenced wiki that agents can read before answering."
[^src-2]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Source types" P103-113 -- "Fetches are detail-aware: broader at standard / deep than at brief."
[^src-3]: `data/raw/github_repo/repo-ndjordjevic-pin-llm-wiki/repo/README.md` -- "Source types" P110 -- "often pulls a companion GitHub repo into one unified page unless <!-- no-companion -->"
[^card-1]: pin-llm-wiki-architecture
