# Change: genesis -> 1.0

node_id:: 20260524_084000_llm_wiki_ingest_compile_query_lint_workflow
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T08:55:00+08:00
run_id:: run_20260524_085500_worker_generation_workflow

## Why this node was created

This node was created to turn the adopted origin/canon, working definition, and three-layer architecture into a bounded maintenance workflow node. The planner selected `cand_004_workflow` to describe ingest/source intake, compile/wiki update, query/synthesis, lint/health-check, update/file-back, and index/log maintenance without expanding into implementation ecosystem survey, enterprise readiness, empirical performance, scale, adoption, or broad comparison.

## Why this first version is acceptable

The first version is acceptable as a candidate because the Karpathy gist directly supports the abstract operations and index/log/writeback loop. Adopted KB nodes provide stable canon, definition, and architecture boundaries. The atomicstrata README and ClawHub listing provide only bounded, directly mined implementation/process examples.

Adoption is pending citation and adoption audit. This change file does not recommend root adoption and does not write adopted metadata.

## Evidence basis

- Primary workflow evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` and `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`.
- Prior KB anchors: `kb/20260524_062000_llm_wiki_origin_and_canon.md`, `kb/20260524_072000_llm_wiki_working_definition.md`, and `kb/20260524_080000_llm_wiki_three_layer_architecture.md`, pinned to their version `1.0` cards.
- Implementation variant evidence: `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` and `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`.
- Secondary boundary evidence: `reports/source_gap_review.md`, `reports/coverage_framework.md`, and the workflow source-mining/planning artifacts.

## Known limits

- No enterprise, adoption, maturity, social-metric, empirical, scale/reliability, governance, privacy/security, or broad comparison claims are included.
- Implementation-specific tools are not treated as abstract LLM Wiki requirements.
- Reports and manifests are secondary only and are not used as direct proof of the workflow.
- Multimodal details are limited to directly present representation-readiness and runtime-surface observations.

## Expected future changes

Future versions may refine the workflow after audit or after authorized source mining for neutral workflow taxonomy, implementation internals, empirical evaluation, citation accuracy, governance, or comparison nodes. A major update to any adopted prior KB anchor should trigger impact review for this candidate after adoption.
