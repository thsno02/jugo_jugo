---
id: llm-wiki-five-install-modes
title: 五种安装模式与跨运行时统一
status: accepted
card_type: system-architecture
tags:
- llm-wiki
- installation
- claude-code
- codex
- opencode
- pi
- agents-md
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-five-install-modes.md
canonical_concept: five-install-modes
aliases:
- install modes
- plugin installation
- 安装模式
- cross-runtime
summary: five-install-modes 跨运行时统一：Claude Code 原生插件（推荐）、OpenAI Codex marketplace 插件（@wiki 调用）、OpenCode 指令文件、Pi 指令文件（适合本地模型 32K 上下文）、AGENTS.md 可移植文件；行为逻辑在单一 wiki-manager skill 中共享，Codex/OpenCode/Pi symlink
  到 Claude 源，自愈同步测试防漂移
related:
- llm-wiki-zero-runtime-dependencies
- llm-wiki-hub-architecture
---

llm-wiki 提供五种安装模式适配不同 LLM agent 环境：
1. **Claude Code**：原生插件，通过 marketplace 安装（`claude plugin install wiki@llm-wiki`），推荐方式
2. **OpenAI Codex**：marketplace 插件（`codex plugin marketplace add nvk/llm-wiki`），用 @wiki 调用
3. **OpenCode**：指令文件通过 opencode.json 引入 skill 路径
4. **Pi**：指令文件，1K system prompt 为 32K 上下文本地模型留出空间
5. **AGENTS.md**：可移植文件，放入任何能读写文件+搜索 web 的 agent 上下文[^src-1]

关键统一设计：行为逻辑存在于单一 wiki-manager skill 中，跨运行时共享。Codex、OpenCode 和 Pi tree 通过 symlink 指向 Claude source of truth，确保无 fork。自愈同步测试（self-healing sync tests）捕获漂移。[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Install" P293 -- "Five install modes: Claude Code (native plugin via the llm-wiki marketplace), OpenAI Codex (marketplace plugin), OpenCode (instruction file), Pi (instruction file — best for local models), and any other LLM agent via the portable AGENTS.md file."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Architecture" P294 -- "The behavioral logic lives in a single wiki-manager skill shared across runtimes — Codex, OpenCode, and Pi trees symlink into the Claude source of truth so there is no fork. Drift is caught by self-healing sync tests."
