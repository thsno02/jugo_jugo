---
id: agents-md-instruction-file
title: agents.md 指令文件的关键作用
status: draft
card_type: design-principle
tags: [llm-wiki, agents-md, instruction-file, governance]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
evidence_basis: practitioner_report
justification: ../justification/agents-md-instruction-file.md
canonical_concept: agents-md-instruction-file
aliases: [agents.md, instruction file, wiki instruction file]
summary: >-
  agents.md 指令文件 instruction-file：定义页面命名规则、新实体创建 vs 更新已有实体的判断标准、矛盾格式化方式。是保持 wiki 长期一致性的主要杠杆 (main lever)，其质量直接决定知识库可靠性。材料建议从项目开始就创建。
related: [llm-wiki-three-layer-architecture, llm-wiki-model-quality-risk]
---

agents.md 是 LLM wiki 三层架构中的指令层，定义 LLM 在 wiki 中的行为规则 [^src-1]。

材料强调其应包含：
- **页面命名规则**——如何给实体页命名
- **创建 vs 更新判断**——何时创建新实体页 vs 更新已有页面
- **矛盾格式化**——如何标注和呈现来源间的冲突

材料将其称为保持 wiki 长期一致性的 "main lever"（主要杠杆），并明确指出其质量直接决定知识库的可靠性 [^src-2]。建议从项目开始就创建 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "How the workflow operates in practice" -- "Create an agents.md file from the start with precise rules: how to name pages, when to create a new entity vs. update an existing one, how to format contradictions."
[^src-2]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Warning" -- "The quality of your agents.md directly determines the base's reliability."
[^card-1]: 参见 [[llm-wiki-three-layer-architecture]] 关于 agents.md 在三层架构中的位置
