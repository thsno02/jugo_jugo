# Validation Trace

run_id:: run_20260524_135000_worker_audit_evaluation_evidence
executor_role:: worker_executor
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0

## Commands Run

### Card validator

command:: `/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md`

result:: pass

output::

```text
card validation passed: 1 cards
```

### Node validator applicability check

command:: `/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_132000_llm_wiki_evaluation_evidence`

result:: expected_not_applicable_for_unadopted_candidate_bundle

output::

```text
nodes/20260524_132000_llm_wiki_evaluation_evidence: missing root node.yaml
node validation failed: 1 errors across 1 nodes
```

reason:: `scripts/kb_validate_node.py` validates adopted node directories from root `nodes/<node_id>/node.yaml` metadata. This candidate intentionally keeps the root metadata gate closed before adoption audit; therefore the root-only validator failure is expected and is not a candidate bundle defect.

## Manual / Read-Only Checks

- Candidate bundle files exist under `nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/`.
- Root `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml` does not exist, confirming root metadata adoption gate remains closed.
- Card citation paths and pinned paths resolve through the official card validator.
- `## References` appears at card line 17.
- `## Footnotes` appears at card line 217.
- `## Footnotes` is the final top-level section.
- No mutating view/index/citation/backlink/status/root/kb/generated script was run.

