# Planning Repair Report

run_id:: run_20260524_063500_worker_node_planning_repair_origin_canon
executor_role:: worker_executor
phase:: node_planning_repair
repair_target_run:: .llmwiki/runs/run_20260524_063000_worker_node_planning_origin_canon
status:: LOOP_DONE

## Issue

The original `next_task_packet.md` and `generation_entry_gate.md` instructed the generator to write:

- `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/change.md`

This does not match the protocol or `llmwiki-node-metadata` skill. A first version must be written as a version bundle under `nodes/<node_id>/versions/1.0/`. Root `nodes/<node_id>/node.yaml` is adopted metadata and must not be written during generation.

## Repair Applied

The repaired task packet now requires generator outputs:

- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/node.yaml`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/card.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/provenance.md`
- `nodes/20260524_062000_llm_wiki_origin_and_canon/versions/1.0/change.md`

It explicitly forbids generation from writing or adopting:

- `nodes/20260524_062000_llm_wiki_origin_and_canon/node.yaml`

## Reusable Contract Patch

This was judged to be a reusable skill/gate failure because the planning skill and gate language allowed output-path drift. Minimal patches were applied:

- `.llmwiki/skills/llmwiki-node-planning/SKILL.md` now requires first-version output paths under `nodes/<node_id>/versions/1.0/` and states that generation must not write root metadata.
- `.llmwiki/control/orchestration_gates.yaml` now requires first-version generation output paths under `nodes/<node_id>/versions/1.0/` and forbids root metadata adoption before audit.

## Not Performed

- Did not generate `node.yaml`, `card.md`, `provenance.md`, or `change.md`.
- Did not modify `nodes/`, `kb/`, or `generated/`.
- Did not retrieve network sources.

## Generator Dispatch

The repaired generation entry gate is `result:: pass`.

It is safe to dispatch a generator using `.llmwiki/runs/run_20260524_063500_worker_node_planning_repair_origin_canon/next_task_packet.md`.
