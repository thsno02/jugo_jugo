# sub-agent 生命周期核心审计

`status`: `AUDIT_DONE`
`audit_result`: `concern`

## 审计结论

当前系统已经从“sub-agent 无边界泛滥”演进到“有任务包、有隔离、有交付检查”的状态，但还没有完成生命周期管理闭环。最大缺口不是 prompt，而是运行时账本：系统能证明某个 worker 写了 `LOOP_DONE`，却不能稳定证明 GUI thread 已关闭、是否仍 active、是否被复用、是否还应该显示在当前 subagents 列表中。

主控验收补充：当前工具层存在 `close_agent`，可以关闭已知 agent id；因此问题不是绝对没有关闭动作，而是关闭动作没有被统一落盘，也不能直接验证 GUI 面板最终状态。

## 证据

1. 父会话中解析到 69 条 sub-agent notification，说明旧 loop 大量依赖一次性 worker。
2. `legacy/audits/context_isolation_audit_20260524/context_isolation_audit.md` 记录旧 loop 存在主控直接执行、审计者越权写入和任务包依赖聊天上下文的问题。
3. `legacy/audits/focus_drift_audit_20260524/root_cause_analysis.md` 记录旧 loop 的生产对象是 `node`，不是 atomic fact card，导致执行者在错误目标上稳定执行。
4. `llm_wiki/loop/SUBAGENT_LIFECYCLE.md` 已规定 `source_mining_worker`、`card_drafting_worker`、`card_audit_worker`、`card_adoption_worker` 和 `independent_evaluator` 都是阅后即焚。
5. `llm_wiki/loop/CONTEXT_ISOLATION.md` 规定执行者默认不 fork 父聊天上下文，只接收 `base_worker`、role prompt 和当前 `task.md`。
6. `llm_wiki/loop/reports/loop_report.md` 记录新版 source mining、drafting revision、card audit 都使用 `fork_context: false`，并声明完成后关闭。
7. 新 main loop session 中 main-agent 多次显式说“先关闭 worker，再验收”，这是良好行为。
8. 环境上下文仍显示历史 subagents `019e56da` 和 `Volta`，说明 `LOOP_DONE` 或 main-agent 声明关闭未必等同于 GUI active 清理。
9. Zeno push worker 在三批 push 后继续处理 Batch 4-7，说明原本短任务在用户连续追加下变成事实上的 resident git worker。
10. Zeno 多次被并行 active loop 新写入拖住，说明 git worker 与生产 loop 没有写入窗口协调。

## 假设

### H1：sub-agent 泛滥来自“保持 main clean”的过度应用。

验证：成立。用户明确要求 main-agent 保持决策者身份，不做具体活；main-agent 为避免上下文污染，把 planning、mining、frontier、generation、audit、adoption、skill eval、sync 等都拆给 sub-agent。旧 loop 中这保护了 main context，但没有配套生命周期账本，因此数量迅速增长。

### H2：旧 loop 泛滥也来自生产对象过大。

验证：成立。旧系统以 `node` / topic coverage 为对象，一个 node 需要多个阶段，所以每个 candidate 都触发一串 worker。若对象改成“一个 atomic fact candidate -> one card”，链路仍需要 worker，但每轮更小，且不应再附带 frontier/topic/coverage 的额外 worker。

### H3：GUI active 风险来自缺少 close ledger，而不是 worker 没有完成任务。

验证：基本成立。大量通知都显示 `LOOP_DONE`，但环境仍可见历史 agent。磁盘上没有统一 `subagent_lifecycle_log.jsonl` 记录 `closed_at`、`close_method`、`gui_state_checked`。因此完成和关闭被混在一起。

### H4：Zeno push 卡住是 worker 能力问题。

验证：不成立。Zeno 的行为反而很稳：白名单外路径出现时停止，不 force push，不 stage 未授权文件。真正问题是 push worker 与仍在写文件的生产 loop 同时运行，导致白名单不断变化。

### H5：fork context 对审计绝对有益。

验证：部分成立。当前审计确实受益于 fork context，能看到用户真实意图和父聊天中的反复纠偏。但 fork context 也会带来叙事偏差，所以必须用 session metadata 和磁盘产物验证；本审计已把不可验证的 GUI 状态标为 `unknown`。

## 为什么出现 sub-agent 泛滥

### 1. 旧 loop 把每个小阶段都人格化

旧 loop 的控制面把任务拆成许多“角色”：source mining、frontier update、node planning、generation、audit、adoption、skill eval、status sync。拆分本身不是错，但其中很多步骤是机械状态变更或脚本校验，不需要一个完整 sub-agent。

### 2. 缺少“不要开 sub-agent”的规则

早期规则强调“main-agent 不要亲自执行”，但没有同等强度地规定：

- 机械任务先脚本化。
- 无独立判断价值的任务不创建 worker。
- 只有能写清 allowed inputs / writes / success criteria 的任务才创建 worker。
- 完成后必须有关闭记录。

结果是，只要 main-agent 想保持干净，就倾向于再开一个 worker。

### 3. 没有生命周期账本

已有 `loop_status.md` 和 `loop_delivery.md`，但它们记录的是任务状态，不是 agent 生命周期。缺少：

```text
agent_id
nickname
role
spawn_reason
lifecycle_type
parent_thread_id
task_path
started_at
done_at
closed_at
close_method
gui_state_checked
reuse_allowed
```

没有这个账本，人类只能在 GUI 里看到一堆 active agent，却不知道哪些完成、哪些应关闭、哪些可复用。

### 4. 任务包替代不了运行时调度器

`render_dispatch.py` 能把 prompt 和 task 渲染成 dispatch payload，但实际 spawn、wait、close、registry update 仍靠 main-agent 临场操作。也就是说，prompt 被稳定化了，生命周期没有被工具化。

## 哪些 sub-agent 必要

必要的判断标准是：它是否提供了 main-agent 不应拥有的隔离、独立判断或完整上下文。

- `source_mining_worker`：必要。它读来源并写事实候选，main-agent 不应亲自做。
- `card_drafting_worker`：必要。它写卡和 provenance，main-agent 不应亲自写。
- `card_audit_worker` / `independent_evaluator`：必要。它们提供独立判断。
- `user-insights` sidecar：必要。它处理会话记忆和人类偏好，不是 KB 事实来源。
- `sub-agent lifecycle auditor`：必要。它需要 fork context 和磁盘证据调查机制问题。
- `git push worker`：在用户明确要求且有严格白名单时可以必要，但应该串行于生产 loop。

## 哪些 sub-agent 不必要或可避免

- 纯 `json.tool`、`validate_scope.py`、`inspect_delivery.py` 检查：脚本足够。
- 纯链接修正、report link 更新、状态字段移动：main-agent 控制面可做，除非有失败证据需要独立审计。
- 每个节点后的常规 skill/process eval：如果只是套模板确认，可以改成批量反思或脚本化 check。
- adoption metadata 和 generated refresh：若是确定性操作，应优先工具化；只有采纳决策需要独立审计。

## 生命周期管理失败点

### `LOOP_DONE` 被误当成 close

`LOOP_DONE` 是任务完成 marker，不是 UI close marker。主控 agent 说“已关闭”也需要落盘证据，否则下一位 agent 和人类无法判断 GUI 里哪个 active 可以清理。

### alive worker 没有显式声明

Zeno 原本是三批 push worker，但后来继续接 Batch 4-7。它的行为合理，却没有从 `disposable` 转成 `short_lived_git_worker` 的决策记录。

### 并行写入没有冻结窗口

push worker 需要稳定工作区。新 main loop 同时继续产出 iteration 文件，导致 Zeno 反复停止。这里应由 main-agent 先暂停生产或声明 push window，而不是让 push worker被动追逐变化。

### fork context 的使用没有分级

大多数生产 worker 应 `fork_context: false`。当前生命周期审计需要 fork context，但应同时要求“先证据、后假设、再验证”，避免复制父聊天偏见。

## main-agent 做得好的地方

- 在新版 source mining / drafting / audit 中坚持 `fork_context: false`。
- 发现 `loop_delivery.md` marker 缺口后，没有手工补 worker 文件，而是修稳定 prompt 并重跑。
- 多次明确关闭 worker 后再验收。
- Zeno push worker 对白名单外变化采取停止策略，避免把活跃 loop 的新产物混进 commit。
- 当前控制面把 hub、cluster、topic coverage 明确列为非目标，减少旧 drift 复发。

## main-agent 被拖住或卡住的地方

- 旧 loop 中主控曾亲自写 source mining artifact，被记录为 controller drift。
- 旧 loop 任务包把控制器叙事写给 worker，导致隔离形式存在但判断不独立。
- Zeno push 期间，生产 loop 继续写文件，push worker 多次被新增产物卡住。
- main-agent 缺少统一 lifecycle registry，只能靠聊天里“我已关闭”维持状态。
- 一些子任务太小也开 sub-agent，使 GUI 噪声大于隔离收益。

## 反直觉发现

1. 开 sub-agent 不自动带来上下文隔离；如果任务包带着父叙事，隔离只是形式。
2. 过度保护 main-agent 上下文，会把复杂度转移给生命周期管理。
3. `fork_context: false` 适合生产 worker，但不适合生命周期审计和 user-insights 这类需要会话语义的任务。
4. push worker 越守规则，越容易在活跃 loop 中停住；这是正确行为暴露出的 orchestration 问题。
5. GUI active 问题不是文档问题，而是运行时状态缺口：文件里 `LOOP_DONE` 不等于 UI 线程关闭。
6. 一个“失败的” drafting iteration 很有价值：它让 base prompt 的 marker 契约缺口暴露出来，避免 main-agent 悄悄修补。

## 总体判断

当前新版 loop 可以继续生产 atomic cards，但必须补上 sub-agent lifecycle registry。否则后续随着 cards 增长，worker 数量仍会再次变成人类不可审计的 GUI active 堆积。
