---
id: olw-knowledge-item-candidates
title: olw 弱证据实体保留机制
status: accepted
card_type: mechanism
tags:
- knowledge-management
- conservative-extraction
- entity-preservation
- evidence-threshold
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-kytmanov-obsidian-local
evidence_basis: code_implementation
justification: ../justification/olw-knowledge-item-candidates.md
canonical_concept: olw-knowledge-item-candidates
aliases:
- knowledge item candidates
- knowledge item ledger
- olw items
- weak entity references
summary: olw 的 knowledge item candidates 机制：对于模糊或低证据的命名引用， 不编译为 wiki article，而保留在单独的 knowledge item ledger 中供后续审查。 接受条件为原文中确切出现该文本（标题/文件名/正文）或结构性突出引用标题。 设计原则为 named reference 不应在源内容无充分支持时成为 concept article。
  knowledge item candidate ledger weak evidence conservative extraction。
related:
- olw-three-stage-pipeline
- olw-llm-as-compiler
---

olw 在 concept 提取之外维护了一套独立的 knowledge item candidates 机制，用于保留那些证据不足以支撑独立 wiki 文章的命名引用 [^src-1] [^card-1]：

**接受条件**：
- LLM 提出的命名引用仅在原文中确切出现该文本（标题、文件名或正文）时才被接受
- 结构性突出的引用标题（如 `"A Practical Guide To Notes"`）也被纳入
- 已确认的 concept 同时镜像到 ledger 中作为 confirmed knowledge item

**不编译为文章**：这些 item 默认不参与 compile 阶段，不产生 wiki article。它们被保留供后续审查、分类或未来证据积累。

**设计原则**：据源材料所述，"a named reference should not become a concept article unless the source content supports it"——item ledger 使引用不会消失，同时避免产生缺乏证据支撑的幻觉文章 [^src-2]。

可通过 `olw items audit` 和 `olw items show` 命令查看这些候选项。

[^src-1]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Knowledge item candidates" P397-408 -- "During ingest, olw keeps a separate knowledge item ledger for ambiguous, low-evidence references found explicitly in notes"
[^src-2]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Knowledge item candidates" P410 -- "a named reference should not become a concept article unless the source content supports it. The item ledger keeps the reference from disappearing while avoiding hallucinated articles."
[^card-1]: 该机制是 olw 三阶段管线 (olw-three-stage-pipeline) 中 ingest 阶段的保守性设计体现，呼应 LLM-as-compiler (olw-llm-as-compiler) 的质量优先理念
