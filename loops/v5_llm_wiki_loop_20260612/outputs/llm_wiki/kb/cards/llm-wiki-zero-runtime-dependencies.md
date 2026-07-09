---
id: llm-wiki-zero-runtime-dependencies
title: 零运行时依赖设计
status: accepted
card_type: design-principle
tags:
- llm-wiki
- zero-dependency
- markdown-native
- host-agent-tools
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-zero-runtime-dependencies.md
canonical_concept: zero-runtime-dependencies
aliases:
- zero dependencies
- no servers
- markdown native
- 零依赖
summary: zero-runtime-dependencies 设计原则：无服务器无服务无遥测，仅使用宿主 agent 内置工具（文件读写 web fetch web search），插件本身就是 Markdown（命令定义 skills 参考文档），编译查询 lint 生成可离线，研究摄取需网络，可选集成 ask-grok-mcp 和 tobi/qmd
related:
- llm-wiki-five-install-modes
- llm-wiki-hub-architecture
- llm-wiki-icloud-shared-hub
---
llm-wiki 奉行零运行时依赖原则：不运行服务器、不启动服务、不收集遥测。它完全运行在宿主 agent 的内置工具（文件读写、web fetch、web search）之上。[^src-1]

插件本身就是 Markdown：命令定义、skills 和参考文档。这使得编译、查询、lint 和生成制品可以完全离线工作——所有内容都是磁盘上的纯 Markdown。研究和摄取功能需要网络，因为它们获取 URL 和搜索 web。[^src-2]

可选集成包括 ask-grok-mcp（tweet 摄取）和 tobi/qmd（超过约 100 篇文章时的本地搜索）。[^src-3]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "FAQ" P310 -- "Zero runtime dependencies. LLM Wiki uses only the built-in tools of the host agent (file read/write, web fetch, web search)."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "FAQ" P309 -- "Compiling, querying, linting, and generating artifacts from an existing wiki work offline — everything is plain Markdown on your disk."
[^src-3]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "FAQ" P311 -- "Optional: ask-grok-mcp for best-in-class tweet ingestion, tobi/qmd for local search beyond ~100 articles."
