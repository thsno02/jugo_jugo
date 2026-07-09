---
id: claude-first-multi-runtime-packaging
title: Claude-First 多运行时包装策略
status: accepted
card_type: distribution-architecture
tags:
- llm-wiki
- claude-code
- codex-plugin
- opencode
- multi-runtime
- plugin-packaging
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-nvk-llm-wiki
evidence_basis: code_implementation
justification: ../justification/claude-first-multi-runtime-packaging.md
canonical_concept: claude-first-multi-runtime-packaging
aliases:
- multi-runtime plugin
- Claude Code plugin
- Codex plugin
- OpenCode skill
- AGENTS.md portable protocol
summary: llm-wiki 采用 Claude-first 设计，维护一个行为真实源（claude-plugin/skills/wiki-manager/SKILL.md），通过同步脚本生成 Codex 和 OpenCode 的打包镜像。Codex 镜像复制 references（marketplace 缓存需要），OpenCode 使用符号链接。AGENTS.md 提供可移植单文件协议适用于任意
  LLM agent。支持 5 种客户端：Claude Code (200K context)、Codex、OpenCode、Pi (本地模型)、任意 agent。漂移由 test-codex-sync.sh 和 test-opencode-sync.sh 自动检测。
related:
- llm-as-knowledge-compiler-metaphor
- hub-topic-wiki-isolation
---

llm-wiki 的分发架构遵循"一个行为源，多个包装层"的策略：

**行为真实源**[^src-1]：
- `claude-plugin/skills/wiki-manager/SKILL.md`——完整行为规范
- `claude-plugin/commands/*.md`——命令定义
- `claude-plugin/skills/wiki-manager/references/*.md`——参考文档（运行时中立措辞）

**生成的包装镜像**：
- `plugins/llm-wiki/`（Codex）：复制的 references（marketplace 缓存需要实体文件）+ Codex 特定的 SKILL.md 文本补丁 + `agents/openai.yaml` 元数据
- `plugins/llm-wiki-opencode/`（OpenCode/Pi）：符号链接到 Claude 源的 references + OpenCode 特定文本补丁[^src-2]

**支持的客户端**：
| 客户端 | 安装方式 | 系统提示大小 | 最佳用途 |
|--------|---------|-------------|---------|
| Claude Code | plugin install | ~22K tokens | 完整 agentic 研究 |
| Codex | marketplace add | ~3K tokens | OpenAI 生态 |
| OpenCode | instructions URL | ~3K tokens | 多 provider |
| Pi | --instructions | ~1K tokens | 本地模型 |
| 任意 agent | AGENTS.md 复制 | 可变 | 通用 fallback |

**同步与漂移检测**：
- `sync-codex-plugin.sh` / `sync-opencode-plugin.sh` 从 Claude 源重新生成
- `test-codex-sync.sh` / `test-opencode-sync.sh` 自动检测漂移并提供自愈修复指令[^src-3]

[^src-1]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Claude-First, Multi-Runtime" -- "claude-plugin/skills/wiki-manager/ is the behavioral source of truth."
[^src-2]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "README.md Claude-First, Multi-Runtime" -- "Both runtime mirrors are generated, not hand-maintained."
[^src-3]: `data/raw/github_repo/repo-nvk-llm-wiki/material_bundle.txt` -- "CLAUDE.md Testing" -- "Drift is caught by ./tests/test-codex-sync.sh and ./tests/test-opencode-sync.sh"
