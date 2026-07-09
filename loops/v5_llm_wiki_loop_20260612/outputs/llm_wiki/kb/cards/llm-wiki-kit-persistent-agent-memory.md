---
id: llm-wiki-kit-persistent-agent-memory
title: llm-wiki-kit 持久化 Agent 记忆方案
status: accepted
card_type: solution-pattern
tags:
- persistent-memory
- agent-memory
- llm-wiki
- karpathy
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-iamsashank-llm-wiki-kit
evidence_basis: code_implementation
justification: ../justification/llm-wiki-kit-persistent-agent-memory.md
canonical_concept: llm-wiki-kit-persistent-agent-memory
aliases:
- llm-wiki-kit
- llm wiki kit
- persistent agent memory
- agent wiki memory
summary: llm-wiki-kit 解决 AI agent 跨会话上下文丢失问题，让 agent 自主维护一个由 markdown 文件组成的持久化 wiki
  知识库。基于 Karpathy 的 LLM Wiki 模式，通过 MCP 协议 集成 Claude Codex Cursor Windsurf 等 agent。核心理念是
  wiki 跨会话持续积累 交叉引用不断复合增长，agent 无需每次重新教学。零锁定设计，数据就是纯 markdown 文件夹，可用 Obsidian VS Code
  等任意工具查看。
related:
- llm-wiki-kit-wiki-architecture
- llm-wiki-kit-mcp-tool-surface
- persistent-memory-motivation
---

llm-wiki-kit 是一个开源 Python 工具，解决 AI agent 跨会话持久记忆缺失的核心问题 [^src-1]。

## 问题定义

每次启动新聊天会话时，agent 无法访问先前对话中积累的知识。用户被迫反复上传材料、重新解释上下文 [^src-2]。

## 解决方案模式

agent 自主维护一个结构化 markdown wiki：
- 用户投喂源材料（PDF、URL、YouTube 视频、markdown）
- agent 自动提取内容、创建 wiki 页面、建立 `[[wiki links]]` 交叉引用
- wiki 跨会话持续存在，知识随源增加而复合增长 [^src-3]

## 设计哲学

- **零锁定**: 数据就是文件夹中的 markdown 文件，可用 Obsidian、VS Code 等查看 [^src-4]
- **markdown 优先**: 建议 git init 获得版本历史，用 Obsidian 可视化图谱
- **agent 自治**: 用户不直接编辑 wiki，agent 完成所有维护工作

## 溯源

基于 Andrej Karpathy 的 LLM Wiki 模式（公开 gist），llm-wiki-kit 是该模式的工程化实现，增加了 MCP 集成、多格式 ingest、FTS5 搜索等能力 [^src-5]。

[^src-1]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "Header" P10 -- "llm-wiki-kit gives your AI agent a persistent, structured memory that compounds over time"
[^src-2]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "The Problem" P22-30 -- "You're constantly re-teaching your agent things it should already know"
[^src-3]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "The Solution" P36-44 -- "The wiki persists. Cross-references build up. Your agent gets smarter with every source you add."
[^src-4]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "What Makes This Different" P141 -- "Zero lock-in | It's just markdown files in a folder — view in Obsidian, VS Code, anywhere"
[^src-5]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "Credits" P262 -- "Based on the LLM Wiki idea by Andrej Karpathy"
