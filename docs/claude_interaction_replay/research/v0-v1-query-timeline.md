# V0-V1 查询级里程碑时间线提案

## 1. 目的与边界

本文为查询级时间线（query-level timeline）选择默认里程碑，不替代完整事件档案。V0 的完整用户输入仍由 `docs/claude_interaction_replay/events/events.codex.prehistory-research.v2.jsonl`、`docs/claude_interaction_replay/events/events.codex.primary-v0-v1.v2.jsonl` 和 `docs/claude_interaction_replay/events/events.codex.retro-daily-audit.v2.jsonl` 提供；V1 的完整用户输入仍由后两个分片提供。页面的全部事件模式（all-events mode）必须继续按 `version_ids` 展示所有输入，不能因为本文只选择默认节点而删减、去重或隐藏用户纠正。

本文只使用归档中的精确 `event_id`，artifact reference 一律使用当前仓库中的 repo-relative path。排序依据是事件的 `times.source_recorded_at`；run 文件名中的声明时间、文件观测时间和 Git 时间不替代事件顺序。

证据类型（kind）采用以下互斥主标签：

- `specified`：该 query 明确规定目标、约束或下一步；不表示随后一定执行。
- `executed`：该 query 后的 reviewed assistant window 报告了动作，且同时期 run artifact 或终态产物可以交叉支持。
- `observed_failure`：用户直接报告可见失败、成本或不符合预期的结果。
- `contradicted`：用户纠正或一手 artifact 推翻了此前的完成、范围或质量主张。
- `retrospective`：后来形成的审计或解释，只能说明后验归因，不能证明原始执行。

阶段标签（phase label）用于叙事导航，不把 V2+ 的 questioning、reframing、fusion 或 scripted ingest 机制倒写进 V0/V1。下表中的项目均建议进入默认密度，因此全部为 `milestone=true`；其余 query 保留在 all-events mode，默认不标里程碑。

## 2. V0 默认里程碑（11）

V0 的主线是：先建立 raw knowledge database 和 coverage-driven source substrate，再运行 filesystem-backed KB 机制 demo；机制产物真实存在，但用户最终指出生产对象从“LLM Wiki topic”漂移成“如何生产 KB”的 meta topic，于是归档并转入 V1。

| # | event_id | phase label | 短标题 | significance | kind | milestone | artifact refs |
|---:|---|---|---|---|---|---|---|
| 1 | `codex:codex-prehistory-research:H001` | 起源（origin） | 先建 raw knowledge database | 把当前阶段限定为资源获取，建立后来 V0/V1 共用的 source substrate；它不是 V0 node build 本身。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/protocol/loop_plan_data_collection.md` |
| 2 | `codex:codex-prehistory-research:H003` | 决策（decision） | arXiv 改为 TeX-first | 明确资料主要供 agent 阅读，要求 source/TeX 优先并只在必要时回退 PDF，改变论文采集合同。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/reports/acquisition_status.md` |
| 3 | `codex:codex-prehistory-research:H004` | 决策（decision） | 用 coverage 定义“资料够不够” | 从“下载相关内容”升级为第一性原理 coverage、缺口审计和补证据判断，为后续循环提供停止标准。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/reports/coverage_framework.md` |
| 4 | `codex:codex-prehistory-research:H009` | 纠偏（correction） | 修复 coverage-driven 闭环 | 用户指出旧 plan 没有持续按 coverage 找资料；修复后 assistant window 报告补入 27 个候选源、manifest 达 72、队列归零。该节点证明采集循环修复，不证明 V0 KB 已生成。 | `executed` | `true` | `loops/v1_topic_hub_skeleton_20260524/reports/goal_satisfaction_audit.md`<br>`loops/v1_topic_hub_skeleton_20260524/reports/coverage_status.md` |
| 5 | `codex:codex-primary-v0-v2-boundary:H001` | 起源（origin） | 启动 KB 初始化计划 | 用户要求全量读取 `loop_plan_init_kb.md` 并准备执行，标志 V0 node build 与前史资料采集的边界。 | `specified` | `true` | `loops/v0_meta_kb_initialization_demo_20260524/.llmwiki_snapshot/runs/run_20260524_050031_kb_initialization_bootstrap/run_plan.md` |
| 6 | `codex:codex-primary-v0-v2-boundary:H002` | 执行（action） | 自治循环产出机制 demo | 在自治与反思要求下，bootstrap、view、graph 与 impact 演示实际运行；终态支持 7 个 adopted nodes、7 个 KB views、35 条 edges、1 个 held 2.0 candidate 和 4 个 open impacts。 | `executed` | `true` | `loops/v0_meta_kb_initialization_demo_20260524/generated/status.yaml`<br>`loops/v0_meta_kb_initialization_demo_20260524/generated/impact_queue.yaml` |
| 7 | `codex:codex-primary-v0-v2-boundary:H003` | 结果（outcome） | 有限检索、失败留证后收口 | 用户规定受限网络下有限尝试并记录失败；同时期 retrieval log 与 dynamic run 支持一次失败来源被排除、一次成功来源被采用。原 goal complete 只代表当时门禁通过。 | `executed` | `true` | `loops/v0_meta_kb_initialization_demo_20260524/.llmwiki_snapshot/control/retrieval_log.yaml`<br>`loops/v0_meta_kb_initialization_demo_20260524/.llmwiki_snapshot/runs/run_20260524_050318_dynamic_retrieval_enterprise_scale/audit_report.md` |
| 8 | `codex:codex-primary-v0-v2-boundary:H004` | 用户质疑（challenge） | 首次指出主语言失配 | 用户直接指出输出没有遵守中文主语言要求；该节点记录可见质量失败，不把后续修复提前算在这里。 | `observed_failure` | `true` | — |
| 9 | `codex:codex-primary-v0-v2-boundary:H006` | 纠偏（correction） | 中文要求落实到文件内容 | 用户把纠正范围从回复扩展到所有人类可读文件，assistant window 报告批量重写并重新验证。 | `executed` | `true` | `scripts/kb_localize_zh.py` |
| 10 | `codex:codex-primary-v0-v2-boundary:H007` | 用户质疑（challenge） | 揭示 meta/object 错位 | 用户指出目标是 LLM Wiki topic KB，而实际产物是“如何生产 KB”的 meta KB；这反证了此前对象层的完成主张，但不否定文件机制确实运行。 | `contradicted` | `true` | `loops/v0_meta_kb_initialization_demo_20260524/kb_initialization_demo_report.md` |
| 11 | `codex:codex-primary-v0-v2-boundary:H008` | 迁移（transition） | 将 V0 归档为 demo-0 | 用户决定保留机制 demo 供审计，同时要求重做 plan、切回 LLM Wiki topic 并使用 `data/`；assistant window 报告归档、重置 active 内容并建立新 topic plan。 | `executed` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_053000_topic_replan/run_plan.md`<br>`loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/control/topic_plan.md` |

### V0 因果边

只建议写入以下有文本指向或明确返工关系的边；没有边不表示两个相邻事件无关，只表示方向证据不足。

| from_event_id | to_event_id | relation | 方向依据 |
|---|---|---|---|
| `codex:codex-prehistory-research:H001` | `codex:codex-prehistory-research:H003` | `corrected` | H003 明确修改 H001 所启动资源采集中的 arXiv 读取面。 |
| `codex:codex-prehistory-research:H003` | `codex:codex-prehistory-research:H004` | `caused` | H004 明示“完成 paper 重新下载后”再建立 coverage 与缺口审计。 |
| `codex:codex-prehistory-research:H004` | `codex:codex-prehistory-research:H009` | `triggered_rework` | H009 明确修复此前 plan，使 H004 定义的 coverage 真正成为循环与停止条件。 |
| `codex:codex-primary-v0-v2-boundary:H001` | `codex:codex-primary-v0-v2-boundary:H002` | `caused` | H001 启动初始化计划，H002 在任务执行中追加自治与反思要求并触发实际 demo build。 |
| `codex:codex-primary-v0-v2-boundary:H003` | `codex:codex-primary-v0-v2-boundary:H007` | `contradicted` | H003 window 宣布 goal complete；H007 随后指出核心 topic 对象做错。 |
| `codex:codex-primary-v0-v2-boundary:H004` | `codex:codex-primary-v0-v2-boundary:H006` | `triggered_rework` | H004 首次指出语言失配，经未选中的 H005 再次要求重做，H006 最终把返工扩展到文件内容。 |
| `codex:codex-primary-v0-v2-boundary:H007` | `codex:codex-primary-v0-v2-boundary:H008` | `triggered_rework` | H007 的 meta/object 反证直接引出 H008 的归档、重置、换 topic 和改用 `data/`。 |

## 3. V1 默认里程碑（14）

V1 的主线是：将 `data/` 设为主要证据层，以 planner/worker、skills 和多门禁循环完整生产 8 个 top-down topic nodes；局部门禁与 worker 隔离得到修复，但用户随后从卡片数量、生产方向、周期和可读性上否定核心对象，版本最终作为 topic hub skeleton 归档。

| # | event_id | phase label | 短标题 | significance | kind | milestone | artifact refs |
|---:|---|---|---|---|---|---|---|
| 1 | `codex:codex-primary-v0-v2-boundary:H009` | 起源（origin） | planner 把 topic 建议变成执行计划 | 用户明确静态 topic plan 只是建议，要求 planner sub-agent 从 sources 与 coverage 生成可执行工作；assistant window 报告改成 planner/generator/auditor 三段式。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_054000_topic_planner/planner_report.md` |
| 2 | `codex:codex-primary-v0-v2-boundary:H012` | 决策（decision） | 以 mining protocol 初始化 skills | 用户提供构建协议，要求重做 plan 并先建立可在 loop 中迭代的 repo-local skills，定义 V1 的 source mining、frontier、node、audit 与 skill-evolution 控制面。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/protocol/KB_INIT_KNOWLEDGE_MINING_PROTOCOL.md`<br>`loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/control/skill_registry.yaml` |
| 3 | `codex:codex-primary-v0-v2-boundary:H013` | 决策（decision） | 规定自治循环的双交付物 | 用户明确目标同时包括“一套 skills”和“一个完整知识库”，且启动 loop 前先完成规划；assistant window 只完成 pre-loop planning，却错误地把阶段 goal 标成完成。 | `specified` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_060000_preloop_planning/preloop_plan.md`<br>`loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/control/autonomous_loop_plan.md` |
| 4 | `codex:codex-primary-v0-v2-boundary:H014` | 用户质疑（challenge） | 规划完成不等于 goal 完成 | 用户直接推翻“只初始化 skills 即完成”的判断，要求用 skills 真正 build KB 并迭代；assistant window 重新进入执行态。 | `contradicted` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_061000_source_mining_origin_canon/controller_drift_note.md` |
| 5 | `codex:codex-primary-v0-v2-boundary:H015` | 执行（action） | main agent 改为 controller | 用户要求主代理保持上下文干净、只做决策，具体执行交给 workers；旧 direct-mining run 被 blocked，origin/canon 随后由 worker 重跑。 | `executed` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_061000_source_mining_origin_canon/controller_drift_note.md`<br>`loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_062000_worker_source_mining_origin_canon/source_mining.md` |
| 6 | `codex:codex-primary-v0-v2-boundary:H016` | 结果（outcome） | 修复 footnote 门禁并交付 8 nodes | 用户把 References 在前、Footnotes 最后定为渲染硬约束；assistant window 报告阻断、repair、迁移旧卡并完成 8 个 adopted nodes、8 个 KB views 和 185 条 citation edges。该结果证明结构流水线完成，不证明产品目标正确。 | `executed` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_113000_worker_repair_footnote_layout_contract/repair_trace.md`<br>`loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/runs/run_20260524_142000_worker_v1_final_qa_delivery/final_delivery_report.md`<br>`loops/v1_topic_hub_skeleton_20260524/generated/status.yaml` |
| 7 | `codex:codex-primary-v0-v2-boundary:H017` | 用户质疑（challenge） | 大量资料为何只有 8 张卡 | 用户用产出密度质疑 final delivery；assistant 承认显性 KB 只是 8 张高密度 backbone cards，而非充分原子化知识层。 | `observed_failure` | `true` | `loops/v1_topic_hub_skeleton_20260524/generated/status.yaml` |
| 8 | `codex:codex-primary-v0-v2-boundary:H018` | 用户质疑（challenge） | top-down 违背 bottom-up | 用户明确指出既定方向应是 atomic-to-hub；这反证 V1 把 topic candidate 直接当生产单元和用 topic coverage 作为完成指标。 | `contradicted` | `true` | `loops/v1_topic_hub_skeleton_20260524/llm_wiki_runtime/control/topic_node_backlog.yaml` |
| 9 | `codex:codex-primary-v0-v2-boundary:H020` | 纠偏（correction） | atomic card 仍需强校验 | 用户纠正“atomic 可轻量校验”的误解，区分 known fact 与 accepted fact，并把 hub 放回已验证 atomic cards 的下游。该节点是新合同的指定，不是 V1 已执行证明。 | `specified` | `true` | — |
| 10 | `codex:codex-primary-v0-v2-boundary:H021` | 决策（decision） | 当前 loop 只建 solid foundation | 用户确认 clustering 对未来 hub 有必要，但明确本轮不做 cluster、hub 或 topic，只生长有依赖也可接受的 atomic cards。 | `specified` | `true` | — |
| 11 | `codex:codex-primary-v0-v2-boundary:H024` | 用户质疑（challenge） | 卡片形态也不可读 | 用户把失败扩大为“核心生产对象错误 + 文档形态错误”：现有 cards 像中间状态，而不是可读 zet-style atomic cards，进一步推翻 `v1_delivered` 的产品含义。 | `contradicted` | `true` | `loops/v1_topic_hub_skeleton_20260524/kb/20260524_062000_llm_wiki_origin_and_canon.md` |
| 12 | `codex:codex-primary-v0-v2-boundary:H026` | 决策（decision） | 分离 card、provenance 与 citation | 用户明确 card 是知识结果，provenance 是把 zet card 做实为 fact 的可读过程 artifact，citation/reference 是轻量出处与连接；这是 V2 前置设计，不倒写为 V1 实现。 | `specified` | `true` | — |
| 13 | `codex:codex-primary-v0-v2-boundary:H029` | 迁移（transition） | 下令归档两版并独立审计 | 用户在新契约明确后要求公开可审计的文件结构，把 V0/V1 移入 legacy，并让独立 sub-agent 审计多余步骤、偏差和不合理处。该 event 只证明指令与迁移启动，不用最终归档快照证明当刻已全部完成。 | `specified` | `true` | — |
| 14 | `codex:codex-primary-v0-v2-boundary:H031` | 后验（retrospective） | focus-drift 审计确认根因 | 用户要求按“先证据、再假设、再验证”调查 loop focus drift；随后形成的后验审计把根因定位到 0→1 topic node 协议及围绕 node adoption/topic coverage 的 gates，并完成归档迁移。它解释 V1 失败，不是原始 worker 执行证明。 | `retrospective` | `true` | `loops/v1_topic_hub_skeleton_20260524/audits/focus_drift_audit_20260524/root_cause_analysis.md`<br>`loops/v1_topic_hub_skeleton_20260524/audits/context_isolation_audit_20260524/context_isolation_audit.md`<br>`loops/v1_topic_hub_skeleton_20260524/README.md` |

### V1 因果边

| from_event_id | to_event_id | relation | 方向依据 |
|---|---|---|---|
| `codex:codex-primary-v0-v2-boundary:H009` | `codex:codex-primary-v0-v2-boundary:H012` | `corrected` | H009 只有 planner 方向；经 all-events 中的 H010 暂停和 H011 私链不可访问后，H012 提供正式 mining protocol 并要求重做 plan。 |
| `codex:codex-primary-v0-v2-boundary:H012` | `codex:codex-primary-v0-v2-boundary:H013` | `caused` | H012 初始化 skills 与流程，H013 随即把它们纳入持续自治 loop，并明确双交付物。 |
| `codex:codex-primary-v0-v2-boundary:H013` | `codex:codex-primary-v0-v2-boundary:H014` | `contradicted` | H013 window 错把 pre-loop planning 当 goal complete，H014 直接指出 skills 和 KB 都必须交付。 |
| `codex:codex-primary-v0-v2-boundary:H014` | `codex:codex-primary-v0-v2-boundary:H015` | `corrected` | H014 重启执行后主代理直接做 mining；H015 明确干预并改成 controller/worker 边界。 |
| `codex:codex-primary-v0-v2-boundary:H016` | `codex:codex-primary-v0-v2-boundary:H017` | `challenged` | H016 window 给出 final delivery，H017 立即以“这么多内容只抽象几张 card”质疑其产出密度。 |
| `codex:codex-primary-v0-v2-boundary:H017` | `codex:codex-primary-v0-v2-boundary:H018` | `caused` | H017 回答确认只有 8 张 backbone cards，使 H018 进一步定位为 top-down 与 bottom-up 方向冲突。 |
| `codex:codex-primary-v0-v2-boundary:H018` | `codex:codex-primary-v0-v2-boundary:H020` | `corrected` | H018 揭示生产方向错误；经 all-events 中 H019 对周期成本的追问，H020 纠正 atomic fact 的强校验与 hub 层级。 |
| `codex:codex-primary-v0-v2-boundary:H020` | `codex:codex-primary-v0-v2-boundary:H021` | `caused` | H020 重建 atomic/hub 边界，H021 据此把当前 loop scope 收敛为只生产 atomic foundation。 |
| `codex:codex-primary-v0-v2-boundary:H024` | `codex:codex-primary-v0-v2-boundary:H026` | `corrected` | H024 指出 card 不可读且混入中间过程；经 all-events 中 H025 的 footnote/reference 权衡，H026 明确结果、论证过程与连接三者分工。 |
| `codex:codex-primary-v0-v2-boundary:H026` | `codex:codex-primary-v0-v2-boundary:H029` | `caused` | H029 明示 card schema、scope、生产范式和本轮重点已经明确，继而转向文件治理、归档和独立审计。 |
| `codex:codex-primary-v0-v2-boundary:H029` | `codex:codex-primary-v0-v2-boundary:H031` | `triggered_rework` | H029 发起 loop 审计，H030 扩展 context-isolation 范围，H031 再要求独立 focus-drift 根因调查并形成审计产物。 |

## 4. 跨版本迁移边

| from_event_id | to_event_id | relation | 方向依据 |
|---|---|---|---|
| `codex:codex-primary-v0-v2-boundary:H008` | `codex:codex-primary-v0-v2-boundary:H009` | `caused` | H008 把 V0 归档、切回 LLM Wiki topic 并要求使用 `data/`；H009 紧接着把新 topic plan 从静态建议改为 planner 驱动的 V1 执行计划。 |

## 5. 默认选择与 all-events 保留

- V0 默认展示上表 11 个 `milestone=true` annotations；V1 默认展示 14 个。
- 未选中的用户输入仍按原顺序存在于 event shards，包括重复纠正、暂停、访问失败、周期追问、schema 简化、footnote/reference 权衡和 context-isolation 追加要求。因果边中的“经 all-events 中……”明确标出重要但未进入默认密度的中间 query。
- `codex:codex-retro-daily-audit:H001`、`codex:codex-retro-daily-audit:H002`、`codex:codex-retro-daily-audit:H003`、`codex:codex-retro-daily-audit:H004`、`codex:codex-retro-daily-audit:H005` 均保持在 V0/V1 all-events mode，默认 `milestone=false`。它们记录 2026-06-11 的后验时间线审计工程，不改变 2026-05-21 至 2026-05-24 的 V0/V1 产品因果主线，也不能作为原始执行证明。
- V0/V1 最终 capsule 的 `README.md`、`manifest.json` 和 `status.json` 只证明当前归档解释与产品状态；除明确标成 `retrospective` 的节点外，不把这些最终快照当作当时 worker 顺序、上下文隔离或 promotion 行为的证明。
- Git 首次整体保存 V0/V1 capsule 时已经是归档 snapshot；因此本文不从后续 Git appearance 推导 run 内部先后，也不把后来的路径迁移和设计文档倒写为原始机制。
