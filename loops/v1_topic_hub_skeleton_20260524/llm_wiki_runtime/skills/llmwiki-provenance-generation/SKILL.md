---
name: llmwiki-provenance-generation
description: Write provenance.md for LLM Wiki KB node versions. Use when documenting why a version exists, which raw and KB inputs were used, how synthesis decisions were made, what uncertainty remains, and why adoption is justified or blocked.
---

# LLM Wiki Provenance Generation

## Purpose

Use this skill to make a node auditable. `provenance.md` explains why the version can be trusted enough for its current status; it is not decorative metadata.

## Required Sections

```markdown
# Provenance

node_id:: ...
version:: ...

## Why this version exists
## Inputs used
### Existing data
### Dynamic retrieval, if any
### Prior KB nodes
### Process artifacts
## Production rationale
## Citation rationale
## Synthesis decisions
## Audit trail
## Adoption rationale
## Limits and uncertainty
## Revision triggers
```

## Distinctions To Preserve

Explicitly distinguish:

- Source-backed observation.
- Current project fact.
- Working definition.
- Interpretation.
- Synthesis.
- Hypothesis.
- Evidence gap.
- Process rationale.

## Hard Rules

- Do not claim synthesis is ground truth.
- List read inputs and used inputs separately when they differ.
- Record any out-of-scope reads with path, reason, and use.
- Tie adoption rationale to audit gates, not vibes.

## Skill Evolution Notes

Patch this skill when provenance omits inputs, hides uncertainty, fails to explain synthesis, or cannot support a later adoption audit.
