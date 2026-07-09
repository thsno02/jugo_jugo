---
id: llm-wiki-agent-config-as-program
title: Agent Config 文件驱动范式
status: draft
card_type: design-pattern
tags: [agent, config-file, coding-agent, claude-code, codex, gemini-cli]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-samuraigpt-llm-wiki-agent]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-agent-config-as-program.md
canonical_concept: agent-config-as-program
aliases: [config-as-program, agent config file, CLAUDE.md, AGENTS.md, GEMINI.md, coding agent skill]
summary: >-
  LLM Wiki Agent 采用 agent-config-as-program 范式：不提供传统 API 或 CLI，
  而是通过标准化 config 文件(CLAUDE.md/AGENTS.md/GEMINI.md)编程 coding agent 行为。
  Agent 打开仓库时自动读取 config 获得 schema + workflow 指令，config 文件即 agent 的 instruction set。
  支持 Claude Code、Codex、OpenCode、Gemini CLI 等多种 coding agent，无需 API key 或 Python setup。
  自称为 "coding agent skill"。
related: []
---

LLM Wiki Agent 将自身定义为 "a coding agent skill"——不是独立应用程序，而是寄生于 coding agent 生态的一个可复用能力单元。[^src-1]

其核心设计模式是通过 agent config 文件来"编程"agent 行为：CLAUDE.md 供 Claude Code 读取，AGENTS.md 供 Codex / OpenCode 读取，GEMINI.md 供 Gemini CLI 读取。用户只需 `git clone` 后在对应 agent 中打开目录，agent 自动读取 config 并获得完整的 wiki 维护能力。[^src-2]

这意味着不需要 API key、Python 环境或任何额外安装——config 文件本身就是完整的 instruction set，定义了 page format、ingest/query/lint/graph workflows、naming conventions 等全部行为规范。[^src-3] [^card-1]

[^src-1]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "Introduction" P1 -- "A coding agent skill."
[^src-2]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "Install" -- "claude # reads CLAUDE.md ... codex # reads AGENTS.md ... gemini # reads GEMINI.md"
[^src-3]: `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md` -- "CLAUDE.md / AGENTS.md" -- "The schema file tells the agent how to maintain the wiki — page formats, ingest/query/lint/graph workflows, naming conventions."
[^card-1]: llm-wiki-agent-compile-once-architecture — config 文件中定义的 workflow 即是编译式架构的具体实现
