---
id: llm-wiki-local-api-agent-skill
title: LLM Wiki 本地 API 与 AI Agent 技能集成
status: draft
card_type: integration-interface
tags: [api, agent-skill, llm-wiki, http-api, claude-code, codex]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-nashsu-llm-wiki]
evidence_basis: code_implementation
justification: ../justification/llm-wiki-local-api-agent-skill.md
canonical_concept: llm-wiki-local-api-agent-skill
aliases: [Local HTTP API, AI Agent Skill, llm_wiki_skill, 本地 API, agent skill integration]
summary: >-
  LLM Wiki 内置本地 HTTP API（127.0.0.1:19828，token 保护）：支持 hybrid search（keyword + vector）、
  文件读取、wikilinks graph 遍历、sources rescan。配套 agent skill（npx skills add）可一键安装到
  Claude Code / Codex，使外部 AI agent 能查询本地运行的 wiki，只读模式并引用 wiki 页面路径。
related: []
---

LLM Wiki 内置本地 HTTP API，绑定 `127.0.0.1:19828`（仅本地访问，token 保护），使外部工具和 AI agent 能够程序化地查询知识库：

**API 端点**：
- `GET /api/v1/health` — 服务状态（无需认证）
- `GET /api/v1/projects` — 列出项目
- `GET /api/v1/projects/{id}/files` / `files/content` — 读取文件和内容
- `POST /api/v1/projects/{id}/search` — 混合检索（keyword + vector），返回 mode / tokenHits / vectorHits / per-result vectorScore
- `GET /api/v1/projects/{id}/graph` — wikilinks 图
- `POST /api/v1/projects/{id}/sources/rescan` — 触发后端重扫描

**Agent Skill 集成**：
配套的 agent skill 仓库（github.com/nashsu/llm_wiki_skill）可通过一条命令安装到 Claude Code / Codex 或任何 skills 兼容运行时：

```
npx skills add https://github.com/nashsu/llm_wiki_skill.git --skill llm_wiki_skill
```

安装后，agent 可响应如"我的 LLM Wiki 里关于 X 说了什么"、"search my 知识库 for Y"、"show the neighborhood of node Z"等提示。该 skill 默认只读，引用 wiki 页面路径供用户在应用内验证。触发规则有意限制——仅在用户明确提到 "LLM Wiki" / "my wiki" / "知识库" 时触发，不响应泛化的"搜索笔记"请求。[^src-1] [^card-1]

[^src-1]: `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md` -- "Local HTTP API + AI Agent Skill" P410-434 -- "built-in local HTTP API at http://127.0.0.1:19828 (token-protected, 127.0.0.1-only) so external tools — including AI agents like Claude Code, Codex..."
[^card-1]: 参见 [[llm-wiki-multi-phase-query-pipeline]] 了解 search 端点底层使用的检索管线
