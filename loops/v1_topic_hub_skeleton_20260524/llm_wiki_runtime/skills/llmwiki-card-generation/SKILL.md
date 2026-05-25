---
name: llmwiki-card-generation
description: Write source-grounded Chinese card.md files for LLM Wiki KB node version bundles. Use when a planner task packet has selected one candidate and the agent must produce readable node content with Footnotes and References sections.
---

# LLM Wiki Card Generation

## Purpose

Use this skill to write `card.md` for one planned node version. A card is a knowledge object, not a run log, taxonomy dump, or protocol explanation.

## Inputs

- The current run's `next_task_packet.md`.
- The current run's `evidence_scope.yaml`.
- Source mining artifacts named in the task packet.
- Existing KB nodes only when explicitly allowed.

## Required Shape

Every card must contain:

```markdown
# Title

...

## References

## Footnotes
```

The body can be a definition, observation, comparison, hub seed, method note, risk note, or demand-oriented explanation.

`## References` must appear before `## Footnotes`, and `## Footnotes` must be the final top-level section in the card. Do not insert any later `##` section after footnotes.

## Writing Rules

- Write primarily in Chinese; keep English terms when they are canonical.
- Mark the epistemic status of important claims: observed fact, interpretation, discourse note, working definition, hypothesis, or evidence gap.
- Bind substantive paragraphs to citations or clearly scoped source references.
- Prefer concise paraphrase over long source quotation.
- Do not present synthesis as ground truth.
- Do not import production-protocol material into object-level topic nodes.

## Comparison And Adjacent-System Rules

For comparison, boundary, risk, governance, evaluation, or adjacent-system cards:

- State the comparison axis before making contrast claims.
- Use primary or technical sources for adjacent-system facts; prior KB nodes may be continuity anchors but must not become primary evidence for new facts about RAG, GraphRAG, agent memory, PKM, enterprise systems, benchmarks, adoption, or governance.
- Avoid absence claims unless directly supported, such as "RAG lacks durable artifacts" or "agent memory has no provenance".
- Avoid superiority claims unless the task packet includes evaluation evidence and explicit baselines.
- Treat overlap as possible by default; do not frame a node as anti-RAG, anti-PKM, anti-memory, or equivalent-to-LLM-Wiki unless directly supported.
- List out-of-scope adjacent systems and evidence gaps instead of smoothing them into a broad taxonomy.

## Completion Check

Before handing off, confirm:

- The card stays inside the planned evidence scope.
- Claims do not exceed source support.
- `## Footnotes` and `## References` include parseable citation blocks.
- `## References` appears before the final `## Footnotes` section, and `## Footnotes` is the last top-level section.
- Evidence gaps are explicit rather than smoothed over.

## Skill Evolution Notes

Patch this skill when cards become too broad, hide uncertainty, mix topic content with process content, or fail citation parsing.
