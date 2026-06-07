---
id: documentation-shared-ownership
title: 文档共同所有权文化
status: accepted
card_type: concept
tags: [documentation, culture, collaboration, writer-developer]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
justification: ../justification/documentation-shared-ownership.md
canonical_concept: documentation-shared-ownership
aliases: [文档共同所有权, 写作者与开发者共有, shared doc ownership]
summary: >-
  documentation-shared-ownership（文档共同所有权 / 写作者与开发者共有 / shared doc ownership）指 docs-as-code 理念所促成的文化转变：技术写作者与开发者双方均对文档拥有所有权感，并协同提升文档质量
related: [docs-as-code, documentation-merge-gate, schema-as-configuration, single-curator-bottleneck]
---

Docs as Code 理念所带来的核心文化转变是**文档共同所有权**：技术写作者（writer）与开发者（developer）双方均对文档产生所有权感，并共同努力将文档做到最好[^src-1]。

这种共同所有权的具体表现包括：写作者能更好地融入开发团队[^src-2]，而开发者也会主动编写文档初稿[^src-3]。这种双向参与打破了"文档是写作者专属职责"的传统分工，形成了跨角色的协作文化。

Falconer 的企业 LLM Wiki 分析从反面印证了这一文化的必要性：个人 LLM Wiki 依赖单一策展人，而在企业规模下这种模式会重新制造它试图解决的 wiki 问题[^card-1]。

Schema-as-configuration 模式中的人机共同演化呈现了一个有趣的平行：docs-as-code 强调写作者与开发者之间的人-人协作，而 LLM Wiki 的 schema 共同演化则是人-LLM 协作的实例，两者在不同协作边界上展示了同一种知识共有模式[^card-2]。

## Footnotes

[^src-1]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "culture" L23 -- "It enables a culture where writers and developers both feel ownership of documentation, and work together to make it as good as possible."
[^src-2]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "benefits" L27 -- "Writers integrate better with development teams"
[^src-3]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "benefits" L29 -- "Developers will often write a first draft of documentation"
[^card-1]: [单一策展人瓶颈](single-curator-bottleneck.md) -- 企业 LLM Wiki 中单一策展人模式的结构性失效，从反面印证了文档共同所有权文化的必要性
[^card-2]: [Schema 文件的配置角色](schema-as-configuration.md) -- 本卡聚焦人-人（写作者与开发者）之间的文档共同所有权，该卡描述人-LLM 之间的 schema 共同演化，两者平行展示了不同协作边界上的知识共有模式
