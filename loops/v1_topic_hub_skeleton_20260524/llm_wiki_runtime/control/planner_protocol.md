# Planner Sub-Agent Protocol

updated_at:: 2026-05-24T06:08:00+08:00
main_language:: zh-CN
active_topic:: llm_wiki
status:: frontier_gated

## 为什么需要 planner sub-agent

LLM Wiki topic corpus 很大，包含 webpages、papers、GitHub repos、PyPI pages、HN threads、blocked sources、reports、manifests 和 extracted claims。静态 `topic_plan` 只能提供方向，不能决定每轮最应该生成哪个 node。

Planner sub-agent 的职责不是从大 corpus 直接跳到 card generation，而是从已 mined 的 candidate frontier 中选择一个可执行 candidate。

## Frontier Gate

`next_task_packet.md` 只有在以下条件满足时才能生成：

1. 当前 candidate 已存在于 `.llmwiki/control/knowledge_frontier.yaml`。
2. candidate status 是 `ready_to_build`。
3. candidate 有 `discovered_from`、`evidence_state`、`candidate_statement` 和 `why_it_matters`。
4. candidate 没有 unresolved retrieval blocker。
5. 本轮或前序 run 已写出与该 candidate 对应的 `source_scope.md`、`source_mining.md` 和 `candidate_frontier_delta.yaml`。

如果这些条件不满足，planner 只能输出 mining task 或 frontier repair task，不能输出 generator task packet。

## 角色分工

### Planner sub-agent

- 读 `.llmwiki/control/knowledge_frontier.yaml`、本轮 source mining artifacts、`data/`、`data/manifests/` 和 `reports/`。
- 选择当前最有价值 `ready_to_build` candidate。
- 写 precise evidence scope。
- 写 generator task packet。
- 标记 evidence gap 与 retrieval need。
- 不写 final card，不 adopted node。

### Main orchestrator

- 启动 planner sub-agent。
- 先用 `llmwiki-loop-orchestration` 审查 candidate 是否通过 frontier gate。
- 审查 planner 输出是否可执行。
- 创建 generator/audit run。
- 运行 validators/builders。
- 维护 control state。

### Generator

- 只使用 planner 指定 evidence scope。
- 生成 version bundle。
- evidence 不足时写 retrieval request，不擅自扩大范围。

### Auditor

- 检查 schema、citation、provenance、source sufficiency 和 adoption readiness。

## Planner 输出契约

每次 planner run 至少写：

- `planner_report.md`：为什么选择这个 node、看过哪些 evidence、哪些候选被推迟。
- `evidence_scope.yaml`：primary/secondary evidence、source ids、claim ids、raw paths、known gaps。
- `next_task_packet.md`：给 generator 的可执行任务。

如果 frontier gate 未通过，planner 不写 `next_task_packet.md`，改写：

- `mining_task_packet.md` 或 `frontier_repair_task.md`
- `planner_blocker.md`

## 当前 planner run

run_id:: run_20260524_054000_topic_planner
agent:: sub-agent
status:: completed_as_evidence_handoff_not_generation_authority

Turing 输出确认 `llm_wiki_origin_and_canon` 是强候选，但该输出早于 frontier gate。它不能直接授权 generator 写 card。下一步必须先完成 origin/canon source mining artifacts，并把 candidate 更新为 `ready_to_build`。

## 硬约束

- Topic 是 LLM Wiki，不是 KB 生产机制。
- `data/` 是 primary evidence layer。
- `loop_plan_init_kb.md` 是生产协议，不是 topic source。
- 公司网络检索只做有限尝试；失败即记录并延期。
- `topic_plan.md` 和 `topic_node_backlog.yaml` 是 guidelines，不是 generation authority。
- Planner 必须从 `knowledge_frontier.yaml` 中选择 candidate；不得直接从默认候选生成 card。
