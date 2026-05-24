---
name: llmwiki-frontier-management
description: Maintain the LLM Wiki candidate knowledge frontier. Use when merging candidate_frontier_delta.yaml into .llmwiki/control/knowledge_frontier.yaml, ranking candidates, changing candidate status, or deciding whether a candidate needs mining, retrieval, build, rejection, or deferral.
---

# LLM Wiki Frontier Management

## Purpose

Use this skill after source mining and before node planning. The frontier is the durable queue of candidate knowledge discovered from sources; it is not a final taxonomy.

This is an executor skill when it changes frontier content. Main agent may decide whether a worker frontier merge should be adopted, but the concrete merge proposal/reconciliation must be worker-attributed.

## Frontier File

The canonical file is `.llmwiki/control/knowledge_frontier.yaml`.

Allowed statuses:

- `discovered`
- `needs_more_mining`
- `ready_to_build`
- `needs_retrieval`
- `built`
- `rejected`
- `deferred`

## Workflow

1. Read the current frontier and the new `candidate_frontier_delta.yaml`.
2. Deduplicate candidates by claim, source set, and proposed node purpose.
3. Preserve source lineage: `discovered_from`, raw paths, claim ids, and coverage records.
4. Set `evidence_state`: `enough_for_first_version`, `insufficient`, `conflicting`, or `not_yet_mined`.
5. Record missing evidence as concrete gaps, not vague TODOs.
6. Rank candidates by evidence readiness, unlock value, scope control, and skill-test value.
7. Keep rejected/deferred candidates with reasons so future agents do not rediscover the same uncertainty.

## Hard Rules

- Do not convert suggested topic areas directly into `ready_to_build` candidates.
- Do not hide weak evidence by moving a candidate to `ready_to_build`.
- Do not delete stale candidates unless they are superseded and the replacement is recorded.
- Do not use `knowledge_frontier.yaml` as a content source for a final card; it is planning state.
- Do not merge a main-authored source-mining delta directly into the frontier. If source-mining artifacts are a controller drift sample, require worker review/rerun before any `ready_to_build` adoption.
- Do not let main agent directly author `frontier_trace.md` or candidate-status changes as concrete execution; main may only record the adoption decision after worker delivery.

## Output Contract

Update `.llmwiki/control/knowledge_frontier.yaml` and record the merge in the current run's `mining_trace.md` or `frontier_trace.md`.

## Skill Evolution Notes

Patch this skill when duplicate candidates accumulate, candidate status drifts from evidence state, later generators cannot understand why a candidate was selected, or frontier execution lacks worker attribution.
