---
id: wikibase-entity-value-hierarchy
title: Wikibase 实体与数据值的层次划分
status: accepted
card_type: distinction
tags: [wikibase, data-model, entity, datavalue, iri, identity]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-entity-value-hierarchy.md
canonical_concept: wikibase-entity-value-hierarchy
aliases: [Entity-DataValue 分层, 实体-数据值区分, Wikibase Value 类型体系]
summary: >-
  wikibase-entity-value-hierarchy（Entity-DataValue 分层 / 实体-数据值区分）Wikibase 将 Value 分为 Entity（Item/Property/Datatype，以 IRI 全局标识，可做 Statement 主语）和 DataValue（数值/字符串/坐标等，以内容标识，不可做主语），这一分层决定了哪些对象能被进一步描述
related: [wikibase-snak-triple-epistemology, wikibase-entity-description, wikibase-flexible-typing]
---

Wikibase 数据模型将所有 Value 划分为两大类别：Entity 和 DataValue，这一区分是整个模型的根基性设计 [^src-1]。

**Entity** 包括 Item（代表维基百科页面的主题，如"柏林"）、Property（描述实体间关系，如"人口"）和 Datatype（指定属性值的类型和格式）。所有 Entity 都通过全局唯一的 IRI（国际化资源标识符）进行标识，例如 Item 的 IRI 形如 `https://www.wikidata.org/entity/Qnnn`，Property 的 IRI 形如 `https://www.wikidata.org/entity/Pnnn` [^src-2]。因为拥有 IRI，Entity 可以作为 Statement 的主语被进一步描述。

**DataValue** 则包括数量值、时间值、地理坐标、字符串等，它们没有独立的 IRI，而是"以其内容来标识的复合值" [^src-3]。DataValue 不能成为 Statement 的主语——Wikidata 不打算存储关于单个数据值（如字符串或数字）的声明 [^src-4]。

这一层次的关键推论是：所有 Entity 都是 Value，但许多 Value 不是 Entity。一个数字作为"数据值"不可被描述，但如果某个数字作为概念在维基百科有专门页面，则可以创建一个 Item 来表示它，从而获得可描述性 [^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/text.txt` -- "Values" section, lines 402-406 -- "Values are basic objects of Wikidata, that only represent one particular thing. Items represent topics of Wikipedia pages, Properties represent the properties that Items (or other Entities) can have, DataValues represent individual values of a particular Datatype"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/text.txt` -- "Values" section, lines 406-407 -- "Items have IRIs of the form https://www.wikidata.org/entity/Qnnn and Properties have IRIs of the form https://www.wikidata.org/entity/Pnnn"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/text.txt` -- "Values" section, lines 418-419 -- "DataValues are not identified by an IRI but can simply be viewed as compound values that are identified by their content"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/wikibase-data-model/text.txt` -- "Overview" section, lines 316-317 -- "All Entities are Values, but many kinds of Values are not Entities... Wikidata does not intend to store Statements about individual data values, such as strings or numbers"
