# Skill Contract Update

decision:: repair_validated

## Contract

All KB/card Markdown must satisfy:

- `## References` appears before `## Footnotes`.
- `## Footnotes` is the final top-level section.
- No later `##` section may appear after `## Footnotes`.

## Skill Changes

- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`: updated required card shape and completion check.
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`: added section layout rule for citation blocks.
- `.llmwiki/skills/llmwiki-view-building/SKILL.md`: added footnote layout gate before adoption/view writes.
- `.llmwiki/skills/llmwiki-adoption-audit/SKILL.md`: added adoption check for the footnote layout gate.

## Skill Update Principle

The revision is intentionally minimal and contract-like: it adds only the layout rule needed to prevent Markdown footnotes from rendering in the middle of a card.

