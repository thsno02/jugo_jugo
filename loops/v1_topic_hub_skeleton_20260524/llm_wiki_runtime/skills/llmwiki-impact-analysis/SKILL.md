---
name: llmwiki-impact-analysis
description: Analyze downstream effects of major LLM Wiki KB node version changes. Use when a major candidate version is created, when change.md marks propagation_required, or when generated/impact_queue.yaml must be refreshed from citation dependencies.
---

# LLM Wiki Impact Analysis

## Purpose

Use this skill when a major semantic change may affect adopted cards that cite the changed node or version.

## Inputs

- Major version `change.md`.
- `kb/_index.yaml`.
- Parsed citation graph from adopted cards.
- Prior impact queue, if any.

## Workflow

1. Parse the major change and identify old meaning, new meaning, and semantic delta.
2. Parse footnotes and references in adopted KB cards.
3. Find cards citing the changed node/version.
4. Classify impact:
   - Footnote dependency: high.
   - Reference dependency: medium.
   - Plain link or incidental mention: low or ignored by default.
5. Write `generated/impact_queue.yaml`.
6. Do not rewrite downstream nodes automatically.

## Hard Rules

- Major candidate adoption must wait until impact review is complete.
- Impact analysis is about dependency risk, not editorial preference.
- Keep queue entries actionable: cited node, dependent node, reason, strength, suggested review.

## Skill Evolution Notes

Patch this skill when major updates do not create review work, or when low-risk links flood the queue with noise.
