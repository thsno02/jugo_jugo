# Draft-First Pipeline V3

V3 optimizes the order of work:

```text
material
-> draft card
-> similarity top 3
-> comparison provenance
-> decision
-> publication gate or fusion audit
-> candidate KB adoption
```

## Stage 1: material_to_draft

Read one source material unit or exhausted article. Produce scoped, knowledge-dense draft cards under `outputs/llm_wiki/drafts/cards/` and draft provenance under `outputs/llm_wiki/drafts/provenance/`.

Do not read the whole KB during this stage. The point is throughput and clean card creation.

## Stage 2: similarity_top3

For each draft title:

- tokenize the draft title with Jieba;
- tokenize accepted card titles from the configured comparison index;
- compute Jaccard set similarity;
- write the top 3 candidates;
- treat the result as candidate retrieval only.

The default comparison base is `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md` until v3 has its own accepted index.

## Stage 3: comparison_provenance

For any draft/A-card pair that affects the action, answer three questions:

1. Why does the draft appear to share something with A?
2. Where is the draft different from A?
3. What is the core basis for the next action?

Write the answers as a provenance artifact. Do not leave them only in a task result or chat.

## Stage 4: decision

Allowed decisions:

- `new_card`: no meaningful overlap with accepted cards; run publication gate.
- `merge_candidate`: draft and A should likely become one card; requires fusion audit.
- `provenance_delta`: draft does not change card body much, but adds evidence or nuance; requires audit.
- `duplicate_skip`: draft is already covered; preserve comparison provenance but do not adopt.
- `revise_before_gate`: draft has promise but lacks information, boundary, evidence, or scope clarity.

## Stage 5: adoption

For `new_card`, adopt into `outputs/llm_wiki/kb/cards/` only after the lightweight publication gate passes.

For `merge_candidate` and `provenance_delta`, adoption is blocked until audit passes and the accepted card provenance links back to the comparison provenance.

## Throughput Principle

The expensive reasoning should happen after draft creation and only around the top 3 likely overlaps. V3 should make it cheap to produce draft knowledge, and expensive only to merge.
