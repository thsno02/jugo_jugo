# Source Scope

run_id:: run_20260524_080000_worker_source_mining_architecture
executor_role:: worker_executor
candidate_id:: cand_003_architecture

## In-Scope Sources

### Primary Architecture Source

- source_id: `karpathy-gist-llm-wiki`
- source_type: `gist_raw`
- local paths:
  - `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
  - `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
- readable state: verified readable; both files are 11985 bytes.
- reason in scope: directly contains the `Architecture` section naming raw sources, wiki, and schema; also describes operations, index/log files, optional tools, and implementation modularity.

### Prior KB Anchors

- node_id: `20260524_062000_llm_wiki_origin_and_canon`
- path: `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- role: adopted origin/canon anchor and boundary support.

- node_id: `20260524_072000_llm_wiki_working_definition`
- path: `kb/20260524_072000_llm_wiki_working_definition.md`
- role: adopted working-definition anchor that already established the source-preserving, LLM/agent-maintained pattern and the no-overclaim boundary.

### Implementation-Flavored Support

- source_id: `repo-atomicstrata-llm-wiki-compiler`
- source_type: `github_repo`
- local path: `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- readable state: verified readable; file is 23143 bytes.
- reason in scope: directly documents one compiler implementation's `sources/`, compile pipeline, `wiki/`, `index.md`, `.llmwiki/schema.json`, review candidates, provenance markers, lint, view, query, and MCP server.
- limitation: implementation evidence only; not primary authority for the abstract architecture and not evidence for ecosystem maturity or empirical success.

- source_id: `clawhub-llm-wiki-karpathy`
- source_type: `webpage`
- local path: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- readable state: verified readable; file is 8201 bytes.
- reason in scope: directly describes a runtime around raw/wiki/schema, multimodal raw kinds, representation storage, generated index/log files, deterministic lint, CLI, MCP, and OpenClaw host entry.
- limitation: plugin/runtime listing; use only for implementation-flavored architecture support.

### Manifests And Reports

- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

Use role: acquisition provenance, coverage status, existing claim ids, and boundary checks. These are not primary architecture sources for final node claims.

## Out Of Scope

- Ecosystem survey beyond the two implementation-flavored support sources.
- Enterprise readiness, adoption metrics, empirical effectiveness, or scale claims.
- Comparison with RAG/PKM/agent memory except as a boundary already present in prior nodes.
- Retrieval or new source acquisition.
