---
id: wikibase-data-model-design-goals
title: Wikibase 数据模型的六项设计要求
status: accepted
card_type: concept
tags: [wikibase, design-goals, requirements, tradeoff, coverage, simplicity, extensibility]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [wikibase-data-model]
justification: ../justification/wikibase-data-model-design-goals.md
canonical_concept: wikibase-data-model-design-goals
aliases: [Wikibase 设计要求, 数据模型六目标, 表达力与复杂性平衡]
summary: >-
  wikibase-data-model-design-goals（Wikibase 设计要求 / 数据模型六目标）Wikibase 数据模型在六项有时冲突的要求间寻求平衡：覆盖度、简单性、可扩展性、灵活性、可交换性、技术可支持性；同时明确划定模型边界——不规定内部数据结构、导出格式和形式语义
related: [wikibase-flexible-typing, wikibase-statement-ranking]
---

Wikibase 数据模型的首要目标是"澄清 Wikibase 中存储了什么信息"，并同时服务于概念清晰性和技术文档两个方面 [^src-1]。

文档列出六项设计要求，并明确指出它们"有时相互冲突" [^src-2]：

1. **覆盖度（Coverage）**：模型应以自然的方式捕捉维基百科中出现的重要数据。
2. **简单性（Simplicity）**：模型不应过于复杂。
3. **可扩展性（Extensibility）**：模型应允许未来扩展。
4. **灵活性（Flexibility）**：应支持数据的访问和再利用；数据的效用不应局限于单一上下文。
5. **可交换性（Exchange）**：数据的各部分应可交换，且即使在 Wikidata 具体系统上下文之外也有明确含义。
6. **技术可支持性（Technical support）**：模型应允许在现有数据格式（如 JSON 或 RDF/OWL）中进行充分表示。

同时，模型明确划定了三条"不负责"的边界 [^src-3]：
- **内部数据结构**：模型使用 UML 规范，但不规定实现中的实际类结构。
- **导出格式**：数据的具体语法表示由单独文档指定。
- **形式语义**：数据的精确形式化解释将在另一文档中给出。

文档还承认了一个根本性的限制：模型"不可能捕捉人们对世界所能做出的所有声明（甚至不是所有重要或合理的声明）"，必须在"表达力与复杂性/可用性之间找到平衡" [^src-4]。

## Footnotes

[^src-1]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 274-278 -- "Conceptual clarity: It should be clear what Wikibase can (and what it cannot) capture... Technical documentation: Almost every component of Wikibase has to work with the data"
[^src-2]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 282-293 -- "Coverage... Simplicity... Extensibility... Flexibility... Exchange... Technical support"
[^src-3]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 296-303 -- "Internal data structures... Export formats... Formal semantics"
[^src-4]: `data/raw/webpage/wikibase-data-model/text.txt` -- "Goals and requirements" section, lines 276-277 -- "It is not possible to capture all statements that one could make about the world... A balance must be found between expressive power and complexity/usability"
