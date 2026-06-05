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
canonical_concept: source-faithfulness-risk
aliases: [模型错误传播, error propagation, 弱模型风险]
summary: >-
  source-faithfulness-risk（模型错误传播 / error propagation / 弱模型风险）指 LLM Wiki 完全依赖
  模型质量管理来源间矛盾，能力不足的模型会静默传播错误；agents.md 质量和定期人工审查是关键缓解措施
related: [source-faithfulness-risk, schema-as-configuration, review-involvement-spectrum]
---

LLM Wiki 的知识库质量**完全依赖于所使用模型的能力**来管理来源之间的矛盾[^src-1]。如果模型能力不足，它可能在不发出任何告警的情况下传播错误信息。这一风险与源忠实性的另一维度——多轮有损变换导致的知识漂移——构成互补的威胁来源。

该来源明确建议两项缓解措施：

1. **定期人工审查**——尤其在使用的前几周，对关键页面进行人工检查[^src-2]
2. **高质量的 agents.md**——指令文件的质量**直接决定**知识库的可靠性[^src-3]

agents.md 被描述为保持 wiki 长期一致性的**主要杠杆（levier principal）**，应从一开始就包含精确的规则：如何命名页面、何时创建新实体而非更新已有实体、如何格式化矛盾[^src-4]。这将 schema 文件从一般性配置提升到了质量保障的核心地位。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "La LLM wiki repose entierement sur la qualite du modele pour gerer les contradictions entre sources. Un modele trop faible peut propager des erreurs sans les signaler."
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "Prevoyez une revue humaine periodique des pages cles, surtout dans les premieres semaines."
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L162 -- "La qualite de votre agents.md determine directement la fiabilite de la base."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/anthemcreation-fr-guide/text.txt` -- L110 -- "Creez un fichier agents.md des le depart avec des regles precises : comment nommer les pages, quand creer une nouvelle entite vs. mettre a jour une existante, comment formater les contradictions. Ce fichier d'instructions est le levier principal pour garder une wiki coherente sur la duree."
