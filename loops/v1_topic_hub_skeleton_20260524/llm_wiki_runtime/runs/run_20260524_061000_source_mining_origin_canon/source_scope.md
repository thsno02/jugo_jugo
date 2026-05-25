# Source Scope: Origin And Canon Batch

run_id:: run_20260524_061000_source_mining_origin_canon
phase:: source_mining
skill:: llmwiki-source-mining
main_language:: zh-CN
created_at:: 2026-05-24T06:10:00+08:00
status:: LOOP_DONE

## Why this batch

This is the first executable mining run because `origin_and_canon` is the strongest locally supported anchor for the LLM Wiki topic KB. It fixes the canonical origin before later nodes define the pattern, compare it to RAG, or discuss implementation/ecosystem claims.

This run follows the `llmwiki-loop-orchestration` gate: it mines sources and updates the frontier before any card generation.

## Primary sources

| source_id | type | local paths | role |
| --- | --- | --- | --- |
| `karpathy-gist-llm-wiki` | `gist_raw` | `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`, `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt` | Canonical idea file and strongest source for the pattern itself. |
| `karpathy-x-launch-post` | `webpage` | `data/raw/webpage/karpathy-x-launch-post/text.txt`, `data/raw/webpage/karpathy-x-launch-post/raw.txt`, `data/raw/webpage/karpathy-x-launch-post/raw.json` | Launch/propagation context; includes 2026-04-04 idea-file post and quoted 2026-04-02 original post. |
| `hacker-news-original-thread` | `hacker_news` | `data/raw/hacker_news/hacker-news-original-thread/text.txt`, `data/raw/hacker_news/hacker-news-original-thread/item.json`, `data/raw/hacker_news/hacker-news-original-thread/page.html` | Early public discussion and skepticism around the idea file. |

## Secondary/navigation sources

| path | use |
| --- | --- |
| `data/manifests/sources.jsonl` | Confirm source ids, status, local dirs, fetch times, source type, and priority. |
| `data/manifests/source_digests.jsonl` | Confirm source summaries, content hashes, source-supported outputs, and digest-level limitations. |
| `data/manifests/claims.jsonl` | Confirm `claim_000001` to `claim_000008` as high-confidence origin/canon claim inventory. |
| `data/manifests/claim_source_links.jsonl` | Confirm claim-to-source support links. |
| `data/manifests/coverage_records.jsonl` | Confirm required origin/canon outputs are supported. |
| `reports/source_gap_review.md` | Confirm known gaps, especially pre-Karpathy lineage. |
| `reports/coverage_framework.md` | Confirm coverage boundaries. |

## Excluded in this run

Secondary explainers, repositories, Reddit captures, and enterprise articles are excluded from substantive origin claims in this run. They may support later ecosystem, implementation, or reception nodes after their own mining runs.

## Network policy

No web retrieval was performed. The current company-machine policy remains limited attempts then defer; this run did not require retrieval.

