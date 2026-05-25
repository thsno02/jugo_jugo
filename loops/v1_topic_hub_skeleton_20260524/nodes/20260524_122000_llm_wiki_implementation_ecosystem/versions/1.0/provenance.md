# Provenance

node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
version:: 1.0

## Why this version exists

This first version exists because `cand_006_implementation_ecosystem` reached `ready_to_build` with `evidence_state: enough_for_first_version` and `retrieval_required_before_generation:: false`. The bundle creates a candidate node for the bounded implementation ecosystem visible in the local corpus: implementation families, engineering surfaces, file/data motifs, package/plugin/project metadata, adjacent implementation boundaries, and evidence gaps.

This version is a candidate only. It does not adopt root metadata, write a `kb/` view, update generated indexes, or perform citation/adoption audit.

## Inputs used

### Existing data

Read and used as primary implementation evidence:

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/pypi/pypi-my-llm-wiki/text.txt`
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/raw/webpage/llm-wiki-net/text.txt`

Read and used as adjacent/source-specific implementation evidence:

- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md`

Read and used only as metadata snapshots or process/gap framing:

- `data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/github_repo.json`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/github_repo.json`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/github_repo.json`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/github_repo.json`
- `data/raw/github_repo/repo-vectifyai-openkb/github_repo.json`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/github_repo.json`
- `data/raw/pypi/pypi-my-llm-wiki/pypi.json`
- `data/raw/pypi/pypi-llm-wiki-mcp/pypi.json`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

Read but not used as substantive authority:

- Existing adopted node examples under `nodes/*/versions/1.0/` for local schema, citation formatting, and run artifact conventions.

### Dynamic retrieval, if any

None. No network retrieval was used.

### Prior KB nodes

Read and used only as boundary continuity anchors:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `nodes/20260524_072000_llm_wiki_working_definition/versions/1.0/card.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `nodes/20260524_080000_llm_wiki_three_layer_architecture/versions/1.0/card.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `nodes/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow/versions/1.0/card.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `nodes/20260524_094000_llm_wiki_vs_rag_write_loop/versions/1.0/card.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`
- `nodes/20260524_104000_llm_wiki_risks_governance_and_provenance/versions/1.0/card.md`

### Process artifacts

Read and used:

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/skills/llmwiki-card-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-citation-formatting/SKILL.md`
- `.llmwiki/skills/llmwiki-provenance-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-change-generation/SKILL.md`
- `.llmwiki/skills/llmwiki-node-metadata/SKILL.md`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/next_task_packet.md`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/node_plan.yaml`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_inventory.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_notes.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_mining.md`

Out-of-scope reads were limited to existing examples and validator code. They were not used as authority for implementation ecosystem facts.

## Production rationale

The card centers on a descriptive implementation landscape rather than adoption or quality. It uses direct README, package, plugin-directory, and project-page sources for implementation-family claims; metadata files only for snapshot fields; process reports only for gaps and source discipline; and prior KB nodes only as vocabulary/boundary anchors.

## Citation rationale

Every implementation-family paragraph is tied to primary implementation or adjacent implementation sources. Package and plugin claims cite PyPI or directory/project pages. GitHub metadata is cited only as metadata. Evidence-gap and non-goal claims cite `source_gap_review.md`, `coverage_framework.md`, and planning/source-mining process artifacts. Prior KB references are included only as continuity anchors and are not used to support new implementation facts.

## Synthesis decisions

- Source-backed observation: the local corpus contains UI/desktop/web app, agent skill/template, skill/plugin UX, CLI/MCP compiler, Obsidian/local-first runtime, Python package, MCP package, plugin/runtime, and multi-runtime project-page implementation forms.
- Source-backed observation: several examples expose raw/wiki/schema or vault-like storage, ingest/compile/query/lint/watch, review, citations/provenance, graph/search/view, MCP/plugin/API/local-provider, and logs/manifests/reports.
- Source-specific boundary: OpenKB and librarian-mcp are useful adjacent implementations but are not collapsed into the LLM Wiki core.
- Metadata boundary: GitHub stars/forks/issues/language/license/timestamps are snapshot metadata only and are not evidence of adoption, quality, ranking, or maturity.
- Evidence gap: no package downloads, plugin installs, active-user counts, traffic/clones, deployment reports, issue/PR outcome analysis, or independent quality evaluation are present.
- Process rationale: prior KB nodes preserve continuity vocabulary but do not support new implementation facts.

## Audit trail

The version bundle was generated by `worker_executor` from `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/next_task_packet.md`. The generation entry decision in the task packet was `pass`. The allowed output paths were limited to the candidate version bundle and generation run artifacts, with optional minimal control status updates. Root node metadata, `kb/`, `generated/`, source evidence, skills, protocol files, archives, and other node bodies were intentionally not written.

## Adoption rationale

Adoption is pending audit. This version is acceptable as a candidate because it separates primary implementation evidence, adjacent/source-specific implementation evidence, metadata snapshots, process/gap notes, and prior-KB anchors; preserves evidence gaps; avoids adoption, ranking, quality, maturity, enterprise readiness, and market claims; and keeps the root metadata adoption gate closed. It should not be adopted until citation and adoption audit confirms parseability, source support, overclaim control, source-category separation, provenance completeness, and the footnote layout contract.

## Limits and uncertainty

This candidate does not claim adoption scale, package downloads, plugin installs, active usage, production deployment, implementation quality, maturity, market position, enterprise readiness, security posture, or reliability. It treats READMEs, PyPI pages, plugin pages, and project pages as self-description unless otherwise stated. It does not use blocked Reddit/community pages or prior KB nodes as factual implementation evidence. It does not generalize long-document, multimodal, graph, MCP, or Obsidian capabilities beyond sources that explicitly claim them.

## Revision triggers

- Audit finds citation parsing errors, unresolved paths, unsupported claims, or source-category confusion.
- Audit finds README, directory, or project-page self-description presented as independent validation.
- Audit finds GitHub stars/forks/open issues used as adoption, ranking, quality, or maturity evidence.
- Audit finds OpenKB, Obsidian, MCP, graph-vault, or long-document capabilities generalized across the whole ecosystem.
- Audit finds prior KB anchors used as new factual implementation evidence.
- New source mining adds package downloads, plugin installs, traffic/clones, issue/PR analysis, deployment reports, independent evaluations, release/security posture, or accessible community discourse.
