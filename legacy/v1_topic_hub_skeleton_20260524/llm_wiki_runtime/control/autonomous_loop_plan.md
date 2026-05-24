# Autonomous LLM Wiki KB Mining Loop Plan

updated_at:: 2026-05-24T06:18:00+08:00
main_language:: zh-CN
active_topic:: llm_wiki
status:: controller_executor_boundary_hardened

## 目标

本 loop 的第一批交付物不是单张卡片，而是：

1. 一套可反复迭代的 LLM Wiki KB mining skills。
2. 一个完整的 LLM Wiki v1 知识库。

“完整 v1”不是声称 topic 已无未知，而是指每个核心 coverage area 至少有 adopted node、所有 adopted node 都有完整 version bundle、所有关键 claim 都能追溯到本地 raw source / manifest / prior KB node，且剩余缺口被写成 frontier、retrieval request 或 blocker。

## Loop Owner

loop_owner:: main_controller_worker_executed

Codex main agent 是 controller / decision-maker，不是 concrete artifact executor。Main 负责：

- 创建、审查和派发 task packet。
- 阅读 worker/sub-agent 的 summary、status、gate report、delivery note 和 failure note。
- 决定 phase transition、adoption / repair / retrieval / defer / stop。
- 更新 control state、action queue、standing status 和 process intervention 记录。

Worker/sub-agent 或独立 worker mode 是 executor。以下具体执行必须由 worker 根据 task packet 完成：`source_mining`、`frontier_update`、`node_planning`、`generation`、`audit`、`view_build`、`skill_eval`。

Main 不得亲自写 source mining observations、frontier delta、planner packet、card/provenance/change、audit report、view artifacts 或 skill eval artifact。若 main 直接写入任何 concrete artifact，只能作为 controller drift sample 保留，并必须触发 skill/process intervention。

## 启动前必须调用的 skills

已调用的外层 skills：

- `agent-loop-runner`：用于把任务设计成可恢复的 filesystem-backed loop。
- `skill-creator`：用于初始化 repo-local skills。

启动自治 loop 前，必须按计划调用 repo-local skills：

0. `llmwiki-loop-orchestration`
   - 检查阶段迁移、artifact checklist、frontier gate、generation entry gate 和 `LOOP_DONE` / `LOOP_BLOCKED` 条件。
1. `llmwiki-source-mining`
   - 产出 `source_scope.md`、`source_mining.md`、`candidate_frontier_delta.yaml`、`evidence_gaps.md`、`retrieval_requests.md`。
2. `llmwiki-frontier-management`
   - 合并 delta 到 `.llmwiki/control/knowledge_frontier.yaml`，给候选设置状态。
3. `llmwiki-node-planning`
   - 只从 frontier 中选择一个 `ready_to_build` 候选，写 `evidence_scope.yaml` 和 `next_task_packet.md`。
4. `llmwiki-card-generation`、`llmwiki-citation-formatting`、`llmwiki-provenance-generation`、`llmwiki-change-generation`、`llmwiki-node-metadata`
   - 生成一个 version bundle。
5. `llmwiki-citation-audit`、`llmwiki-adoption-audit`
   - 决定 repair / retrieval / adopt / defer。
6. `llmwiki-view-building`
   - 只渲染 adopted versions。
7. `llmwiki-impact-analysis`
   - 仅在 major change 时运行。
8. `llmwiki-skill-evolution`
   - 每轮记录 skill failure，并在满足 patch rule 时更新 skill。

## 初始自治状态机

```text
pre_loop_planning
-> source_mining
-> frontier_update
-> node_planning
-> generation_entry_gate
-> version_bundle_generation
-> citation_and_adoption_audit
-> view_building
-> skill_evaluation
-> next_decision
```

动态 retrieval 可以中断 `source_mining` 或 `version_bundle_generation`，但 retrieval 结果必须先保存到 `data/raw/` 并进入 manifest，再回到 source mining。

## 第一轮候选

Turing planner run 已确认 `origin_and_canon` 证据最强，但这不是跳过 mining 的许可。第一轮自治 loop 应先使用 `llmwiki-source-mining` 处理以下 source batch：

- `karpathy-gist-llm-wiki`
- `karpathy-x-launch-post`
- `hacker-news-original-thread`

第一轮 expected frontier update：

- `llm_wiki_origin_and_canon` 从 `needs_more_mining` 进入 `ready_to_build`，前提是 mining artifacts 写完且 citation feasibility 通过。

## Generation Entry Gate

在任何 `card.md` 写入前，必须先写 `.llmwiki/runs/<run_id>/generation_entry_gate.md`，并且 gate result 必须是 `pass`。

Gate 需要证明：

- `next_task_packet.md` 指向 `knowledge_frontier.yaml` 中已存在的 candidate。
- candidate status 是 `ready_to_build`。
- candidate 的 source lineage 和 evidence state 可追溯。
- packet 引用了让 candidate ready 的 source mining run。
- allowed inputs、forbidden inputs、version target 和 output paths 都明确。

缺任一项时不得启动 generation skills。

## V1 KB Coverage 目标

v1 KB 至少覆盖：

- 起源与 canonical sources。
- Working definition。
- 三层架构：raw sources / wiki artifacts / schema-instructions。
- ingest / compile / query / lint / update 工作流。
- 与 RAG、PKM、knowledge graph、agent memory、documentation systems 的比较。
- implementation ecosystem。
- evaluation evidence 与 empirical limits。
- risks / governance / provenance。
- scale boundaries 与 enterprise applicability。

每个 coverage area 可由多个小 node 累积完成；不要为了“完整”写过宽 hub node。

## 自治边界

Main 可以自治执行 controller 工作：

- 读取 control summaries、worker status、delivery、gate、failure 和 bounded summary artifacts。
- 创建或审查 worker task packet。
- 更新 `.llmwiki/control/` 中的 state、queue、standing status、summary 和 gate policy。
- 决定是否采用 worker 输出、要求 repair、派发下一 worker、记录 blocker 或结束 loop。

Worker/sub-agent 可以在 task packet 约束内执行：

- 读取本地 `data/`、`data/manifests/` 和 reports。
- 写 `.llmwiki/runs/<run_id>/` concrete artifacts。
- 执行 source mining、frontier merge proposal、node planning、candidate bundle generation、audit、view build 和 skill eval。
- 有限普通网络尝试后的失败记录与延期。

Controller/executor hard boundary:

- Main agent 不得直接写 `source_scope.md`、`source_mining.md`、`candidate_frontier_delta.yaml`、`evidence_gaps.md`、`retrieval_requests.md`、`frontier_trace.md`、`planner_report.md`、`evidence_scope.yaml`、`next_task_packet.md`、`node.yaml`、`card.md`、`provenance.md`、`change.md`、`citation_audit.md`、`audit_report.md`、view/generated artifacts 或 run-local `skill_eval.md`，除非该文件明确是 controller drift note / intervention note。
- Main 可以写 run-level `controller_drift_note.md`、`loop_status.md`、`loop_delivery.md` 来标记流程错误和下一步控制决策。
- 任何 main-authored concrete artifact 都不得直接进入 adoption；必须由 worker 复核、重跑或明确采纳，并留下 executor attribution。

必须停止或记录 blocker：

- 需要破坏性 git 操作。
- 想绕过公司网络限制。
- 没有本地 evidence 却要 adopted claim。
- 要把 protocol/control layer 当作 object-level topic content。
- 要改变 node schema 或 validator contract 且会破坏已存档 demo。

## Stop / Continue Logic

继续 loop，直到：

- v1 coverage checklist 全部有 adopted support，或
- 剩余项全部被明确 retrieval blocker 阻塞，且 blocker 已写入 retrieval queue / gap report。

不要因为轮数达到某个数字而停止。每轮只选择一个 highest-value next action。

## Current Controller Drift Sample

`run_20260524_061000_source_mining_origin_canon` 的 source mining artifacts 是 main agent 直接写入的 concrete artifacts，因此标记为 controller drift sample。不要删除这些 artifacts；后续只能把它们当作 drift sample 和 worker repair/review input。下一步不是继续由 main merge frontier 或写 KB content，而是由 main 创建或派发 worker task packet，要求 worker 复核 / 重跑该 source-mining batch 并产出可归属的 executor delivery。
