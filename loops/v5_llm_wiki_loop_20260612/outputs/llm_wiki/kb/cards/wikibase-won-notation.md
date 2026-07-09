---
id: wikibase-won-notation
title: Wikidata Object Notation (WON) 的设计目的
status: accepted
card_type: notation-system
tags:
- wikibase
- WON
- serialization
- notation
- BNF
- examples
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- wikibase-data-model
evidence_basis: documentation
justification: ../justification/wikibase-won-notation.md
canonical_concept: wikibase-won-notation
aliases:
- WON
- Wikidata Object Notation
summary: Wikidata Object Notation (WON) 是概念文档中使用的简单序列化语法，用于给出具体数据实例 示例和描述到 JSON/RDF 的映射。明确不打算用于实际实现。特点：位置编码（省略属性名）、 BNF 文法描述、与数据模型结构一一对应。
related:
- wikibase-conceptual-data-model
---

Wikidata Object Notation（WON）是数据模型文档中引入的简单序列化语法，用于两个目的：

1. **给出具体实例示例**——让抽象的 UML 结构有具象的数据表示
2. **描述数据模型到其他语法的映射**——如到 JSON 或 RDF 的对应关系

**明确的非目标**：WON 不打算用于实际软件实现。

**技术特点**：
- 位置编码：省略属性名，仅按位置编码值
- 使用 BNF 文法描述
- 基本数据类型序列化：quotedString、integer、decimal、IRI（`< >`包围）、GlobalSiteIdentifier、UserLanguageCode
- 遵循常见转义约定（`\"` 和 `\\`）

**BNF 元语法**：终结符用单引号，非终结符用粗体，`{}` 表零或多，`[]` 表零或一，`|` 表选择。[^src-1]

[^src-1]: `data/raw/webpage/wikibase-data-model/markdown.md` -- "Wikidata Object Notation" P54-72 -- "The WON is not intended to be used in implementations, but it is useful to give examples and to describe how the data model maps to other syntaxes"
[^card-1]: 参见 [wikibase-conceptual-data-model] 了解 WON 服务的文档定位
