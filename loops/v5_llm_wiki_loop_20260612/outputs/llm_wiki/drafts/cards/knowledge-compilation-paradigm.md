---
id: knowledge-compilation-paradigm
title: 知识编译范式
status: draft
card_type: architectural-concept
tags: [knowledge-compilation, wiki, paradigm, llm-wiki]
created_time: 2026-06-12T19:00:00+08:00
edited_time: 2026-06-12T19:00:00+08:00
edited_entity: llm
source_ids: [repo-sdyckjq-llm-wiki-skill]
evidence_basis: code_implementation
justification: ../justification/knowledge-compilation-paradigm.md
canonical_concept: knowledge-compilation-paradigm
aliases: [知识编译, knowledge compilation, 编译一次持续维护, compile-once maintain-forever]
summary: >-
  llm-wiki 的核心架构范式：知识被编译一次、持续维护，而非每次查询从原始文档重新推导。AI agent 在 ingest 阶段将原始素材分析后生成结构化 wiki 页面（实体页、主题页、摘要），查询时直接读取已编译产物。区别于 RAG 的每次查询时检索并推导模式。原始素材不可变存于 raw/，编译产物存于 wiki/。源自 Karpathy llm-wiki 方法论。
related: [digital-landscape-knowledge-graph, confidence-level-annotation]
---

llm-wiki 项目的核心架构范式是"知识编译"：知识被编译一次、持续维护，而不是每次查询都从原始文档重新推导。[^src-1]

具体而言，AI agent 在 ingest（消化）阶段将原始素材分析后生成结构化 wiki 页面——包括实体页（人物、概念、工具）、主题页、素材摘要等——之后查询时直接读取已编译的 wiki 产物，不再回溯原文。这与 RAG（检索增强生成）的"每次查询时检索原始文档并重新推导"模式形成对比。[^src-2]

目录结构体现了该范式的分离原则：raw/ 存放原始素材（不可变），wiki/ 存放 AI 生成的结构化页面。[^src-3]

该方法论源自 Andrej Karpathy 的 llm-wiki gist。[^src-4]

[^src-1]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "30 秒上手" -- "知识被编译一次，持续维护，而不是每次查询都从原始文档重新推导"
[^src-2]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "核心亮点" -- "自动生成实体页、主题页、素材摘要，用 [[双向链接]] 互相关联"
[^src-3]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "目录结构" -- "raw/ # 原始素材（不可变）... wiki/ # AI 生成的知识库"
[^src-4]: `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md` -- "致谢" -- "Andrej Karpathy — llm-wiki gist，核心方法论来源"
