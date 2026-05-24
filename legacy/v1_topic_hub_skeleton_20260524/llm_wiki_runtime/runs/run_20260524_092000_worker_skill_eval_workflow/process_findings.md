# Process Findings

run_id:: run_20260524_092000_worker_skill_eval_workflow
candidate:: cand_004_workflow
decision:: revise_skills_then_continue

## Controller Boundary

The main/controller boundary was maintained across the reviewed `cand_004_workflow` chain. Source mining, node planning, generation, audit, adoption/view, and this skill evaluation were worker-attributed. No evidence was found that the main agent directly authored concrete source, KB, audit, view, or skill-eval artifacts in this chain.

## Gate Clarity

The source-mining, frontier, planning, generation-entry, bundle, audit, and view gates were mostly clear and executable. The candidate moved from source-backed readiness to generation to audit to adoption/view without redoing work or bypassing worker attribution.

The weak gate is adoption/view metadata consistency. `gate_007_view_to_skill_eval` requires generated view/status artifacts and a skill-eval handoff, but the underlying view-building skill did not explicitly say whether adoption workers may update the selected version bundle metadata after audit pass. That left an adopted root metadata file pointing at a version metadata file that still says candidate.

## Validator Caveat

`generated/status.yaml` reports `adopted_nodes=4`, `citation_edges=51`, and `impact_queue_open=0`; card validation and view generation passed. However, `scripts/kb_validate_node.py --all` fails with:

```text
nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/node.yaml: adopted root points to non-adopted version
node validation failed: 1 errors across 4 nodes
```

This should not remain only a validator-expression difference. It conflicts with the existing node metadata rule to keep version bundle metadata and adopted root metadata consistent. The appropriate interpretation is a narrow process/skill contract gap: adoption/view workers should be allowed to update adoption metadata fields on the selected version metadata file after audit pass, while still preserving the generated bundle content.

## Reusable Improvement

The reusable improvement is to separate metadata adoption fields from evidence/content files in adoption/view task packets. Future packets should allow minimal updates to `versions/<version>/node.yaml` adoption fields after audit pass, while continuing to forbid rewriting `card.md`, `provenance.md`, `change.md`, source files, archive/protocol originals, or unrelated nodes.

## Next Coverage Direction

After the metadata repair worker makes node validation pass, continue toward v1 KB coverage by source-mining/decomposing `cand_005_comparison_space`. It should not generate a broad comparison node directly; it should first choose a bounded comparison slice, likely `cand_010_vs_rag_write_loop`, using primary adjacent-system sources already listed in the frontier.
