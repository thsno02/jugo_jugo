---
id: schema-template-verticals
title: Schema 模板的领域垂直化
status: accepted
card_type: example_pattern
tags: [llm-wiki, schema, templates, verticals, productization]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
justification: ../justification/schema-template-verticals.md
canonical_concept: schema-template-verticals
aliases: [Schema 模板垂直化, schema verticals, 领域模板, domain-specific templates]
summary: >-
  schema-template-verticals（Schema 模板垂直化 / schema verticals / 领域模板）
  指 LLM Wiki 的 schema 层已被产品化为五个领域垂直模板（general / research / engineering /
  product / SEO），每个模板以 schema.md + CLAUDE.md 组合交付，体现模式从通用规范到领域配置的成熟
related:
  - schema-as-configuration
  - use-case-domains
---

LLM Wiki 的 schema 层已从通用规范演化为**领域垂直化的模板产品**。aillm.wiki 提供五套经过实战检验（"battle-tested"）的 schema.md 模板，覆盖以下领域[^src-1]：

1. **General**——通用场景
2. **Research**——研究场景
3. **Engineering**——工程场景
4. **Product**——产品场景
5. **SEO**——搜索引擎优化场景

每套模板以 **schema.md + CLAUDE.md 的组合**形式交付，声称"gets an LLM to produce clean entity pages on the first try"[^src-2]。用户的起步路径是从五套模板中选择一个，根据项目需要编辑，或在熟悉模式后从头构建[^src-3]。

值得注意的是，这五个垂直方向与 Karpathy 原始 gist 中列举的使用场景（个人 / 研究 / 书籍 / 业务团队 / 其他）并不完全对应——"SEO"和"Product"是生态中新增的领域分类，而"书籍阅读"和"个人成长"则未被单独模板化。这反映了社区在实际应用中对模式适用域的重新划分。

每套模板都声称在真实项目上经过测试："Each schema is battle-tested against real projects before it ships — no wishful examples"[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/aillm-wiki-directory/text.txt` -- L47,61,85 -- "5 battle-tested schema.md templates (general, research, engineering, product, SEO)"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/aillm-wiki-directory/text.txt` -- L47 -- "Each template ships with the exact schema.md and CLAUDE.md combo that gets an LLM to produce clean entity pages on the first try"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/aillm-wiki-directory/text.txt` -- L61 -- "Start from one of our five battle-tested schema.md templates... Edit it to fit your project, or start from scratch once you have seen the pattern a few times."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/aillm-wiki-directory/text.txt` -- L85 -- "Each schema is battle-tested against real projects before it ships — no wishful examples, only the shapes that actually produce clean LLM Wiki output."
