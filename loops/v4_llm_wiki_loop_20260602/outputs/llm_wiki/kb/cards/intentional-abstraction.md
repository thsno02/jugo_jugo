---
id: intentional-abstraction
title: 刻意抽象与模块化
status: accepted
card_type: source_claim
tags: [llm-wiki, design-philosophy, modularity]
created_time: 2026-06-04T22:30:00+08:00
edited_time: 2026-06-04T22:30:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/intentional-abstraction.md
canonical_concept: intentional-abstraction
aliases: [刻意抽象, intentional abstraction, 模块化设计, 意向性抽象]
summary: >-
  intentional-abstraction（刻意抽象 / intentional abstraction / 模块化设计 / modularity）
  是 LLM Wiki gist 的设计哲学：描述模式而非实现，所有组件可选且模块化，与 LLM 协作实例化
related: [schema-as-configuration]
---

LLM Wiki gist 采用**刻意抽象**的设计哲学——文档描述的是模式（pattern）而非具体实现。目录结构、schema 约定、页面格式、工具选择都取决于用户的领域、偏好和所选 LLM[^src-1]。

文档中提到的所有组件都是**可选且模块化的**——用有用的部分、忽略不需要的。具体示例包括：纯文本资料不需要图片处理、小规模 wiki 不需要搜索引擎、不关心幻灯片就只用 markdown 页面[^src-2]。

正确的使用方式是：将文档分享给 LLM agent，协作实例化一个适合自己需求的版本。文档的唯一职责是传达模式，「你的 LLM 可以搞定其余部分」[^src-3]。这种模块化在 schema 的可定制性中体现得最为具体[^card-1]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Note" P1 -- "The exact directory structure, the schema conventions, the page formats, the tooling — all of that will depend on your domain, your preferences, and your LLM of choice."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Note" P1 -- "Everything mentioned above is optional and modular — pick what's useful, ignore what isn't."
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Note" P1 -- "The right way to use this is to share it with your LLM agent and work together to instantiate a version that fits your needs. The document's only job is to communicate the pattern. Your LLM can figure out the rest."
[^card-1]: [Schema 文件的配置角色](schema-as-configuration.md) -- 模块化设计在 schema 可定制性中最具体体现
