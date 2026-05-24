# LLM Wiki 循环报告

## 为什么存在（why_this_loop）

这个循环存在的原因是：LLM Wiki 的知识库不能从主题骨架或枢纽页开始，而要从可以被来源支撑的原子事实知识卡开始。

当前不追求覆盖率，也不追求结构完整。当前要降低的不确定性是：能否稳定地从本地来源中抽出事实候选，并经过出处论证和审计，沉淀为可读的 zet 风格知识卡。

## 当前决策（current_decision）

当前状态：第一轮 `source_mining_worker` 已派发，正在从一个已获取本地来源中挖掘事实候选。

当前决策：接受 `user-insights` 的 `coverage: partial` 作为非阻塞残余风险，因为它不是知识卡事实来源；本轮选择 `data/raw/gist_raw/karpathy-gist-llm-wiki` 作为唯一来源，原因是它为 `status: ok` 的本地已获取 `gist_raw` 来源，接近原始材料、可离线读取，且适合第一轮 bottom-up 挖掘事实候选。主控 agent 只监控任务包、状态、读日志和交付，不亲自抽取事实。

## 过程轨迹（process_trace）

- 2026-05-25：创建循环控制面初版。
- 2026-05-25：明确主控 agent 是决策者，执行者只做有界任务。
- 2026-05-25：把当前阶段非目标固定为枢纽页、聚类、主题覆盖和复杂元数据。
- 2026-05-25：记录第 0 轮 bootstrap 交付，保证循环状态可从磁盘恢复。
- 2026-05-25：独立执行者审计通过控制面，并指出 4 个最小修复点；已修复读写顺序、选源准则、恢复准则和审计写入范围。
- 2026-05-25：补充预定义 system prompt 层，把稳定角色边界从主控 agent 的临场判断中移出。
- 2026-05-25：完成 Codex hooks + custom agents 最小可行性调查；结论是 hooks 适合做 guardrail/context/stop 检查，不适合直接作为原生 sub-agent dispatcher。
- 2026-05-25：建立前置门禁、上下文隔离、main-agent 弹性、sub-agent 演化、生命周期、CLI 验证和用户洞察记录。
- 2026-05-25：完成 Claude CLI 与 Codex CLI 的最小 worker runtime smoke；Claude 无工具写作 smoke 返回 `READY`，Codex `--ephemeral --sandbox read-only` smoke 返回 `READY`，同时确认外部 Codex CLI 会触发已信任 hooks 并产生日志噪声。
- 2026-05-25：`user-insights` sidecar 已写入顶层 `user-insights/`，coverage 标记为 `partial`；`llm_wiki/loop/user_insights/` 仅保留为 pre-skill fallback。
- 2026-05-25：已派发 `iteration_20260525_0001_prelaunch_validation` 独立审计，检查前置门禁是否足以进入 source mining。
- 2026-05-25：独立审计结论为 `concern`；已修正 canonical 用户洞察链接，显式接受 `coverage: partial` 为非阻塞残余风险，并补足后续 CLI smoke 审计输入范围。
- 2026-05-25：新增给下一位 main-agent 的长程执行计划，覆盖 KB 生产、skills/prompt 演化、文件系统管理和 out-of-loop 反思；同时把通用 long-horizon loop pattern 沉淀进 `agent-loop-runner` skill。
- 2026-05-25：创建并派发 `iteration_20260525_0002_source_mining_karpathy_gist`；任务包通过 `validate_scope.py`，dispatch 使用 `fork_context: false`，执行者只接收 base worker、source mining worker prompt 和当前 task packet。

## 关键指标（key_metrics）

当前还没有知识卡产出，因此不统计卡片数量。

后续最小指标：

- 事实候选数量。
- 草稿知识卡数量。
- 审计通过数量。
- 已采纳知识卡数量。
- 因上下文泄漏、focus drift、来源不足或语言漂移导致的返工次数。

## 证据链接（evidence_links）

- [循环 README](../README.md)
- [运行手册](../RUNBOOK.md)
- [执行者边界](../SUBAGENT_SCOPE.md)
- [循环状态](../loop_state.json)
- [循环清单](../loop_manifest.json)
- [前置要求](../PRELAUNCH_REQUIREMENTS.md)
- [上下文隔离](../CONTEXT_ISOLATION.md)
- [main-agent 弹性](../MAIN_AGENT_ELASTICITY.md)
- [sub-agent 演化](../SUBAGENT_EVOLUTION.md)
- [sub-agent 生命周期](../SUBAGENT_LIFECYCLE.md)
- [技术验证](../TECH_VALIDATION.md)
- [用户洞察索引](../../../user-insights/index.md)
- [用户洞察 session log](../../../user-insights/sessions/session_20260525_llm_wiki_loop_bootstrap/session_log.md)
- [system prompt 目录](../system_prompts/README.md)
- [任务队列](../queues/task_queue.md)
- [第 0 轮 bootstrap](../iterations/iteration_0000_bootstrap/loop_delivery.md)
- [第 0 轮独立审计摘要](../iterations/iteration_0000_bootstrap/artifacts/independent_scope_audit.md)
- [Codex hooks 可行性 smoke](../iterations/iteration_0000_bootstrap/artifacts/codex_hooks_feasibility_smoke.md)
- [CLI worker smoke](../iterations/iteration_0000_bootstrap/artifacts/cli_worker_smoke.md)
- [前置门禁审计任务](../iterations/iteration_20260525_0001_prelaunch_validation/task.md)
- [前置门禁审计报告](../iterations/iteration_20260525_0001_prelaunch_validation/artifacts/independent_audit.md)
- [前置 concern 处理决策](../decisions/20260525-0208-prelaunch-concern-resolution.md)
- [Main-agent 长程执行计划](../plans/main_agent_long_horizon_execution_plan.md)
- [Main-agent 执行计划自审计](../reflections/20260525-main-agent-plan-self-audit.md)
- [第一轮 source mining 任务包](../iterations/iteration_20260525_0002_source_mining_karpathy_gist/task.md)
- [第一轮 source mining dispatch](../iterations/iteration_20260525_0002_source_mining_karpathy_gist/dispatch_request.json)
- [知识库产物面](../../kb/README.md)
- [来源索引](../../../data/manifests/acquired_sources_index.md)

## 风险与失败（risks_and_failures）

- 主控 agent 可能再次变成具体执行者，导致上下文变脏。
- 执行者如果没有窄任务包，容易把来源摘要写成主题页。
- 如果任务包允许输入过宽，独立审计就无法判断上下文泄漏。
- 公司网络环境可能限制网页 retrieve，因此当前优先使用 `data/` 中已获取来源。
- 如果知识卡写成审计日志或中间状态，说明 `card_drafting_worker` 的任务模板需要演化。
- `user-insights` 本次覆盖率是 `partial`；它只作为过程洞察和人类 recall，不作为知识卡事实来源。未来获得完整 transcript 或 verified refreshed fork 后再做 coverage repair。
