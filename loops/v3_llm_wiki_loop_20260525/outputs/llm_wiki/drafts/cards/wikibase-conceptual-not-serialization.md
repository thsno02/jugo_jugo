---
id: wikibase-conceptual-not-serialization
title: Wikibase 数据模型是"概念模型"——不规定实现、不规定序列化、不规定形式语义
status: draft
card_type: source_claim
tags: [#wikibase, #specification, #data-modeling]
created_time: 2026-05-26T15:30:00+08:00
edited_time: 2026-05-26T15:30:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
provenance_card: ../provenance/wikibase-conceptual-not-serialization.md
aliases: [Wikibase conceptual model, WON]
related: [wikibase-item-property-snak-statement, wikibase-three-snak-types, wikibase-statement-rank-and-references, llm-wiki-schema-is-most-important, robin-cartier-schema-as-product-doc, aillm-wiki-schema-as-bottleneck]
---

## 这份文档**不是**什么

Wikibase 数据模型文档反复强调它是 *conceptual model*，不是：

1. **不是 binding / 实现规范**——它不规定用 PHP、Java、Python 应该用什么 class 结构；同样的数据可以"more optimized" 存储。
2. **不是序列化规范**——JSON、RDF 序列化由独立文档定义（"Separate documents describe the serialization of the Wikibase data model in JSON and in RDF"）。
3. **不是形式语义**——文档"explains what the data is intended to express, and gives concrete examples. However, it is not a completely precise specification of how to interpret this data formally"，形式语义在另一文档里。

文档用 **UML class diagram** 来描述类型关系，配一个叫 **Wikidata Object Notation (WON)** 的轻量 BNF 仅用于给例子和说明，**不打算用于实际实现**。WON 用单引号字符串、`{ ... }` 表示零或多次、`[ ... ]` 表示零或一次、`|` 表示 alternative。

## 为什么要这样设计

- **conceptual / serialization / implementation 解耦**让 Wikidata 能演化：换底层存储、加新 binding（PHP→Lua、JS→Python SDK）、改 JSON dump 格式都不会动 schema 本身。
- 与 RDF / OWL 不同——Wikibase 的目标是"对人和软件都清晰"，不是"机器可自动推理"。因此故意不写形式语义，把推理留给应用层。
- **goals 与 requirements 是一组互相冲突的要求**：coverage / simplicity / extensibility / flexibility / exchange / technical support——文档明说"a balance must be found between expressive power and complexity/usability"，所以模型不追求完备，而追求"在 Wikidata 这个项目范围内够用"。

## 边界与误用

- 文档自带 "Editorial Note"，说明若干小节仍是草案——比如 GeoShapeValue、MediaValue 都还只是占位。
- 不要把 UML 当作"必须实现成这些 class"——优化的存储可能完全不同结构。
- 若做 RAG over Wikidata，应当读 **JSON / RDF 序列化文档**而不是本文，否则会在字段拼写、年份编码等细节上出错。

## References

- "conceptual model" 自我定位：`data/raw/webpage/wikibase-data-model/text.txt` 第 244-250 行（开篇）。
- UML + WON 用途：第 326-400 行（§4 How to read this document）。
- goals & requirements 列表：第 274-294 行（§2）。
- "形式语义在别处": 第 302 行 (Editorial Note 之前一段)。

## Footnotes

- 自定位原文："This is a living document, describing the conceptual data model behind Wikibase. It is not a specification of any concrete binding, implementation, mapping, or serialization."（第 244 行）
- 三种 things this model is not："Internal data structures: ... this does not mean that it mandates the actual class structures ... Export formats: Data could be exported in many syntactic forms. Other documents will specify how this is done ... Formal semantics: This document explains what the data is intended to express, and gives concrete examples. However, it is not a completely precise specification of how to interpret this data formally"（第 298-302 行）
- WON 性质："The WON is not intended to be used in implementations, but it is useful to give examples and to describe how the data model maps to other syntaxes, such as JSON or RDF."（第 366 行）
