# Change: genesis -> 1.0

node_id:: 20260524_072000_llm_wiki_working_definition
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T07:35:00+08:00
run_id:: run_20260524_073500_worker_generation_working_definition

## Why this node was created

This node was created to turn `cand_002_working_definition` into a first candidate version bundle. The project needs a bounded working definition before later architecture, workflow, comparison, risk/governance, evaluation, or ecosystem nodes can depend on a shared meaning of LLM Wiki.

## Why this first version is acceptable

The first version is acceptable as a candidate because the gist directly supports the core definition: immutable raw sources, a persistent LLM-generated markdown/wiki layer, schema or instruction files, ingest/query/lint operations, index/log navigation, writeback, optional tooling, and human source/question steering.

It remains `candidate_pending_audit`. No root node metadata, KB view, generated view, or adoption marker was written.

## Evidence basis

- Primary definition evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`.
- Prior KB anchor: adopted `kb/20260524_062000_llm_wiki_origin_and_canon.md`, pinned to `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`.
- Bounded context only: HN original thread and Karpathy X launch capture.
- Secondary framing only: `reports/source_gap_review.md` and `reports/coverage_framework.md`.

## Known limits

This version does not claim enterprise readiness, empirical proof, broad adoption, complete ecosystem coverage, complete historical lineage, social-metric meaning, HN-authoritative technical proof, or rigorous comparison against adjacent systems. It also does not resolve deferred retrieval requests for comparison, evaluation, ecosystem, enterprise/scale, or broader community discourse.

## Expected future changes

Expected future changes include citation or provenance repairs after audit, boundary refinements after comparison mining, and possible wording changes if the adopted origin/canon node receives a major update. Because this candidate is not adopted and has no downstream adopted dependents, no propagation is required at creation time.
