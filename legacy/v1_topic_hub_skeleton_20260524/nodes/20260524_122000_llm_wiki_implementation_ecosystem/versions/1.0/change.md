# Change: genesis -> 1.0

node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
from_version:: genesis
to_version:: 1.0
change_scale:: major
propagation_required:: false
created_at:: 2026-05-24T12:40:00+08:00
run_id:: run_20260524_124000_worker_generation_implementation_ecosystem
adoption_status:: pending_audit

## Why this node was created

This node was created from `cand_006_implementation_ecosystem` to capture the LLM Wiki implementation ecosystem visible in the local corpus. The target is a bounded first-version landscape of implementation families, implementation surfaces, package/plugin/project metadata, adjacent-system boundaries, and missing evidence.

## Why this first version is acceptable

The first version is acceptable as a candidate because it stays inside the planned evidence scope, ties implementation-family claims to direct README/package/plugin/project-page evidence, treats metadata as metadata, marks OpenKB/graph-vault/Obsidian/MCP/long-document sources as adjacent or source-specific where needed, and avoids adoption, ranking, quality, maturity, enterprise readiness, deployment, and market claims.

Adoption remains pending. No root `node.yaml`, `kb/` view, or `generated/` index was written.

## Evidence basis

Primary implementation evidence comes from:

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/pypi/pypi-my-llm-wiki/text.txt`
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/raw/webpage/llm-wiki-net/text.txt`

Adjacent/source-specific implementation evidence comes from:

- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md`

Process and gap boundaries come from:

- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

## Known limits

- Most implementation facts are project self-descriptions.
- GitHub metadata is a local snapshot and not adoption or quality evidence.
- Package pages do not provide download counts in the evidence used here.
- Plugin/project pages do not provide install or active-use counts.
- Reddit/community discourse, traffic/clones, issue/PR outcome analysis, release-health, deployment reports, and independent implementation evaluations are not available in the planned evidence scope.
- Adjacent OpenKB, graph-vault, Obsidian, MCP, and long-document claims are not generalized across all LLM Wiki implementations.

## Expected future changes

Future versions should change if audit finds unsupported claims, if source mining adds adoption or quality evidence, if package/plugin metadata changes materially, if new implementations alter the implementation-family map, or if prior adopted LLM Wiki boundary nodes receive major updates. Because this is a genesis candidate with no adopted downstream dependents, no propagation is required before audit.
