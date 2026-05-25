# status

`AUDIT_DONE`

# audit_result

`concern`

本次审计结论：旧 LLM Wiki loop 的 sub-agent 数量确实过多；根因不是单个 worker 失控，而是把“main-agent 保持干净”过度实现成“每个细小动作都开一个 sub-agent”，且没有同步建立可审计的 `spawned -> completed -> closed` 生命周期账本。

当前新版控制面方向明显更好：`fork_context: false`、任务包隔离、`read_log.md`、`loop_delivery.md`、one-shot worker 和完成后关闭的规则已经写入控制面，并在 `loop_report.md` 中反复执行。但这些仍主要是文档和主控叙事证据，尚未形成运行时 registry；因此 `LOOP_DONE` 仍不能等同于 GUI thread 已关闭，`close_agent` 调用也不能等同于已可从文件系统恢复最终 GUI active 状态。

必须区分两层证据：

- 已提交历史：当前 `HEAD` 是 `d8ab36c Start control-plane audit run`；允许读取的核心控制面文件中，`loop_state.json`、`loop_manifest.json`、`task_queue.md`、`loop_report.md`、`CONTEXT_ISOLATION.md`、`SUBAGENT_LIFECYCLE.md`、`render_dispatch.py` 在本次 path-scoped status 中未显示修改，可以作为当前已提交/工作树一致证据读取。
- 当前未提交控制面草稿：`SUBAGENT_SCOPE.md` 是已跟踪但未提交修改；`llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/` 整个旧审计 folder 是未跟踪内容。完整 `git status --short` 还显示其它控制面 draft 文件有改动或未跟踪，但本 worker未读取这些文件内容，只把 status path list 作为“当前工作树仍在变动”的证据。

# evidence_read

允许范围内读取：

- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/README.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/evidence_log.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/subagent_inventory.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/lifecycle_audit.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/recommendations.md`
- `llm_wiki/loop/audits/20260525-subagent-lifecycle-session-audit/main_agent_acceptance.md`
- `llm_wiki/loop/SUBAGENT_LIFECYCLE.md`
- `llm_wiki/loop/CONTEXT_ISOLATION.md`
- `llm_wiki/loop/SUBAGENT_SCOPE.md`
- `llm_wiki/loop/loop_manifest.json`
- `llm_wiki/loop/loop_state.json`
- `llm_wiki/loop/queues/task_queue.md`
- `llm_wiki/loop/reports/loop_report.md`
- `llm_wiki/loop/tools/render_dispatch.py`
- `git status --short` / path-scoped `git status --short`
- `git log --oneline --decorate` / path-scoped `git log`

必要的额外读取及 reason：

- `/Users/lw/.codex/skills/agent-loop-runner/SKILL.md`：系统技能指令要求在 loop / audit / worker 生命周期任务中使用该 skill，用于确认 worker isolation、orchestration、registry、report 和 decision 的通用审计标准。
- `/Users/lw/.codex/skills/agent-loop-runner/references/loop-lessons.md`：同一 skill 明确要求审计既有 loop 时读取，用于复核 report loop / prompt loop 中 worker 隔离、handoff 和 monitor 的可迁移经验。
- `/Users/lw/.codex/skills/agent-loop-runner/references/long-horizon-loop-patterns.md`：同一 skill 明确要求长程 loop 控制面设计读取，用于复核 resident / short-lived / disposable worker 分层、main-agent elasticity 和 filesystem control plane。

未读取内容但通过 `git status --short` 看到的其它未提交控制面路径：`DRAFT_FIRST_PIPELINE.md`、`README.md`、`RUNBOOK.md`、`draft_backlog.md`、部分 similarity/fusion prompts/templates，以及同级 `task_flow_audit.md`。这些仅作为工作树未冻结证据，不作为内容结论依据。

# findings

## P0

无 P0。没有看到当前证据表明 sub-agent 已经越权写入本审计允许路径之外，也没有看到需要立即停止当前生产 loop 的生命周期灾难。

## P1

### P1.1 生命周期 registry 仍是最大缺口

`SUBAGENT_LIFECYCLE.md` 已要求 dispatch 记录包含 `agent_id`、`role`、`lifecycle`、`fork_context`、`task_path`、`allowed_inputs`、`allowed_writes`、`started_at`、`closed_at`，但当前读取范围内没有可执行的 `subagent_lifecycle.jsonl` 或等价 registry。旧 audit 的修正结论仍成立：当前工具层存在 `close_agent`，问题不是完全不能 close，而是 close/completed/gui_state 没有统一落盘。

影响：未来 agent 只能从聊天叙事、GUI 感觉和 `LOOP_DONE` 推断状态，无法可靠回答“哪些 sub-agent 还活着、哪些已完成但 GUI 未清理、哪些允许复用”。

### P1.2 旧 loop 的 sub-agent 过多结论仍成立，但它是未提交审计草稿

旧 audit folder 记录父会话解析到 69 条 sub-agent notification，并指出旧链路把 source mining、frontier update、node planning、generation、audit、adoption、skill/process eval、status/frontier sync 都人格化。这个分析与当前控制面文档一致，结论仍成立。

但该 audit folder 当前是 `??` 未跟踪文件，不能被当作已提交历史。它是当前未提交控制面审计草稿，应由 main-agent 后续决定是否采纳、归档或转写成正式 decision。

### P1.3 当前新版仍有“one-shot 数量膨胀”的结构性风险

`loop_report.md` 显示新版 loop 大量使用 one-shot `source_mining_worker`、`card_drafting_worker`、`card_audit_worker`、`card_adoption_worker`，并且多数用 `fork_context:false`、`inspect_delivery.py` 和关闭叙事收口。这比旧 loop 好，但如果继续按“每张卡 drafting -> audit -> adoption”逐步派发，GUI thread 数量仍会随卡数量线性增长。

当前切换到 Atomic Draft First / batch drafting 是对吞吐和 thread 数量的合理修正；但 batch worker 也扩大单次写入面，必须维持小批量、单一 role、disjoint write set 和后置 audit/publication gate。

### P1.4 git/push worker 必须与生产 loop 串行，不能和 active writer 并行

旧 audit 关于 Zeno 的结论仍成立：Zeno 的白名单、禁止 `git add .`、不 force push、遇到白名单外变化停止，都是正确行为。卡住的根因是 push worker 与仍在写文件的生产 loop 并行，工作树持续出现新变化。

规则层面应把 git worker 定义为 `short_lived`，且只有在生产 loop 暂停、当前 worker 完成或写入窗口冻结后创建。否则越守规则的 git worker 越会被正确地卡住。

### P1.5 `fork_context` 规则方向正确，但例外需要登记

当前控制面默认不 fork 父聊天上下文：`CONTEXT_ISOLATION.md` 规定执行者默认不 fork，`render_dispatch.py` payload 固定 `"fork_context": False`，`SUBAGENT_SCOPE.md` 规定 worker 只把当前 `task.md` 当作任务来源。这是生产 worker 的正确默认。

例外也成立：lifecycle / context isolation / focus drift 审计、user-insights sidecar 可能需要完整会话语义。但例外必须写入 task packet 或 registry：为什么需要 fork、如何控制叙事污染、哪些结论必须回到磁盘证据验证。旧 audit 使用 fork context 是合理的，但其结论必须标记为未提交草稿。

## P2

### P2.1 `SUBAGENT_SCOPE.md` 当前是未提交修改，规则还不能当作稳定基线

`SUBAGENT_SCOPE.md` 内容很好，尤其是“不创建新的 sub-agent”“不运行 git 操作，除非任务包明确要求”“结束前必须写三件套”。但它当前在 git status 中是 `M`，说明这些规则可能仍是控制面草稿。后续主控应明确这是采纳中草稿还是待审草稿。

### P2.2 monitor 的写入边界偏宽

`loop_manifest.json` 中 monitor 的 default write includes 当前 iteration 目录和 artifacts。按生命周期原则，resident/monitor 应低噪声只读，最多写自己的低噪声 status/heartbeat。当前配置没有直接造成失败，但会给 resident monitor 留出不必要写入面。

### P2.3 `render_dispatch.py` 稳定了 payload，但没有负责登记生命周期

`render_dispatch.py` 已能把 base prompt、role prompt、task packet 合成 dispatch payload，并固定 `fork_context:false`。但它只输出 `dispatch_request.json`，没有生成或更新 lifecycle registry。也就是说 dispatch 被工具化了，spawn/wait/complete/close 仍靠 main-agent 临场纪律。

### P2.4 close 条件没有包含 GUI 状态验证降级

`SUBAGENT_LIFECYCLE.md` 的关闭条件覆盖 `loop_status.md`、`loop_delivery.md`、`read_log.md` 和 artifact existence，但缺少 `completed`、`closed`、`close_unverified` 的状态分离。旧 audit 已修正“close API 不存在”的说法；下一步应该落地“close 可调用但 GUI final state 可能 unknown”的降级记录。

# what_is_working

- 新版 loop 的方向正确：main-agent 保持决策者身份，生产 worker 执行有界任务。
- `fork_context:false` 已成为生产 worker 默认，并由 `render_dispatch.py` 固化。
- `CONTEXT_ISOLATION.md` 和 `SUBAGENT_SCOPE.md` 把 allowed inputs、allowed writes、`read_log.md`、父聊天隔离、旧审计隔离写得清楚。
- `loop_report.md` 中多次记录 worker 完成后关闭、`inspect_delivery.py` pass、失败后走 prompt/template repair，而不是由 main-agent 偷偷补 worker 产物。
- `loop_state.json` 当前没有 blockers，状态清楚指向 batch drafting dispatch ready。
- 旧 audit 对 close API 的事实修正很重要：不是“没有 close”，而是“没有 registry 和 GUI final-state audit”。
- Zeno push worker 的停止策略是正确守边界的例子，暴露的是 orchestration 写入窗口问题。

# recommended_rules

1. 默认不创建 sub-agent，除非任务满足至少一个条件：需要独立事实生产、需要独立判断、需要上下文隔离、需要完整 fork context 审计，或用户明确要求 sidecar/git worker。

2. 明确不要开 sub-agent 的情况：纯脚本校验、JSON 检查、状态字段同步、补链接、机械 report 更新、任务包尚不能列清 allowed inputs/writes、当前已有 worker 正在写同一目录。

3. lifecycle 类型固定为三类：

- `resident`：只允许 `main_agent` 和只读/低噪声 `monitor`。resident 不写生产 KB，不做事实判断，不隐式接生产任务。
- `short_lived`：git worker、skill evolution、同一失败簇 repair worker、一次 user-insights record 周期。必须有结束条件；连续接新任务前必须写 lifecycle decision。
- `disposable`：source mining、card drafting、card audit、card adoption、independent evaluator。一次只处理一个 task packet，完成后关闭，不复用上下文。

4. `fork_context` 默认 `false`。允许 `true` 的例外必须在 task packet 或 registry 写明：`fork_reason`、`bias_control`、`disk_evidence_required`、`session_context_not_fact_source`。

5. 新增 `llm_wiki/loop/logs/subagent_lifecycle.jsonl` 或等价 registry。最小事件：

```json
{"event":"spawned","agent_id":"...","role":"card_drafting_worker","lifecycle_type":"disposable","fork_context":false,"task_path":"...","allowed_write_root":"...","started_at":"..."}
{"event":"completed","agent_id":"...","result":"LOOP_DONE","delivery_path":"...","done_at":"..."}
{"event":"closed","agent_id":"...","close_method":"close_agent","closed_at":"...","gui_state_checked":"unknown","reuse_allowed":false}
```

6. `LOOP_DONE` 只表示任务完成，不表示 close。`close_agent` 只表示发起关闭，不表示 GUI final state 已验证。registry 必须允许 `close_unverified`。

7. git worker 必须串行于生产写入：先写 `push_window` decision，等待 active production worker 完成或暂停，再按白名单 stage/commit/push。出现新未授权变化时停止，而不是扩大范围。

8. batch worker 可以减少 sub-agent 数量，但必须满足：单一 role、小批量、同一 iteration 写入、批内每张卡独立 manifest、后置 similarity/audit/publication gate。

9. main-agent 可以做控制面最小修复，但不能补写 worker 事实产物。若 worker 产物不合格，创建 repair/evolution/audit 任务并记录失败证据。

# open_questions

- 当前运行时是否能提供“读取 GUI active subagents 面板”的 API？如果不能，registry 中 `gui_state_checked: unknown` 应是默认降级。
- 旧未跟踪 lifecycle audit folder 是否应被正式采纳、迁移为 decision，还是仅作为草稿证据保留？
- `SUBAGENT_SCOPE.md` 当前未提交修改是否已经被 main-agent 接受为新规则，还是仍需独立审计后才能作为稳定基线？
- monitor 是否应该从 `loop_manifest.json` 的 writable role 改成只读 role，只写独立 heartbeat/status？
- batch drafting 的最大批量应固定为 6，还是按来源大小和候选清晰度动态调整？

# next_actions

1. 先不要继续增加新的 lifecycle 文档；优先落地 lifecycle registry，让每次 dispatch/completed/close 都有一行可恢复记录。

2. 在 `render_dispatch.py` 或 main-agent runbook 增加 registry 写入步骤：render dispatch 后登记 `spawned`，收到 delivery 后登记 `completed`，调用 close 后登记 `closed` 或 `close_unverified`。

3. 在下一次 git worker 之前写 `push_window` decision，并确认当前生产 worker 没有继续写入同一工作树。

4. 把旧未跟踪 audit folder 的结论拆成两类：已被主控接受的规则进入正式 decision；仅依赖 fork context 或 GUI 推断的内容保留为草稿证据。

5. 审查 monitor role 的 allowed writes，把 resident/monitor 限制为只读低噪声状态面，必要时只写自己的 heartbeat。

6. 当前 batch drafting 可以继续，但完成后必须走 similarity gate 和 batch audit，不要把 batch draft 直接当 accepted card。
