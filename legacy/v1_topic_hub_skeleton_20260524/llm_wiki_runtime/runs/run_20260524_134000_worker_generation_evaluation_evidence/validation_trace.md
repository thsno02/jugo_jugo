# Validation Trace

run_id:: run_20260524_134000_worker_generation_evaluation_evidence
candidate:: cand_007_evaluation_evidence
node_id:: 20260524_132000_llm_wiki_evaluation_evidence
version:: 1.0

## Checks Run

### Card validator

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md
```

Result:

```text
card validation passed: 1 cards
```

### Footnote layout gate

Contract: `## References` must appear before `## Footnotes`, and `## Footnotes` must be the final top-level section.

Command:

```bash
/opt/homebrew/bin/python3 -c "from pathlib import Path; p=Path('nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/card.md'); lines=p.read_text().splitlines(); sections=[(i+1,l) for i,l in enumerate(lines) if l.startswith('## ')]; refs=[i for i,l in sections if l=='## References']; foot=[i for i,l in sections if l=='## Footnotes']; ok=bool(refs and foot and refs[-1] < foot[-1] and sections[-1][1]=='## Footnotes'); print('footnote_layout_gate:', 'pass' if ok else 'fail'); print('top_sections:', sections); raise SystemExit(0 if ok else 1)"
```

Result:

```text
footnote_layout_gate: pass
top_sections: [(17, '## References'), (217, '## Footnotes')]
```

### Candidate node YAML sanity check

Command:

```bash
/opt/homebrew/bin/python3 -c "from pathlib import Path; from scripts.kb_common import load_yaml; p=Path('nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml'); data=load_yaml(p); required=['schema','id','node_id','version','title','version_status','adoption_status','created_by','paths','audit','citation_summary']; missing=[k for k in required if k not in data]; files=[Path(data['paths'][k]) for k in ['card','provenance','change']]; print('candidate_node_yaml_parse:', 'pass'); print('required_fields_missing:', missing); print('bundle_paths_exist:', all(f.exists() for f in files)); raise SystemExit(0 if not missing and all(f.exists() for f in files) else 1)"
```

Result:

```text
candidate_node_yaml_parse: pass
required_fields_missing: []
bundle_paths_exist: True
```

### Adopted-node validator applicability

Command:

```bash
/opt/homebrew/bin/python3 scripts/kb_validate_node.py nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml
```

Result:

```text
nodes/20260524_132000_llm_wiki_evaluation_evidence/versions/1.0/node.yaml: missing root node.yaml
node validation failed: 1 errors across 1 nodes
```

Interpretation: this validator expects an adopted node directory with root `node.yaml`. It is not applicable as a pass/fail gate for this candidate bundle because generation is explicitly forbidden from writing `nodes/20260524_132000_llm_wiki_evaluation_evidence/node.yaml` before audit/adoption. Candidate-specific YAML sanity check passed.

## Sanity Summary

- Card section/citation validator: pass.
- Footnote layout gate: pass.
- Candidate node YAML parse and required fields: pass.
- Candidate bundle files present: pass.
- Adopted-root node validator: not applicable to candidate bundle; failure is expected because root adoption metadata is intentionally absent.

