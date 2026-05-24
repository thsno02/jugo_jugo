# Validation Trace

run_id:: run_20260524_110000_worker_generation_risks_governance_provenance
executor_role:: worker_executor

## Planned checks

- Bundle files exist at the four allowed version paths.
- `card.md` starts with a level-1 title and contains `## Footnotes` and `## References`.
- Citation blocks include required fields: `target`, `target_version`, `pinned_version`, `citation_role`, `why_cited`, and `evidence_summary`.
- Citation target and pinned paths resolve from repo root.
- Card claims stay within evidence scope and avoid forbidden claim classes.
- Root node metadata is not written before audit/adoption.

## Script checks

`/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`

Result: pass.

Output:

```text
card validation passed: 1 cards
```

`/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_104000_llm_wiki_risks_governance_and_provenance`

Result: expected pre-adoption failure.

Output:

```text
nodes/20260524_104000_llm_wiki_risks_governance_and_provenance: missing root node.yaml
node validation failed: 1 errors across 1 nodes
```

## Node validator note

`scripts/kb_validate_node.py` validates adopted root node directories and requires root `nodes/<node_id>/node.yaml`. This candidate generation task is explicitly forbidden from writing root node metadata before audit/adoption, so the node validator is not applicable to this candidate bundle at generation time. The audit worker should validate the version bundle directly and keep the root metadata gate closed until adoption.

## Manual sanity checks

- Bundle exists only under `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/`.
- Root `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/node.yaml` does not exist after generation.
- `kb/` and `generated/` were not written.
- `card.md` has 16 footnote blocks and 21 reference blocks; citation blocks include required fields.
- YAML parse sanity check passed for version `node.yaml`, `.llmwiki/control/action_queue.yaml`, and `.llmwiki/control/state.yaml`.
- Citation path sanity check found 37 target/pinned paths and 0 missing paths.
- Primary LLM Wiki facts cite implementation READMEs and WiCER.
- ALCE, Memory as Metabolism, eTAMP, PoisonedRAG, and GraphRAG poisoning are labeled adjacent.
- OWASP/NIST/Microsoft are broad framework or vendor vocabulary only.
- HN is early discourse only.
- Prior KB anchors are continuity references only.
- No enterprise/compliance/legal/privacy/measured-effectiveness/adoption/scale/incident-rate claim was added.

## Audit concerns

- Confirm no generic AI governance filler.
- Confirm source preservation is not framed as security/privacy safety.
- Confirm citation presence is not framed as citation faithfulness.
- Confirm adjacent threat models are not presented as direct LLM Wiki incidents.
- Confirm prior KB anchors are not used as new evidence.
- Confirm root metadata remains absent before adoption.
