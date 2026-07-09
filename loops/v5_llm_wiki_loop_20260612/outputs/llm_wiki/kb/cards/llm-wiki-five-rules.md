---
id: llm-wiki-five-rules
title: LLM Wiki 五条规则
status: accepted
card_type: principle-set
tags:
- llm-wiki
- rules
- compile-first
- writeback
- wiki-before-rag
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-ss1024ss-llm-wiki
evidence_basis: code_implementation
justification: ../justification/llm-wiki-five-rules.md
canonical_concept: llm-wiki-five-rules
aliases:
- Five rules
- 五条规则
- LLM Wiki rules
summary: 'LLM Wiki 五条规则 (llm-wiki-five-rules): (1) Compile-first 不只回答要写入 wiki； (2) Writeback is mandatory 每个决策必须回写 wiki；(3) Wiki before RAG ~100 docs 内直读无需向量库； (4) Obsidian is replaceable paradigm is not
  引擎是 LLM+filesystem+markdown； (5) Ideas outrank Code wiki 决策比代码更有价值。强制性递进关系。'
related:
- llm-compilation-paradigm
- raw-wiki-code-architecture
---

LLM Wiki 系统定义了五条操作规则，构成其工程纪律的核心：[^src-1]

1. **Compile-first** — 不只是回答问题，要将结论写入 wiki 页面。
2. **Writeback is mandatory** — 每一个决策都必须回写到 wiki。"Every single one."
3. **Wiki before RAG** — ~100 docs（~80k tokens）以内，LLM 直接读取，无需向量数据库。
4. **Obsidian is replaceable, the paradigm is not** — 引擎是 LLM + filesystem + markdown，工具可换范式不可换。
5. **Ideas outrank Code** — wiki 中的决策和公式比它生成的代码更有价值。

规则间似乎呈递进补充关系：compile-first 是基础行为，writeback 是强制约束（措辞最强硬），ideas-outrank-code 是最终价值判断。[^src-2] [^card-1] [^card-2]

[^src-1]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "The Idea" P3 -- "1. Compile-first — Don't just answer. Write conclusions into wiki pages. 2. Writeback is mandatory — Every decision goes back to the wiki. Every single one."
[^src-2]: `data/raw/github_repo/repo-ss1024ss-llm-wiki/repo/README.md` -- "The Idea" P3 -- "5. Ideas outrank Code — Your wiki of decisions and formulas is worth more than the code it generates."
[^card-1]: llm-compilation-paradigm — 五条规则是编译范式的操作化表达
[^card-2]: raw-wiki-code-architecture — 规则 3 (wiki-before-RAG) 直接约束三层架构的读取策略
