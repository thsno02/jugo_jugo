# Evidence Scope

run_id:: run_20260524_123000_worker_node_planning_implementation_ecosystem
target_candidate:: cand_006_implementation_ecosystem
target_node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
source_mining_run:: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem
evidence_state:: enough_for_first_version
retrieval_required_before_generation:: false

## Primary Implementation Sources

Use these as direct evidence for implementation facts. Claims should be attributed to the implementation or package that states them, not generalized across the entire ecosystem.

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md`; `data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json`: UI/desktop/web-app implementation and repository metadata snapshot.
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md`; `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/github_repo.json`: coding-agent skill/template implementation and file-structure motif.
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md`; `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/github_repo.json`: skill/plugin UX, cache, hooks, reports, comparisons, and timeline output motifs.
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`; `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/github_repo.json`: CLI/MCP compiler, ingest/compile/query/view/lint/watch, review, citations/provenance, confidence/contradiction metadata.
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`; `data/raw/github_repo/repo-kytmanov-obsidian-local/github_repo.json`: Obsidian/local-first runtime, provider switching, source hashes, review feedback, annotations, hand-edit protection.
- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md`; `data/raw/github_repo/repo-vectifyai-openkb/github_repo.json`: adjacent OpenKB/long-document implementation, scoped to source-specific claims.
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md`; `data/raw/github_repo/repo-ngmeyer-librarian-mcp/github_repo.json`: adjacent MCP/graph-vault implementation.
- `data/raw/pypi/pypi-my-llm-wiki/text.txt`; `data/raw/pypi/pypi-my-llm-wiki/pypi.json`: Python package metadata and package self-description.
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt`; `data/raw/pypi/pypi-llm-wiki-mcp/pypi.json`: MCP package metadata, tools/skills, and storage safety mechanics.
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`: plugin/runtime distribution listing; directory self-description only.
- `data/raw/webpage/llm-wiki-net/text.txt`: multi-runtime project-page implementation evidence; project self-description only.

## Secondary and Process Notes

- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`: source-to-claim mapping and source-quality limits.
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_mining.md`: synthesis and high-level evidence sufficiency summary.
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_notes.md`: planning notes on implementation patterns, package/plugin signals, metadata boundaries, and gaps.
- `reports/source_gap_review.md`: process/gap context, especially weak adoption/community evidence.
- `reports/coverage_framework.md`: planning constraint that implementation survey must be representative and not make any single implementation definitive.

## Prior-KB Anchors

Use adopted prior KB nodes only as continuity and boundary anchors. They may define vocabulary and guardrails, but they must not support new implementation facts.

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`

## Allowed Claim Types

- Descriptive implementation-family claims backed by direct README/package/plugin/project-page evidence.
- Source-specific feature-surface claims, such as ingest/compile/query/lint/watch, review, graph/view, citation/provenance, provider/runtime, MCP/plugin/API, raw/wiki/schema, Obsidian vault, and local filesystem storage.
- Package and repository metadata snapshot claims, limited to fields preserved in local package pages/json and `github_repo.json`.
- Evidence-quality claims about missing adoption, downloads, active users, independent evaluation, deployment reports, security posture, and community discourse.

## Forbidden Claim Types

- Tool rankings, market maps, market share, active-use estimates, package download claims, plugin-install counts, quality claims, maturity claims, enterprise readiness, or production-deployment claims.
- Claims that README self-description independently validates capability, reliability, or sustained maintenance.
- Claims that stars/forks/open issues indicate usage, quality, or adoption.
- Broad community trend claims from blocked Reddit/community pages or directory pages.
- Unqualified claims that all LLM Wiki implementations support long-document ingestion, multimodality, graph UX, MCP, or Obsidian.

## Footnote Layout Contract

Any generated card must place `## References` before the final `## Footnotes` section. `## Footnotes` must be the last top-level section.
