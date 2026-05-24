# Next Worker Task Packet

task_name:: cand_006_implementation_ecosystem_source_mining_frontier
target_candidate:: cand_006_implementation_ecosystem
target_slug:: llm_wiki_implementation_ecosystem
recommended_run_dir:: .llmwiki/runs/run_20260524_121000_worker_source_mining_implementation_ecosystem
executor_role:: worker_executor
decision_target:: ready_to_plan | needs_more_mining | needs_retrieval | blocked

## Mission

Perform source mining and frontier update for a bounded v1 candidate on the LLM Wiki implementation ecosystem. The goal is to determine whether local corpus evidence is sufficient to plan a first-version ecosystem landscape node, not to generate the node.

## Topic Boundary

Cover representative implementation patterns and evidence quality across local captured repos, package metadata, plugin/directory pages, and source-gap reports.

In scope:

- implementation taxonomy: CLI compiler, MCP server, Codex/Claude/OpenCode/OpenClaw plugin/skill, Obsidian/local-first workflow, graph/viewer/web UI, package/library, long-document/OpenKB-like systems
- concrete capabilities present in local repos/docs: ingest, compile, query, view, lint, watch, review queue, citations/provenance, source hashes, graph UI, MCP, package metadata, provider/runtime choices
- surface adoption/activity signals from preserved metadata: stars, forks, open issues, created/updated/pushed timestamps, language, license, package version metadata
- evidence limits: stars are not usage; README claims are author claims; plugin/directory pages are not independent quality evidence

Out of scope:

- generating or adopting KB nodes
- broad empirical quality claims
- enterprise readiness/compliance claims
- package download counts unless already preserved locally
- source code deep audit across all repos
- unrestricted network retrieval

## Allowed Inputs

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/skills/llmwiki-source-mining/SKILL.md`
- `.llmwiki/skills/llmwiki-frontier-management/SKILL.md`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/raw/github_repo/*/github_repo.json`
- representative `data/raw/github_repo/*/repo/README.md`
- `data/raw/pypi/`
- relevant local plugin/directory/webpage captures already present under `data/raw/`
- adopted KB anchors only for boundary continuity, not as primary ecosystem evidence

## Allowed Writes

- `.llmwiki/runs/run_20260524_121000_worker_source_mining_implementation_ecosystem/`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`

## Forbidden Writes

- `nodes/`
- `kb/`
- `generated/`
- data source files
- archive/protocol originals
- skill files unless separately authorized by a later skill-eval task

## Retrieval Limits

Default to local corpus. Do not browse or retrieve broadly.

Allowed retrieval behavior:

- If a manifest-referenced local file is missing and the missing source is essential to decide `ready_to_plan`, write a retrieval request instead of attempting broad retrieval.
- If using dynamic retrieval is explicitly necessary, limit to one narrow source acquisition attempt and record exact query, URL/source id, and result.
- If blocked by company network or access controls, mark `deferred_company_network_block` and continue with bounded local evidence if possible.

## Required Artifacts

Write all of the following in the run directory:

- `task.md`
- `source_scope.md`
- `source_inventory.md`
- `source_notes.md`
- `source_mining.md`
- `evidence_matrix.yaml`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`
- `frontier_update.md`
- `frontier_trace.md`
- `next_task_packet.md`
- `loop_status.md`
- `loop_delivery.md`

## Required Checks

- Verify executor attribution in `loop_delivery.md`.
- Separate primary repo/package evidence from directory/blog/vendor framing.
- Treat `github_repo.json` metadata as activity/traction metadata only, not proof of quality or usage.
- Sample representative repos rather than reading every source file.
- Preserve uncertainty about stale captures, README self-description, package maturity, and blocked community sources.
- Do not mark the candidate `ready_to_build` unless the frontier delta includes discovered_from, evidence_state, candidate_statement, why_it_matters, missing_evidence, build_constraints, retrieval_required_before_build, and citation_feasibility.

## Decision Schema

Use one of:

- `ready_to_plan`: local evidence is sufficient for a bounded v1 implementation ecosystem node; no retrieval required before node planning.
- `needs_more_mining`: local evidence likely sufficient but needs another bounded source-profiler pass before planning.
- `needs_retrieval`: a specific missing source class blocks a bounded v1; write retrieval requests.
- `blocked`: task cannot proceed within allowed inputs/writes.

`loop_delivery.md` must end with `LOOP_DONE` or `LOOP_BLOCKED` and include `next_action`.

