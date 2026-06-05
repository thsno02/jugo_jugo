---
id: wiki-deduplication-fragility
title: Wiki 去重的脆弱性
status: accepted
card_type: source_claim
tags: [llm-wiki, deduplication, scaling-limit, deterministic-guard]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
justification: ../justification/wiki-deduplication-fragility.md
canonical_concept: wiki-deduplication-fragility
aliases: [去重脆弱性, deduplication fragility, 近似重复页面, wiki dedup]
summary: >-
  wiki-deduplication-fragility（去重脆弱性 / deduplication fragility / 近似重复页面）
  指 LLM Wiki 的去重完全依赖 LLM 判断、在规模增长时变得脆弱——缺乏确定性保护机制时 wiki 会逐渐积累近似重复页面
related: [alias-cross-language-dedup, entity-resolution-hybrid-search]
  - llm-wiki-scale-boundary
  - lint-operation
  - alias-cross-language-dedup
---

LLM Wiki 的一个已识别局限性是：**去重完全依赖 LLM 判断，在规模增长时变得脆弱**[^src-1]。

在小型 wiki 中，LLM 能够通过阅读 index.md 识别已有页面并避免重复创建。但随着 wiki 规模增长，如果没有**确定性保护机制（deterministic guard）**——如基于标题/实体名的精确匹配检查——wiki 将逐渐积累近似重复页面（near-duplicate pages）[^src-1]。

这一问题的根源在于 LLM 对「两个页面是否覆盖同一主题」的判断本身是概率性的：不同措辞的标题、不同粒度的概念切分、不同摄入会话的上下文差异，都可能导致 LLM 创建实质上重复的页面而未意识到重复。巡检（lint）操作[^card-1]可以事后发现部分重复，但无法从根本上解决摄入时的非确定性问题。

Obsidian LLM Wiki 插件的别名系统[^card-2]是一种确定性保护机制的实践——通过强制别名和两层语义检测在 Tier 1 提供确定性匹配锚点。而 Graphiti 的混合搜索管线虽增加了向量和全文检索信号，其最终裁决仍依赖 LLM[^dist-1]，并未根本解决本卡所述的确定性缺失问题。

## Footnotes

[^src-1]: `data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt` -- L43 -- "Deduplication is LLM-dependent and fragile at scale — without a deterministic guard, the wiki will accumulate near-duplicate pages over time."
[^card-1]: `lint-operation` -- 巡检操作：检查一致性、发现问题的维护流程
[^card-2]: [别名系统与跨语言去重](alias-cross-language-dedup.md) -- 本卡指出纯 LLM 去重的脆弱性，该卡的别名系统（强制别名+两层语义检测）正是一种确定性保护机制的实践
[^dist-1]: [混合搜索实体消解流程](entity-resolution-hybrid-search.md) -- 本卡主张缺乏确定性保护机制时 LLM 去重必然脆弱，该卡的混合检索虽增强候选质量但最终仍依赖 LLM 裁决，区分点在于：统计检索信号是否足以替代确定性规则保护
