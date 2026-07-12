# V2-V3 查询级里程碑时间线策展

## 1. 范围与证据口径

本文为 `query-timeline` 展示层提议 V2、V3 的查询级里程碑（query-level milestones），不改写 registry。主时间依据是三组顶层、用户锚定事件：

- `docs/claude_interaction_replay/events/events.codex.primary-v2-boundary.v2.jsonl`
- `docs/claude_interaction_replay/events/events.codex.primary-v2-v3.v2.jsonl`
- `docs/claude_interaction_replay/events/events.claude.primary-v3.v2.jsonl`

每个注释保留归档中的完整 `event_id`。排序按事件的 `times.source_recorded_at`；同一事件中的用户输入说明触发条件，`assistant.summary/actions/observed_effects` 说明该输入后、下一条用户输入前可见的执行结果。

两版共提议 32 条注释、对应 31 个唯一事件；`codex:codex-primary-v2-v3-handoff:H033` 被有意同时放在 V2 的 `transition_out/handoff` 与 V3 的 `precursor/handoff`，因为它就是两版共享的桥接事件。

证据性质严格分为：

- `specified`：用户决定、合同、prompt 或设计明确规定；不自动证明执行。
- `executed`：primary event 明确记录动作及效果，并有同期或最终运行产物可以旁证。
- `observed_failure`：运行中断、用户看到的覆盖/成本失败，或机械执行虽成功但目标未满足。
- `contradicted`：后续一手检查或专项审计推翻此前流程假设、完成声明或指标含义。
- `retrospective`：执行后的解释、成本审计、流程复盘或 future plan；不能倒写为原始运行合同。

`milestone` 使用 query-timeline schema 的角色词：`origin`、`decision`、`action`、`challenge`、`correction`、`validation`、`failure`、`handoff`、`retrospective`。产物引用前缀表示其证据角色：`[S]` 为规范（specification），`[E]` 为运行产物（execution artifact），`[R]` 为复盘或审计（retrospective/audit）。当前目录中的最终修复快照只能证明最终状态；原始执行次序和当时机制仍以 primary events 为准。

## 2. V2 里程碑注释提议（16 条）

V2 的安全叙事是：先恢复事实卡、可读卡与 provenance 的基本契约，再用旧式逐卡链产出 15 张卡；吞吐反证随后触发 draft-first、Top-3、comparison provenance 和 scoped-card 设计。后半段设计在 V2 内没有端到端跑通，而是被固化并交接给 V3。

| # | event_id | phase | title | significance | kind | milestone | artifact_refs |
|---:|---|---|---|---|---|---|---|
| 1 | `codex:codex-primary-v0-v2-boundary:H020` | precursor / contract recovery | atomic card 恢复强事实校验 | 用户纠正“轻量校验”理解，重申 known fact / accepted fact 与强校验；这是 V2 事实层的入口约束，不证明后来的 scoped-card pipeline 已执行。 | `specified` | `correction` | - |
| 2 | `codex:codex-primary-v0-v2-boundary:H024` | precursor / card form | 卡必须是可读知识结果 | 用户同时指出目标漂移和文档不可读；card 应像 zet card，审计与过程信息应退出正文。 | `specified` | `correction` | - |
| 3 | `codex:codex-primary-v0-v2-boundary:H026` | precursor / provenance | 区分 card 结果与 provenance 过程 | 明确 card 是知识结果，provenance 是证明其可接受性的过程 artifact，audit 决定接受或拒绝；这成为后续逐卡链的逻辑基础。 | `specified` | `decision` | - |
| 4 | `codex:codex-primary-v0-v2-boundary:H046` | launch boundary | 确认无预设 topic | 核对 card 由 agent 从本地来源 bottom-up 探索，不按 hub、cluster 或 topic coverage 规划；该边界约束随后进入启动 prompt。 | `specified` | `validation` | `[S] loops/v2_llm_wiki_loop_20260525/plans/main_agent_long_horizon_execution_plan.md` |
| 5 | `codex:codex-primary-v0-v2-boundary:H048` | launch handoff | 形成可复制并审计的启动 prompt | 将来源挖掘、逐卡 drafting/audit/adoption、上下文隔离、失败驱动演化和停止条件交给下一 main-agent；这是可执行交接物，不是生产结果。 | `executed` | `handoff` | `[S] loops/v2_llm_wiki_loop_20260525/plans/main_agent_long_horizon_execution_plan.md` |
| 6 | `codex:codex-primary-v2-v3-handoff:H001` | original execution / source mining | 启动旧式逐卡生产链 | 新会话按 prompt 恢复 `READY_FOR_SOURCE_MINING`，选一个本地来源并派发 source-mining worker。此时主对象仍是 `atomic_fact_card`。 | `executed` | `action` | `[E] loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md` |
| 7 | `codex:codex-primary-v2-v3-handoff:H002` | original execution / failure-feedback | delivery marker 失败触发最小修复 | source mining 得到 12 个候选；第一张 drafting 因缺少完成标记未通过验收，随后修 prompt、独立审计并重跑。它证明 failure-feedback 实际发生，而非只写在 runbook。 | `observed_failure` | `correction` | `[E] loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0003_card_drafting_raw_sources_truth/loop_delivery.md`; `[E] loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/loop_delivery.md` |
| 8 | `codex:codex-primary-v2-v3-handoff:H003` | original execution / publication | 旧式链累计采纳 15 张卡 | 严格的 one-shot worker 与逐卡 draft→audit→adoption 链累计形成 15 张 loop-local accepted cards。它们先于 V2 scoped-card 合同，不能被倒写成新合同的执行结果。 | `executed` | `validation` | `[E] loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/`; `[R] loops/v2_llm_wiki_loop_20260525/reports/loop_report.md` |
| 9 | `codex:codex-primary-v2-v3-handoff:H004` | transition_out / throughput | 7 小时 15 卡成为吞吐反证 | 用户直接挑战产出速度；回复把成本定位到三段式 worker、细粒度落盘、频繁提交和过度串行。这个失败观察触发生产模型重构。 | `observed_failure` | `challenge` | `[R] loops/v2_llm_wiki_loop_20260525/reports/loop_report.md` |
| 10 | `codex:codex-primary-v2-v3-handoff:H005` | transition_out / draft-first origin | 提出先耗尽材料、后融合 | 用户提出 material→draft backlog，再做相似判断与融合；控制面开始形成 batch dispatch。但 V2 唯一新 backlog 卡最终仍停在 `similarity_pending`，所以这里只认定设计与部分脚手架执行。 | `specified` | `origin` | `[E] loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/`; `[E] loops/v2_llm_wiki_loop_20260525/queues/draft_backlog.md` |
| 11 | `codex:codex-primary-v2-v3-handoff:H006` | transition_out / fusion contract | comparison 三问与融合审计 | 用户纠正把 similarity 当决策的误解：相似候选后必须回答共同点、差异和下一步依据；merge/provenance delta 必须审计并留下 provenance 链。 | `specified` | `correction` | `[S] loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md` |
| 12 | `codex:codex-primary-v2-v3-handoff:H008` | transition_out / retrieval decision | Jieba/Jaccard Top-3 与信息密度 | 轻量召回收敛为标题分词、Jaccard、Top-3；同时用户否定“标题复述式 atomic card”，把信息密度和 bounded knowledge 提升为质量标准。 | `specified` | `decision` | `[S] loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md` |
| 13 | `codex:codex-primary-v2-v3-handoff:H010` | transition_out / card contract | 固定 metadata、自由正文、双层引用 | 决定 metadata 使用稳定模板，正文不设强模板；References 承担 card-level 来源，Footnotes 承担 inline locator。后来的 unified Footnotes 不能前置到此事件。 | `specified` | `decision` | `[S] loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md` |
| 14 | `codex:codex-primary-v2-v3-handoff:H023` | transition_out / design freeze | V2 scoped-card 设计正式固化 | 冻结旧控制面快照，正式写入 scoped card、Top-3、三问 comparison provenance 和 brain mailbox。这里证明设计被固化，不证明 15 张旧卡已迁移或新管线已跑完。 | `specified` | `decision` | `[S] loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md`; `[S] loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md`; `[E] loops/v2_llm_wiki_loop_20260525/loop_state.json` |
| 15 | `codex:codex-primary-v2-v3-handoff:H031` | transition_out / repository boundary | 区分 loop 候选 KB 与稳定产品 | 明确 `loops/<run>/outputs/llm_wiki/` 是实验候选，仓库根稳定 `llm_wiki/` 只有 human promotion 后才存在；因此 15 张卡是 loop-local publish，不是稳定 promotion。 | `specified` | `decision` | `[S] loops/v2_llm_wiki_loop_20260525/README.md` |
| 16 | `codex:codex-primary-v2-v3-handoff:H033` | handoff / V2→V3 | 建立 V3 draft-first capsule | 用户明确开启 V3；助手把 V2 后期设计转成独立 V3 scaffold、queues、reports 与 output skeleton。此事件是交接与规范，不是 V3 原始生产完成。 | `specified` | `handoff` | `[S] loops/v3_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE_V3.md`; `[S] loops/v3_llm_wiki_loop_20260525/SIMILARITY_MECHANISM_V3.md`; `[S] loops/v3_llm_wiki_loop_20260525/PROVENANCE_CONTRACT_V3.md` |

### V2 支持的因果边

| from_event_id | relation | to_event_id | 支持说明 |
|---|---|---|---|
| `codex:codex-primary-v0-v2-boundary:H024` | `caused` | `codex:codex-primary-v0-v2-boundary:H026` | card 必须可读且过程信息退出正文，直接促成 card / provenance / audit 三层分工。 |
| `codex:codex-primary-v0-v2-boundary:H046` | `validated` | `codex:codex-primary-v0-v2-boundary:H048` | 无预设 topic 与 card-first 边界被写入下一会话启动 prompt。 |
| `codex:codex-primary-v0-v2-boundary:H048` | `caused` | `codex:codex-primary-v2-v3-handoff:H001` | `H001` 是对前一事件产出的新会话 goal prompt 的实际启动。 |
| `codex:codex-primary-v2-v3-handoff:H001` | `caused` | `codex:codex-primary-v2-v3-handoff:H003` | 启动的 source-mining→逐卡链累计形成 15 张 loop-local accepted cards。 |
| `codex:codex-primary-v2-v3-handoff:H001` | `challenged` | `codex:codex-primary-v2-v3-handoff:H002` | 生命周期要求与 delivery failure 暴露旧控制面的高摩擦执行方式。 |
| `codex:codex-primary-v2-v3-handoff:H003` | `challenged` | `codex:codex-primary-v2-v3-handoff:H004` | “15 张已采纳”的结果直接触发“7 小时为何只有 15 张”的吞吐质疑。 |
| `codex:codex-primary-v2-v3-handoff:H004` | `triggered_rework` | `codex:codex-primary-v2-v3-handoff:H005` | 吞吐失败促成先批量 draft、后比较/融合的生产重排。 |
| `codex:codex-primary-v2-v3-handoff:H005` | `corrected` | `codex:codex-primary-v2-v3-handoff:H006` | 初版“相似后直接融合”被改为三问 comparison provenance 与审计门。 |
| `codex:codex-primary-v2-v3-handoff:H006` | `caused` | `codex:codex-primary-v2-v3-handoff:H008` | comparison gate 的候选召回问题，经讨论收敛为 Jieba/Jaccard Top-3。 |
| `codex:codex-primary-v2-v3-handoff:H008` | `caused` | `codex:codex-primary-v2-v3-handoff:H010` | “卡片不能只是标题复述”的信息密度要求推动 scoped-card contract 成形。 |
| `codex:codex-primary-v2-v3-handoff:H010` | `validated` | `codex:codex-primary-v2-v3-handoff:H023` | card/citation 合同与 similarity/fusion 规则被正式固化为 V2 设计文件。 |
| `codex:codex-primary-v2-v3-handoff:H023` | `caused` | `codex:codex-primary-v2-v3-handoff:H033` | V3 scaffold 明确继承 V2 后期的 scoped card、draft-first、Top-3 与 comparison provenance。 |
| `codex:codex-primary-v2-v3-handoff:H031` | `caused` | `codex:codex-primary-v2-v3-handoff:H033` | 稳定 capsule / candidate product 边界使 V3 能以独立 loop 目录启动，而不覆盖 V2。 |

## 3. V3 里程碑注释提议（16 条）

V3 的原始执行必须先展示：handoff→4 张首轮 draft→全量 171 drafts→comparison→interlinks→adoption。Citation/related 统一、成本审计、comparison corpus 反证和 questioning loop 都发生在其后；其中 questioning 是下一轮设计，不属于 171 张卡的生产机制。

| # | event_id | phase | title | significance | kind | milestone | artifact_refs |
|---:|---|---|---|---|---|---|---|
| 1 | `codex:codex-primary-v2-v3-handoff:H033` | handoff / precursor | V3 capsule 从 V2 后期设计中建立 | 建立 draft-first、Top-3、comparison provenance 和独立 output skeleton；它只证明交接规范存在，不证明 Claude 已执行。 | `specified` | `handoff` | `[S] loops/v3_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE_V3.md`; `[S] loops/v3_llm_wiki_loop_20260525/CONTEXT_BOUNDARY.md` |
| 2 | `claude_code:claude-primary-v3:H001` | execution / bootstrap | 首个正式 draft-first pass | Claude 按启动 prompt 处理一个 Karpathy 材料，产出 4 张 draft、4 份 provenance 和 4 份 similarity；明确禁止本 pass adoption/fusion。 | `executed` | `action` | `[S] loops/v3_llm_wiki_loop_20260525/LOOP_START_PROMPT.md`; `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 3 | `claude_code:claude-primary-v3:H002` | execution / coverage challenge | “为什么只有 4 张”暴露 pass 与全量目标差距 | 4 张符合首轮 1 material、2-5 cards 的合同，但不满足用户对 `data/raw` 全量消费的预期；这是覆盖目标失败，不是首轮合同失败。 | `observed_failure` | `challenge` | `[S] loops/v3_llm_wiki_loop_20260525/LOOP_START_PROMPT.md` |
| 4 | `claude_code:claude-primary-v3:H005` | execution / batch production | 72 个材料有状态，形成 171 张中文 draft | 在用户要求处理剩余材料并保持中文主语言后，43 个可读来源产出 171 drafts，22 个空源和 7 个上游阻塞被记账。该事件证明 draft-first 批处理真实执行。 | `executed` | `validation` | `[E] loops/v3_llm_wiki_loop_20260525/queues/material_queue.md`; `[E] loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/`; `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 5 | `claude_code:claude-primary-v3:H006` | execution / comparison | 为 171 drafts 生成 comparison provenance | 171 份 comparison 工件落盘并更新 bookkeeping。当时它被当作完整比较阶段；后续 `H026` 才证明候选语料只含 V2。 | `executed` | `action` | `[E] loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison/` |
| 6 | `claude_code:claude-primary-v3:H007` | execution / graph weave | publication 前补 974 条 related 边 | 所有 drafts 被人工/agent interlink，报告 0 dangling、0 orphan。该阶段是手工图治理，不是后来从 Footnotes 派生的 related。 | `executed` | `action` | `[E] loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/cards/`; `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 7 | `claude_code:claude-primary-v3:H008` | execution / interruption | publication gate 被 provider 额度中断 | fusion audit 与 publication gate 已启动，但 provider 错误中止本轮；因此不能把 `H008` 写成 adoption 完成。 | `observed_failure` | `failure` | `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 8 | `claude_code:claude-primary-v3:H009` | execution / loop-local publish | 恢复并采纳 171 张卡 | 次日 `continue` 后完成 171 cards/provenance 的 loop-local KB 写入、索引和 bookkeeping。这里只证明 capsule 内发布，不证明 root stable promotion。 | `executed` | `validation` | `[E] loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/`; `[E] loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/provenance/`; `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 9 | `claude_code:claude-primary-v3:H019` | post-publication redesign / citation | related 改为 Footnotes 派生 metadata | 经 `H011`-`H018` 讨论后，用户决定不再独立维护 related，而从可同时引用 raw source 与 knowledge card 的 Footnotes 派生。此时只是新设计决定。 | `specified` | `decision` | - |
| 10 | `claude_code:claude-primary-v3:H020` | post-publication migration / citation | 171 张 KB 卡执行 unified-citation 迁移 | 更新合同与派生脚本，并把 References、Footnotes 和 related 收敛为统一 citation graph。该迁移发生在 `H009` adoption 之后，不能作为原始 draft 合同。 | `executed` | `action` | `[S] loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`; `[S] loops/v3_llm_wiki_loop_20260525/tools/derive_metadata_from_footnotes.py`; `[R] loops/v3_llm_wiki_loop_20260525/reports/loop_report.md` |
| 11 | `claude_code:claude-primary-v3:H021` | retrospective / cost audit | 启动全程审计与 token 消耗审计 | 用户要求分别形成 journey、主题审计和成本审计；执行后留下完整性、边界、worker、decision quality 与 token consumption 报告。它们解释 V3，不是 V3 原始执行步骤。 | `retrospective` | `retrospective` | `[R] loops/v3_llm_wiki_loop_20260525/docs/v3_loop_journey.md`; `[R] loops/v3_llm_wiki_loop_20260525/audits/token_consumption_audit.md` |
| 12 | `claude_code:claude-primary-v3:H022` | retrospective / scaling failure | 高 KV cache 命中仍无法承受约 1200 RMB/轮 | 用户用后台成本反证“cache hit 高即可接受”的假设，并质疑 material→draft 是否真是最大成本。后续审计显示主要浪费来自同卡多阶段反复读写、adoption 与 late migration。 | `observed_failure` | `challenge` | `[R] loops/v3_llm_wiki_loop_20260525/audits/token_consumption_audit.md` |
| 13 | `claude_code:claude-primary-v3:H025` | retrospective / process correction | draft 进入 KB 前必须经过集合级加工 | 用户纠正“draft 直接入 card folder”的隐含流程，明确 duplication、internal link/footnote、metadata derive 与 fusion 都应位于 draft→KB 之间。该模型是执行后重构，不是原始 171-card pipeline。 | `contradicted` | `correction` | `[R] loops/v3_llm_wiki_loop_20260525/audits/loop_flow_expected_vs_actual_audit.md` |
| 14 | `claude_code:claude-primary-v3:H026` | retrospective / comparison failure | 审计确认 171 drafts 从未做 V3 self-comparison | 用户指出 comparison 不应只和 V2 跑；专项审计发现工具硬编码 V2 的 15-card index，comparison worker 又禁止读兄弟 drafts。`163 new + 8 delta + 0 merge` 因而不能证明 V3 无重复。 | `contradicted` | `failure` | `[R] loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`; `[S] loops/v3_llm_wiki_loop_20260525/tools/similarity_top3.py` |
| 15 | `claude_code:claude-primary-v3:H036` | retrospective / intent correction | 批处理是刻意策略，真正缺口是 set-level gate | 用户修正流程审计：批处理避免同一 material 重复消费，也避免预设 seed/root card；adoption 更像 schema 修补，失败点是批量生产后没有集合级 dedup/fusion。 | `retrospective` | `correction` | `[R] loops/v3_llm_wiki_loop_20260525/audits/loop_flow_expected_vs_actual_audit.md` |
| 16 | `claude_code:claude-primary-v3:H059` | future specification / questioning | 形成 building/evolving questioning loop 设计 | 在执行后对“单次阅读能否 exhaust material”的讨论中，三个设计 agent 形成 Mode A building 与 Mode B evolving 协议。它是 V4/future 的设计输入，绝不能放到 `H001`-`H009` 之前或用于证明 171 张卡采用 questioner↔reader。 | `specified` | `handoff` | `[S] loops/v3_llm_wiki_loop_20260525/future_plans/questioning_loop_design.md` |

### V3 支持的因果边

| from_event_id | relation | to_event_id | 支持说明 |
|---|---|---|---|
| `codex:codex-primary-v2-v3-handoff:H033` | `caused` | `claude_code:claude-primary-v3:H001` | V3 capsule 与启动合同被交给无历史上下文的 Claude，并在 `H001` 执行首轮。 |
| `claude_code:claude-primary-v3:H001` | `challenged` | `claude_code:claude-primary-v3:H002` | 首轮仅 4 张的可见结果直接触发全量覆盖质疑。 |
| `claude_code:claude-primary-v3:H002` | `triggered_rework` | `claude_code:claude-primary-v3:H005` | 覆盖质疑与“处理剩余材料”指令促成 72-material 批处理及 171 drafts。 |
| `claude_code:claude-primary-v3:H005` | `caused` | `claude_code:claude-primary-v3:H006` | 全量 drafts 成为 171 份 comparison provenance 的输入集合。 |
| `claude_code:claude-primary-v3:H006` | `caused` | `claude_code:claude-primary-v3:H007` | comparison 完成后，用户要求 publication 前补 interlinks。 |
| `claude_code:claude-primary-v3:H007` | `caused` | `claude_code:claude-primary-v3:H008` | interlink 完成后进入 fusion/publication gate，随后发生 provider 中断。 |
| `claude_code:claude-primary-v3:H008` | `triggered_rework` | `claude_code:claude-primary-v3:H009` | 中断后的 `continue` 恢复 adoption，并完成 171 张 loop-local 发布。 |
| `claude_code:claude-primary-v3:H009` | `challenged` | `claude_code:claude-primary-v3:H019` | 发布后的 link 追问（中间事件 `H011`-`H018`）最终挑战手工 related 与双引用机制，收敛为 Footnotes 事实源。 |
| `claude_code:claude-primary-v3:H019` | `caused` | `claude_code:claude-primary-v3:H020` | related-from-Footnotes 决定触发合同、脚本和 171 张卡的迁移。 |
| `claude_code:claude-primary-v3:H020` | `caused` | `claude_code:claude-primary-v3:H021` | late migration 与完整 V3 快照成为全程 journey、完整性和 token audit 的审计对象。 |
| `claude_code:claude-primary-v3:H021` | `challenged` | `claude_code:claude-primary-v3:H022` | token audit 结果引出“高 cache hit 仍不可扩展”的成本追问。 |
| `claude_code:claude-primary-v3:H022` | `triggered_rework` | `claude_code:claude-primary-v3:H025` | 对重复读写成本的追问推动 draft→KB 阶段重新排序。 |
| `claude_code:claude-primary-v3:H025` | `contradicted` | `claude_code:claude-primary-v3:H026` | 一旦要求 duplication/fusion 位于准入前，现有 comparison 语料错误立即成为阻断性反证。 |
| `claude_code:claude-primary-v3:H026` | `corrected` | `claude_code:claude-primary-v3:H036` | corpus 审计后，用户进一步纠正“批处理本身有错”的复盘，把缺口精确定位为 set-level dedup/fusion gate。 |

## 4. V2→V3 跨版本桥接边

| from_event_id | relation | to_event_id | 支持说明 |
|---|---|---|---|
| `codex:codex-primary-v2-v3-handoff:H004` | `triggered_rework` | `codex:codex-primary-v2-v3-handoff:H033` | V2 的 7 小时/15 卡吞吐反证，经 `H005`-`H023` 的 draft-first、Top-3、comparison 与 card-contract 讨论，最终触发 V3 scaffold。 |
| `codex:codex-primary-v2-v3-handoff:H023` | `caused` | `claude_code:claude-primary-v3:H001` | V2 末期固化的 scoped-card/draft-first 规范，经 `H033`-`H044` handoff 转成 V3 首轮执行合同。 |
| `codex:codex-primary-v2-v3-handoff:H031` | `validated` | `claude_code:claude-primary-v3:H009` | V3 的 171 张卡仍写入 loop capsule，而非 root stable product，验证了 candidate publication / human promotion 边界。 |
| `codex:codex-primary-v2-v3-handoff:H008` | `caused` | `claude_code:claude-primary-v3:H006` | V2 选定的 Jieba/Jaccard Top-3 与三问比较机制在 V3 被规模化执行；`H026` 随后反证的是 comparison corpus，而不是“171 份 comparison 文件是否生成”。 |

## 5. 不得倒写的边界

1. V2 的 15 张 accepted cards 是旧式逐卡链的执行结果；`CARD_CONTRACT_V2.md` 与 `LOOP_DESIGN_V2.md` 是其后固化的设计。不得用最终 V2 快照声称 15 张卡已经执行 scoped-card metadata、Top-3 或 comparison/fusion。
2. V3 `H001`-`H009` 的真实顺序是 draft→cross-version comparison→手工 related→loop-local adoption。当前 KB 的 unified Footnotes 与 citation-derived related 来自 `H019`-`H020` 的发布后迁移。
3. `H006` 证明 171 份 comparison provenance 被执行；`H026` 证明它们只比较 V2 的 15 张卡、没有 intra-V3 comparison。二者同时成立，后者不抹除文件生成事实，前者也不能证明 dedup/fusion coverage。
4. `merge_candidate=0` 是错误候选语料下的观察值，不是“V3 不存在重复”的验证。comparison corpus drift audit 估计的重复簇属于复盘发现。
5. `H021` 之后的 token、flow、integrity audits 是复盘证据；约 10M token、adoption/migration 排名和可节省空间不能被写成原运行时预算或预先 gate。
6. `H025`、`H036` 的 Fork/Weave/Derive 与 set-level gate 是执行后的流程重构；它们解释 V3 缺口，不是原始 adoption 的合同。
7. `H059` 的 questioner↔reader、Mode A/Mode B 与后续 reviewer/JJ/typed-footnote 设计属于 future/V4 specification。它们不能出现在 V3 原始执行之前，也不能为 171 张 V3 cards 的 extraction 质量背书。
8. V2、V3 都只完成 loop-local candidate publication；最终 outputs、version docs 或 replay registry 不能替代一次未发生的 root stable promotion。
