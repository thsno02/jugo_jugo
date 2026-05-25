# Controller Drift Note

run_id:: run_20260524_061000_source_mining_origin_canon
status:: controller_drift_sample
recorded_at:: 2026-05-24T06:18:00+08:00

## Finding

The source-mining artifacts in this run were written directly by the main agent. That is a process failure: main agent must be controller / decision-maker, not concrete executor.

## Preserved Artifacts

Do not delete or rewrite the existing source-mining artifacts:

- `source_scope.md`
- `source_mining.md`
- `candidate_frontier_delta.yaml`
- `evidence_gaps.md`
- `retrieval_requests.md`
- `mining_trace.md`
- `frontier_trace.md` if present later

They are retained as a controller drift sample and as possible input for a worker review/rerun.

## Required Intervention

- Block direct adoption of this run's candidate frontier delta.
- Do not proceed to KB node generation from these main-authored artifacts.
- Main must create or dispatch a worker task packet for origin/canon source-mining review or rerun.
- Worker delivery must include executor attribution, bounded inputs, outputs written, and `LOOP_DONE` / `LOOP_BLOCKED`.

## Boundary Rule

Future `source_mining`, `frontier_update`, `node_planning`, `generation`, `audit`, `view_build`, and `skill_eval` concrete execution must be performed by worker/sub-agent or independent worker mode from a task packet. Main may only create/review packets, read summary/status/gate/delivery, and decide adoption/next action.
