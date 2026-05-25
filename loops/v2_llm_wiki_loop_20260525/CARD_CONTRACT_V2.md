# Card Contract V2

`status`: active design

V2 treats a card as knowledge, not as a title restatement. A card should teach a
bounded idea, distinction, mechanism, operational rule, or source-grounded
understanding. It may be small, but it should still contain information.

## Scope

A card is scoped when a future reader can tell:

- what the knowledge is;
- where it applies;
- what would be a misuse, over-extension, or neighboring idea;
- which source evidence supports it.

The body should not be forced into a rigid template. Some cards need an
algorithmic explanation, some need a boundary, some need a contrast, and some
need a concrete operational definition. Do not add an "importance" section just
to satisfy a format.

## Required Metadata

Cards use a fixed metadata block for later processing and analysis:

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
related: []
---
```

Field rules:

- `id`: stable slug.
- `title`: short human title, not a restatement-only sentence.
- `status`: `draft`, `accepted`, `rejected`, or `superseded`.
- `card_type`: agent-chosen descriptor such as `concept`, `mechanism`,
  `distinction`, `operational_rule`, `source_claim`, or `example_pattern`.
- `tags`: free-form hashtags such as `#llm`, `#decoding`, `#agent`.
- `created_time`: first creation time.
- `edited_time`: most recent substantive edit time.
- `edited_entity`: `llm`, `human`, or `llm+human`.
- `source_ids`: local source ids used by the card.
- `provenance_card`: path to the provenance artifact.
- `aliases`: optional search aliases.
- `related`: optional linked card ids or paths.

## Body Expectations

The body is free-form, but it must be knowledge-dense enough to be useful after
the source is closed.

Avoid:

- a body that only paraphrases the title;
- generic background not supported by the source;
- over-splitting a single concept until each card loses informational content;
- hiding important operational meaning only in provenance.

Prefer:

- a clear explanation of the knowledge itself;
- a small "how" or mechanism when that is the useful part;
- a boundary or contrast when it prevents confusion;
- source-grounded examples when they sharpen the concept.

## References And Footnotes

`References` and `Footnotes` are different objects.

`References` are source-level citations. They should explain what the source is,
why it is used, and what range or fragment supports the card.

`Footnotes` are inline citation locators. They do not need explanation; they
only point to a URL, path, line, paragraph, timestamp, or JSON pointer.

Rules:

- `References` must appear before `Footnotes`.
- `Footnotes` must be the final section when present.
- Inline footnote markers should point to the final `Footnotes` section.
