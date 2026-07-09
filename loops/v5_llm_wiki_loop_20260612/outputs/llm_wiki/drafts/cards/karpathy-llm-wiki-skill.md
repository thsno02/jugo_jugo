---
id: karpathy-llm-wiki-skill
title: karpathy-llm-wiki 可复用 Agent Skill 实现
status: draft
card_type: tool-implementation
tags: [agent-skills, karpathy, llm-wiki, ingest-query-lint]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-astro-han-karpathy-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/karpathy-llm-wiki-skill.md
canonical_concept: karpathy-llm-wiki-skill
aliases: [karpathy-llm-wiki, Astro-Han/karpathy-llm-wiki, npx add-skill karpathy-llm-wiki]
summary: >-
  karpathy-llm-wiki 是 Karpathy LLM Wiki gist 的非官方社区实现，打包为 agentskills.io
  标准的可复用 Agent Skill。提供三个核心操作：Ingest（收集源到 raw/ 并编译为 wiki 页面）、
  Query（检索 wiki 并带 citations 引用回答）、Lint（检查 index 完整性、links 链接和 wiki
  健康度）。通过 npx add-skill 安装，兼容 Claude Code、Cursor、Codex CLI、OpenCode。
  生产环境数据：94 篇文章、13 个主题目录、99 个源、自 2026-04 起每日维护。
related: [llm-wiki-knowledge-system, llm-wiki-vs-rag]
---

`karpathy-llm-wiki` 是 Karpathy LLM Wiki 思想的非官方社区实现，将其打包为一个遵循 agentskills.io 开放标准的可复用 Agent Skill。[^src-1]

## 三个核心操作

| 操作 | 功能 | 输出 |
|------|------|------|
| **Ingest** | 收集源材料到 `raw/` 并编译为 wiki | 新建或更新 wiki 页面 |
| **Query** | 检索 wiki 并带引用回答 | 链接到 markdown 页面的基于事实的回答 |
| **Lint** | 检查 index 完整性、链接、wiki 健康度 | 自动修复和问题报告 |

[^src-2]

## 安装与兼容性

通过 `npx add-skill Astro-Han/karpathy-llm-wiki` 安装，兼容支持 Agent Skills 标准的各类工具：Claude Code、Cursor、Codex CLI、OpenCode 等。[^src-3]

## 生产环境验证

据材料报告，基于自 2026 年 4 月起每日维护的生产知识库：94 篇 wiki 文章、13 个主题目录、99 个源材料、近 7 天 87 条操作日志。[^src-4]

## 独特贡献

其价值在于可复用的工作流（reusable workflow）、prompt 结构、以及经过实战验证的知识编译规则（battle-tested knowledge-compilation rules）。同领域项目还有 lucasastorian/llmwiki 和 atomicmemory/llm-wiki-compiler。[^src-5] [^card-1]

---
[^src-1]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "Inspired By" P1 -- "Unofficial community implementation of the workflow from Karpathy's LLM Wiki idea."
[^src-2]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "What Is an LLM Wiki?" P2 -- "This skill gives you three operations: Ingest / Query / Lint"
[^src-3]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "Tool Compatibility" P1 -- "This skill follows the agentskills.io open standard"
[^src-4]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "Usage Stats" P1 -- "94 wiki articles across 13 topic directories, 99 source materials ingested, 87 operation log entries"
[^src-5]: data/raw/github_repo/repo-astro-han-karpathy-llm-wiki/repo/README.md -- "Inspired By" P2 -- "The value here is the reusable workflow, prompt structure, and battle-tested knowledge-compilation rules."
[^card-1]: llm-wiki-knowledge-system -- LLM wiki 核心架构定义
