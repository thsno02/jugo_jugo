---
name: llmwiki-citation-formatting
description: Format parseable Footnotes and References blocks for LLM Wiki KB cards. Use when writing or repairing citation blocks with target, target_version, pinned_version, citation_role, why_cited, and evidence_summary fields.
---

# LLM Wiki Citation Formatting

## Purpose

Use this skill whenever a card needs citations that can be parsed into dependency and evidence graphs.

## Required Fields

Every footnote and reference block must include:

- `target`
- `target_version`
- `pinned_version`
- `citation_role`
- `why_cited`
- `evidence_summary`

## Footnote Pattern

```markdown
[^1]:
    target: data/raw/.../text.txt
    target_version: raw_snapshot
    pinned_version: data/raw/.../text.txt
    citation_role: claim_support
    why_cited: Explains exactly which claim this source supports.
    evidence_summary: Summarizes the specific evidence used.
```

## Reference Pattern

```markdown
### [R1] Source or cited node title

target: kb/example_node.md
target_version: 1.0
pinned_version: nodes/example_node/versions/1.0/card.md
citation_role: background_definition
why_cited: Explains why this context matters.
evidence_summary: Summarizes what is reused from the reference.
```

## Citation Direction

`A cites B` means `A` depends on `B`. A major update to `B` can trigger impact review for `A`.

## Section Layout

Place `## References` before `## Footnotes`. `## Footnotes` must be the final top-level section in every KB/card Markdown file so Markdown footnotes render at the end of the document.

## Hard Rules

- Make `why_cited` specific; never write generic phrases like "for support".
- Use raw source paths for source evidence and node paths for KB dependencies.
- Do not cite a manifest as if it were original content; use manifests for navigation or coverage status.
- Keep `pinned_version` stable enough for audit.

## Skill Evolution Notes

Patch this skill when parser failures recur, citation roles are vague, or downstream impact analysis cannot infer dependency direction.
