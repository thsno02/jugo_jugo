# Audit Report

run_id:: run_20260524_125500_worker_audit_implementation_ecosystem_replacement
executor_role:: worker_executor
worker_role:: cand_006_implementation_ecosystem replacement citation/adoption audit worker
target_candidate:: cand_006_implementation_ecosystem
target_node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
target_version:: 1.0
status:: LOOP_DONE
decision:: adopt_recommended

## Scope

Inputs audited:

- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/node.yaml`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/provenance.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md`
- `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/loop_delivery.md`

## Gate results

- `card_validator`: pass.
- `footnote_layout_gate`: pass.
- `citation_target_gate`: pass by validator plus timeboxed pinned-path coverage.
- `implementation_source_support_gate`: pass.
- `metadata_boundary_gate`: pass.
- `adjacent_system_boundary_gate`: pass.
- `prior_kb_anchor_gate`: pass.
- `provenance_gate`: pass.
- `change_gate`: pass.
- `root_metadata_gate`: pass, still closed.

## Key audit findings

### GitHub metadata boundary

Pass. The card says GitHub metadata can record stars, forks, open issues, language, license, and timestamps as snapshot fields, and explicitly says those fields cannot prove usage, quality, maturity, community consensus, production deployment, or adoption scale.

### Adjacent feature boundary

Pass. OpenKB, librarian-mcp, Obsidian, MCP, graph-vault, long-document, and multimodal features are written as source-specific or adjacent evidence. The card explicitly rejects the inference that all LLM Wiki implementations support long PDFs, multimodality, graph UI, MCP, or Obsidian.

### Primary implementation support

Pass. Implementation-family claims are attached to direct README, PyPI, plugin-directory, and project-page sources. The synthesis paragraph is phrased as recurring surfaces observed in several cited examples, not as a universal ecosystem requirement.

### Prior KB usage

Pass. Prior KB citations are included only as continuity, vocabulary, and boundary anchors. They are not used to support new implementation facts.

### Provenance completeness and separation

Pass. `provenance.md` has clear sections for why the version exists, inputs used, existing data, adjacent/source-specific implementation evidence, metadata/process/gap framing, dynamic retrieval, prior KB nodes, process artifacts, production rationale, citation rationale, synthesis decisions, audit trail, adoption rationale, limits, and revision triggers. It keeps primary implementation, adjacent, metadata, process, and prior-KB sources separated.

### Change file

Pass. `change.md` is `genesis -> 1.0`, marks `adoption_status:: pending_audit`, explains first-version creation, preserves evidence limits, and states no root `node.yaml`, `kb/` view, or `generated/` index was written by generation.

### Root metadata gate

Pass. `nodes/20260524_122000_llm_wiki_implementation_ecosystem/node.yaml` and `kb/20260524_122000_llm_wiki_implementation_ecosystem.md` are absent, so the root adoption gate remains closed before controller action.

## Decision

`adopt_recommended`

## Minimal repair task

None. No repair is required before adoption on the audited criteria. If the controller wants a stricter evidence audit, the next optional task would be exhaustive source-line verification of every feature-surface phrase against each cited README/package page, but this is not required by the timeboxed audit result.
