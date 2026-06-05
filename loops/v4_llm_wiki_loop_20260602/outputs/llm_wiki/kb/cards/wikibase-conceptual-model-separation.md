---
id: wikibase-conceptual-model-separation
title: Wikibase 概念模型与技术表示的分离
status: accepted
card_type: concept
tags: [wikibase, conceptual-model, serialization, json, rdf, abstraction]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-conceptual-model-separation.md
canonical_concept: wikibase-conceptual-model-separation
aliases: [概念模型与实现分离, 模型-序列化分层, Wikibase 抽象层次]
summary: >-
  wikibase-conceptual-model-separation（概念模型与实现分离 / 模型-序列化分层）Wikibase 数据模型明确定位为概念模型（"需要支持哪些信息"），与技术表示（"软件应使用哪些数据结构"）和语法表示（"数据在文件中如何表达"）分离，JSON/RDF 序列化由独立文档规定
related: [wikibase-data-model-design-goals, wikibase-entity-value-hierarchy]
---

Wikibase 数据模型文档在开篇即做出了一个核心定位声明：这是一份"概念模型"文档，回答的是"我们需要支持哪些信息？"这一问题，而非"软件应使用哪些数据结构？"或"数据在文件中应如何表达？"[^src-1]

这一分离体现在三个层次上：

1. **概念层**（本文档）：使用 UML 类图描述数据结构，但"这并不意味着它规定了实现中使用的实际类结构"。在许多具体场景中，数据可以以更优化的方式存储 [^src-2]。

2. **序列化层**（独立文档）：数据的 JSON 序列化和 RDF 序列化由各自的独立文档规定 [^src-3]。文档还引入了 WON（Wikidata Object Notation）作为示例性伪序列化，明确声明"WON 不打算在实现中使用" [^src-4]。

3. **语义层**（另一独立文档）：数据的精确形式化解释也被推迟到单独文档中 [^src-5]。

这种分层的实用价值在于：概念模型提供了一个"公共理解"，使得 Wikibase 的各种内部表示（对象、语法格式、用户界面等）都能有"唯一且无歧义的解读" [^src-6]。同时，模型本身被设计为可由扩展文档补充——例如 WikibaseLexeme 的词条数据模型即为此模型的扩展 [^src-7]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- opening section, lines 247-248 -- "This document describes a conceptual model ('Which information do we have to support?') and does not specify how this data should be represented technically ('Which data structures should the software use?') or syntactically ('How should the data be expressed in a file?')"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 297-299 -- "this does not mean that it mandates the actual class structures to be used in implementation... data can be stored in a more optimized way"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- opening section, line 248 -- "Separate documents describe the serialization of the Wikibase data model in JSON and in RDF"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Wikidata Object Notation" section, line 366 -- "The WON is not intended to be used in implementations, but it is useful to give examples"
[^src-5]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 302-303 -- "Formal semantics... this will be given in a separate document"
[^src-6]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 278-279 -- "it is only important that each representation has a unique and unambiguous reading in terms of the data model"
[^src-7]: `data/raw/webpage/wikibase-data-model/text.txt` -- opening section, lines 252-254 -- "This document is extended by other documents... WikibaseLexeme - Lexeme Data Model"
