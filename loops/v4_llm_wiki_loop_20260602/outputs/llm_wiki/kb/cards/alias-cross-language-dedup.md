---
id: alias-cross-language-dedup
title: 别名系统与跨语言去重
status: accepted
card_type: mechanism
tags: [llm-wiki, dedup, alias, cross-language, quality]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
justification: ../justification/alias-cross-language-dedup.md
canonical_concept: alias-cross-language-dedup
aliases: [跨语言去重, 别名去重, alias dedup, cross-language duplicate detection, 两层语义去重]
summary: >-
  alias-cross-language-dedup（跨语言去重 / 别名去重 / alias dedup / 两层语义去重）
  是 LLM Wiki 插件的去重机制：每页强制至少 1 个别名（翻译/缩写/别称），
  通过两层语义检测（Tier 1 直接匹配始终 LLM 验证 + Tier 2 间接信号填充 token 预算）消除跨语言重复页
related: [entity-resolution-hybrid-search, wiki-deduplication-fragility]
  - lint-operation
---

Karpathy LLM Wiki 插件采用**别名系统 + 两层语义检测**来解决跨语言重复页问题。

**强制别名规则**：每个生成的页面必须包含至少 1 个别名（翻译、缩写或替代名称）[^src-1]。例如，"Supervised Learning" 页面会自动生成别名 "监督学习"[^src-2]。别名是去重的基础设施——缺失别名会导致同一概念的不同语言版本被创建为独立页面（如 "CoT" 和 "思维链" 并存）[^src-3]。

**两层语义检测**（v1.7.10+）[^src-4]：
- **Tier 1**（始终经 LLM 验证）：直接名称匹配——跨语言翻译、缩写、高相似度标题
- **Tier 2**（填充剩余 token 预算）：间接信号——共享链接、中等相似度候选

检测到重复后，插件提供**智能合并**：合并内容并保留双方所有别名，防止未来重复[^src-5]。对于历史遗留页面（v1.7.11 之前生成），可通过 Lint 报告中的 "Complete Aliases" 批量生成缺失别名[^src-6]。

别名系统的两层检测正是针对纯 LLM 去重脆弱性[^card-1]的确定性保护机制实践，与 Graphiti 的混合搜索实体消解[^card-2]形成互补——前者以精确别名匹配为锚点，后者以向量相似度检索为起点。

## Footnotes

[^src-1]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Knowledge Quality" L262-263 -- "Mandatory Page Aliases — Every generated page includes at least 1 alias (translation, acronym, alternate name), enabling cross-language duplicate detection"
[^src-2]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Example" L341 -- "aliases: [\"监督学习\", \"Supervised Learning\"]"
[^src-3]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "FAQ Aliases & Duplicates" L412 -- "Pre-v1.7.10 versions lacked alias-aware duplicate detection. Run Lint Wiki → Merge Duplicates to fuse them."
[^src-4]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "FAQ Aliases & Duplicates" L413-414 -- "Two-tier semantic detection: Tier 1 (always LLM-verified) catches cross-language matches, abbreviations, high-similarity titles. Tier 2 fills remaining token budget with moderate-similarity candidates."
[^src-5]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "Knowledge Quality" L265-266 -- "Duplicate Detection & Merge — Semantic tiering catches true duplicates (cross-language translations, abbreviations, spelling variants); intelligent LLM merge fuses content and preserves aliases"
[^src-6]: `data/raw/webpage/obsidian-community-plugin/text.txt` -- "FAQ" L410-411 -- "Click Complete Aliases in the Lint report to batch-generate translations, acronyms, and alternate names."
[^card-1]: [Wiki 去重的脆弱性](wiki-deduplication-fragility.md) -- 本卡聚焦别名机制作为确定性去重方案，该卡指出缺乏确定性保护时 LLM 去重在规模增长时的脆弱性
[^card-2]: [混合搜索实体消解流程](entity-resolution-hybrid-search.md) -- 本卡采用别名匹配 + LLM 验证的去重路径，该卡采用向量嵌入 + 全文搜索 + LLM 消解的混合检索路径
