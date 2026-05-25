# Pre-Loop Skill Coverage Audit

run_id:: run_20260524_060000_preloop_planning
audit_scope:: pre-loop skill coverage only
audited_protocol_sections:: 3,5,6,7,8,9,10,11,12,13,14
status:: needs_work

## Read Scope

- `KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md`
- `.llmwiki/skills/llmwiki-*/SKILL.md`
- `.llmwiki/control/topic_plan.md`
- `.llmwiki/control/planner_protocol.md`

## Coverage By Protocol Section

| Protocol section | Coverage | Notes |
|---|---:|---|
| 3. Agent Hierarchy | partial | L2 specialist roles are mostly covered by skills. Source Profiler is folded into `llmwiki-source-mining`; L1 run orchestration and L0 controller duties are not represented as an explicit skill or contract. |
| 5. Source Mining Loop | covered | `llmwiki-source-mining` covers source selection, reading lenses, source-backed observations, candidate delta, citation feasibility, evidence gaps, and retrieval requests. |
| 6. Dynamic Retrieval Loop | covered | `llmwiki-dynamic-retrieval` requires retrieval requests, raw preservation, manifest update, re-mining before card use, provenance recording, and limited attempts on company machines. |
| 7. 0-1 Node Build Loop | mostly covered | `llmwiki-node-planning`, `llmwiki-node-metadata`, `llmwiki-card-generation`, `llmwiki-provenance-generation`, and `llmwiki-change-generation` cover the bundle build. The missing piece is an explicit orchestrator gate that proves the selected candidate came from the mined frontier before generation starts. |
| 8. Card Build Rules | covered | `llmwiki-card-generation` and `llmwiki-citation-formatting` cover required sections, citation blocks, scope limits, epistemic status, and parseable references. |
| 9. Provenance Build Rules | covered | `llmwiki-provenance-generation` covers required sections, input separation, synthesis rationale, audit trail, adoption rationale, uncertainty, and revision triggers. |
| 10. Change Build Rules | covered | `llmwiki-change-generation` covers genesis-to-1.0 and major-version semantic delta requirements, including impact expectations. |
| 11. Audit And Adoption Loop | covered | `llmwiki-citation-audit` and `llmwiki-adoption-audit` cover schema, citation, provenance, epistemic checks, adoption statuses, and major-version impact blocking. |
| 12. Impact Loop | covered | `llmwiki-impact-analysis` covers major-change parsing, citation graph use, dependent-card classification, and impact queue output. |
| 13. Skill Evolution Loop | covered | `llmwiki-skill-evolution` covers inputs, failure-mode analysis, patch criteria, outputs, and skill patch discipline. |
| 14. Initialization Loop Structure | partial | Individual loop skills exist, but there is no single pre-loop/autonomous-loop contract that enforces stage order, required artifacts, stop conditions, and handoffs across mining, frontier, planning, generation, audit, adoption, view build, and skill evolution. |

## Missing Skills Or Contracts Before Autonomous Loop

1. Add a pre-loop run orchestration contract or skill.
   - It should define the allowed state machine from source mining to frontier merge to node planning to generation to audit/adoption to view build to skill evaluation.
   - It should require an artifact checklist before each transition.
   - It should define `LOOP_DONE` / `LOOP_BLOCKED` conditions for each loop type.

2. Add or tighten a frontier-gated planner contract.
   - `llmwiki-node-planning` correctly says planning happens only after source mining has produced frontier candidates.
   - `planner_protocol.md` currently emphasizes reading `data/`, manifests, and reports to produce `planner_report.md`, `evidence_scope.yaml`, and `next_task_packet.md`, but it does not explicitly require `knowledge_frontier.yaml` or `candidate_frontier_delta.yaml` as the planner's source of candidate authority.
   - This creates a contract mismatch: the planner could select a topic directly from corpus review or suggested topic areas instead of selecting a mined candidate.

3. Add an explicit source profiler contract or make its merger into source mining explicit.
   - Protocol section 3 lists Source Profiler separately.
   - `llmwiki-source-mining` includes source selection, so this is probably acceptable, but the skill should state that it covers both Source Profiler and Source Miner responsibilities if no separate profiler skill exists.

4. Add a generation-entry gate.
   - Before `llmwiki-card-generation` runs, the orchestrator should verify that `next_task_packet.md` names a candidate with `ready_to_build` status, cites supporting `source_mining.md`, and includes bounded allowed inputs.
   - This is the most important hard stop against premature card generation.

## Direct Card Generation Risk

Risk status:: present_but_mitigated

Mitigations already present:

- Protocol section 1 defines the required path as raw data -> source mining -> candidate frontier -> 0-1 node build.
- Section 5 explicitly says source mining converts sources into candidate knowledge, not immediately into cards.
- `llmwiki-source-mining` says the goal is not to write final cards directly.
- `llmwiki-frontier-management` forbids converting suggested topic areas directly into `ready_to_build` candidates.
- `llmwiki-node-planning` forbids planning directly from a static backlog unless the frontier already supports it.
- `llmwiki-card-generation` requires a planner task packet, evidence scope, and named source mining artifacts.
- `topic_plan.md` says suggested topic areas are not an execution order and that generator cannot bypass planner.

Remaining risk:

- `planner_protocol.md` can be read as letting the planner inspect the corpus and directly produce a task packet, without requiring a prior `candidate_frontier_delta.yaml` merge into `.llmwiki/control/knowledge_frontier.yaml`.
- `topic_plan.md` includes a default candidate and default evidence scope. Although it says the planner must decide from evidence, an autonomous agent could treat those defaults as enough to generate a node if no explicit frontier gate is enforced.
- No single orchestration contract currently blocks card generation when source mining/frontier artifacts are absent or stale.

## Conclusion

verdict:: needs_work

The new skill set covers most protocol responsibilities for sections 5 through 13. The main gap is not individual specialist coverage; it is pre-loop control. Before starting an autonomous loop, add a hard orchestration/planner gate that requires mined source artifacts and a frontier-backed `ready_to_build` candidate before any generator skill can create `card.md`.

Highest priority fix:

Patch `planner_protocol.md` and/or add a dedicated pre-loop orchestration skill so that `next_task_packet.md` may only be emitted from a candidate already present in `.llmwiki/control/knowledge_frontier.yaml` with source lineage, evidence state, and no unresolved retrieval blocker. This should be the required contract before generator execution.
