# Skill Invocation Plan

run_id:: run_20260524_060000_preloop_planning
status:: planning_complete_gate_added

## Pre-Loop Skill Calls

### 0. llmwiki-loop-orchestration

用途：启动或恢复自治 loop 前的硬闸门。它检查 state machine、artifact checklist、frontier authority、generation-entry gate 和 `LOOP_DONE` / `LOOP_BLOCKED` 条件。

落盘结果：

- `.llmwiki/control/orchestration_gates.yaml`
- `generation_entry_gate.md`，在未来 generation 前写入。

### 1. agent-loop-runner

用途：把 KB 初始化定义为可恢复 loop，而不是一次性内容生成。

落盘结果：

- `.llmwiki/control/autonomous_loop_plan.md`
- `.llmwiki/control/loop_manifest.yaml`
- `.llmwiki/control/knowledge_frontier.yaml`

### 2. skill-creator

用途：初始化 protocol-aligned repo-local skills，并让后续 loop 能对 skills 自我评估和 patch。

落盘结果：

- `.llmwiki/skills/llmwiki-*/SKILL.md`
- `.llmwiki/control/skill_registry.yaml`

### 3. llmwiki-source-mining

启动 loop 后第一调用。它必须先处理 origin/canon source batch，写 source mining artifacts。

### 4. llmwiki-frontier-management

第二调用。它接收 `candidate_frontier_delta.yaml`，更新 `knowledge_frontier.yaml`，决定候选是否 `ready_to_build`。

### 5. llmwiki-node-planning

第三调用。它只允许从 `ready_to_build` frontier 中选择一个 node，写 generator packet。

### 6. Generation Skills

在 node planning 之后调用：

- `llmwiki-node-metadata`
- `llmwiki-card-generation`
- `llmwiki-citation-formatting`
- `llmwiki-provenance-generation`
- `llmwiki-change-generation`

### 7. Audit Skills

生成后调用：

- `llmwiki-citation-audit`
- `llmwiki-adoption-audit`

### 8. View / Impact / Skill Evolution

Adoption 后调用：

- `llmwiki-view-building`
- `llmwiki-impact-analysis`，仅 major change。
- `llmwiki-skill-evolution`，每轮必调。

## Hard Gate

没有 `source_scope.md`、`source_mining.md`、`candidate_frontier_delta.yaml`、frontier `ready_to_build` 状态和 `generation_entry_gate.md: pass` 的候选，不得直接进入 card generation。
