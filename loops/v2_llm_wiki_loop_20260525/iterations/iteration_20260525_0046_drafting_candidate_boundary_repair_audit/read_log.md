- path: ~/.codex/skills/agent-loop-runner/SKILL.md
  reason: developer skill instructions require using the loop skill for loop/iteration tasks
  purpose: operational workflow guidance only, not audit evidence
- path: llm_wiki/loop/iterations/iteration_20260525_0046_drafting_candidate_boundary_repair_audit/task.md
  reason: current task package
  purpose: audit scope, allowed inputs, allowed writes, success gates
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/task.md
  reason: allowed target task package
  purpose: verify target role, allowed inputs, allowed writes, and repair scope
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_status.md
  reason: allowed target status
  purpose: verify target lifecycle state and recoverability
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/loop_delivery.md
  reason: allowed target delivery
  purpose: verify completion marker, claimed outputs, and scope
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/read_log.md
  reason: allowed target read log
  purpose: verify target read boundary and evidence usage
- path: llm_wiki/loop/iterations/iteration_20260525_0045_drafting_candidate_boundary_repair/artifacts/prompt_repair_report.md
  reason: allowed target artifact
  purpose: inspect repair rationale and audit recoverability
- path: llm_wiki/loop/system_prompts/card_drafting_worker.md
  reason: allowed changed system prompt
  purpose: inspect final repair content and scope
- path: llm_wiki/loop/task_templates/card_drafting_task.md
  reason: allowed changed task template
  purpose: inspect final repair content and scope
- path: llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/read_log.md
  reason: allowed failure evidence read log
  purpose: verify candidate 6 boundary failure evidence
- path: llm_wiki/loop/decisions/20260525-0733-card-drafting-candidate-6-requires-boundary-repair.md
  reason: allowed failure decision
  purpose: verify prior decision framing without assuming parent context
- path: llm_wiki/loop/reflections/20260525-read-boundary-noise-reflection.md
  reason: allowed failure reflection
  purpose: verify reflection evidence and intended repair lane
