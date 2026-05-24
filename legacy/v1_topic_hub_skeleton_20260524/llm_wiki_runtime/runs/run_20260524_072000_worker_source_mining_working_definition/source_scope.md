# Source Scope

run_id:: run_20260524_072000_worker_source_mining_working_definition
executor_role:: worker_executor
candidate_id:: cand_002_working_definition
candidate_slug:: llm_wiki_working_definition

## In-Scope Source Batch

### Primary topic evidence

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
  - source_id: `karpathy-gist-llm-wiki`
  - type: preserved readable gist text
  - author/org: Andrej Karpathy
  - date state: local raw snapshot; exact capture date is not asserted by this mining run
  - role: primary source for the working definition
  - readable state: non-empty, readable markdown text
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  - source_id: `karpathy-gist-llm-wiki`
  - type: raw duplicate/snapshot of gist content
  - role: raw/source-preservation check
  - readable state: non-empty

### Prior adopted KB anchor

- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `kb/20260524_062000_llm_wiki_origin_and_canon.md`

Role: adopted origin/canon anchor. This is used to confirm that the prior blocker for cand_002 has been cleared and to inherit evidence boundaries. It is not used as a substitute for reading the primary gist.

### Boundary and discourse checks

- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/raw/hacker_news/hacker-news-original-thread/item.json`
- `data/raw/webpage/karpathy-x-launch-post/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.json`

Role: source inventory, launch context, and early-discourse boundary checks. They do not support broad adoption, enterprise, effectiveness, or ecosystem claims for this candidate.

### Navigation and coverage state only

- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`

Role: navigation, coverage status, and gap/boundary confirmation. These artifacts are not treated as primary topic evidence except when the claim is explicitly about coverage status.

## Byte-Size Verification

`wc -c` verification during this run:

| Path | Bytes | Mining Use |
| --- | ---: | --- |
| `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` | 11985 | primary readable source |
| `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt` | 11985 | raw snapshot check |
| `data/raw/webpage/karpathy-x-launch-post/text.txt` | 11825 | bounded launch/source inventory |
| `data/raw/webpage/karpathy-x-launch-post/raw.txt` | 11825 | bounded launch/source inventory |
| `data/raw/webpage/karpathy-x-launch-post/raw.json` | 11825 | bounded launch/source inventory |
| `data/raw/hacker_news/hacker-news-original-thread/text.txt` | 50430 | early discourse boundary |
| `data/raw/hacker_news/hacker-news-original-thread/item.json` | 1018 | story metadata boundary |

## Why This Batch Is In Scope

`cand_002_working_definition` was previously blocked on `needs_origin_anchor_first`. The adopted origin/canon node is now present and usable as support in `kb/_index.yaml`; the gist directly supports the working-definition elements; and the reports/manifests identify origin/definition coverage as strong while keeping broader empirical, enterprise, ecosystem, and comparison claims out of scope.
