---
name: llmwiki-node-planning
description: Choose the next LLM Wiki KB node from the mined knowledge frontier and write an executable 0-1 node build task packet. Use when selecting one candidate for node generation, defining evidence scope, or preparing generator/auditor handoff.
---

# LLM Wiki Node Planning

## Purpose

Use this skill only after source mining has produced frontier candidates. Node planning chooses one bounded candidate and turns it into a task packet; it does not write the card.

This is an executor skill for planning artifacts. Main agent may request, review, accept, repair, or reject a planning packet, but should not directly write `planner_report.md`, `evidence_scope.yaml`, or `next_task_packet.md` for KB generation.

## Selection Criteria

Choose one candidate using:

- Evidence readiness.
- Usefulness for current KB initialization.
- Unlock value for later nodes.
- Ability to test an important skill.
- Scope small enough for a trustworthy first version.
- No unresolved retrieval blocker.

## Required Outputs

Write these files under `.llmwiki/runs/<run_id>/`:

- `planner_report.md`
- `evidence_scope.yaml`
- `next_task_packet.md`

## Task Packet Requirements

The packet must specify:

- Target candidate and proposed `node_id`.
- Version target, normally `1.0` for the first adopted version.
- Allowed primary and secondary inputs.
- Forbidden inputs and overclaim boundaries.
- File-state assumptions inherited from source mining must be rechecked against the current checkout before being written into evidence boundaries; verify byte size/content for any path described as empty, missing, unreadable, or inventory-only due to file state.
- Required output files for first-version generation:
  `nodes/<node_id>/versions/1.0/node.yaml`,
  `nodes/<node_id>/versions/1.0/card.md`,
  `nodes/<node_id>/versions/1.0/provenance.md`,
  `nodes/<node_id>/versions/1.0/change.md`.
- Explicitly state that generation must not write or adopt root
  `nodes/<node_id>/node.yaml`; root metadata is created only after adoption audit passes.
- Audit gates: object topic, source scope, citation, provenance, overclaim, retrieval, and language.
- Completion marker: `LOOP_DONE` or `LOOP_BLOCKED`.

## Hard Rules

- Do not plan directly from a static backlog unless the frontier already supports it.
- Do not skip source mining artifacts.
- Do not ask the generator to retrieve web pages unless a retrieval request exists.
- Do not select a broad hub node when a smaller first-version node can anchor it.
- Do not plan from controller drift sample artifacts unless a worker has reviewed/rerun them and recorded executor attribution.
- Do not propagate empty-file claims from earlier artifacts unless the planner has repeated local file-size/content verification in the planning run.
- If main agent needs the next planning step, it must create or dispatch a worker task packet rather than writing KB-generation planning artifacts itself.

## Skill Evolution Notes

Patch this skill when selected nodes are too broad, task packets omit allowed inputs, generators repeatedly need to read outside the planned scope, or planning artifacts are directly authored by main agent.
