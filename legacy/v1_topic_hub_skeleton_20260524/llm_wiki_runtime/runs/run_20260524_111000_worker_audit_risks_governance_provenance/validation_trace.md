# Validation Trace

run_id:: run_20260524_111000_worker_audit_risks_governance_provenance
executor_role:: worker_executor
status:: completed
decision:: adopt_recommended

## Official Card Validator

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
```

Output:

```text
card validation passed: 1 cards
```

Result: pass.

## Candidate Node Validator

No candidate-version-specific node validator exists in `scripts/`. The available node validator is `scripts/kb_validate_node.py`, and inspection shows it requires a root `nodes/<node_id>/node.yaml` with adopted-root metadata before checking the selected version bundle.

Root-only validator not run as an adoption gate for this candidate because the task explicitly forbids root metadata before audit, and the expected state is:

```text
nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml absent
```

The root metadata gate is therefore checked by filesystem existence, not by the root-only validator.

## Bundle Presence

Observed bundle files:

```text
card.md
change.md
node.yaml
provenance.md
```

## Citation Count

Command:

```bash
rg -c "^(\[\^[0-9]+\]:|### \[R[0-9]+\])" nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
```

Output:

```text
37
```

Result: matches `citation_blocks_expected: 37`.

## Root Metadata Gate

Command:

```bash
test -e nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml; echo root_node_yaml=$?
```

Output:

```text
root_node_yaml=1
```

Result: pass. Root metadata is absent before adoption.

## Trace Note

`scripts/kb_parse_citations.py` was inspected during validator discovery and was briefly run once against the card. It writes `generated/citation_graph.yaml` and `generated/backlinks.yaml`, so it is not treated as an allowed audit validator for this run. The audit decision above relies on the official card validator, direct bundle inspection, source reads, and root-gate existence checks.
