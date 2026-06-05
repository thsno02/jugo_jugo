---
id: maintenance-cost-zero
title: 维护成本归零论点
status: accepted
card_type: source_claim
tags: [llm-wiki, maintenance, wiki-failure]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/maintenance-cost-zero.md
canonical_concept: maintenance-cost-zero
aliases: [维护成本归零, zero maintenance cost, wiki 失败原因, 知识库维护]
summary: >-
  maintenance-cost-zero（维护成本归零 / zero maintenance cost / wiki 失败原因 / 知识库维护）
  是 LLM Wiki 核心论点：人类放弃 wiki 因维护负担增长快于价值，LLM 使维护成本趋近于零
related: [cognitive-deskilling-risk, human-llm-role-division, llm-as-maintenance-engine, retrieval-vs-maintenance, writing-as-thinking]
---

LLM Wiki 模式成立的核心经济论点是：维护知识库的困难部分不是阅读或思考，而是**簿记工作**——更新交叉引用、保持摘要时效性、标注新旧数据矛盾、在数十个页面间维持一致性[^src-1]。

人类放弃 wiki 的原因在于**维护负担的增长速度超过了价值的增长速度**。而 LLM 不会感到无聊、不会忘记更新交叉引用、可以一次操作触及 15 个文件。Wiki 得以维护是因为维护成本趋近于零[^src-2]。维护成本归零后，人机之间的具体分工见角色分工卡[^card-1]。这一论点在概念层与 LLM 维护引擎角色重构相呼应[^card-2]；从反面论证，检索层再好也无法替代维护循环[^card-3]。

然而，本卡将簿记工作定性为纯成本的前提受到两方面挑战：「书写即思考」论点主张这些过程本身即认知价值的产生场所[^dist-1]；而实践者的去技能化报告表明，即使维护成本归零，过度委托也可能导致人类自身认知能力的退化[^dist-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" 第1段 -- "The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. Updating cross-references, keeping summaries current, noting when new data contradicts old claims, maintaining consistency across dozens of pages."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Why this works" P1 -- "Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."
[^card-1]: [人机角色分工](human-llm-role-division.md) -- 本卡论证维护成本归零，该卡展开人机各自职责
[^card-2]: [LLM 作为维护引擎的角色重构](llm-as-maintenance-engine.md) -- 本卡论证维护成本归零的经济逻辑，该卡从角色定义层阐述维护引擎的概念内涵
[^card-3]: [检索与维护的区别](retrieval-vs-maintenance.md) -- 本卡从正面论证维护成本归零使 wiki 可行，该卡从反面论证检索工具无法替代维护循环
[^dist-1]: [书写即思考](writing-as-thinking.md) -- 本卡主张簿记工作是纯成本并可由 LLM 归零，该卡主张簿记过程本身即思考和洞察的产生场所，区分点在于对 grunt work 认知价值的根本分歧
[^dist-2]: [认知去技能化风险](cognitive-deskilling-risk.md) -- 本卡乐观地论证维护成本归零使 wiki 可行，该卡警告即使成本归零，过度委托仍导致人类认知能力退化，区分点在于是否考虑了委托的隐性认知代价
