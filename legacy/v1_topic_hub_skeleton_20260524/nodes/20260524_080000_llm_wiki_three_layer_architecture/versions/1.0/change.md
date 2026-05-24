# Change: genesis -> 1.0

node_id:: 20260524_080000_llm_wiki_three_layer_architecture
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T08:15:00+08:00
run_id:: run_20260524_081500_worker_generation_architecture

## Why this node was created

This node was created to isolate the LLM Wiki architecture claim from broader origin, definition, workflow, ecosystem, and comparison topics. The planner selected `cand_003_architecture` to describe the bounded three-layer structure: raw source layer, compiled wiki layer, and schema/instruction layer, with index/log/tooling as supporting infrastructure.

## Why this first version is acceptable

The first version is acceptable as a candidate because the Karpathy gist directly names the three layers and describes their roles. Adopted origin/canon and working-definition nodes provide stable prior KB boundaries. Implementation sources provide only bounded, directly mined examples of supporting infrastructure.

Adoption is pending audit. This file does not recommend root adoption and does not write adopted metadata.

## Evidence basis

- Primary architecture evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` and `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`.
- Prior KB anchors: `kb/20260524_062000_llm_wiki_origin_and_canon.md` and `kb/20260524_072000_llm_wiki_working_definition.md`, pinned to their version `1.0` cards.
- Implementation-flavored evidence: `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md` and `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`.
- Secondary boundary evidence: `reports/source_gap_review.md`, `reports/coverage_framework.md`, and the architecture source-mining/planning artifacts.

## Known limits

- No enterprise, adoption, maturity, social-metric, empirical, scale, governance, privacy/security, or broad comparison claims are included.
- Detailed ingest/compile/query/lint workflow is not the main topic and should be handled by a separate workflow node.
- Implementation-specific tools are not treated as required by the abstract architecture.
- Reports and manifests are secondary only and are not used as direct proof of Karpathy's architecture.

## Expected future changes

Future versions may refine the distinction between core layers and support infrastructure after audit or after authorized source mining for workflow, implementations, neutral architecture taxonomy, evaluation, governance, or comparison nodes. A major update to either adopted prior KB anchor should trigger impact review for this node.
