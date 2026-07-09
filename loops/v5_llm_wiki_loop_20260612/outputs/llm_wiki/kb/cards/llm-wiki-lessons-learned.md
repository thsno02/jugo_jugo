---
id: llm-wiki-lessons-learned
title: Lessons Learned 会话经验提取
status: accepted
card_type: mechanism
tags:
- llm-wiki
- lessons-learned
- error-patterns
- self-improvement
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- llm-wiki-net
evidence_basis: documentation
justification: ../justification/llm-wiki-lessons-learned.md
canonical_concept: lessons-learned-extraction
aliases:
- lessons learned
- /wiki:ll
- error-fix patterns
- 经验提取
summary: lessons-learned-extraction 机制：从当前会话提取经验教训包括 error-fix patterns 用户纠正和发现，保存为结构化笔记供 wiki 后续查询，--rules 选项输出可执行规则而非散文
related:
- llm-wiki-compounding-knowledge
- llm-wiki-audit-trust-verification
---

llm-wiki 的 lessons learned 功能（/wiki:ll）从当前会话中提取经验教训——包括 error→fix patterns、用户纠正和发现。这些被保存为结构化笔记，wiki 可在后续查询中检索。[^src-1]

使用 --rules 标志时，输出可执行规则（enforceable rules）而非散文形式，便于自动化应用。支持 --dry-run 预览。[^src-2]

[^src-1]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Lessons Learned" P37 -- "Extract lessons learned from the current session — error→fix patterns, user corrections, discoveries. Saved as structured notes the wiki can query later."
[^src-2]: `data/raw/webpage/llm-wiki-net/markdown.md` -- "Lessons Learned" P37 -- "--rules emits enforceable rules instead of prose."
