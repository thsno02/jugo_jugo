---
id: mcp-multi-client-integration
title: MCP 多客户端集成架构
status: accepted
card_type: integration-pattern
tags:
- mcp
- cli
- openclaw
- integration
- agent-toolchain
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- clawhub-llm-wiki-karpathy
evidence_basis: documentation
justification: ../justification/mcp-multi-client-integration.md
canonical_concept: mcp-multi-client-integration
aliases:
- MCP server
- stdio MCP
- OpenClaw
- config generator
- 多客户端集成
summary: mcp-multi-client-integration llm-wiki-karpathy 以四种形态发布：standalone CLI、 stdio
  MCP server（兼容 Claude Code/Codex/Cursor/Gemini CLI 等 MCP-capable agents）、 config
  generator（为不同 client 配线）、OpenClaw-compatible host entry（团队使用）。 CLI 与 MCP 共享同一 runtime
  contract。
related:
- llm-wiki-mcp-architecture
- llm-wiki-kit-mcp-tool-surface
- librarian-mcp-as-llm-wiki-productization
---

## MCP 多客户端集成架构

llm-wiki-karpathy 以四种形态发布 [^src-1]：

1. **Standalone CLI**: 直接执行 `kb_*` workflow 命令
2. **stdio MCP server**: 兼容 Claude Code、Codex、Cursor、Gemini CLI 及其他 MCP-capable agents
3. **Config generator**: 为不同客户端自动生成 MCP server 配线
4. **OpenClaw-compatible host entry**: 面向同时使用 OpenClaw 的团队

CLI 和 MCP 是同一 runtime contract 的不同封装 [^src-2]，MCP 暴露的工具集与 CLI 命令一一对应（共 20 个工具）。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "LLM Wiki Karpathy" P6-10 -- "@harrylabs/llm-wiki-karpathy is the deterministic runtime... It ships as:"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P29 -- "CLI and MCP wrappers around the same runtime contract"
[^card-2]: [[runtime-agent-responsibility-boundary]] — MCP 是 agent 通过标准协议调用 runtime 能力的接口
