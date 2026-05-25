---
name: llmwiki-loop-orchestration
description: Enforce autonomous LLM Wiki KB loop stage order, artifact gates, planner/frontier authority, LOOP_DONE/LOOP_BLOCKED conditions, and safe handoffs. Use before starting or resuming the KB mining loop, before emitting generator task packets, and before any card generation/adoption transition.
---

# LLM Wiki Loop Orchestration

## Purpose

Use this skill as the hard control layer for the autonomous KB mining loop. It prevents agents from jumping directly from a topic guideline, planner hunch, or default candidate into card generation.

It also enforces the role boundary: main agent is the controller / decision-maker, while worker/sub-agent or independent worker mode executes concrete KB/run artifacts from task packets.

## Roles

Main agent may:

- Create or review task packets.
- Read worker summary/status/gate/delivery artifacts.
- Decide phase transition, adoption, repair, retrieval, defer, stop, or next action.
- Update control state and process intervention records.

Main agent must not directly execute or write concrete artifacts for `source_mining`, `frontier_update`, `node_planning`, `generation`, `audit`, `view_build`, or `skill_eval`.

Worker/sub-agent must:

- Execute only from a bounded task packet.
- Create the run directory and write `task.md` plus an initial `loop_status.md` before doing long-running inspection, validation, retrieval, or script execution.
- State executor role, task packet, allowed inputs, outputs written, and `LOOP_DONE` / `LOOP_BLOCKED`.
- Leave enough summary/status for main to decide without becoming the executor.

## State Machine

Allowed order:

```text
pre_loop_planning
-> source_mining
-> frontier_update
-> node_planning
-> generation_entry_gate
-> version_bundle_generation
-> citation_and_adoption_audit
-> view_building
-> skill_evaluation
-> next_decision
```

Dynamic retrieval may interrupt source mining or generation, but retrieved material must be preserved under `data/raw/`, added to manifests, and mined before card use.

## Transition Gates

### source_mining -> frontier_update

Require:

- `source_scope.md`
- `source_mining.md`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`

### frontier_update -> node_planning

Require:

- `.llmwiki/control/knowledge_frontier.yaml`
- Candidate status is `ready_to_build`.
- Candidate has `discovered_from`, evidence state, missing evidence, and no unresolved retrieval blocker.

### node_planning -> generation_entry_gate

Require:

- `planner_report.md`
- `evidence_scope.yaml`
- `next_task_packet.md`
- The task packet names a candidate already present in `knowledge_frontier.yaml`.
- The task packet cites the source mining run that made the candidate ready.

### generation_entry_gate -> version_bundle_generation

Require:

- The generation-entry gate report says `pass`.
- Allowed inputs are bounded.
- Forbidden inputs and overclaim boundaries are explicit.
- The version target and output paths are explicit.

### version_bundle_generation -> citation_and_adoption_audit

Require:

- `versions/<version>/node.yaml`
- `versions/<version>/card.md`
- `versions/<version>/provenance.md`
- `versions/<version>/change.md`

### audit -> view_building

Require:

- Citation audit passes.
- Adoption audit says `adopt`.
- Major versions have completed impact analysis before adoption.

### view_building -> skill_evaluation

Require:

- Validators/build scripts have run or failures are recorded.
- Generated status is refreshed or the failure is durable.

## LOOP_DONE / LOOP_BLOCKED

Each run must end with:

- `LOOP_DONE`: required artifacts exist, the transition decision is recorded, and one next action is named.
- `LOOP_BLOCKED`: a named blocker prevents progress and is written to state, gap, retrieval, or validation artifacts.

If a worker cannot progress after startup or hits a timebox, it must update `loop_status.md` and emit `LOOP_BLOCKED` with the minimal unblock condition. Silent `initialized` or missing-status hangs are process failures and require a replacement worker or process review.

## Hard Rules

- Do not let `topic_plan.md`, `topic_node_backlog.yaml`, or a planner default candidate authorize generation.
- Do not let a planner emit `next_task_packet.md` from corpus review alone; it must select from `knowledge_frontier.yaml`.
- Do not let a generator run if the candidate lacks source mining artifacts.
- Do not adopt without audit and view build follow-through.
- Do not let audit workers run view-building or generated-mutating scripts such as citation/backlink/status/impact refresh unless the task packet explicitly grants adoption/view authority. If this happens accidentally, record it as audit overreach and require a later adoption/view worker to refresh generated outputs inside its legal scope before treating generated state as authoritative.
- Do not let main agent directly write concrete artifacts. If main writes `source_mining/card/provenance/change/audit/view/frontier_update/node_planning/skill_eval` artifacts, mark the run as a controller drift sample, preserve the artifacts, block direct adoption, and require worker review/rerun.

## Skill Evolution Notes

Patch this skill whenever a stage transition happens without required artifacts, a planner bypasses the frontier, a generator starts from a default candidate, or main agent drifts from controller into concrete executor.
