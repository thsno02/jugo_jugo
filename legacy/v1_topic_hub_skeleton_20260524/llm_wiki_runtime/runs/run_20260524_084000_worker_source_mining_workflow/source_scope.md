# Source Scope

run_id:: run_20260524_084000_worker_source_mining_workflow
executor_role:: worker_executor
candidate_id:: cand_004_workflow
status:: scoped

## In-Scope Source Batch

| source_id | source type | author/org | local path | role in this run |
|---|---|---|---|---|
| `karpathy-gist-llm-wiki` | gist/idea file | Andrej Karpathy | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`; `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt` | Primary workflow source. Directly describes operations, index/log, human involvement, optional tooling, and abstract/modular boundary. |
| `repo-atomicstrata-llm-wiki-compiler` | GitHub repo README | atomicstrata | `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` | Implementation/process support only. Directly maps the pattern to ingest, compile, query/save, lint, watch, review queue, citations, viewer, and MCP. |
| `clawhub-llm-wiki-karpathy` | plugin listing/webpage | harrylabsj / ClawHub listing | `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` | Implementation/runtime support only. Directly lists raw/wiki/schema runtime, representation-first ingest, prepare/upsert tools, gap mapping, index/log, lint, CLI/MCP. |
| `20260524_062000_llm_wiki_origin_and_canon` | adopted KB node | local KB | `kb/20260524_062000_llm_wiki_origin_and_canon.md` | Prior KB anchor for bounded canon and overclaim boundaries. |
| `20260524_072000_llm_wiki_working_definition` | adopted KB node | local KB | `kb/20260524_072000_llm_wiki_working_definition.md` | Prior KB anchor for source-preserving, agent-maintained definition and maintenance loop. |
| `20260524_080000_llm_wiki_three_layer_architecture` | adopted KB node | local KB | `kb/20260524_080000_llm_wiki_three_layer_architecture.md` | Prior KB anchor for raw/wiki/schema layers and "workflow should be separate" boundary. |
| manifests/reports | local process evidence | local corpus | `data/manifests/*.jsonl`, `reports/coverage_framework.md`, `reports/source_gap_review.md` | Coverage/gap and claim-lineage support; not primary technical authority. |

## Why This Batch Is In Scope

`cand_004_workflow` is the direct continuation of the adopted architecture node. The gist gives the abstract workflow directly, while the repo README and ClawHub listing give enough local implementation evidence to avoid unsupported extrapolation from the gist alone. This batch is intentionally narrow: it prepares one workflow node, not an implementation ecosystem or evaluation node.

## Readability And Size Verification

Before mining, byte sizes were checked with `wc -c` and readable content was checked with targeted `nl`, `sed`, `rg`, and `jq` reads. No scoped source was treated as empty. Recorded sizes:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`: 10146 bytes
- `kb/20260524_072000_llm_wiki_working_definition.md`: 11849 bytes
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`: 13064 bytes
- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`: 11985 bytes
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`: 11985 bytes
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`: 23143 bytes
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`: 8201 bytes
- `data/manifests/sources.jsonl`: 45835 bytes
- `data/manifests/source_digests.jsonl`: 250601 bytes
- `data/manifests/claims.jsonl`: 57043 bytes
- `data/manifests/claim_source_links.jsonl`: 313303 bytes
- `data/manifests/coverage_records.jsonl`: 40665 bytes
- `reports/coverage_framework.md`: 34686 bytes
- `reports/source_gap_review.md`: 24527 bytes

