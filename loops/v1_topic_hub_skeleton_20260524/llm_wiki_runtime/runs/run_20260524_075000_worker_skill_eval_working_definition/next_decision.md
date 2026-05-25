# Next Decision

run_id:: run_20260524_075000_worker_skill_eval_working_definition
executor_role:: skill_eval_worker
status:: LOOP_DONE

## Decision

next_action:: dispatch_worker_task_packet_for_cand_003_architecture_source_mining

Choose exactly one next action: main controller should create or dispatch a worker task packet for `cand_003_architecture` source mining.

## Rationale

`cand_001_origin_and_canon` and `cand_002_working_definition` are now built and adopted. The frontier still has `cand_003_architecture` as the next discovered candidate, with `evidence_state: needs_source_batch_mining` and `next_action: source_mining_after_definition`.

Architecture is higher value than workflow for the next run because the working definition explicitly established the system boundary, while architecture supplies the structural support for later workflow, implementation ecosystem, comparison, and risk nodes. Workflow should remain next after architecture unless new source-mining evidence changes the frontier.

## Controller Boundary

The next action is dispatch only. Main controller should not perform architecture source mining, frontier update, node planning, generation, audit, view build, or skill evaluation directly.

## Suggested Worker Packet Target

- candidate_id: `cand_003_architecture`
- phase: source_mining + frontier update
- expected run family: `run_<timestamp>_worker_source_mining_architecture`
- required outcome: either mark `cand_003_architecture` `ready_to_build` with evidence-bound constraints or record retrieval/evidence blockers.

