---
name: llmwiki-source-mining
description: Mine LLM Wiki KB knowledge from preserved raw papers, web pages, repos, manifests, and reports. Use when converting data/raw or data/manifests into source_scope.md, source_mining.md, candidate_frontier_delta.yaml, evidence_gaps.md, or retrieval_requests.md during KB initialization.
---

# LLM Wiki Source Mining

## Purpose

Use this skill before building a node. The goal is to turn preserved sources into traceable observations and candidate knowledge, not to write the final card directly.

This skill is an executor skill. In the autonomous loop, source mining must be performed by a worker/sub-agent or independent worker mode from a task packet. The main agent may create/review the packet and decide what to do with the worker delivery, but must not directly write the mining artifacts.

## Inputs

- `data/raw/`
- `data/manifests/sources.jsonl`
- `data/manifests/source_digests.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `data/manifests/coverage_records.jsonl`
- `reports/coverage_framework.md`
- `reports/source_gap_review.md`
- Existing `kb/_index.yaml` and `nodes/`

## Workflow

1. Select a source or source batch using relevance, canonical value, diversity, gap coverage, first-version readiness, and skill-test value.
2. Write `source_scope.md` with source type, author/org, date, raw paths, source ids, readable text state, and why this source batch is in scope.
   Before declaring any raw path empty, verify both byte size and readable content with a local command such as `wc -c` plus a short read/parse check, and record that verification in `mining_trace.md`.
3. Read with lenses: structure, source-backed observations, candidate knowledge, citation feasibility, and evidence gaps.
4. Write `source_mining.md` as source-backed observations. Mark each row or bullet as observed fact, interpretation, discourse note, implementation evidence, risk, method, or gap.
5. Write `candidate_frontier_delta.yaml` with candidates that should update `.llmwiki/control/knowledge_frontier.yaml`.
6. Write `evidence_gaps.md` and `retrieval_requests.md` when evidence is insufficient.

## Hard Rules

- Do not use chat memory or model priors as evidence.
- Do not promote a candidate to `ready_to_build` unless citation feasibility is clear.
- Do not turn secondary explainers into primary source claims.
- Do not perform web retrieval from this skill. Emit a retrieval request instead.
- When running on a company machine, record blocked/intercepted sources and defer retries.
- Do not call a file empty from memory, manifest summaries, failed reads, or line counts alone. If a file is present but unusable for scope reasons, describe the process boundary rather than an empty-file state.

## Output Contract

Each mining run writes these files under `.llmwiki/runs/<run_id>/`:

- `source_scope.md`
- `source_mining.md`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`

Each run must also include executor attribution in `mining_trace.md` or `loop_delivery.md`:

- `executor_role`
- `task_packet`
- `allowed_inputs`
- `outputs_written`
- `LOOP_DONE` or `LOOP_BLOCKED`

If these artifacts were written by main agent directly, mark the run as `controller_drift_sample`, preserve the files, and require worker review/rerun before frontier adoption.

## Skill Evolution Notes

Patch this skill when mining misses source-backed distinctions, confuses evidence grades, promotes unsupported candidates, fails to record gaps that later block card generation, or allows main agent to execute mining instead of controlling worker execution.
