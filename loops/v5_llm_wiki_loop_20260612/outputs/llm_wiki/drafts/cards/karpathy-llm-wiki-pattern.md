---
id: karpathy-llm-wiki-pattern
title: Karpathy LLM Wiki 模式
status: draft
card_type: concept-definition
tags: [llm-wiki, personal-knowledge-management, maintenance-loop]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/karpathy-llm-wiki-pattern.md
canonical_concept: karpathy-llm-wiki-pattern
aliases: [LLM Wiki, LLM Wiki pattern, Karpathy's LLM Wiki]
summary: >-
  Karpathy LLM Wiki pattern 由 raw/ 不可变源文件夹、wiki/ LLM 生成页面、CLAUDE.md schema 组成；LLM 循环执行编译/反向链接/矛盾检测/健康检查四项维护操作；类比 Obsidian=IDE LLM=programmer wiki=codebase；核心创新在 maintenance loop 而非 search
related: []
---

Karpathy 的 LLM Wiki 是一种个人知识管理模式：将纯 Markdown 知识库交由 LLM 编译和维护，使其随时间复利式增长。[^src-1]

**组成结构**：
- `raw/` 文件夹：不可变源材料（文章、论文、转录、笔记）
- `wiki/` 文件夹：LLM 生成的结构化页面（摘要、概念文章、交叉引用、索引）
- `CLAUDE.md` schema 文件：告诉 agent 如何操作整个 vault

**LLM 循环执行的四项操作**：
1. 将 raw 源编译为结构化 wiki 页
2. 创建和维护页面间反向链接，使多源出现的概念相互连接
3. 当同一事实在不同源中出现差异时，标记矛盾与缺口
4. 运行周期性健康检查（lint 一致性/缺失上下文/过时信息）

Karpathy 将此工作流类比为：Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。用户探索和提问，LLM 承担维护工作。[^src-2]

[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "What Karpathy's LLM Wiki does" P14 -- "There's a raw/ folder where source material goes... There's a wiki/ folder of LLM-generated pages... And there's a CLAUDE.md schema file that tells the agent how to operate on the vault."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "What Karpathy's LLM Wiki does" P16 -- "Karpathy describes the workflow as Obsidian being the IDE, the LLM being the programmer, and the wiki being the codebase."
