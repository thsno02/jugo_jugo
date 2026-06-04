---
id: human-llm-role-division
title: 人机角色分工
status: accepted
card_type: distinction
tags: [llm-wiki, roles, human-llm-collaboration]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/human-llm-role-division.md
canonical_concept: human-llm-role-division
aliases: [人机分工, 角色分工, human vs LLM roles]
summary: >-
  human-llm-role-division 是 LLM Wiki 的角色分工原则：人类负责策展资料、引导分析、
  提好问题、思考意义；LLM 负责摘要、交叉引用、归档和簿记——一切苦差事
related: []
---

LLM Wiki 中人类和 LLM 有明确的角色分工[^src-1]：

**人类的职责**：策展资料来源、引导分析方向、提出好问题、思考全局意义[^src-2]。

**LLM 的职责**：一切苦差事——摘要、交叉引用、归档和簿记，即让知识库长期有用的那些维护工作[^src-3]。

作者使用了一个类比来描述实践中的工作状态：Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。用户在一侧打开 LLM agent 对话，在另一侧打开 Obsidian 浏览 wiki——跟随链接、检查图谱视图、阅读更新后的页面[^src-4]。

用户「从不（或很少）自己写 wiki」——LLM 写并维护全部内容[^src-5]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" 第2段 -- "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "You're in charge of sourcing, exploration, and asking the right questions."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
[^src-5]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" 第4段 -- "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."
