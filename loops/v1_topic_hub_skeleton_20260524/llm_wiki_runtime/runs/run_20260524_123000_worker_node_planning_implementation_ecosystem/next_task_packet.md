# Next Worker Task Packet

task_name:: cand_006_implementation_ecosystem_generation
target_candidate:: cand_006_implementation_ecosystem
target_node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
version_target:: 1.0
executor_role:: worker_executor
recommended_run_dir:: .llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem
decision_target:: candidate_bundle_generated | needs_planning_repair | needs_retrieval | blocked
source_mining_run:: .llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem
node_planning_run:: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem
generation_entry_decision:: pass

## Mission

Generate the first-version node bundle for `20260524_122000_llm_wiki_implementation_ecosystem@1.0`, using only the planned evidence scope. The node should describe the LLM Wiki implementation ecosystem represented in the local corpus: implementation families, implementation surfaces, file/data motifs, package/plugin/project metadata, and evidence boundaries.

Do not audit or adopt. Do not write root node metadata, `kb/`, or `generated/`.

## Allowed Inputs

Primary implementation sources:

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md`
- `data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/github_repo.json`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/github_repo.json`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/github_repo.json`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/github_repo.json`
- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md`
- `data/raw/github_repo/repo-vectifyai-openkb/github_repo.json`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/github_repo.json`
- `data/raw/pypi/pypi-my-llm-wiki/text.txt`
- `data/raw/pypi/pypi-my-llm-wiki/pypi.json`
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
- `data/raw/pypi/pypi-llm-wiki-mcp/pypi.json`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/raw/webpage/llm-wiki-net/text.txt`

Secondary/process notes:

- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_inventory.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_notes.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_mining.md`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/node_plan.yaml`
- `.llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem/evidence_scope.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`

Prior-KB anchors, boundary only:

- `kb/20260524_062000_llm_wiki_origin_and_canon.md`
- `kb/20260524_072000_llm_wiki_working_definition.md`
- `kb/20260524_080000_llm_wiki_three_layer_architecture.md`
- `kb/20260524_084000_llm_wiki_ingest_compile_query_lint_workflow.md`
- `kb/20260524_094000_llm_wiki_vs_rag_write_loop.md`
- `kb/20260524_104000_llm_wiki_risks_governance_and_provenance.md`

## Forbidden Inputs

- New web retrieval unless the generation worker records a blocker and returns to retrieval planning.
- Blocked Reddit/community pages, package download estimates, plugin install estimates, traffic/clones, issue/PR outcome analysis, or deployment claims not present in allowed inputs.
- Prior KB nodes as primary evidence for new implementation facts.
- Controller drift sample artifacts as authority.

## Allowed Writes

- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/node.yaml`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/provenance.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/change.md`
- Generation run artifacts under `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/`
- Minimal control status updates only if required by the generation task packet and orchestration gates.

## Forbidden Writes

- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/node.yaml`
- Any other root adopted node metadata
- `kb/`
- `generated/`
- source evidence files
- skills, protocol files, archives, or unrelated run artifacts

## Required Artifacts

- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/node.yaml`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/card.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/provenance.md`
- `nodes/20260524_122000_llm_wiki_implementation_ecosystem/versions/1.0/change.md`
- `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/task.md`
- `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/generation_report.md`
- `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/loop_status.md`
- `.llmwiki/runs/run_20260524_124000_worker_generation_implementation_ecosystem/loop_delivery.md`

## Citation, Provenance, and Change Constraints

- Every implementation-family claim needs a direct citation to a repo README, package page/json, plugin page, project page, or local metadata file.
- `github_repo.json` supports only snapshot fields: stars, forks, open issues, language, license, and timestamps.
- Reports are process/gap notes only.
- Prior KB anchors are continuity/boundary only, not support for new implementation facts.
- README, package, plugin, and project-page claims should be attributed as source self-description unless corroborated by another allowed source.
- Keep change/provenance explicit that this is first-version generation from `cand_006_implementation_ecosystem`, source-mining run `run_20260524_122000_worker_source_mining_implementation_ecosystem`, and planning run `run_20260524_123000_worker_node_planning_implementation_ecosystem`.
- Do not state or imply adoption scale, market share, usage, quality, maturity, enterprise readiness, package downloads, production deployment, or broad community trend.

## Audit Concerns

- Overreading stars/forks/open issues as adoption, popularity ranking, quality, or maturity.
- Collapsing adjacent OpenKB, Obsidian, MCP, graph-vault, and long-document systems into the LLM Wiki core without boundary language.
- Presenting README or directory self-description as independent validation.
- Using reports or prior KB anchors as primary implementation evidence.
- Generalizing source-specific features, such as multimodal ingest or long-PDF handling, across the whole ecosystem.
- Violating first-version generation path rules by writing root `node.yaml`, `kb/`, or `generated/`.

## Footnote Layout Contract

The generated `card.md` must place `## References` before the final `## Footnotes` section.

`## Footnotes` must be the final top-level section.

No old ordering that places Footnotes before References is allowed.

retrieval_required_before_generation:: false
recommended_next_action:: generation
