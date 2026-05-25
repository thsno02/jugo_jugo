# Skill Eval: Controller Drift

run_id:: run_20260524_061000_source_mining_origin_canon
status:: process_intervention_required
recorded_at:: 2026-05-24T06:18:00+08:00

## Observation

Main agent directly executed source mining and wrote concrete run artifacts. The content may be useful as a sample, but the process violated the controller/executor boundary.

## Failure Class

hard_contract_break:: main_agent_executed_worker_stage

Affected stages:

- `source_mining`
- downstream `frontier_update` if adopted without worker review
- downstream `node_planning` / `generation` if allowed to proceed

## Required Skill Patches

- `llmwiki-loop-orchestration`: define main as controller and worker as executor; add process intervention for main-authored concrete artifacts.
- `llmwiki-source-mining`: require worker attribution for mining artifacts.
- `llmwiki-frontier-management`: block direct frontier adoption from controller drift sample artifacts.
- `llmwiki-node-planning`: block generation planning from unreviewed controller drift samples.

## Decision

Do not delete existing artifacts. Preserve this run as a controller drift sample, update process gates, and make the next action a worker task packet or worker dispatch for review/rerun.
