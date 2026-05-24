# Next Worker Task Packet

task_name:: cand_006_implementation_ecosystem_node_planning
target_candidate:: cand_006_implementation_ecosystem
target_slug:: llm_wiki_implementation_ecosystem
suggested_target_node_id:: 20260524_122000_llm_wiki_implementation_ecosystem
executor_role:: worker_executor
recommended_run_dir:: .llmwiki/runs/run_20260524_123000_worker_node_planning_implementation_ecosystem
decision_target:: generation_entry_pass | needs_more_mining | needs_retrieval | blocked

## Mission

Plan a bounded first-version node for the LLM Wiki implementation ecosystem using the worker-attributed source mining run `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/`.

## Evidence Scope

Primary sources:

- `data/raw/github_repo/repo-nashsu-llm-wiki/repo/README.md`
- `data/raw/github_repo/repo-nashsu-llm-wiki/github_repo.json`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/repo/README.md`
- `data/raw/github_repo/repo-samuraigpt-llm-wiki-agent/github_repo.json`
- `data/raw/github_repo/repo-sdyckjq-llm-wiki-skill/repo/README.md`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/repo/README.md`
- `data/raw/github_repo/repo-atomicstrata-llm-wiki-compiler/github_repo.json`
- `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md`
- `data/raw/github_repo/repo-vectifyai-openkb/repo/README.md`
- `data/raw/github_repo/repo-ngmeyer-librarian-mcp/repo/README.md`
- `data/raw/pypi/pypi-my-llm-wiki/text.txt`
- `data/raw/pypi/pypi-my-llm-wiki/pypi.json`
- `data/raw/pypi/pypi-llm-wiki-mcp/text.txt`
- `data/raw/pypi/pypi-llm-wiki-mcp/pypi.json`
- `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
- `data/raw/webpage/llm-wiki-net/text.txt`

Process/gap context:

- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/evidence_matrix.yaml`
- `.llmwiki/runs/run_20260524_122000_worker_source_mining_implementation_ecosystem/source_mining.md`

Prior KB anchors are boundary-only continuity, not primary evidence.

## Suggested Node Shape

Plan a descriptive landscape node with sections such as:

- implementation families in the local corpus;
- common implementation surfaces: raw/wiki/schema, ingest/compile/query/lint/watch, review, citations/provenance, graph/view, MCP/plugin integration, provider/runtime choices;
- activity and package metadata signals, explicitly bounded;
- evidence-quality warnings and missing adoption/community metrics.

## Non-Goals

- Do not rank tools.
- Do not claim market share, active usage, adoption scale, quality, maturity, or enterprise readiness.
- Do not claim package downloads.
- Do not make broad community trend claims from blocked Reddit or directory pages.
- Do not generalize long-document/multimodal support beyond implementations that explicitly claim it.

## Citation Constraints

- Each implementation claim needs a repo README, package page/json, plugin page, or project page citation.
- `github_repo.json` supports stars/forks/open issues/language/license/timestamps only.
- Reports are secondary/process notes for coverage and gaps.
- Prior KB anchors may define boundaries but cannot support new implementation facts.

## Generation Risks

- Overreading stars/forks as usage or quality.
- Treating README self-description as independent validation.
- Collapsing adjacent OpenKB/MCP/Obsidian tools into the LLM Wiki core concept without boundary language.
- Turning a landscape node into a market map.
- Losing the distinction between package metadata, repo implementation facts, and directory/plugin listings.

## Footnote Layout Contract

Any card-oriented planning note or generation packet must require:

- `## References` before the final `## Footnotes` section.
- `## Footnotes` as the final top-level section.
- No old ordering that places Footnotes before References.

retrieval_required_before_generation:: false
recommended_next_action:: node_planning

