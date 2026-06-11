# Worker Task Packet: v1_final_qa_delivery_worker

You are the LLM Wiki loop worker for final QA and v1 delivery. Work in `.`. You are not the only agent in the repo; do not revert or overwrite unrelated changes. Do not spawn sub-agents.

## Role

Final QA / delivery worker for LLM Wiki v1.

## Required First Step

Create:

- `.llmwiki/runs/run_20260524_142000_worker_v1_final_qa_delivery/task.md`
- `.llmwiki/runs/run_20260524_142000_worker_v1_final_qa_delivery/loop_status.md`

Do this before long reads or validation. If timeboxed/no-progress, write `LOOP_BLOCKED` with the minimal unblock condition.

## Required Reads

- `.llmwiki/control/orchestration_gates.yaml`
- `.llmwiki/control/skill_registry.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`
- `.llmwiki/control/summary_state.md`
- `generated/status.yaml`
- `generated/impact_queue.yaml`
- `kb/_index.yaml`
- all adopted `nodes/*/node.yaml`
- all adopted selected-version `nodes/*/versions/1.0/node.yaml`
- all adopted selected-version `card.md`, `provenance.md`, `change.md`
- all `kb/*.md` cards
- latest relevant skill-eval reports, especially `.llmwiki/runs/run_20260524_141000_worker_skill_eval_evaluation_evidence/loop_delivery.md`

## Allowed Writes

- `.llmwiki/runs/run_20260524_142000_worker_v1_final_qa_delivery/`
- `.llmwiki/control/action_queue.yaml`
- `.llmwiki/control/state.yaml`
- `.llmwiki/control/standing_status.md`
- `.llmwiki/control/summary_state.md`
- `.llmwiki/control/knowledge_frontier.yaml` only for lifecycle/status consistency repair, not evidence changes
- `generated/status.yaml`
- `generated/impact_queue.yaml`
- `generated/citation_graph.yaml`
- `generated/backlinks.yaml`
- `kb/_index.yaml`

## Forbidden Writes

- Do not edit `card.md`, `provenance.md`, `change.md`, or substantive KB content.
- Do not edit data sources, raw archives, protocol originals, or unrelated run artifacts.
- Do not change skill files unless final QA finds a hard-contract bug; if so, stop and write `LOOP_BLOCKED` instead of patching.

## Required Validation

Run and record:

- target/all node validators for all 8 adopted nodes;
- target/all card validators for all selected-version cards and KB views;
- view/index refresh;
- citation graph/backlinks refresh;
- impact refresh;
- status refresh;
- YAML parse checks for control, node, index, and generated YAML.

## Footnote Layout Contract

For every adopted selected-version `card.md` and every `kb/*.md` view:

- `## References` must appear before `## Footnotes`;
- `## Footnotes` must be the final top-level section;
- no content may follow final `## Footnotes` except footnote lines.

Record an all-cards/all-views footnote layout gate with counts and failures.

## Required Final QA Checks

1. frontier/action_queue consistency:
   - all 8 adopted v1 candidates should be `built_adopted` or otherwise explicitly closed;
   - no stale `ready_to_build` lifecycle should remain for adopted candidates;
   - action queue should mark cand_007 skill eval done and final delivery done or in final state.
2. retrieval-deferred log summary:
   - summarize deferred retrieval from adopted nodes as v2/future work;
   - confirm no deferred retrieval item blocks v1 delivery.
3. skills inventory:
   - list active skills from `.llmwiki/control/skill_registry.yaml`;
   - summarize skill changes already made across the loop;
   - confirm no new skill patch is required.
4. KB index summary:
   - list adopted nodes, versions, titles, tags, and audit/adoption runs from `kb/_index.yaml`.
5. status refresh:
   - refresh `standing_status.md` and `summary_state.md` with final v1 status and blocker state.
6. final delivery report:
   - write `final_qa_report.md`;
   - write `v1_delivery_report.md`;
   - write final `loop_status.md`;
   - write `loop_delivery.md`.

## Decision Schema

Return one of:

- `v1_delivered`
- `v1_delivery_blocked`

## Required Final Response / Delivery Fields

`loop_delivery.md` and final response must include:

- decision;
- adopted KB status summary;
- validators summary;
- all-cards footnote layout gate summary;
- frontier/action_queue consistency result;
- retrieval-deferred summary;
- skills inventory summary;
- KB index summary;
- files written;
- blocker and minimal unblock condition if blocked;
- `LOOP_DONE` or `LOOP_BLOCKED`.

