---
id: llm-wiki-mcp-skills-vs-tools-workflow
title: llm-wiki-mcp 的 skill 层 vs tool 层：工具给能力，skill 给 workflow
status: accepted
card_type: distinction
tags: [#llm-wiki-mcp, #claude-code, #skills, #workflow]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T14:22:00+08:00
edited_entity: llm
source_ids: [pypi-llm-wiki-mcp]
provenance_card: ../provenance/llm-wiki-mcp-skills-vs-tools-workflow.md
aliases: [wiki-init, wiki-ingest, wiki-query, wiki-lint, skills vs tools]
related: [llm-wiki-mcp-four-tools, karpathy-llm-kb-three-operations, cognition-human-approved-skill-md, llm-wiki-mcp-design-boundary-mechanics-not-content]
---

## 两层分工

`llm-wiki-mcp` 给 Claude Code 用户提供两个互补的层：

- **Tool 层（4 个 MCP tool）**：`wiki_read` / `wiki_write_page` / `wiki_log_append` / `wiki_inventory` [^v3-1]，给 agent **能力**——能读写、能查整张图、能写日志。
- **Skill 层（4 个 Claude Code skill）**：`wiki-init` / `wiki-ingest` / `wiki-query` / `wiki-lint` [^src1]，给 agent **workflow**——告诉它每种意图下应该按什么顺序调哪些 tool、应该补哪些 bookkeeping。

## 四个 skill 对应的工作流

| Skill | 用户说什么 | 是否需要 MCP server |
|---|---|---|
| `wiki-init` | "在 ~/wikis/ai-safety 给我搭一个 AI safety 主题的 LLM wiki" | No（一次性 scaffolder） |
| `wiki-ingest` | "把 https://arxiv.org/abs/2310.12345 这篇 ingest 进 wiki" | Yes |
| `wiki-query` | "wiki 里关于 steering vectors 怎么说？" | Yes |
| `wiki-lint` | "跑一次 wiki 体检" | Yes |

`wiki-init` 是一次性脚手架；其余三个对应 Karpathy 原始 gist 提出的三大操作（Ingest / Query / Lint） [^v3-2]。

## 为什么 skill 层必要

> "Other MCP clients (Claude Desktop, Cursor) get the four tools but not the skills. The agent has to derive the workflow from tool descriptions alone, which works for one-off reads and writes but tends to skip the bookkeeping (log entries, backlink audits) the skills make explicit."
> —— `text.txt:153` [^src3]

只给 tool 不给 workflow，agent 能完成单次读写，但会**跳过 bookkeeping**（log entry、backlink 审计、contradiction 标注）。这些 bookkeeping 正是让 wiki 长期不退化的关键，必须用 skill 把"必做步骤"显式编码出来 [^v3-3]。

## 关键设计选择：每次都重读 schema

> "Each skill reads wiki/CLAUDE.md for the active schema on every run, so you can evolve the schema without re-installing anything."
> —— `text.txt:139` [^src2]

skill 不把 schema 硬编码进自己的 prompt，而是**每次运行都重新读** `wiki/CLAUDE.md`。这让用户可以在 wiki 本地迭代 schema，不需要重装 plugin，也避免 skill 与 schema 版本漂移 [^v3-4]。

## 分发方式

- skill 通过 Claude Code 的 plugin marketplace 安装：
  ```
  claude plugin marketplace add https://github.com/flsteven87/llm-wiki-mcp
  claude plugin install llm-wiki-skills@llm-wiki-mcp
  ```
- 这些 skill 以 package data 形式打包在 `llm_wiki_mcp/skills/` 下，**也可以通过 `importlib.resources`** 由非 Claude Code 的 agent 加载 [^src4]。

## 操作含义

- 用 Claude Code 时：装 skills 是默认推荐；不装就要在 prompt 里手动告诉 agent "ingest 后记得 log_append + 检查 backlink"。
- 用 Claude Desktop / Cursor 时：只有 tool，没有 workflow guard；agent 一致性靠用户 prompt 兜底，或者参考 README 自己写 system prompt 模拟 skill。
- 不用 Claude 系列时：可通过 `importlib.resources` 把 skill markdown 取出来塞进自己的 agent system prompt。

## Footnotes

[^src1]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 141–151 行，四个 skill 列表与对应问句（含 `text.txt:151` verbatim："wiki-init is a one-shot scaffolder; the other three are Karpathy's three operations."）。
[^src2]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 139 行 verbatim："Each skill reads wiki/CLAUDE.md for the active schema on every run, so you can evolve the schema without re-installing anything."
[^src3]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 153 行 verbatim："Other MCP clients (Claude Desktop, Cursor) get the four tools but not the skills. The agent has to derive the workflow from tool descriptions alone, which works for one-off reads and writes but tends to skip the bookkeeping (log entries, backlink audits) the skills make explicit."
[^src4]: `data/raw/pypi/pypi-llm-wiki-mcp/text.txt` — 第 195 行，非 Claude 用户通过 `importlib.resources` 加载 skill markdown 的说明。
[^v3-1]: [llm-wiki-mcp-four-tools](llm-wiki-mcp-four-tools.md) — 四个 MCP tool 的契约（annotation / CAS / 故意留白）。
[^v3-2]: [karpathy-llm-kb-three-operations](karpathy-llm-kb-three-operations.md) — Karpathy "LLM KB" 的三个操作 Ingest / Query / Lint，是 skill 层 wiki-ingest / wiki-query / wiki-lint 的概念源头。
[^v3-3]: [cognition-human-approved-skill-md](cognition-human-approved-skill-md.md) — Cognition 把 SKILL.md 作为人工审批闸门，与本卡 "skill 把必做步骤显式编码出来" 是同一思路的不同实例化。
[^v3-4]: [llm-wiki-mcp-design-boundary-mechanics-not-content](llm-wiki-mcp-design-boundary-mechanics-not-content.md) — server 不烧 schema 进去，skill 每次重读 `wiki/CLAUDE.md` 正是这条边界在 skill 层的对应物。
