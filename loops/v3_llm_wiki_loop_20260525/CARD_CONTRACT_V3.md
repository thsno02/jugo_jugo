# Card Contract V3

V3 keeps the important v2 correction: a card is knowledge. It should teach a bounded idea, distinction, mechanism, operational definition, example pattern, or source-grounded claim. A card that only restates or paraphrases its title is not useful.

## Scope

There is no hard universal atom size. `beam search` can be one card, but a specific understanding of `N` in beam search or the algorithmic idea behind pruning can also be a card if it carries useful knowledge.

A good card makes the reader understand:

- the knowledge itself;
- how it works or how to use the distinction when that matters;
- the boundary or neighboring idea when confusion is likely;
- which source evidence supports it.

The body is intentionally not a rigid template. Do not add empty sections to satisfy format.

## Required Metadata

```yaml
---
id:
title:
status: draft
card_type:
tags: []
created_time:
edited_time:
edited_entity: llm
source_ids: []
provenance_card:
aliases: []
related: []                # AUTO-DERIVED from body footnotes; do not maintain manually
---
```

Rules:

- `id`: stable slug.
- `title`: short human title, not a title-only claim disguised as a sentence.
- `status`: `draft`, `accepted`, `rejected`, or `superseded`.
- `card_type`: agent-chosen descriptor such as `concept`, `mechanism`, `distinction`, `operational_rule`, `source_claim`, or `example_pattern`.
- `tags`: free-form hashtags such as `#llm`, `#decoding`, `#agent`, or `#knowledge-system`.
- `created_time`: first creation time.
- `edited_time`: most recent substantive edit time.
- `edited_entity`: `llm`, `human`, or `llm+human`.
- `source_ids`: local source ids used by the card. Card-level heritage; manually maintained (or derivable from raw footnotes).
- `provenance_card`: path to the card-level provenance artifact.
- `aliases`: optional search aliases.
- `related`: **auto-derived** from the body `## Footnotes` section. Lists other KB card ids (v3 same loop or v2 cross-loop) referenced by footnotes. Do **not** maintain this by hand; regenerate via `tools/derive_metadata_from_footnotes.py` after each body edit.

## Body Expectations

Prefer knowledge density over uniform shape. The body should still be readable after the source is closed.

Avoid:

- title restatement;
- generic background not supported by the source;
- splitting until every card loses information;
- hiding the actual knowledge only in provenance.

Prefer:

- a crisp explanation of the idea;
- mechanism or operational meaning when useful;
- boundary, contrast, or misuse condition;
- small source-grounded examples when they sharpen the point.

## Citations: Unified Footnote Model

V3 has **one** citation mechanism: markdown footnote-style markers in body, expanded in a single `## Footnotes` section at the end. Each footnote may point to any of four target domains.

### Why one mechanism (rationale)

Previous v3 contracts separated `## References` (card-level "this card refers to this idea / source") from `## Footnotes` (claim-level inline locators). That split forced authors into structural decisions per citation and left frontmatter `related:` semantically dangling (no body anchor → silently rots). The unified footnote model:

- handles 1-to-N citations per sentence naturally (chain `[^a][^b][^c]`);
- treats raw sources, v3 cards, v2 cards, and external URLs as the same kind of citable thing — only the target path differs;
- becomes the single source of truth from which graph metadata (`related:`) can be auto-derived.

### Footnote target domains

| target type | example footnote expansion |
|---|---|
| **raw source** | `[^src1]: \`data/raw/webpage/karpathy-x-launch-post/text.txt\` — JSON pointer \`$.tweet.text\` — "Karpathy: ..."` |
| **v3 KB card** (same loop) | `[^v3-1]: [karpathy-gist-three-layers](karpathy-gist-three-layers.md) — 本卡的三层骨架来自这里` |
| **v2 KB card** (cross-loop) | `[^v2-1]: v2 anchor [llm-wiki-three-layer-architecture](../../../../../v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md) — 本卡是该卡的 delta` |
| **external URL** | `[^url1]: <https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f>` |

### Body usage rules

- Anchor with `text[^id]` markers at the specific sentence whose claim is supported / extended / contradicted / referenced by the target.
- Multiple targets at one anchor: chain markers `text[^a][^b][^c]`.
- Footnote IDs are author-chosen, free-form. Common conventions:
  - prefix-based: `src1`, `v3-1`, `v2-1`, `url1` (signals target type at marker)
  - numeric: `1`, `2`, `3` (compact; type only visible in expansion)
- Each `[^id]` marker in body must have exactly one `[^id]: ...` expansion in `## Footnotes`.

### `## Footnotes` section

- One section per card, placed at end of body.
- Contains every expansion. Order should follow first appearance in body, but tools may sort otherwise.
- Each expansion is one line, markdown link plus an optional short narrative after `—`.
- No `## References` section. Card-level "what this card is broadly about" is expressed by:
  - `source_ids:` frontmatter (raw-source heritage); and/or
  - body footnotes anchored at the first relevant sentence (idea-level pointer).

### Derived frontmatter (`related:`)

`related:` is populated by `tools/derive_metadata_from_footnotes.py`. The script:

- scans `## Footnotes` for v3-card and v2-card targets;
- emits the union as `related: [id1, id2, ...]` in frontmatter;
- runs idempotently — re-running after a body edit refreshes the field.

Authors should treat `related:` as **read-only** in editing. To change the graph, change the body footnotes.

Raw-source and external-URL footnote targets do not enter `related:` — they enter `source_ids:` (raw) or are body-only (URL). The script may also regenerate `source_ids:` from raw footnotes if you opt in (see script CLI).
