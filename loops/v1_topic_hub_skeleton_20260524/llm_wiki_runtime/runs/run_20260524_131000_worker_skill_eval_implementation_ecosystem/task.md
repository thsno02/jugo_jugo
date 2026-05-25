# Task

run_id:: run_20260524_131000_worker_skill_eval_implementation_ecosystem
executor_role:: skill_eval_worker
worker_role:: cand_006_implementation_ecosystem skill-eval / next-decision evaluator
task_packet:: user/controller instruction in current thread

## Scope

Evaluate the `cand_006_implementation_ecosystem` run chain from source mining through adoption/view, with special attention to:

- controller/worker boundary drift risk
- bounded implementation-ecosystem evidence closure and deferred retrieval handling
- replacement audit startup failure / silent initialized risk
- audit worker generated-output overreach and adoption recovery
- footnote layout contract enforcement
- selected-version adoption metadata synchronization
- next source-mining/frontier worker packet for continued v1 coverage

## Allowed Writes

- `.llmwiki/runs/run_20260524_131000_worker_skill_eval_implementation_ecosystem/`
- `.llmwiki/control/skill_eval_log.yaml`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- minimal targeted skill revisions if evidence warrants

## Forbidden Writes

- `nodes/`, `kb/`, or `generated/` KB content
- data source files
- archive/protocol originals
- `.llmwiki/control/knowledge_frontier.yaml` in this run, because it was not listed as an allowed write target

