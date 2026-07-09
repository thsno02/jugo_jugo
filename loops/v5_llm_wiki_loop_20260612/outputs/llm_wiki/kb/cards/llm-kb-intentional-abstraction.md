---
id: llm-kb-intentional-abstraction
title: LLM KB 意图性抽象设计哲学
status: accepted
card_type: design-philosophy
tags:
- knowledge-management
- karpathy
- design-philosophy
- open-ended
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- developersio-jp-pattern
evidence_basis: practitioner_report
justification: ../justification/llm-kb-intentional-abstraction.md
canonical_concept: llm-kb-intentional-abstraction
aliases:
- intentional abstraction
- hacky collection of scripts
- 意図的な抽象さ
summary: 'Karpathy 刻意将 LLM Knowledge Base 保持抽象/模糊: 自称 "hacky collection of scripts",
  明言 "intentionally kept abstract/vague because there are so many directions"。非成品方法论而是探索方向共享。暗示产品化空间:
  "room for an incredible new product"。llm-kb-intentional-abstraction 意図的 抽象 hacky'
related:
- karpathy-llmc-minimalism-philosophy
- llm-wiki-intentional-abstraction
- karpathy-post-naming-effect
---

Karpathy 在 gist 中刻意保持 LLM KB 概念的开放性 [^src-1]:

- **自我定位**: "hacky collection of scripts" — 明确非成品、非方法论
- **抽象意图**: "intentionally kept a little bit abstract/vague because there are so many directions to take this in" — 方向太多, 不宜过早固化
- **产品化暗示**: "I think there is room here for an incredible new product instead of a hacky collection of scripts" [^src-2]

对实装者的含义: 没有规范答案, 三层/三操作皆可按需变形。Schema 可以是 CLAUDE.md 也可以是别的形式; Wiki 可以是纯 Markdown 也可以附加向量层。Karpathy 提供的是思考框架而非实施规范 [^card-1]。

[^src-1]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "意図的な「抽象さ」" P23 -- "gist を読んで印象的だったのは、Karpathy 氏自身がこれを「hacky collection of scripts」と呼んでいることです...「intentionally kept a little bit abstract/vague because there are so many directions to take this in」"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/markdown.md` -- "まとめ" P64 -- "I think there is room here for an incredible new product instead of a hacky collection of scripts."
[^card-1]: 参见 [kb-compile-implementation] — 作者的实装选择即为此开放性的体现
