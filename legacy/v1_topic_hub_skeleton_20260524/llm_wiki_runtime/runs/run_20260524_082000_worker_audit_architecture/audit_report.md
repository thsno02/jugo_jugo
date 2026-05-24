# Adoption Audit Report

run_id:: run_20260524_082000_worker_audit_architecture
executor_role:: independent_audit_worker
target_node_id:: 20260524_080000_llm_wiki_three_layer_architecture
target_version:: 1.0
decision:: adopt_recommended

## Summary

The architecture candidate bundle passes citation and adoption audit. It is recommended for adoption by the controller/adoption worker. This audit did not adopt it.

## Gate Results

| Gate | Result | Notes |
| --- | --- | --- |
| bundle_files | pass | `node.yaml`, `card.md`, `provenance.md`, and `change.md` exist under `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/`. |
| provenance_path_typo | pass | The actual `provenance.md` file exists at the correct version path. Planning, generation, and bundle metadata point to `versions/1.0/provenance.md`; the Ramanujan provenance issue is therefore a message-level typo, not an actual missing or misplaced bundle file. |
| official_card_validator | pass | `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md` returned `card validation passed: 1 cards`. |
| yaml_metadata | pass | Candidate `node.yaml` parses as YAML and records `status: candidate`, `version_status: candidate_pending_audit`, `adoption_status: not_adopted`, and `adopted: false`. |
| citation_gate | pass | 14 footnote/reference blocks have required fields; all targets and pinned versions resolve. |
| source_scope_gate | pass | Gist supports the three-layer architecture. Prior KB nodes support canon/definition continuity. README and ClawHub are used as implementation variants only. Reports are secondary boundary/gap framing only. |
| overclaim_gate | pass | No workflow, ecosystem, enterprise, empirical, scale, adoption, or broad comparison expansion is made. |
| provenance_gate | pass | `provenance.md` includes required sections, separates existing data from dynamic retrieval, identifies prior KB nodes and process artifacts, separates source-backed observations from worker synthesis, records limits, and states adoption pending. |
| change_gate | pass | `change.md` is `genesis -> 1.0`, explains first-version creation, records adoption pending, and does not recommend root adoption. |
| root_adoption_boundary | pass | Root `nodes/20260524_080000_llm_wiki_three_layer_architecture/node.yaml` is absent; no `kb/` or generated adopted view was written by this audit. |

## Key Findings

No blocking repairs found.

The card's architecture claim remains bounded to the three named layers: raw sources, the wiki, and the schema/instruction layer. It correctly treats `index.md`, `log.md`, search, CLI, MCP, viewer, lint, review, provenance/citation markers, and representation storage as supporting infrastructure or implementation variants rather than a fourth required layer.

Implementation details from `llm-wiki-compiler` and ClawHub are not promoted into mandatory architecture claims. They are framed as visible implementation examples, which matches the mined evidence.

## Decision

decision:: adopt_recommended

Rationale: bundle completeness, official validation, citation resolution, source support, provenance/change completeness, and adoption-boundary checks all pass. Adoption remains a separate controller/adoption action.

## Repair Items

None required before adoption.

