# Skills Inventory

Run: `run_20260524_142000_worker_v1_final_qa_delivery`

## Active `.llmwiki/skills/llmwiki-*` Skills

- `llmwiki-adoption-audit`
- `llmwiki-card-generation`
- `llmwiki-change-generation`
- `llmwiki-citation-audit`
- `llmwiki-citation-formatting`
- `llmwiki-dynamic-retrieval`
- `llmwiki-frontier-management`
- `llmwiki-impact-analysis`
- `llmwiki-loop-orchestration`
- `llmwiki-node-metadata`
- `llmwiki-node-planning`
- `llmwiki-provenance-generation`
- `llmwiki-skill-evolution`
- `llmwiki-source-mining`
- `llmwiki-view-building`

## Key Guardrails Exercised Across This Loop

- Controller boundary: main/controller creates packets and decisions; workers execute concrete source mining, planning, generation, audit, view build, skill evaluation, and delivery artifacts.
- Startup/no-progress: workers must write `task.md` and initial `loop_status.md` before long reads/work; timebox/no-progress must write `LOOP_BLOCKED`.
- Audit read-only: audit workers must not run view/generated mutating scripts; any accidental generated-output mutation must be disclosed and recovered by an adoption/view worker.
- Footnote layout: `## References` before final `## Footnotes`; `## Footnotes` last top-level section. This run verified 16/16 selected cards and KB views.
- Selected-version metadata: adopted root metadata and selected-version metadata must agree; node validators are the enforcement gate.
- Comparison/adjacent systems: comparison nodes must avoid anti-RAG/strawman claims, unsupported superiority/equivalence/absence claims, and prior-KB misuse.

## Skill Changes In This Final QA Run

None. This run did not modify skills. Existing guardrails were sufficient for final delivery.
