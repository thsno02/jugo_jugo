---
id: three-layer-architecture
title: 三层架构
status: accepted
card_type: concept
tags: [llm-wiki, architecture]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/three-layer-architecture.md
canonical_concept: three-layer-architecture
aliases: [三层架构, three layers, raw-wiki-schema]
summary: >-
  three-layer-architecture（三层架构 / three layers / raw-wiki-schema）是 LLM Wiki 的三层结构：
  不可变原始资料层（source of truth）、LLM 拥有的 wiki 层（markdown 页面）、人机共同演化的 schema 层
related: []
---

LLM Wiki 的架构由三层组成[^src-1]：

**原始资料层（Raw Sources）**——用户策展的源文档集合：文章、论文、图片、数据文件。这一层是不可变的——LLM 只读取不修改，是整个系统的 source of truth。

**Wiki 层**——由 LLM 生成的 markdown 文件目录：摘要、实体页面、概念页面、比较、概览、综合。LLM 完全拥有这一层——创建页面、在新资料到达时更新、维护交叉引用、保持一致性。用户只阅读，LLM 负责写入[^src-2]。

**Schema 层**——一份配置文档（如 Claude Code 的 CLAUDE.md 或 Codex 的 AGENTS.md），告知 LLM wiki 的结构、约定和工作流程。这是关键配置文件——它使 LLM 成为有纪律的 wiki 维护者而非通用聊天机器人。用户和 LLM 随使用经验共同演化 schema[^src-3]。Schema 层的详细配置角色和共同演化机制见专题卡[^card-1]。原始资料层的不可变性对源忠实性风险的锚点意义见风险卡[^card-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture" 开头 -- "There are three layers"
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The wiki" -- "The LLM owns this layer entirely. It creates pages, updates them when new sources arrive, maintains cross-references"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > The schema" P1 -- "it's what makes the LLM a disciplined wiki maintainer rather than a generic chatbot. You and the LLM co-evolve this over time"
[^card-1]: [Schema 文件的配置角色](schema-as-configuration.md) -- 本卡是架构概览，该卡展开 schema 层的配置角色和共同演化机制
[^card-2]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 原始资料层的不可变性是防止 wiki 知识漂移的结构性锚点
