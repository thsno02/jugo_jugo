audit_result: concern

evidence:

- 当前任务包明确列出允许输入、禁止输入、允许写入、成功门禁和阻塞条件；`python3 llm_wiki/loop/tools/validate_scope.py llm_wiki/loop/iterations/iteration_20260525_0001_prelaunch_validation/task.md` 返回 `scope_validation: pass`。
- `llm_wiki/loop/PRELAUNCH_REQUIREMENTS.md` 覆盖 6 个前置门禁：上下文隔离、受限 main-agent 弹性、预定义 sub-agent 演化、技术最小验证、sub-agent 生命周期和用户洞察记录，并规定只有门禁满足后 `loop_state.json.status` 才能进入 `READY_FOR_SOURCE_MINING`。
- `llm_wiki/loop/CONTEXT_ISOLATION.md` 要求执行者只接收稳定 system prompt 和当前 `task.md`，只读取任务包允许输入，只写任务包允许写入，并在结束前留下 `loop_status.md`、`loop_delivery.md` 和 `read_log.md`。
- `llm_wiki/loop/MAIN_AGENT_ELASTICITY.md` 把 main-agent 的允许动作限制在任务包创建、机械脚本、派发、交付检查、独立审计和技能演化上；禁止其亲自挖掘来源、写卡、审计采纳或用父聊天上下文补证据。
- `llm_wiki/loop/SUBAGENT_EVOLUTION.md` 定义了基于失败证据的演化流程，修改对象限定为 system prompt、task template、manifest、scope、runbook 和机械检查脚本，并禁止 main-agent 临场发明无边界 sub-agent。
- `llm_wiki/loop/SUBAGENT_LIFECYCLE.md` 区分常驻、短期驻留和阅后即焚角色；`source_mining_worker`、`card_drafting_worker`、`card_audit_worker`、`card_adoption_worker` 和 `independent_evaluator` 均被列为阅后即焚。
- `llm_wiki/loop/TECH_VALIDATION.md` 记录了 Codex CLI、Claude CLI、Codex hooks 的已确认事实、当前结论、未验证项、风险和短中长期路线；允许读取的 `codex_hooks_feasibility_smoke.md` 与 `cli_capability_probe.md` 能支撑 hooks 与 CLI 能力基线。
- `llm_wiki/loop/RUNBOOK.md` 要求 `PRELAUNCH_IN_PROGRESS` 阶段只能推进前置要求，不能派发 `source_mining_worker` 生产事实候选。
- `llm_wiki/loop/loop_state.json` 当前仍为 `PRELAUNCH_IN_PROGRESS`，`next_action` 是等待本次 independent evaluator 完成前置门禁审计后再决定是否进入 `READY_FOR_SOURCE_MINING`。
- `llm_wiki/loop/queues/task_queue.md` 中 `task_20260525_0003_source_mining_bootstrap` 仍在 queued，且 note 明确只有前置门禁通过后才允许写入具体 `source_id`、`source_path` 并派发。
- `llm_wiki/loop/loop_manifest.json` 固定当前对象为 `atomic_fact_card`，把 `hub`、`cluster`、`topic_coverage`、`complex_metadata` 和 `agent_synthesis_as_source` 列为非目标，并列出各角色的默认输入、写入和 prompt/template 路径。
- `llm_wiki/loop/tools/README.md`、`create_task.py`、`render_dispatch.py`、`validate_scope.py` 和 `inspect_delivery.py` 显示已有机械脚本可生成任务包、组合 dispatch、检查 scope 和交付文件，从而减少 main-agent 临场写大段 prompt。
- 顶层 `user-insights/` 存在，且包含 `sessions/session_20260525_llm_wiki_loop_bootstrap/session_log.md`、`metadata.json`、`session_registry.json`、`session/cursor.json`、`session/sidecar_state.json` 和 `index.md`；`sidecar_state.json` 标记 `status: idle_after_record`，并列出这些文件为本次写入。
- `user-insights/sessions/session_20260525_llm_wiki_loop_bootstrap/session_log.md` 明确 `Canonical Target` 为顶层 `user-insights/`，并说明 `llm_wiki/loop/user_insights` 是 pre-skill fallback，本次未修改。
- `user-insights/` 的 `coverage` 标记为 `partial`，原因是当前运行环境没有暴露独立 refresh fork 或 full transcript 工具；它没有伪装成完整 transcript。
- `llm_wiki/loop/reports/loop_report.md` 的过程轨迹记录了顶层 `user-insights/` 已写入且旧 fallback 仅保留为历史痕迹，但 `evidence_links` 中的“用户洞察记录”仍指向 `../user_insights/session_20260525.md`，即旧 fallback 路径。
- 在允许输入中未发现当前阶段转向 hub、cluster、topic coverage 或复杂 metadata 的执行动作；这些词出现时主要作为非目标、禁止动作或用户洞察中的历史纠偏证据。

hypotheses:

- H1：当前前置控制面已经足以隔离执行者上下文，并阻止 source mining 在门禁通过前启动。
- H2：当前 main-agent 不再需要临场编写大段 worker prompt，因为稳定 prompt、任务模板和机械脚本已经形成基本调度面。
- H3：当前 sub-agent 的演化与生命周期规则足以支持后续失败修复，不需要 main-agent 临场扩权。
- H4：技术验证记录足以支持短期使用 Codex 原生 sub-agent 加 `render_dispatch.py`，同时保留 hooks 和 CLI runtime 的替代路线。
- H5：`user-insights/` 记录已由正式 sidecar 写入，但仍存在 canonical 链接和 coverage 风险。
- H6：当前文档主语言保持中文，英文主要出现在路径、命令、schema 字段、状态码、工具名和固定名词中。

validated_findings:

- H1 基本成立。任务包、隔离文档、状态文件和队列共同形成了上下文与阶段门禁；`source_mining_worker` 尚未被允许执行，当前状态也没有进入 `READY_FOR_SOURCE_MINING`。
- H2 成立。`MAIN_AGENT_ELASTICITY.md`、`RUNBOOK.md` 和 `tools/` 明确把 main-agent 的临场发挥收缩到任务包变量和机械脚本调用；`render_dispatch.py` 会组合 `base_worker`、角色 prompt 和 `task.md`。
- H3 成立。`SUBAGENT_EVOLUTION.md` 和 `SUBAGENT_LIFECYCLE.md` 给出了新增/修改条件、失败证据链、独立审计步骤和关闭条件；这能避免无边界执行者。
- H4 基本成立。`TECH_VALIDATION.md` 对 hooks、Codex CLI、Claude CLI 的能力、限制、未验证项和替代路线写得清楚；但它引用的 `cli_worker_smoke.md` 不在本任务允许输入中，本轮只能验证记录清晰性，不能独立复核该 smoke 细节。
- H5 部分成立。正式 sidecar 的顶层 `user-insights/` 输出存在，并明确旧目录不是 canonical target；但 coverage 是 `partial`，且 `loop_report.md` 仍把“用户洞察记录”链接到旧 fallback 路径，可能误导未来 agent 读取非 canonical 入口。
- H6 成立。允许输入中的人类可读控制文档以中文为主；英文使用集中在路径、命令、schema 字段、状态码、工具名、角色名和固定技术名词中。

required_changes:

- 在进入 `READY_FOR_SOURCE_MINING` 前，主控 agent 应修正 `llm_wiki/loop/reports/loop_report.md` 的“用户洞察记录”证据链接，使其指向顶层 `user-insights/index.md` 或本次 sidecar session log，而不是 `llm_wiki/loop/user_insights/` fallback。
- 主控 agent 应显式记录对 `user-insights` `coverage: partial` 的处理决策：如果接受 partial coverage 作为进入首轮 source mining 的残余风险，需要在状态或报告中写明；如果不接受，需要等 full transcript / refreshed fork 可用后做 coverage repair。
- 后续若继续审计技术验证，任务包应把 `llm_wiki/loop/iterations/iteration_0000_bootstrap/artifacts/cli_worker_smoke.md` 加入允许输入，或把该 smoke 的关键事实完整纳入 `TECH_VALIDATION.md`，避免审计者必须读取未授权证据才能复核 CLI worker 闭环。
- 除上述 concern 外，本轮未发现需要写入允许范围之外文件才能完成审计的阻塞项；不建议由 independent evaluator 代替主控 agent 修改全局控制文档。
