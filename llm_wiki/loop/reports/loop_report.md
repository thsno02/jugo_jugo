# LLM Wiki 循环报告

## 为什么存在（why_this_loop）

这个循环存在的原因是：LLM Wiki 的知识库不能从主题骨架或枢纽页开始，而要从可以被来源支撑的原子事实知识卡开始。

当前不追求覆盖率，也不追求结构完整。当前要降低的不确定性是：能否稳定地从本地来源中抽出事实候选，并经过出处论证和审计，沉淀为可读的 zet 风格知识卡。

## 当前决策（current_decision）

当前状态：第一轮 `source_mining_worker` 已完成并通过交付检查；第一次 drafting 产物因 `loop_delivery.md` 缺少标准 marker 未通过交付检查。已完成最小 prompt 修复并通过独立审计；候选 8 的 drafting revision 已通过交付检查，card audit 任务包已创建。

当前决策：接受 `user-insights` 的 `coverage: partial` 作为非阻塞残余风险，因为它不是知识卡事实来源；第一轮 source mining 产出 12 个候选并通过 `inspect_delivery.py`。第一次 drafting 暴露出 delivery marker 契约缺口，已把 `loop_delivery.md` 内必须写入 `LOOP_DONE` 或 `LOOP_BLOCKED` 的要求补入 `base_worker.md`，且独立审计为 `pass`。旧 drafting iteration 不手工补写，候选 8 已通过 revision 重跑进入审计准备状态。sub-agent 生命周期采用有意图管理：完成且不需复用的 worker 关闭；未来如遇反复读取同一大来源，可显式设置 alive worker 降低重复 IO 和上下文消耗。

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
- 2026-05-25：`source_mining_worker` 返回 `LOOP_DONE`，主控 agent 随即关闭该 sub-agent；`inspect_delivery.py` 返回 `pass`，12 个事实候选进入候选集。
- 2026-05-25：写入决策 `20260525-0241-source-mining-accepted-candidate-8.md`，选择候选 8 进入 `iteration_20260525_0003_card_drafting_raw_sources_truth`。
- 2026-05-25：候选 8 第一次 drafting 生成草稿卡和 provenance，但 `inspect_delivery.py` 因 `loop_delivery.md` 缺少 `LOOP_DONE` / `LOOP_BLOCKED` 失败；主控 agent 未补写 worker 交付，而是记录失败并修复稳定 prompt。
- 2026-05-25：`iteration_20260525_0004_delivery_marker_prompt_repair` 最小修改 `base_worker.md` 的交付 marker 规则；`iteration_20260525_0005_prompt_repair_audit` 独立审计结论为 `audit_result: pass`，审计 worker 已关闭。
- 2026-05-25：创建 `iteration_20260525_0006_card_drafting_raw_sources_truth_r1`，在修复后的 worker prompt 下重跑候选 8 drafting revision。
- 2026-05-25：候选 8 drafting revision 返回 `LOOP_DONE`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，草稿卡和 provenance 进入 card audit 准备状态。
- 2026-05-25：创建 `iteration_20260525_0007_card_audit_raw_sources_truth_r1`，任务包通过 `validate_scope.py`，dispatch 使用 `fork_context: false`。

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
- [第一轮事实候选](../iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md)
- [接受 source mining 并选择候选 8 的决策](../decisions/20260525-0241-source-mining-accepted-candidate-8.md)
- [候选 8 drafting 任务包](../iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/task.md)
- [候选 8 drafting dispatch](../iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/dispatch_request.json)
- [delivery marker prompt 修复任务](../iterations/iteration_20260525_0004_delivery_marker_prompt_repair/task.md)
- [prompt 修复报告](../iterations/iteration_20260525_0004_delivery_marker_prompt_repair/artifacts/prompt_repair_report.md)
- [prompt 修复独立审计](../iterations/iteration_20260525_0005_prompt_repair_audit/artifacts/independent_audit.md)
- [接受 prompt 修复决策](../decisions/20260525-0254-accept-delivery-marker-prompt-repair.md)
- [候选 8 drafting revision 任务包](../iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/task.md)
- [候选 8 drafting revision dispatch](../iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/dispatch_request.json)
- [候选 8 草稿卡](../iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/draft_card.md)
- [候选 8 provenance](../iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/provenance.md)
- [候选 8 drafting revision 可审计决策](../decisions/20260525-0301-card-drafting-revision-ready-for-audit.md)
- [候选 8 audit 任务包](../iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/task.md)
- [候选 8 audit dispatch](../iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/dispatch_request.json)
- [知识库产物面](../../kb/README.md)
- [来源索引](../../../data/manifests/acquired_sources_index.md)

## 风险与失败（risks_and_failures）

- 主控 agent 可能再次变成具体执行者，导致上下文变脏。
- 执行者如果没有窄任务包，容易把来源摘要写成主题页。
- 如果任务包允许输入过宽，独立审计就无法判断上下文泄漏。
- 公司网络环境可能限制网页 retrieve，因此当前优先使用 `data/` 中已获取来源。
- 如果知识卡写成审计日志或中间状态，说明 `card_drafting_worker` 的任务模板需要演化。
- `user-insights` 本次覆盖率是 `partial`；它只作为过程洞察和人类 recall，不作为知识卡事实来源。未来获得完整 transcript 或 verified refreshed fork 后再做 coverage repair。
