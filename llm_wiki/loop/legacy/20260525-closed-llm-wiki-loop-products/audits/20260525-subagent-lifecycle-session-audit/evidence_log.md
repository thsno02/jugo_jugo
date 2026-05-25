# 证据时间线

`status`: `AUDIT_DONE`

## 证据来源

- 父会话 session: `/Users/lw/.codex/sessions/2026/05/24/rollout-2026-05-24T04-50-07-019e569a-36b9-7c22-9567-869dcbdbf87c.jsonl`
- 当前审计 session: `/Users/lw/.codex/sessions/2026/05/25/rollout-2026-05-25T03-04-22-019e5b5f-befe-78e0-aa64-e388f5bcbba9.jsonl`
- 新 main loop session: `/Users/lw/.codex/sessions/2026/05/25/rollout-2026-05-25T02-33-10-019e5b43-2e1d-7970-9247-a824c63e95fc.jsonl`
- Zeno push session: `/Users/lw/.codex/sessions/2026/05/25/rollout-2026-05-25T02-37-47-019e5b47-6821-7341-bdd1-ebc53f7e0609.jsonl`
- 既有审计与控制面：`legacy/audits/*`、`llm_wiki/loop/*`、`user-insights/*`

## 2026-05-24 早期：从 demo 到 planner sub-agent

- 用户最初要求全量阅读 `loop_plan_init_kb.md` 并准备 goal mode。
- main-agent 先完成 demo，并生成了旧 `.llmwiki` / `kb` / `nodes` / `generated` 结构。
- 用户指出：核心目的不是生产“KB 设计 topic”，而是从 `data/` 里的来源挖知识。
- main-agent 启动 planner sub-agent `019e56c4-a5a6-7d41-8b1e-765c521dcde6`，让它从 `data/` 产出 planner 输出。

审计观察：这是第一处“用 sub-agent 保持 main clean”的合理尝试，但 planner 输出仍然把候选压成 node/topic 方向，为后续 drift 留下结构性风险。

## 2026-05-24 06:00-14:20：旧 v1 loop 的 sub-agent 链式增长

可见通知显示旧 loop 持续创建大量 worker：

- `019e56da`：pre-loop skill coverage 审计，结论 `needs_work`。
- `019e56e6`：修复角色边界，把主控写 source mining artifact 标为 `controller_drift_sample`。
- `019e56ea`：source mining worker。
- `019e56ee`：frontier update worker。
- `019e56f0` / `019e56f3`：node planning 与 repair。
- `019e56f6`：generation worker。
- `019e56f9` / `019e5701`：audit / re-audit。
- `019e5704`：adoption worker。
- 后续多个 candidate 继续重复 source mining、planning、generation、audit、adoption、skill eval、status sync。

父会话中共解析到 69 条 sub-agent notification。旧 loop 最终做到了大量产物和状态推进，但代价是 GUI 和生命周期管理难以被人类审计。

## 2026-05-24 15:27-15:34：旧问题被独立审计确认

`legacy/audits/context_isolation_audit_20260524/context_isolation_audit.md` 记录：

- 主控 agent 曾直接执行具体来源挖掘。
- 审计执行者曾运行会写入 `generated/` 的脚本，越过只读边界。
- 一些任务包依赖当前线程指令，无法完全从磁盘复现。
- 任务包有时预先写入控制器叙事，削弱 sub-agent 独立判断。

`legacy/audits/focus_drift_audit_20260524/root_cause_analysis.md` 记录：

- 旧系统把 `node` 设成生产对象，把主题覆盖设成规划框架。
- 执行者在错误对象层级内正常执行，导致“错误目标被完整执行”。

审计观察：旧 sub-agent 泛滥与 focus drift 是同源问题。对象层级错了，越拆 worker，越稳定地生产错误层级的产物。

## 2026-05-25 01:11-02:06：新版 loop 前置控制面

- `019e5af8` / Boole：独立 scope 审计，指出流程规则基本可用但非程序级强制。
- `019e5b0d` / Volta：调查 hooks 与 sub-agent 可行性。结论：hooks 可做 guardrail/context/stop，不适合直接当 sub-agent dispatcher。
- `019e5b22` / Hubble：`user-insights` sidecar 写入顶层 `user-insights/`，coverage 标记 `partial`。
- `019e5b26` / Plato：前置门禁审计，结论 `concern`，要求处理 canonical 链接和 partial coverage 决策。

相关新版控制面文件：

- `llm_wiki/loop/CONTEXT_ISOLATION.md`
- `llm_wiki/loop/SUBAGENT_EVOLUTION.md`
- `llm_wiki/loop/SUBAGENT_LIFECYCLE.md`
- `llm_wiki/loop/plans/main_agent_long_horizon_execution_plan.md`

审计观察：新版设计已吸收旧教训，写出了“阅后即焚”和 `fork_context: false`；但仍缺少实际的 lifecycle ledger 和 GUI close 证据。

## 2026-05-25 02:33-03:08：新 main loop 的 worker 链

新 main session `019e5b43-2e1d-7970-9247-a824c63e95fc` 按 next goal prompt 执行：

- `019e5b46` / Schrodinger：source mining worker，写 12 个事实候选。
- main-agent 明确说“关闭刚完成的 source_mining_worker”，再验收。
- `019e5b4d` / Mendel：第一次 card drafting worker，产出草稿卡和 provenance。
- main-agent 关闭 Mendel 后发现 `inspect_delivery.py` 失败，因为 `loop_delivery.md` 缺少 `LOOP_DONE` / `LOOP_BLOCKED`。
- main-agent 没有手工补产物，而是创建 prompt repair 任务。
- `019e5b53` / Meitner：prompt repair 独立审计，结论 pass。
- `019e5b59` / Turing：drafting revision worker，产物通过交付检查。
- `019e5b61` / Laplace：card audit worker，`audit_result: pass`。

审计观察：这是做得好的部分。main-agent 多次声明先关闭 worker 再验收；遇到失败没有亲自修 worker 文件，而是修稳定 prompt 并重跑。

## 2026-05-25 02:37-03:01：Zeno push worker 与活跃 loop 写入冲突

用户要求开 sub-agent 分批 push 当前未提交内容。Zeno `019e5b47` 接收明确边界：

- 只做 git inspect / validate / stage / commit / push。
- 不编辑文件。
- 不用 `git add .`。
- 不 force push。
- 分三批 push。

Zeno 先成功完成 Batch 1-3：

- `cdd1476`：user insights。
- `a47a6cd`：long horizon plans。
- `32995e7`：loop control plane。

随后，工作区被新 main loop 持续写入，Zeno 多次遇到白名单外变化并停止：

- Batch 4 第一次：目标文件外出现新的 `iteration_0003` 目录。
- Batch 4 第二次：出现 `loop_state.json`、`queues/task_queue.md`、`reports/loop_report.md` 等控制面变化。
- Batch 4 第三次：出现 `loop_status.md`、`read_log.md` 等完整交付文件。
- Batch 5：stage 后又出现新的 prompt repair audit 状态文件。
- Batch 6：commit 后用户追加“当前有 loop 在跑，不要 push”，Zeno停止 push；后续用户又要求只 push 已存在 commit。
- Batch 7：第一次因新 r1 drafting 状态文件停止；第二次在完整交付后通过并 push。

审计观察：Zeno 本身执行边界很稳，但它被放在一个持续写入的工作区里做 git 收口，因此不断被新产物拖住。这里的问题不是 git worker 不守规则，而是 main-agent 没有先冻结写入窗口或把 push worker 设为和生产 loop 串行。

## 2026-05-25 03:04 之后：当前生命周期审计

当前审计线程 `019e5b5f-befe-78e0-aa64-e388f5bcbba9` 的 metadata 显示：

- `thread_source`: `subagent`
- nickname: `Heisenberg`
- parent: `019e569a-36b9-7c22-9567-869dcbdbf87c`

用户要求本审计创建 `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/`，并只写该 folder。审计者已遵守该写入边界；开始写入前，`git status` 显示已有新 main loop 的未提交变化，本审计没有修改这些生产文件。
