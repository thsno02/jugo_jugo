---
id: obsidian-wiki-agent-agnostic-skill-framework
title: obsidian-wiki 代理无关的 skill 框架设计
status: draft
card_type: design-decision
tags: [agent-agnostic, skill-file, multi-agent, setup-sh, symlink]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [repo-ar9av-obsidian-wiki]
evidence_basis: code_implementation
justification: ../justification/obsidian-wiki-agent-agnostic-skill-framework.md
canonical_concept: agent-agnostic-skill-framework
aliases: [agent-agnostic, multi-agent skills, skill-based framework, Agent Skills spec]
summary: >-
  obsidian-wiki 采用代理无关设计（agent-agnostic-skill-framework）：
  整个框架是一组 markdown skill 文件（.skills/ 目录），不依赖特定 agent SDK。
  setup.sh 自动将 skill 目录 symlink 到 16+ 种代理的发现路径（Claude Code、Cursor、
  Windsurf、Codex、Gemini CLI、Kiro、Pi 等）。兼容 Agent Skills spec（agentskills.io）。
  技能通过 slash commands 或自然语言描述触发。
related: [obsidian-wiki-compile-not-retrieve-pattern]
---

obsidian-wiki 的一个关键设计决策是代理无关（agent-agnostic）：框架由一组 markdown skill 文件构成，任何能读取文件的 AI 编码代理均可驱动[^src-1]。

**实现机制**：所有技能定义位于 `.skills/` 目录。`setup.sh` 脚本自动将该目录 symlink 到各代理的 skills 发现路径[^src-2]：
- Claude Code: `.claude/skills/` + `~/.claude/skills/`
- Cursor: `.cursor/skills/`
- Windsurf: `.windsurf/skills/`
- Codex: `~/.codex/skills/`
- Gemini CLI: `~/.gemini/skills/`
- 以及 Kiro、Pi、Hermes、OpenClaw、Copilot、Trae、Aider、Factory Droid 等

该框架支持 16+ 种代理[^src-3]，并兼容 [Agent Skills spec](https://agentskills.io/specification)，可与其他 skill 包（如 kepano/obsidian-skills）无冲突共存[^src-4]。

安装方式支持 `npx skills add Ar9av/obsidian-wiki`（Skills CLI）或 `git clone` + `bash setup.sh`[^src-5]。

[^card-1]: [obsidian-wiki-compile-not-retrieve-pattern] — skill 框架是编译式模式的执行载体

[^src-1]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Header" P2 -- "The whole thing is a set of markdown skill files that any AI coding agent (Claude Code, Cursor, Windsurf, Pi, whatever you use) can read and execute."
[^src-2]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Project Structure" P1 -- ".skills/ — Canonical skill definitions (source of truth)"
[^src-3]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Agent Compatibility" P1 -- "Works with any AI coding agent that can read files — Claude Code, Cursor, Windsurf, Pi, Codex, Gemini CLI, Kiro, and more."
[^src-4]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Recommended: Obsidian Skills by Kepano" P1 -- "Both projects use the same Agent Skills spec, so they coexist in the same .skills/ directory with no conflicts."
[^src-5]: data/raw/github_repo/repo-ar9av-obsidian-wiki/repo/README.md -- "Quick Start" P1 -- "npx skills add Ar9av/obsidian-wiki"
