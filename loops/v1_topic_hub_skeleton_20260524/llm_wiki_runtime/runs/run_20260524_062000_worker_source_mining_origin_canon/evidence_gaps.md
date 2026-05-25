# Evidence Gaps

run_id:: run_20260524_062000_worker_source_mining_origin_canon
executor_role:: worker_executor
phase:: source_mining
status:: LOOP_DONE

## Non-Blocking Gaps For `cand_001_origin_and_canon`

1. `karpathy-x-launch-post` raw files are empty.
   - `data/raw/webpage/karpathy-x-launch-post/text.txt`: 0 lines.
   - `data/raw/webpage/karpathy-x-launch-post/raw.txt`: 0 lines.
   - `data/raw/webpage/karpathy-x-launch-post/raw.json`: 0 lines.
   - Effect: first-version origin/canon can still proceed using gist + HN, but must not quote or rely on exact X launch wording, timestamps, view counts, likes, bookmarks, or quoted-post text.

2. `hacker-news-original-thread/item.json` is empty.
   - Effect: HN structured metadata cannot be cited from JSON. Use only visible metadata in `text.txt`, such as story title, points, comment count, links, and comment text.

3. Exact publication chronology is incomplete in allowed raw evidence.
   - Effect: a first node may say the gist is the local canonical idea file and HN is immediate public discussion, but should avoid over-precise chronology unless later raw evidence provides exact timestamps.

## Blocking Gaps For Other Candidates

1. Historical lineage before Karpathy is not resolved.
   - HN mentions older concepts such as Licklider-style intelligence amplification and existing PKM/wiki systems, but this batch does not establish a primary-source lineage.

2. Ecosystem/adoption evidence is out of scope for this run.
   - GitHub repos, PyPI packages, plugin pages, and directories are referenced in manifests/reports but were not allowed raw evidence for this worker run.

3. Empirical effectiveness is out of scope for this run.
   - Token savings, benchmark quality, long-term maintenance success, and citation accuracy require separate empirical/research mining.

4. Governance and risk evidence is incomplete.
   - HN supplies early discourse risks, but privacy, access control, poisoning, source licensing, auditability, team governance, and stale-claim rates require separate sources.

5. Blocked Reddit and intercepted enterprise materials remain unresolved at corpus level.
   - These do not block the bounded origin/canon node, but they block broader community reception and enterprise-readiness claims.

## Build Boundary Recommendation

`cand_001_origin_and_canon` is ready to build only under these boundaries:

- Primary canonical evidence: `karpathy-gist-llm-wiki`.
- Early discourse evidence: `hacker-news-original-thread/text.txt`.
- X source: source-inventory/provenance mention only until raw recapture.
- Do not use this node to prove adoption, effectiveness, enterprise suitability, or full intellectual history.

