# 出处论证

## 事实来源

这张草稿卡来自 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16` 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:68-69`。候选字段只用于核对本次任务指定的候选 5，事实支撑以这两组原文行为准。

## 支撑关系

第 15 行直接说明，用户通常很少亲自写 wiki，LLM 写作并维护它；同一行把人的职责放在 sourcing、exploration 和 asking the right questions 上，把 LLM 的工作放在 summarizing、cross-referencing、filing 和 bookkeeping 上。第 68 行再次用更概括的方式说明，人负责策展来源、指挥分析、提出好问题并思考意义，而 LLM 负责其余工作。

这两处证据都在描述同一类人机分工，因此可以支撑“该来源把人的角色描述为负责来源、探索和提出问题，而把 LLM 的角色描述为负责总结、交叉引用、归档和维护知识库”这一事实候选。

## 明说与整理

来源明说的部分包括：人负责来源、探索、好问题、分析方向和意义判断；LLM 负责写作、维护、总结、交叉引用、归档和簿记。

卡片中的中文表述做了轻度整理：把 sourcing 归纳为“来源策展”，把 filing 和 bookkeeping 放入“归档和簿记等知识库劳动”，并把两处证据合并为一条原子事实。整理没有加入新的角色、工具或背景判断。

## 成立范围

该事实只在这个来源对 LLM Wiki 人机分工的描述中成立。它不证明这种分工适用于所有知识库、所有 LLM agent、所有 Obsidian 使用方式或所有人机协作场景。

## draft 原因

当前卡片只使用任务指定的一份来源及其指定行号，尚未经过主控 agent 的采纳流程，也没有额外独立来源交叉校验。因此它可以作为可读草稿事实，但应保持 `status: draft`。
