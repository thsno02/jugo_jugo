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
  human-llm-role-division（人机分工 / 角色分工 / human vs LLM roles）是 LLM Wiki
  的角色分工原则：人类策展/引导/提问/思考，LLM 负责摘要、交叉引用、归档和簿记
related: [confirm-first-skill-capture, maintenance-cost-zero, mirror-vs-compensate-principle, review-involvement-spectrum, understanding-bottleneck, writing-as-thinking]
---

LLM Wiki 中人类和 LLM 有明确的角色分工[^src-1]：

**人类的职责**：策展资料来源、引导分析方向、提出好问题、思考全局意义[^src-2]。

**LLM 的职责**：一切苦差事——摘要、交叉引用、归档和簿记，即让知识库长期有用的那些维护工作[^src-3]。

作者使用了一个类比来描述实践中的工作状态：Obsidian 是 IDE，LLM 是程序员，wiki 是代码库。用户在一侧打开 LLM agent 对话，在另一侧打开 Obsidian 浏览 wiki——跟随链接、检查图谱视图、阅读更新后的页面[^src-4]。

用户「从不（或很少）自己写 wiki」——LLM 写并维护全部内容[^src-5]。这一分工之所以可行，根本原因在于 LLM 使维护成本趋近于零[^card-1]。Karpathy 进一步从认知层面论证：即使 LLM 代劳，人类阅读 wiki 仍促进理解[^card-2]。

然而，HN 社区对「苦差事可外包」这一核心前提提出了根本性的反驳：摘要、交叉引用等过程本身就是洞察产生的场所，外包过程即消灭思考[^dist-1]。

将 LLM 定位为纯粹执行者的假设，与伴侣记忆系统中的镜像-补偿原则形成对照：后者主张 LLM 在认知失败维度上应主动纠偏用户[^dist-2]。在实践中，角色边界的执行可通过门控机制实现——如 Cognition 的确认优先规则要求 LLM 产出须经人类明确批准[^card-4]，而参与程度本身也是可调节的[^card-3]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P2 -- "The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "You're in charge of sourcing, exploration, and asking the right questions."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "The LLM does all the grunt work — the summarizing, cross-referencing, filing, and bookkeeping"
[^src-4]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase."
[^src-5]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "You never (or rarely) write the wiki yourself — the LLM writes and maintains all of it."
[^card-1]: [维护成本归零论点](maintenance-cost-zero.md) -- 本卡描述角色分工，该卡论证分工成立的经济基础
[^card-2]: [理解瓶颈](understanding-bottleneck.md) -- 本卡描述人机角色的实践分工，该卡从认知层面论证即使 LLM 代劳写作，人类阅读 wiki 仍促进理解
[^dist-1]: [书写即思考](writing-as-thinking.md) -- 本卡将苦差事定性为可外包的维护工作，该卡主张苦差事过程本身即思考与洞察的产生场所，外包过程即消灭认知价值
[^dist-2]: [镜像-补偿设计原则](mirror-vs-compensate-principle.md) -- 本卡将 LLM 定位为执行苦差事的仆人角色，该卡赋予 LLM 在认知失败维度上主动纠偏的自主权；区分点在于 LLM 是否拥有超越用户意图的代理权
[^card-3]: [人类参与程度谱系](review-involvement-spectrum.md) -- 本卡设定固定的人机角色边界，该卡将该边界描述为可调节的连续谱系
[^card-4]: [确认优先的技能捕获规则](confirm-first-skill-capture.md) -- 本卡描述人机角色的宏观分工，该卡提供一种具体的门控机制实现角色边界
