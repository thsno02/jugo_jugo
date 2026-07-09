---
id: llmwiki-epistemic-metadata
title: llmwiki 认识论元数据模型
status: accepted
card_type: data-model
tags:
- epistemic-metadata
- provenance
- confidence
- contradiction-tracking
- lint
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-atomicstrata-llm-wiki-compiler
evidence_basis: code_implementation
justification: ../justification/llmwiki-epistemic-metadata.md
canonical_concept: llmwiki-epistemic-metadata
aliases:
- epistemic metadata
- page metadata
- confidence
- provenanceState
- contradictedBy
- claim-level provenance
summary: llmwiki 为编译页面附加认识论元数据：confidence（0-1 LLM 自报）、 provenanceState（extracted/merged/inferred/ambiguous）、contradictedBy（冲突页面列表）。 多源合并时取 min confidence、设 merged 状态、合并 contradictedBy。 段落级溯源使用 ^[source.md]
  标记，精确声明可引用行范围 ^[file:42-58]。 llmwiki lint 校验溯源标记有效性。
related:
- llmwiki-two-phase-pipeline
- llmwiki-compile-first-architecture
- memory-lifecycle-fields
---

llmwiki 为每个编译生成的 wiki 页面附加可选的认识论元数据，使下游消费者能判断页面的可信度。[^src-1] [^card-1]

三个核心字段：`confidence`（0-1，LLM 自报的综合置信度）、`provenanceState`（取值 extracted / merged / inferred / ambiguous）、`contradictedBy`（与当前页面存在矛盾的其他页面 slug 列表）。[^src-2]

多源合并时的协调规则：取所有来源中的最低 confidence、将 provenanceState 设为 'merged'、对 contradictedBy 取去重并集。[^src-3]

段落级溯源通过 `^[source.md]` 标记实现；需要更精确验证的声明可锚定到源文件的行范围，如 `^[filename.md:42-58]` 或 `^[filename.md#L42-L58]`。[^src-4]

`llmwiki lint` 提供三条与认识论元数据相关的检查规则：`low-confidence`（置信度低于阈值）、`contradicted-page`（存在矛盾标记）、`excess-inferred-paragraphs`（未引用散文段落过多）。[^src-5]

[^src-1]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Page metadata" P312 -- "Compiled pages can carry epistemic metadata in frontmatter so consumers know how trustworthy each page is."
[^src-2]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Page metadata" P317-328 -- "confidence: 0.82 ... provenanceState: merged ... contradictedBy: - slug: probabilistic-reasoning"
[^src-3]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Page metadata" P329 -- "When multiple sources merge into one slug, metadata is reconciled: min confidence, provenanceState = 'merged', union of contradictedBy (deduped by slug)."
[^src-4]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Claim-level provenance" P341-349 -- "For claims that need tighter verification, pages can pin a statement to a line range in the ingested source: ^[architecture-notes.md:42-58]"
[^src-5]: data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md -- "Page metadata" P331-335 -- "llmwiki lint adds three rules that surface this metadata: low-confidence, contradicted-page, excess-inferred-paragraphs"
[^card-1]: llmwiki-two-phase-pipeline -- 两阶段管线生成的页面即为认识论元数据的载体
