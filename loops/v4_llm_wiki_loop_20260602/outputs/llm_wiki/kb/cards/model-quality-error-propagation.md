---
id: model-quality-error-propagation
title: 模型能力不足导致的错误传播风险
status: accepted
card_type: operational_rule
tags: [llm-wiki, model-quality, error-propagation, human-review, agents-md]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
justification: ../justification/model-quality-error-propagation.md
canonical_concept: model-error-propagation
aliases: [模型错误传播, error propagation, 弱模型风险]
summary: >-
  model-error-propagation（模型错误传播 / error propagation / 弱模型风险）指 LLM Wiki 完全依赖
  模型质量管理来源间矛盾，能力不足的模型会静默传播错误；agents.md 质量和定期人工审查是关键缓解措施
related: [compilation-gap, review-involvement-spectrum, schema-as-configuration, source-faithfulness-risk]
---

LLM Wiki 的知识库质量**完全依赖于所使用模型的能力**来管理来源之间的矛盾[^src-1]。如果模型能力不足，它可能在不发出任何告警的情况下传播错误信息。这一风险与源忠实性的另一维度——多轮有损变换导致的知识漂移——构成互补的威胁来源[^card-1]。编译缺口的实验数据则表明，即使单次编译步骤也可能灾难性地丢弃超过半数的关键事实，盲编译失败率高达 53-60%[^card-2]。

该来源明确建议两项缓解措施：

1. **定期人工审查**——尤其在使用的前几周，对关键页面进行人工检查[^src-2]
2. **高质量的 agents.md**——指令文件的质量**直接决定**知识库的可靠性[^src-3]

agents.md 被描述为保持 wiki 长期一致性的**主要杠杆（levier principal）**，应从一开始就包含精确的规则：如何命名页面、何时创建新实体而非更新已有实体、如何格式化矛盾[^src-4]。这将 schema 文件从一般性配置提升到了质量保障的核心地位。

## Footnotes

[^src-1]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "La LLM wiki repose entierement sur la qualite du modele pour gerer les contradictions entre sources. Un modele trop faible peut propager des erreurs sans les signaler."
[^src-2]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "Prevoyez une revue humaine periodique des pages cles, surtout dans les premieres semaines."
[^src-3]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "La qualite de votre agents.md determine directement la fiabilite de la base."
[^src-4]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L110 -- "Creez un fichier agents.md des le depart avec des regles precises : comment nommer les pages, quand creer une nouvelle entite vs. mettre a jour une existante, comment formater les contradictions. Ce fichier d'instructions est le levier principal pour garder une wiki coherente sur la duree."
[^card-1]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 本卡聚焦模型能力不足作为错误传播根因，该卡聚焦多轮有损变换导致的渐进性知识漂移
[^card-2]: [编译缺口](compilation-gap.md) -- 本卡关注模型能力维度的错误传播，该卡量化编译过程中的事实丢失程度（53-60% 灾难性失败率）
