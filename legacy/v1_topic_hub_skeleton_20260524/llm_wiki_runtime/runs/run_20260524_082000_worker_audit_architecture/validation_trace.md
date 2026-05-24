# Validation Trace

run_id:: run_20260524_082000_worker_audit_architecture
executor_role:: independent_audit_worker
status:: pass

## Bundle Existence

- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/node.yaml`: exists
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`: exists
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/provenance.md`: exists
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/change.md`: exists

## Official Validator

Command:

```sh
/opt/homebrew/bin/python3 scripts/kb_validate_card.py nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md
```

Result:

```text
card validation passed: 1 cards
```

## YAML Parse Check

Candidate `node.yaml` parsed with `/opt/homebrew/bin/python3` and `yaml.safe_load`.

- `status`: `candidate`
- `version_status`: `candidate_pending_audit`
- `adoption_status`: `not_adopted`
- `adopted`: `false`

## Citation Field And Path Check

Audit script parsed 14 citation/reference blocks. Every block had:

- `target`
- `target_version`
- `pinned_version`
- `citation_role`
- `why_cited`
- `evidence_summary`

Every `target` and `pinned_version` exists.

## Source Support Checks

- Gist lines around `## Architecture` directly name `Raw sources`, `The wiki`, and `The schema`.
- Gist also supports `index.md`, `log.md`, optional CLI/search/MCP tooling, and implementation-dependence/modularity.
- README supports the implementation examples cited by the card: `sources/`, hash checks, compile pipeline, wiki directories, schema, review queue, source markers, line-range citations, lint, viewer, query/save, watch, and MCP.
- ClawHub supports implementation examples cited by the card: raw/wiki/schema operating language, generated `wiki/index.md` and `wiki/log.md`, deterministic lint, CLI/MCP wrappers, OpenClaw host entry, and representation storage.

## Root Adoption Boundary

`nodes/20260524_080000_llm_wiki_three_layer_architecture/node.yaml` does not exist. No adopted root metadata was written by this audit.

## Worktree Note

The candidate bundle directory is untracked in the current worktree, but audit instructions were to audit the candidate bundle in place. This audit did not modify those bundle files.

