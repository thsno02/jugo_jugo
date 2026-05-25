# Source Scope

run_id:: run_20260524_062000_worker_source_mining_origin_canon
executor_role:: worker_executor
phase:: source_mining
status:: LOOP_DONE

## Source Batch

This run mines the origin/canon batch for the LLM Wiki topic. The batch is in scope because it contains the strongest local evidence for the canonical pattern, its initial framing, and early public discussion.

| source_id | type | author/org | date state | local raw paths | readable text state | scope reason |
| --- | --- | --- | --- | --- | --- | --- |
| `karpathy-gist-llm-wiki` | gist raw / idea file | Andrej Karpathy per manifest URL and content attribution | manifest fetched `2026-05-21T09:54:23.182365+00:00`; source text itself does not expose an exact publication timestamp | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`, `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt` | present; 75 lines | Canonical local source for the LLM Wiki pattern, architecture, operations, and non-prescriptive implementation boundary. |
| `karpathy-x-launch-post` | webpage / X API mirror | Andrej Karpathy per manifest URL and digest summary | manifest fetched `2026-05-21T09:54:24.193022+00:00`; raw files currently empty | `data/raw/webpage/karpathy-x-launch-post/text.txt`, `data/raw/webpage/karpathy-x-launch-post/raw.txt`, `data/raw/webpage/karpathy-x-launch-post/raw.json` | not usable in current raw files; all allowed raw paths are 0 lines | Manifest and digest indicate this was intended as launch-context evidence, but raw evidence cannot be independently re-read in this worker run. Treat as a retrieval/recapture gap, not as direct text support. |
| `hacker-news-original-thread` | Hacker News thread | HN community; story by `tamnd` in captured text | captured text says `45 days ago`; manifest fetched `2026-05-21T09:54:25.989860+00:00` | `data/raw/hacker_news/hacker-news-original-thread/text.txt`, `data/raw/hacker_news/hacker-news-original-thread/item.json` | text present; `item.json` is 0 lines | Early public discussion evidence: story metadata, links to gist/X mirror, RAG comparison debate, support, skepticism, and risk/scale concerns. |

## Manifest Context

- `sources.jsonl` records all three batch sources as `status: ok`, with gist as `gist_raw`, X as `webpage`, and HN as `hacker_news`.
- `source_digests.jsonl` records completed digests for all three batch sources and maps them to `origin_and_canon`.
- `claims.jsonl` and `coverage_records.jsonl` mark origin/canon outputs as supported at corpus level, but this worker run only promotes claims that can be bounded to the allowed evidence.
- `reports/source_gap_review.md` treats origin/definition coverage as strong while noting gaps in historical precedence, blocked Reddit, and enterprise evidence.
- `reports/coverage_framework.md` defines a working LLM Wiki around source preservation, knowledge compilation, persistent representation, provenance/auditability, and maintenance.

## Scope Boundary

The run can support a first origin/canon node about the canonical idea-file pattern and immediate HN discourse. It should not claim a complete historical lineage, broad adoption, enterprise readiness, empirical effectiveness, or exact X-launch post contents unless the empty X raw files are recaptured or otherwise validated in a later retrieval task.

