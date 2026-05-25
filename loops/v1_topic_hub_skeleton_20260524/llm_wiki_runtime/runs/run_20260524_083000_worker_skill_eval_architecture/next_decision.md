# Next Decision

run_id:: run_20260524_083000_worker_skill_eval_architecture
executor_role:: skill_eval_worker
status:: LOOP_DONE

## Decision

next_action:: dispatch_worker_task_packet_for_cand_004_workflow_source_mining

The next action should be a main-controller dispatch of a worker task packet for `cand_004_workflow` source mining and frontier update. Main should not directly perform source mining, frontier update, node planning, generation, audit, view build, or skill evaluation.

## Rationale

`cand_003_architecture` is now built/adopted and gives the KB a stable three-layer structure: raw sources, compiled wiki, and schema/instruction layer. The frontier explicitly says detailed ingest/compile/query/lint workflow should be handled by `cand_004_workflow` rather than overexpanded inside architecture.

`cand_004_workflow` is the highest-value next candidate because it bridges static architecture into the executable maintenance loop needed for v1 coverage. Comparison/risk mining remains important, but the frontier marks comparison as broad and needing decomposition, while risk sources need a separate risk-mining batch. Workflow is the most direct continuation from the adopted architecture node and can reuse the same primary gist plus local implementation sources without network retrieval.

## Rejected Alternatives For This Turn

- comparison/risk mining: valuable, but broader and less ready than workflow for the immediate post-architecture run.
- implementation ecosystem: source-rich but requires curation/taxonomy before a bounded node run.
- main execution: disallowed by orchestration gates; main remains controller.

## Exact Next Packet Shape

The next controller-created packet should ask a worker to mine and frontier-update `cand_004_workflow`, using allowed local sources only unless a later explicit retrieval policy changes:

- primary candidate: `cand_004_workflow`
- phase: source_mining_and_frontier_update
- likely source focus: Karpathy gist, adopted origin/canon node, adopted working-definition node, adopted architecture node, local implementation README/plugin sources, coverage/gap reports
- required outputs: source_scope.md, source_mining.md, candidate_frontier_delta.yaml, evidence_gaps.md, retrieval_requests.md, mining_trace.md, frontier_trace.md, loop_status.md, loop_delivery.md
- forbidden outputs: node generation, adoption, `nodes/`, `kb/`, `generated/`

