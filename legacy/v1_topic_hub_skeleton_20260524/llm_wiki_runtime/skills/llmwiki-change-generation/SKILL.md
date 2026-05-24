---
name: llmwiki-change-generation
description: Write change.md for LLM Wiki KB node versions. Use when creating genesis-to-1.0 rationale, minor revision notes, or major-version semantic delta and propagation records.
---

# LLM Wiki Change Generation

## Purpose

Use this skill to explain why a version exists and what downstream review it requires.

## First Version Shape

For a first version, write:

```markdown
# Change: genesis -> 1.0

node_id:: ...
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: ...
run_id:: ...

## Why this node was created
## Why this first version is acceptable
## Evidence basis
## Known limits
## Expected future changes
```

## Later Major Version Shape

For major updates, include:

- Why this changed.
- Old meaning.
- New meaning.
- Semantic delta.
- Why this is major.
- Expected impact.

## Hard Rules

- Do not use a fixed iteration count as adoption rationale.
- Do not mark a semantic rewrite as minor.
- Do not set `propagation_required:: false` for a major adopted node unless no downstream dependency can exist.

## Skill Evolution Notes

Patch this skill when impact analysis cannot understand the semantic delta or when version changes are mislabeled.
