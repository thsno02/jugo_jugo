---
id: openkb-two-layer-architecture
title: OpenKB 双层架构——Wiki Foundation 与 Generators
status: accepted
card_type: system-architecture
tags:
- openkb
- two-layer-architecture
- wiki-foundation
- generators
- knowledge-compilation
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-vectifyai-openkb
evidence_basis: code_implementation
justification: ../justification/openkb-two-layer-architecture.md
canonical_concept: openkb-two-layer-architecture
aliases:
- wiki foundation
- generators
- two layers
- wiki compilation layer
summary: OpenKB openkb-two-layer-architecture 双层架构; wiki-foundation编译维护知识(init/add/remove/watch/lint); generators将wiki转化为输出(query/chat/skill-factory); wiki是基底generators是表面; 添加文档时LLM生成summary读取已有concepts创建更新跨文档综合更新index和log;
  单个源可触及10-15个wiki页面知识累积
related:
- openkb-compiled-wiki-over-rag
- openkb-pageindex-vectorless-retrieval
- openkb-skill-factory
---

OpenKB 采用双层架构设计：wiki foundation（编译与维护层）和 generators（输出生成层）。Wiki 是基底，generators 是表面。[^src-1] [^card-1]

**Wiki Foundation** 负责编译和维护知识，包含命令：init（初始化）、add（添加文档并编译至 wiki）、remove（移除文档并清理 wiki 页面）、watch（监控 raw/ 自动编译）、lint（结构与知识健康检查）、list、status。Wiki 目录结构包含 index.md（概览）、log.md（操作时间线）、AGENTS.md（wiki schema / LLM 指令）、sources/、summaries/、concepts/（跨文档综合）、explorations/、reports/。[^src-2]

**知识编译流程**：添加文档时，LLM 执行四步——1) 生成 summary 页；2) 读取已有 concept 页；3) 创建或更新 concepts 实现跨文档综合；4) 更新 index 和 log。单个源可能触及 10-15 个 wiki 页面，每个文档丰富现有 wiki 而非孤立存在。[^src-3]

**Generators** 读取已编译的 wiki 产出有用输出：query（带引用的单问答）、chat（交互式多轮对话）、Skill Factory（蒸馏为可分发技能）。[^src-4]

[^card-1]: 参见 [[openkb-compiled-wiki-over-rag]] 关于编译式 wiki 设计哲学
[^src-1]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "What is OpenKB" P2 -- "OpenKB has two layers: a wiki foundation that compiles and maintains your knowledge, and generators (query / chat / Skill Factory) that turn it into useful output."
[^src-2]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Wiki Foundation — compile and maintain" P1 -- command table
[^src-3]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Knowledge Compilation" P1 -- "A single source might touch 10-15 wiki pages. Knowledge accumulates: each document enriches the existing wiki rather than sitting in isolation."
[^src-4]: `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md` -- "Generators — turn the wiki into output" P1 -- "A 'generator' reads from the compiled wiki and produces something usable: an answer, a conversation, a skill folder."
