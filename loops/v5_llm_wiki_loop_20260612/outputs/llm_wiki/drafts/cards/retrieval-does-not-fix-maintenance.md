---
id: retrieval-does-not-fix-maintenance
title: 检索工具不解决维护问题
status: draft
card_type: critique
tags: [retrieval, semantic-search, glean, notion-ai, confluence, maintenance-loop]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [falconer-enterprise-guide]
evidence_basis: practitioner_report
justification: ../justification/retrieval-does-not-fix-maintenance.md
canonical_concept: retrieval-does-not-fix-maintenance
aliases: [retrieval doesn't solve this, 检索不解决维护, semantic search over stale content]
summary: >-
  Glean Notion-AI Confluence-search 等企业检索工具只解决找到已捕获内容而不解决底层维护问题；语义搜索指向过时知识库返回自信但错误答案 better retrieval over bad context delivers wrong answers more quickly；LLM Wiki 有趣之处在 maintenance loop 非 search layer
related: [maintenance-loop-as-core-innovation, context-rot-vs-compounding]
---

材料论证：市场上多数企业知识工具（Glean、Notion AI、Confluence search）本质上是检索工具——让已捕获的内容更容易被找到——但检索不修复底层的维护问题。[^card-1]

核心论据："A semantic search engine pointed at a stale knowledge base returns confidently-worded answers from documents that haven't been true since Q2."——语义搜索引擎指向过时知识库，返回措辞自信但内容已过时的答案。[^src-1]

材料的一句话总结："Better retrieval over bad context delivers wrong answers more quickly than slow retrieval over bad context."——更好的检索覆盖坏上下文只是更快地产出错误答案。[^src-2]

这一批判将检索工具定位为必要但不充分条件：它们处理了四属性中的部分（如 capture 和查询），但不处理维护循环——而维护循环是系统保持准确的关键。[^card-2]

[^card-1]: 参见 [[maintenance-loop-as-core-innovation]] 中维护循环与检索层的区分
[^card-2]: 参见 [[context-rot-vs-compounding]] 中腐烂路径的论述
[^src-1]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Why retrieval tools don't solve this" P62 -- "A semantic search engine pointed at a stale knowledge base returns confidently-worded answers from documents that haven't been true since Q2."
[^src-2]: `data/raw/webpage/falconer-enterprise-guide/markdown.md` -- "Why retrieval tools don't solve this" P62 -- "Better retrieval over bad context delivers wrong answers more quickly than slow retrieval over bad context."
