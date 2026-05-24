# Retrieval Requests

run_id:: run_20260524_062000_worker_source_mining_origin_canon
executor_role:: worker_executor
phase:: source_mining
status:: LOOP_DONE

## Required Before Broader Claims

### RR-001: Recapture X launch post raw body

- Priority: P0 for exact X launch wording and metrics; non-blocking for bounded origin/canon first version.
- Target source: `karpathy-x-launch-post`
- Current local paths:
  - `data/raw/webpage/karpathy-x-launch-post/text.txt`
  - `data/raw/webpage/karpathy-x-launch-post/raw.txt`
  - `data/raw/webpage/karpathy-x-launch-post/raw.json`
- Problem: all current raw files are empty, despite source and digest manifests recording the source as acquired.
- Needed evidence:
  - post text
  - exact timestamp
  - quoted original post, if still available
  - social metrics only if preserved in raw capture
- Use before claiming: exact X launch wording, exact post date/time, viral metrics, or quoted original X text.

### RR-002: Restore or recapture HN structured item JSON

- Priority: P1; non-blocking for current first version.
- Target source: `hacker-news-original-thread`
- Current local path: `data/raw/hacker_news/hacker-news-original-thread/item.json`
- Problem: file is empty.
- Needed evidence:
  - story id
  - timestamp
  - score/comment fields
  - canonical URL
- Use before claiming: structured HN API metadata or exact HN creation time.

### RR-003: Historical lineage batch

- Priority: P1.
- Problem: HN comments point to older related ideas, but this origin/canon batch does not establish pre-Karpathy lineage.
- Needed evidence:
  - primary/near-primary sources for Memex, Licklider, semantic wikis, PKM, agent memory, and wiki/knowledge-compilation precedents.
- Use before claiming: Karpathy invented the concept, did not invent the concept, or any complete genealogy.

### RR-004: Community and enterprise gap recovery

- Priority: P1/P2 depending on downstream node.
- Problem: blocked Reddit and intercepted enterprise sources remain corpus-level gaps.
- Needed evidence:
  - approved Reddit exports or manual captures for practical reception threads
  - replacement or recovered enterprise deployment/case-study evidence
- Use before claiming: broad community adoption, plugin reception, long-PDF reception, or enterprise readiness.

## No Retrieval Required Before Bounded `cand_001_origin_and_canon`

The worker recommends `ready_to_build` for a bounded first-version origin/canon node because the gist directly supports the canonical pattern and HN directly supports immediate public discussion. The build must respect the evidence boundaries above.

