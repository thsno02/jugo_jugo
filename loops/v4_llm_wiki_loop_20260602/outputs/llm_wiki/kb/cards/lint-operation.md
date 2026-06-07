---
id: lint-operation
title: 巡检操作
status: accepted
card_type: operational_rule
tags: [llm-wiki, operations, lint, maintenance]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/lint-operation.md
canonical_concept: lint-operation
aliases: [巡检操作, lint, wiki 健康检查, health-check]
summary: >-
  lint-operation（巡检操作 / lint / wiki 健康检查 / health-check）是 LLM Wiki
  定期健康检查操作：检测矛盾、过时主张、孤立页面、缺失概念页、缺失交叉引用、数据缺口
related: [continuous-drift-detection, governance-over-retrieval, llm-as-maintenance-engine, maintenance-cost-zero, source-faithfulness-risk, workflow-taxonomy]
---

巡检（Lint）是 LLM Wiki 的三大操作之一，用于定期维护 wiki 的健康状态。用户触发后，LLM 检查以下问题[^src-1]：

- 页面之间的矛盾
- 已被新资料取代的过时主张
- 没有入站链接的孤立页面
- 被提及但缺少独立页面的重要概念
- 缺失的交叉引用
- 可通过网络搜索填补的数据缺口

LLM 还善于建议新的调查问题和新的资料来源[^src-2]。巡检保持 wiki 在增长过程中的健康状态。从概念层看，巡检是 LLM 作为维护引擎的核心操作实例[^card-2]，其经济可行性来自 LLM 将维护成本趋近于零[^card-3]。在企业规模下，巡检从按需触发演化为持续自动运行的偏移检测循环[^card-4]。工作流分类法则将 lint 归入 Audit 类工作流[^card-5]。值得注意的是，巡检检查的是时效性和结构健康，但不直接验证 wiki 内容是否忠于原始来源——这一缺口在源忠实性风险卡中分析[^card-1]。Atlan 的"治理优先于检索"论点为巡检操作提供了更宏观的理论支撑——巡检本质上是一种数据治理实践，其价值不在于改善检索效率而在于维护知识的可信度[^card-6]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" P1 -- "Look for: contradictions between pages, stale claims that newer sources have superseded, orphan pages with no inbound links, important concepts mentioned but lacking their own page, missing cross-references, data gaps that could be filled with a web search."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" P1 -- "The LLM is good at suggesting new questions to investigate and new sources to look for."
[^card-1]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 巡检不检查源忠实度，该卡分析这一缺口
[^card-2]: [LLM 作为维护引擎的角色重构](llm-as-maintenance-engine.md) -- 本卡描述巡检的具体操作步骤，该卡从概念层论证巡检属于 LLM 维护引擎角色的核心体现
[^card-3]: [维护成本归零论点](maintenance-cost-zero.md) -- 本卡描述巡检做什么，该卡论证 LLM 执行这些维护工作的经济逻辑
[^card-4]: [持续偏移检测](continuous-drift-detection.md) -- 本卡描述个人规模的按需巡检，该卡描述企业规模下巡检演化为持续自动化偏移检测
[^card-5]: [工作流五类分类法](workflow-taxonomy.md) -- 本卡描述 lint 操作本身，该卡将 lint 归入 Audit 类工作流的整体分类框架
[^card-6]: [治理优先于检索架构](governance-over-retrieval.md) -- Atlan 论证"规模决定架构，治理决定结果"，巡检操作是该治理原则在个人 LLM Wiki 中的具体实践——检测矛盾和过时主张本质上是数据治理而非检索优化
