# Validation Trace

run_id:: run_20260524_112000_worker_adoption_view_risks_governance_provenance
executor_role:: worker_executor
decision:: adoption_blocked

## Official Validators

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
```

Result:

```text
card validation passed: 1 cards
```

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py --all
```

Result:

```text
card validation passed: 11 cards
```

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance
```

Result:

```text
nodes/20260524_104000_llm_wiki_risks_governance_and_provenance: missing root node.yaml
node validation failed: 1 errors across 1 nodes
```

This is expected before adoption because root metadata must not be written until all adoption gates pass.

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_node.py --all
```

Result:

```text
nodes/20260524_104000_llm_wiki_risks_governance_and_provenance: missing root node.yaml
node validation failed: 1 errors across 6 nodes
```

This is expected before adoption because the target candidate node has no root `node.yaml`.

## Footnote Layout Gate

footnote_layout_gate:: fail

Check:

```bash
rg -n '^#{1,6} ' nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md
```

Relevant result:

```text
1:# LLM Wiki 的风险、治理与 provenance 边界
25:## Footnotes
155:## References
```

Reason:

`Footnotes` is not the final top-level section, and `References` appears after `Footnotes`.

## Build Validation

View/index/citation/backlinks/impact/status build commands were not run because adoption was blocked before metadata or view writes.

Current retained counts from existing `generated/status.yaml`:

- adopted_nodes: 5
- citation_edges: 73
- open impact count: 0
