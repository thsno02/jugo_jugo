# LLM Wiki 循环报告

## 为什么存在（why_this_loop）

这个循环存在的原因是：LLM Wiki 的知识库不能从主题骨架或枢纽页开始，而要从可以被来源支撑的原子事实知识卡开始。

当前不追求覆盖率，也不追求结构完整。当前要降低的不确定性是：能否稳定地从本地来源中抽出事实候选，并经过出处论证和审计，沉淀为可读的 zet 风格知识卡。

## 当前决策（current_decision）

当前状态：已有 2 张原子事实知识卡采纳到 KB。第一轮 source mining 产出 12 个候选，其中候选 8 和候选 7 都已完成 drafting、audit 和 adoption。小批量后的 out-of-loop 反思已完成，adoption 任务模板修复已通过修正版独立审计；候选 10 drafting 任务包已创建。

当前决策：接受 `user-insights` 的 `coverage: partial` 作为非阻塞残余风险，因为它不是知识卡事实来源；候选 8 的知识卡 `Raw sources 是只读事实来源` 和候选 7 的知识卡 `LLM Wiki 的三层架构` 已采纳为 `accepted`。`card_adoption_task.md` 的目标路径读取边界已修复并通过独立审计；恢复 KB 生产，候选 10 进入 drafting。

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
- 2026-05-25：`card_audit_worker` 返回 `audit_result: pass`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，写入采纳准备决策。
- 2026-05-25：创建 `iteration_20260525_0008_card_adoption_raw_sources_truth`，指定 `card_id` 为 `raw-sources-readonly-source-of-truth`，目标 KB 路径不存在，任务包通过 `validate_scope.py`。
- 2026-05-25：`card_adoption_worker` 返回 `LOOP_DONE`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，知识卡、provenance 和最小索引已写入 `llm_wiki/kb/`。
- 2026-05-25：记录 sub-agent 生命周期策略：独立判断和单次写入 worker 完成后关闭；若未来出现大来源或高重复 IO，可显式使用 alive worker，但必须在任务包或 decision 中声明边界。
- 2026-05-25：创建 `iteration_20260525_0009_card_drafting_architecture_layers`，选择候选 7，证据范围为 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33`，任务包通过 `validate_scope.py`。
- 2026-05-25：候选 7 drafting worker 返回 `LOOP_DONE`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，草稿卡和 provenance 进入 card audit 准备状态。
- 2026-05-25：创建 `iteration_20260525_0010_card_audit_architecture_layers`，任务包通过 `validate_scope.py`，dispatch 使用 `fork_context: false`。
- 2026-05-25：候选 7 `card_audit_worker` 返回 `audit_result: pass`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，写入采纳准备决策。
- 2026-05-25：创建 `iteration_20260525_0011_card_adoption_architecture_layers`，指定 `card_id` 为 `llm-wiki-three-layer-architecture`，目标 KB 路径不存在，任务包通过 `validate_scope.py`。
- 2026-05-25：候选 7 `card_adoption_worker` 返回 `LOOP_DONE`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，第二张 KB 卡采纳完成。
- 2026-05-25：两轮 adoption 的 `read_log.md` 均记录目标 KB 路径读取为额外读取；主控 agent 将其记录为重复边界噪声，暂停生产并进入反思与模板修复。
- 2026-05-25：写入小批量采纳后的反思；最小修复 `card_adoption_task.md`，把目标 KB 卡片、目标 provenance 和索引文件列为允许读取，但用途限定为存在性、覆盖冲突和最小索引增量更新。
- 2026-05-25：创建 `iteration_20260525_0013_adoption_template_repair_audit`，任务包通过 `validate_scope.py`，dispatch 使用 `fork_context: false`。
- 2026-05-25：`iteration_20260525_0013_adoption_template_repair_audit` 返回 `audit_result: concern`；原因是审计任务包把 out-of-loop reflection 误列为 `target_artifacts`。已写入澄清决策，并创建 `iteration_20260525_0014_adoption_template_repair_audit_r1`。
- 2026-05-25：修正版 adoption template 修复审计返回 `audit_result: pass`；接受模板修复并恢复 KB 生产，下一步选择候选 10。
- 2026-05-25：创建 `iteration_20260525_0015_card_drafting_schema_layer`，选择候选 10，证据范围为 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:33`，任务包通过 `validate_scope.py`。
- 2026-05-25：候选 10 drafting worker 返回 `LOOP_DONE`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，草稿卡和 provenance 进入 card audit 准备状态。
- 2026-05-25：创建 `iteration_20260525_0016_card_audit_schema_layer`，审计输入限定为候选 10 草稿卡、provenance 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:33`；任务包通过 `validate_scope.py`，dispatch 使用 `fork_context:false`。
- 2026-05-25：候选 10 `card_audit_worker` 返回 `audit_result: pass`，主控 agent 关闭该 worker；`inspect_delivery.py` 返回 `pass`，写入采纳准备决策。
- 2026-05-25：创建 `iteration_20260525_0017_card_adoption_schema_layer`，指定 `card_id` 为 `llm-wiki-schema-configuration-document`，目标 KB 路径不存在，任务包通过 `validate_scope.py`。

## 关键指标（key_metrics）

- 事实候选数量：12。
- 草稿知识卡数量：3 个有效 drafting 产物，1 个因交付 marker 缺失而不采纳的失败 drafting iteration。
- 审计通过数量：3。
- 已采纳知识卡数量：2。
- 因交付 marker 缺失导致的返工次数：1。
- 因 adoption 模板未显式允许读取目标 KB 路径导致的非阻塞边界噪声：2。
- 因上下文泄漏、focus drift、来源不足或语言漂移导致的返工次数：0。

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
- [候选 8 audit 报告](../iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md)
- [候选 8 audit pass 决策](../decisions/20260525-0308-card-audit-pass-candidate-8.md)
- [候选 8 adoption 任务包](../iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/task.md)
- [候选 8 adoption dispatch](../iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/dispatch_request.json)
- [候选 8 adoption 交付](../iterations/iteration_20260525_0008_card_adoption_raw_sources_truth/loop_delivery.md)
- [候选 8 采纳决策](../decisions/20260525-0316-card-adoption-accepted-candidate-8.md)
- [sub-agent 生命周期策略决策](../decisions/20260525-0316-subagent-lifecycle-policy.md)
- [已采纳知识卡：Raw sources 是只读事实来源](../../kb/cards/raw-sources-readonly-source-of-truth.md)
- [已采纳 provenance：Raw sources 是只读事实来源](../../kb/provenance/raw-sources-readonly-source-of-truth.md)
- [知识卡索引](../../kb/indexes/cards.md)
- [候选 7 drafting 任务包](../iterations/iteration_20260525_0009_card_drafting_architecture_layers/task.md)
- [候选 7 drafting dispatch](../iterations/iteration_20260525_0009_card_drafting_architecture_layers/dispatch_request.json)
- [候选 7 草稿卡](../iterations/iteration_20260525_0009_card_drafting_architecture_layers/artifacts/draft_card.md)
- [候选 7 provenance](../iterations/iteration_20260525_0009_card_drafting_architecture_layers/artifacts/provenance.md)
- [候选 7 drafting 可审计决策](../decisions/20260525-0324-card-drafting-candidate-7-ready-for-audit.md)
- [候选 7 audit 任务包](../iterations/iteration_20260525_0010_card_audit_architecture_layers/task.md)
- [候选 7 audit dispatch](../iterations/iteration_20260525_0010_card_audit_architecture_layers/dispatch_request.json)
- [候选 7 audit 报告](../iterations/iteration_20260525_0010_card_audit_architecture_layers/artifacts/audit_report.md)
- [候选 7 audit pass 决策](../decisions/20260525-0330-card-audit-pass-candidate-7.md)
- [候选 7 adoption 任务包](../iterations/iteration_20260525_0011_card_adoption_architecture_layers/task.md)
- [候选 7 adoption dispatch](../iterations/iteration_20260525_0011_card_adoption_architecture_layers/dispatch_request.json)
- [候选 7 adoption 交付](../iterations/iteration_20260525_0011_card_adoption_architecture_layers/loop_delivery.md)
- [候选 7 采纳决策](../decisions/20260525-0337-card-adoption-accepted-candidate-7.md)
- [已采纳知识卡：LLM Wiki 的三层架构](../../kb/cards/llm-wiki-three-layer-architecture.md)
- [已采纳 provenance：LLM Wiki 的三层架构](../../kb/provenance/llm-wiki-three-layer-architecture.md)
- [小批量采纳后的反思](../reflections/20260525-small-batch-adoption-template-reflection.md)
- [adoption template 修复任务](../iterations/iteration_20260525_0012_adoption_template_repair/task.md)
- [adoption template 修复报告](../iterations/iteration_20260525_0012_adoption_template_repair/artifacts/template_repair_report.md)
- [adoption template 修复审计任务](../iterations/iteration_20260525_0013_adoption_template_repair_audit/task.md)
- [adoption template 修复审计 dispatch](../iterations/iteration_20260525_0013_adoption_template_repair_audit/dispatch_request.json)
- [adoption template 修复审计 concern](../iterations/iteration_20260525_0013_adoption_template_repair_audit/artifacts/independent_audit.md)
- [adoption template 审计 concern 澄清决策](../decisions/20260525-0348-adoption-template-audit-concern-resolution.md)
- [adoption template 修正版审计任务](../iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/task.md)
- [adoption template 修正版审计 dispatch](../iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/dispatch_request.json)
- [adoption template 修正版审计报告](../iterations/iteration_20260525_0014_adoption_template_repair_audit_r1/artifacts/independent_audit.md)
- [接受 adoption template 修复决策](../decisions/20260525-0354-accept-adoption-template-repair.md)
- [候选 10 drafting 任务包](../iterations/iteration_20260525_0015_card_drafting_schema_layer/task.md)
- [候选 10 drafting dispatch](../iterations/iteration_20260525_0015_card_drafting_schema_layer/dispatch_request.json)
- [候选 10 草稿卡](../iterations/iteration_20260525_0015_card_drafting_schema_layer/artifacts/draft_card.md)
- [候选 10 provenance](../iterations/iteration_20260525_0015_card_drafting_schema_layer/artifacts/provenance.md)
- [候选 10 drafting 可审计决策](../decisions/20260525-0403-card-drafting-candidate-10-ready-for-audit.md)
- [候选 10 audit 任务包](../iterations/iteration_20260525_0016_card_audit_schema_layer/task.md)
- [候选 10 audit dispatch](../iterations/iteration_20260525_0016_card_audit_schema_layer/dispatch_request.json)
- [候选 10 audit 报告](../iterations/iteration_20260525_0016_card_audit_schema_layer/artifacts/audit_report.md)
- [候选 10 audit pass 决策](../decisions/20260525-0409-card-audit-pass-candidate-10.md)
- [候选 10 adoption 任务包](../iterations/iteration_20260525_0017_card_adoption_schema_layer/task.md)
- [候选 10 adoption dispatch](../iterations/iteration_20260525_0017_card_adoption_schema_layer/dispatch_request.json)
- [知识库产物面](../../kb/README.md)
- [来源索引](../../../data/manifests/acquired_sources_index.md)

## 风险与失败（risks_and_failures）

- 主控 agent 可能再次变成具体执行者，导致上下文变脏。
- 执行者如果没有窄任务包，容易把来源摘要写成主题页。
- 如果任务包允许输入过宽，独立审计就无法判断上下文泄漏。
- 公司网络环境可能限制网页 retrieve，因此当前优先使用 `data/` 中已获取来源。
- 如果知识卡写成审计日志或中间状态，说明 `card_drafting_worker` 的任务模板需要演化。
- adoption worker 为了避免覆盖读取了目标 KB 路径并已记录原因；后续应把“读取目标写入路径做存在性和冲突检查”显式写入 adoption 任务模板，减少边界噪声。
- `user-insights` 本次覆盖率是 `partial`；它只作为过程洞察和人类 recall，不作为知识卡事实来源。未来获得完整 transcript 或 verified refreshed fork 后再做 coverage repair。
