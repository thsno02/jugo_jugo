# LLM Wiki V2-V3 审计机制证据审计

## 1. 范围与证据规则

本文只审计 V2-V3 的审计机制（audit mechanism），并把证据映射到七个稳定阶段：

1. `audit-contract`
2. `mechanical-filter`
3. `shard-judge`
4. `synthesize-verdict`
5. `adversarial-probe`
6. `root-cause-audit`
7. `remediation-experiment`

同时评估十项控制：`source-eligibility`、`source-faithfulness`、`inference-boundary`、`schema-validity`、`fusion-boundary`、`graph-integrity`、`cross-source-leakage`、`state-consistency`、`pipeline-conformance`、`knowledge-depth`。

事实状态严格区分如下：

- **specified**：合同、task、prompt、skill 或设计文档规定了控制，但没有充分证据证明该控制按规定执行。
- **executed**：primary event 明确报告动作或结果，并有同阶段运行产物支撑。这里仍是运行期报告（reported execution），不是隐藏工具调用日志。
- **observed_failure / contradicted**：用户、运行产物或后验审计给出反证，说明控制失败、漏检或合同与执行不一致。
- **retrospective**：执行后形成的审计、修订合同、future plan、回放事件或本次只读核对；能解释终态和根因，不能倒写为原始执行。

三条证据限制贯穿全文：

1. V2 当前的 `loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md`、`loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md` 和 `loops/v2_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE.md` 是 15 张卡生产后形成的设计，不证明 15 张卡按这些合同生产或审计。
2. V3 当前 171 张 KB cards 是 2026-05-28 unified-citation 迁移后的终态；`pipeline_integrity_audit.md` 验证的是该后期快照，不证明 2026-05-26 的 drafts 或 2026-05-27 的 publication gate 已采用最终合同。
3. V3 后期的 token、decision、pipeline、comparison-corpus 和 expected-vs-actual 审计属于复盘。它们不能被当作 adoption 前已运行的 gate。

事件使用完整 `event_id`；artifact 均使用仓库相对路径。Replay 目录在本次审计时整体仍是未跟踪工作树内容，因此事件归档是当前回放证据，不是既有 Git 提交本身。

## 2. 结论摘要

### 2.1 V2：真实运行的是逐卡独立审计，不是后期 V2 合同

V2 的实际审计主链是单来源候选的逐卡 `draft -> card_audit_worker -> adoption`。`codex:codex-primary-v2-v3-handoff:H003` 报告累计采纳并推送 15 张卡；仓库保留 16 份 card audit report，其中 15 次最终 `pass`，另有一次 `revise` 后重写、复审再 `pass`。最强的闭环样例是：

- 初审 `revise`：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`
- 修订后复审 `pass`：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/artifacts/audit_report.md`
- 最终采纳：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0056_card_adoption_idea_file_agent_builds/loop_delivery.md`

该旧链对单卡的来源支撑、范围、事实类型、可读性和 References/Footnotes 顺序做了真实判断；它没有独立机械全量初筛、集合级分片、全 KB 综合 verdict、图审计或融合审计。`codex:codex-primary-v2-v3-handoff:H004` 至 `codex:codex-primary-v2-v3-handoff:H010` 在吞吐与信息量质疑后才提出 batch drafts、Top-3、comparison 三问、scoped knowledge card 和 provenance/fusion 审计；`codex:codex-primary-v2-v3-handoff:H023` 才把它们固化为 V2 设计。V2 自身没有跑完这套后期合同。

### 2.2 V3：真实执行了 publication/fusion checks，后期才做过程审计

V3 的实际发布门禁由 `loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md` 定义：163 张 `new_card` 走 6 项 `publication_gate`，8 张 `provenance_delta` 走 4 项 `fusion_audit`。`claude_code:claude-primary-v3:H008` 记录启动后因 provider 额度中断，`claude_code:claude-primary-v3:H009` 记录恢复并完成 171 张卡与 provenance 的 loop-local adoption。运行报告给出 163/163 publication pass、8/8 fusion pass；accepted provenance 中保存 `gate` 块。

但 V3 当时没有形成 `mechanical-filter -> suspect shards -> semantic judge -> synthesize` 的 FSJS 闭环。adoption workers 直接按卡分批做 agent 判断，随后汇总为全通过。`claude_code:claude-primary-v3:H021` 才调用 sub-agent 生成 pipeline、decision、token、boundary、worker 和 hook/classifier 等专题审计；`claude_code:claude-primary-v3:H026`、`claude_code:claude-primary-v3:H027` 才发现并溯源 comparison corpus 问题；`claude_code:claude-primary-v3:H035`、`claude_code:claude-primary-v3:H036` 又形成 expected/contracted/executed 流程复盘。这些都是发布后的 retrospective audits。

### 2.3 V3 的 V2-only similarity corpus 是已确认且未回写修复的矛盾

V3 的 171/171 similarity JSON 全部只比较 V2 的 15 张 accepted cards。`loops/v3_llm_wiki_loop_20260525/tools/similarity_top3.py` 硬编码 `V2_INDEX`，comparison worker 又被禁止读取其他 V3 drafts。因此 163 `new_card`、8 `provenance_delta`、0 `merge_candidate` 只描述“V3 draft 对 V2 小语料”的判定，不是 V3 集合内 dedup/fusion 结果。

`claude_code:claude-primary-v3:H026` 明确指出 comparison 应与 V3 自身运行；`claude_code:claude-primary-v3:H027` 又确立每个 loop 独立 0->1、V3 不应依赖 V2。`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md` 将问题定性为 origin defect，并估计约 15-20 张 intra-V3 近重复。当前终态仍保留原 171 similarity、171 comparison、8 个 `v2_anchor` 和 V2 footnotes；修复方案被写入审计和 future plans，但 V3 corpus 没有重跑，故状态是 **contradicted + retrospective diagnosis，remediation not executed**。

## 3. 七阶段稳定映射

| 稳定阶段 | V2 | V3 | 证据判定 |
|---|---|---|---|
| `audit-contract` | **executed（旧逐卡合同）**：每个 audit task 限定 draft、provenance、原始来源、JSON pointer/候选，并逐项检查主要事实、source support、fact type、scope、可读性和 section 顺序。后期 scoped-card、Top-3、fusion 合同仅 **specified**。 | **executed（发布合同）**：adoption prompt 定义 6 项 publication gate 与 4 项 fusion audit。unified-citation、self-only comparison、Fork/Weave/Derive 和 JJ/reviewer 合同均为后期修订或 future design。 | V2：`codex:codex-primary-v0-v2-boundary:H048`、`codex:codex-primary-v2-v3-handoff:H003`、`codex:codex-primary-v2-v3-handoff:H008` 至 `codex:codex-primary-v2-v3-handoff:H010`、`codex:codex-primary-v2-v3-handoff:H023`；`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md`。V3：`claude_code:claude-primary-v3:H008`、`claude_code:claude-primary-v3:H009`、`claude_code:claude-primary-v3:H019`、`claude_code:claude-primary-v3:H025`、`claude_code:claude-primary-v3:H057` 至 `claude_code:claude-primary-v3:H079`；`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`。 |
| `mechanical-filter` | **not executed as a distinct stage**：格式、字段与 section 顺序由每个 audit agent 手工检查；没有先全量脚本扫描再输出 suspect list。 | **not executed before publication as a distinct stage**：interlink 阶段报告 974 edges、0 dangling、0 orphan，adoption agents 检查字段；但系统化计数/schema/悬挂核对由发布后的 pipeline integrity audit 完成。 | V2 的 audit reports 是语义报告，不是机械 filter 工件。V3：`claude_code:claude-primary-v3:H007`、`claude_code:claude-primary-v3:H021`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md` 是 retrospective。 |
| `shard-judge` | **executed in per-card isolation, without prior filter**：每张卡由 fresh `card_audit_worker` 读一个窄 task packet 并给 `pass/revise/reject`；这是 card shard + semantic judge，但不是 suspect-driven shard。 | **executed as publication batches, not FSJS**：5 个 publication workers 审 163 张，1 个 fusion worker 审 8 张；没有机械 suspect manifest，也没有逐 suspect 的统一 judge ledger。 | V2：`codex:codex-primary-v2-v3-handoff:H003`；`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/skills/llmwiki-card-audit/SKILL.md`；16 份精确 report 路径见 §5.2。V3：`claude_code:claude-primary-v3:H009`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`；`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`。 |
| `synthesize-verdict` | **partial**：每卡 verdict 与 main-agent adoption 已执行；没有 15 卡的统一质量 verdict 或分母化控制报告。 | **executed, but over-broad**：运行报告综合为 163/163 publication pass、8/8 fusion pass、171 accepted。该 verdict 对单卡门禁成立，但没有覆盖 intra-V3 dedup；后期 comparison audit 推翻了“0 merge 可代表无重复”的隐含解读。 | V2：各 audit report + adoption delivery。V3：`claude_code:claude-primary-v3:H009`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`；`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`。 |
| `adversarial-probe` | **executed by user feedback**：`codex:codex-primary-v2-v3-handoff:H004` 以“7 小时 15 卡”挑战吞吐；`codex:codex-primary-v2-v3-handoff:H008` 检查并指出部分卡正文只是标题复述、信息量不足。它们不是预设 audit control，而是用户反证。 | **executed after publication**：`claude_code:claude-primary-v3:H010` 复核 3 个 similarity misses；`claude_code:claude-primary-v3:H011` 至 `claude_code:claude-primary-v3:H020` 追问 interlink/citation 语义；`claude_code:claude-primary-v3:H022` 至 `claude_code:claude-primary-v3:H025` 追问成本与加工顺序；`claude_code:claude-primary-v3:H026` 直接指出 comparison corpus 错位。 | 证据均为本行完整 event_id。 |
| `root-cause-audit` | **partial retrospective**：吞吐被归因于三段 worker、细粒度落盘、频繁提交和过度串行；另有 sub-agent lifecycle、task boundary、task flow audits，但没有针对 15 卡质量做统一根因审计。 | **executed retrospectively**：`claude_code:claude-primary-v3:H021` 的六类审计解释 token、dispatch、boundary、pipeline 与 decision；`claude_code:claude-primary-v3:H026`、`claude_code:claude-primary-v3:H027` 锁定 V2-only corpus；`claude_code:claude-primary-v3:H035`、`claude_code:claude-primary-v3:H036` 区分 corrected ideal、as-contracted 和 as-executed。 | V2：`codex:codex-primary-v2-v3-handoff:H004`、`codex:codex-primary-v2-v3-handoff:H013`；`loops/v2_llm_wiki_loop_20260525/audits/20260525-control-plane-subagent-task-audit/`。V3：`loops/v3_llm_wiki_loop_20260525/audits/`。 |
| `remediation-experiment` | **partial / handed off to V3**：一张 batch draft 被派发，但 V2 backlog 仍为 `similarity_pending`；真正的 draft-first 规模实验在 V3 执行。 | **mixed**：3 个 similarity misses 被 recheck 并维持原判；unified-citation migration 已执行；classifier 失败由 agent fallback 补齐。V2-only corpus 只有修复方案，没有重跑 self-comparison、去污染或 merge。 | V2：`codex:codex-primary-v2-v3-handoff:H005` 至 `codex:codex-primary-v2-v3-handoff:H010`、`codex:codex-primary-v2-v3-handoff:H023`；`loops/v2_llm_wiki_loop_20260525/queues/draft_backlog.md`。V3：`claude_code:claude-primary-v3:H010`、`claude_code:claude-primary-v3:H020`、`claude_code:claude-primary-v3:H027`；`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`。 |

## 4. 十项控制评估

状态词：**strong** 表示有直接运行证据；**partial** 表示只覆盖部分风险或只有报告性证据；**absent** 表示原运行没有该控制；**contradicted** 表示控制结论被后续反证。

| 控制 | V2 | V3 | 关键证据与边界 |
|---|---|---|---|
| `source-eligibility` | **strong per-card**：task 精确限定一个本地 source、一个 JSON pointer/行段和一个 fact candidate，禁止其他输入。 | **partial-to-strong queue eligibility**：72 materials 均有状态，43 readable、22 empty、7 upstream blocked；publication gate 要求非空 `source_ids` 与具体源引用。缺少完整逐材料 access log，不能重放所有实际 read。 | V2：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md`。V3：`claude_code:claude-primary-v3:H005`；`loops/v3_llm_wiki_loop_20260525/queues/material_queue.md`；`loops/v3_llm_wiki_loop_20260525/source_access_log.jsonl`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md` §9（retrospective）。 |
| `source-faithfulness` | **strong at card scope**：audit agent 读取 raw evidence，逐卡判断 statement/support；一次不受 pointer 支撑的作者归属被判 `revise`。 | **partial**：publication gate 检查“至少一个具体引用片段”，后期 decision audit 抽样 8/8 源支撑充分；没有 171 张逐 claim entailment ledger，最终 integrity audit 主要检查 marker/schema，不证明语义忠实。 | V2：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`、`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/artifacts/audit_report.md`。V3：`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/audits/decision_quality_audit.md`（retrospective sample）。 |
| `inference-boundary` | **strong at old schema**：`fact_type`、`scope`、`support` 必审；禁止用未列 KB/草稿/父上下文补事实，作者归属案例证明 gate 会收缩推断。 | **weak/partial**：production 与 comparison 有读取边界，gate 检查 source support 和知识密度，但没有 explicit says-vs-implies、hedge preservation 或 inference label。`provenance_delta` 还允许“新边界但无新源”的解释升级。 | V2：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md` 与上述两轮 report。V3：`loops/v3_llm_wiki_loop_20260525/CONTEXT_BOUNDARY.md`；`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/audits/decision_quality_audit.md` §6.3（retrospective）。 |
| `schema-validity` | **partial**：每卡人工检查旧字段和 References/Footnotes 顺序；没有 parser/schema 全量 gate。15 张卡不符合后期 V2 metadata contract，不能用最终合同宣称通过。 | **executed then contract-changed**：5 月 27 gate 检查必填字段、References、Footnotes、非空 related；5 月 28 最终合同删除 References、允许 4 张空 related。后期 integrity audit 证明迁移终态一致，不证明原 gate 使用最终 schema。 | V2：`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/skills/llmwiki-card-audit/SKILL.md`；`loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md`。V3：`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md`。 |
| `fusion-boundary` | **absent in executed 15-card chain; late specified**：Top-3、三问、`merge_candidate/provenance_delta` 和 fusion audit 在吞吐质疑后形成，V2 无 comparison/fusion ledger。 | **executed cross-version, contradicted intra-version**：8 个 V2 provenance deltas 经 fusion audit；没有 V3-vs-V3 candidate、merge 或 duplicate decision。V2 side 因写入边界未回链。 | V2：`codex:codex-primary-v2-v3-handoff:H006` 至 `codex:codex-primary-v2-v3-handoff:H008`、`codex:codex-primary-v2-v3-handoff:H023`；`loops/v2_llm_wiki_loop_20260525/queues/draft_backlog.md`。V3：`claude_code:claude-primary-v3:H006`、`claude_code:claude-primary-v3:H009`、`claude_code:claude-primary-v3:H026`；`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`。 |
| `graph-integrity` | **absent**：旧 15 卡没有后期 `related` graph；只有 provenance/card 路径与 index。 | **strong structural, weak decision lineage**：第一代 agent interlink 报告 974 edges、0 dangling、0 orphan；第二代把 KB links 放进 Footnotes 并派生 related。后期 integrity audit 验证终态，但 974 条初始边没有逐边 decision ledger，draft 与 KB 图属于不同世代。 | `claude_code:claude-primary-v3:H007`、`claude_code:claude-primary-v3:H019`、`claude_code:claude-primary-v3:H020`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`；`loops/v3_llm_wiki_loop_20260525/tools/derive_metadata_from_footnotes.py`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md`。 |
| `cross-source-leakage` | **strong preventive boundary**：禁止父上下文、旧审计、其他来源、其他候选、KB cards 和其他 drafts；`read_log.md` 记录实际读取。没有另一个 semantic leakage audit，但暴露面很窄。 | **partial**：material workers、comparison workers 与 adoption workers有读取白名单；但没有发布前的 semantic leakage control。V2 cards 被合同有意引入 similarity/fusion，按后来的 loop 独立性原则又成为 cross-loop contamination。 | V2：`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md`、`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/read_log.md`。V3：`loops/v3_llm_wiki_loop_20260525/CONTEXT_BOUNDARY.md`；`loops/v3_llm_wiki_loop_20260525/task_templates/comparison_worker_prompt.md`；`claude_code:claude-primary-v3:H027`。 |
| `state-consistency` | **partial-to-strong iteration state**：每轮有 task/status/delivery/read_log，main-agent 按 verdict 决定 adoption；路径与 delivery-marker 缺口曾触发修复。没有统一卡集审计状态。 | **strong final snapshot, retrospective proof**：后期 integrity audit 复算六类 171 计数并与 `loops/v3_llm_wiki_loop_20260525/loop_state.json` 一致；`claude_code:claude-primary-v3:H008` 中断后 `claude_code:claude-primary-v3:H009` 恢复。最终状态不能证明每个中间 transition 都一致，Git bookkeeping 还曾被 classifier 阻塞。 | V2：`codex:codex-primary-v2-v3-handoff:H002`、`codex:codex-primary-v2-v3-handoff:H003`。V3：`claude_code:claude-primary-v3:H021`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md`；`loops/v3_llm_wiki_loop_20260525/audits/hook_and_classifier_audit.md`。 |
| `pipeline-conformance` | **strong for old chain, contradicted for late V2 design**：15 cards 确实按逐卡链运行；batch/Top-3/scoped-card pipeline 未在 V2 闭环。 | **mixed / contradicted**：draft-first、comparison、interlink、adoption 确实依次执行；但合同从起点允许 V2-only base，未定义 intra-V3 dedup，adoption 后又做 citation migration。后期流程审计将缺口定位到设计合同而非 worker 漏做。 | V2：`codex:codex-primary-v2-v3-handoff:H003` 至 `codex:codex-primary-v2-v3-handoff:H005`、`codex:codex-primary-v2-v3-handoff:H023`。V3：`claude_code:claude-primary-v3:H001`、`claude_code:claude-primary-v3:H005` 至 `claude_code:claude-primary-v3:H009`、`claude_code:claude-primary-v3:H020`、`claude_code:claude-primary-v3:H035`、`claude_code:claude-primary-v3:H036`；`loops/v3_llm_wiki_loop_20260525/audits/loop_flow_expected_vs_actual_audit.md`。 |
| `knowledge-depth` | **contradicted**：旧 audit 检查“单一事实、可读、zet 风格”，但没有检验删除标题后正文是否仍提供机制/边界；`codex:codex-primary-v2-v3-handoff:H008` 后发现部分卡只是标题复述、过度 atomic。后期 scoped-card 合同是修正，不是原审计成功证据。 | **executed as publication criterion, retrospectively sampled**：gate 要求不是标题复述、至少若干机制/边界/反例/操作规则及三段 substantive 中文；163/163 报告通过，后期 8-card sample 8/8 通过，`claude_code:claude-primary-v3:H042` 表示用户可接受 V3 粒度。仍无 171-card 独立深度审计。 | V2：`codex:codex-primary-v2-v3-handoff:H008` 至 `codex:codex-primary-v2-v3-handoff:H010`。V3：`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/audits/decision_quality_audit.md`（retrospective sample）。 |

## 5. V2 实际逐卡审计的证据边界

### 5.1 实际执行合同

`codex:codex-primary-v0-v2-boundary:H046`、`codex:codex-primary-v0-v2-boundary:H047`、`codex:codex-primary-v0-v2-boundary:H048` 先规定 bottom-up、非 hub、draft 必须审计后才能交付。`codex:codex-primary-v2-v3-handoff:H001` 启动 source-mining -> drafting -> audit -> adoption；`codex:codex-primary-v2-v3-handoff:H002` 报告 delivery marker 缺口触发 prompt repair 与独立审计；`codex:codex-primary-v2-v3-handoff:H003` 报告累计 15 张 accepted cards。

以 candidate 3 为例，`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/task.md` 同时规定：

- 允许输入只有一张 draft、一份 provenance、`raw.json` 的 `$.tweet.text`、candidate 3；
- 禁止父聊天、旧 audit、其他来源、其他 candidate、其他 KB/draft；
- 必须检查主要事实、source support、`fact_type`、`scope`、`support`、provenance、可读性与 section 顺序；
- 只允许写本次 iteration 的 status/delivery/read_log/audit report。

初审抓到 statement 中“Karpathy 的发布帖”无法由允许的 `$.tweet.text` 证明，给出 `revise`；修订把它收缩为“这条发布帖”，复审 `pass`。这是 V2 对 `source-faithfulness + inference-boundary + remediation` 的直接执行证据，而不是设计文档推断。

### 5.2 16 份 audit reports 与 15 张 accepted cards

V2 保存以下 16 份 card audit reports；多出的一份正是 candidate 3 的 revise/re-audit：

1. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/artifacts/audit_report.md`
2. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0010_card_audit_architecture_layers/artifacts/audit_report.md`
3. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0016_card_audit_schema_layer/artifacts/audit_report.md`
4. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0019_card_audit_wiki_layer/artifacts/audit_report.md`
5. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0022_card_audit_persistent_wiki_mode/artifacts/audit_report.md`
6. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0025_card_audit_rag_no_accumulation/artifacts/audit_report.md`
7. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0028_card_audit_ingest_workflow/artifacts/audit_report.md`
8. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0031_card_audit_query_workflow/artifacts/audit_report.md`
9. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0034_card_audit_persistent_composite_wiki/artifacts/audit_report.md`
10. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/artifacts/audit_report.md`
11. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0042_card_audit_human_llm_roles/artifacts/audit_report.md`
12. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0049_card_audit_llm_wiki_use_cases/artifacts/audit_report.md`
13. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`
14. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0055_card_audit_idea_file_agent_builds_r1/artifacts/audit_report.md`
15. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0058_card_audit_idea_file_abstract_vague/artifacts/audit_report.md`
16. `loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0061_card_audit_wiki_health_checks/artifacts/audit_report.md`

这组文件证明的是 **per-card semantic audit**。它不证明机械脚本覆盖、集合级去重、graph integrity、全局 state synthesis 或后期 V2 schema。

### 5.3 后期 V2 合同不可回填为原执行

`codex:codex-primary-v2-v3-handoff:H004` 先指出 7 小时 15 卡吞吐过低；`codex:codex-primary-v2-v3-handoff:H005` 提议 material 先 exhaust 成 drafts；`codex:codex-primary-v2-v3-handoff:H006` 至 `codex:codex-primary-v2-v3-handoff:H008` 定义 similarity Top-3、comparison 三问与 fusion audit；`codex:codex-primary-v2-v3-handoff:H008` 至 `codex:codex-primary-v2-v3-handoff:H010` 又因“过度 atomic、标题复述”重定义 knowledge-depth 与 card schema；`codex:codex-primary-v2-v3-handoff:H023` 才正式固化 V2 设计。

对应后期 artifacts：

- `loops/v2_llm_wiki_loop_20260525/CARD_CONTRACT_V2.md`
- `loops/v2_llm_wiki_loop_20260525/LOOP_DESIGN_V2.md`
- `loops/v2_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE.md`
- `loops/v2_llm_wiki_loop_20260525/queues/draft_backlog.md`

V2 backlog 中唯一新式 batch candidate 仍为 `similarity_pending`，没有 V2 similarity/comparison/fusion artifact。安全表述是：“V2 真实执行了旧式逐卡审计，并在失败反馈后设计了下一代合同”；不能写成“V2 已用 Top-3 + fusion + scoped-card 审计 15 张卡”。

## 6. V3 publication checks 与后期审计的边界

### 6.1 发布前实际执行

V3 运行期主链的关键事件是：

| event_id | 运行事实 | 状态 |
|---|---|---|
| `claude_code:claude-primary-v3:H005` | 72 materials 全部有状态，43 个可读材料形成 171 张中文 drafts。 | executed |
| `claude_code:claude-primary-v3:H006` | 171 份 comparison provenance 落盘。 | executed |
| `claude_code:claude-primary-v3:H007` | publication 前补 974 条 related edges，报告 0 empty、0 dangling、0 orphan。 | executed, reported |
| `claude_code:claude-primary-v3:H008` | 启动 fusion audit 与 publication gate，随后 provider 额度错误中断。 | observed interruption |
| `claude_code:claude-primary-v3:H009` | 恢复后完成 171 张 cards/provenance 的 loop-local adoption。 | executed |
| `claude_code:claude-primary-v3:H010` | 复核 3 个 similarity misses，维持原判并补 recheck。 | remediation executed |

实际 gate 合同是 `loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`。它要求 new cards 检查知识密度、源支撑、References/Footnotes、frontmatter 和 non-empty related；要求 provenance deltas 回答三问、核对 V2 anchor body、保持 V2 scope、记录单向 provenance link。

同阶段证据包括：

- `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/provenance/mem0-extract-update-pipeline.md`
- `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/kb/provenance/karpathy-llm-kb-three-layer-arch.md`
- `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison/karpathy-llm-kb-three-layer-arch.md`
- `loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`

这些工件支持“gate 被报告执行、accepted provenance 保存 verdict”。它们不能证明存在发布前的机械全量 filter、suspect list 或独立集合级 judge。

### 6.2 发布后的 process/token/comparison audits

`claude_code:claude-primary-v3:H021` 才组织多主题审计，主要 artifacts 为：

- `loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md`
- `loops/v3_llm_wiki_loop_20260525/audits/decision_quality_audit.md`
- `loops/v3_llm_wiki_loop_20260525/audits/token_consumption_audit.md`
- `loops/v3_llm_wiki_loop_20260525/audits/boundary_compliance_audit.md`
- `loops/v3_llm_wiki_loop_20260525/audits/worker_dispatch_audit.md`
- `loops/v3_llm_wiki_loop_20260525/audits/hook_and_classifier_audit.md`

它们分别证明或估计最终计数/schema、抽样 decision quality、约 9.5-11M token 成本、写入边界、worker dispatch 与 fallback 成本。特别注意：

- `pipeline_integrity_audit.md` 的“全部通过”是 5 月 28 migration 后快照的结构完整性结论；它没有做 171 张 raw-source entailment，也没有发现 V3 sibling dedup 缺失。
- `decision_quality_audit.md` 的 8 张 KB cards、5 份 comparison、8 个 fusion decisions 抽样都通过，证明抽样单卡判断质量高；它不能外推为 171 张全量 semantic pass，更不能替代 set-level dedup audit。
- `token_consumption_audit.md` 与 `hook_and_classifier_audit.md` 解释成本和 fallback，是过程复盘，不是 publication acceptance control。

`claude_code:claude-primary-v3:H035`、`claude_code:claude-primary-v3:H036` 后形成的 `loops/v3_llm_wiki_loop_20260525/audits/loop_flow_expected_vs_actual_audit.md` 又把 corrected ideal、as-contracted、as-executed 分开，并确认 batch 是刻意的 material consumption 设计、adoption 更接近 schema 修补、真正缺口是 set-level dedup/fusion gate。这是 retrospective correction，不是原始合同。

### 6.3 最终 repaired snapshot 不证明原 publication execution

`claude_code:claude-primary-v3:H019` 决定 `related` 不应单独维护，而应从 Footnotes 派生；`claude_code:claude-primary-v3:H020` 才执行 unified-citation migration。最终：

- KB cards 删除 `## References`，统一使用 `## Footnotes`；
- 加入 504+ KB-internal footnotes；
- `related` 改为派生 metadata；
- 4 张只引 raw/URL 的卡合法保持 `related: []`。

但 5 月 27 adoption gate 要求 References 存在且 related 非空。两者是不同 schema 世代：

- 原 publication contract：`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`
- 后期 final contract：`loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`
- migration 规则：`loops/v3_llm_wiki_loop_20260525/tools/derive_metadata_from_footnotes.py`
- migration 运行事实：`claude_code:claude-primary-v3:H020`、`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`

脚本本身还被 classifier 阻塞，最终 171 张 related 更新由 fresh agent 用 Read+Edit fallback 完成。因此“当前终态符合派生规则”不等于“脚本在原运行中成功执行”，更不等于“publication gate 当时使用最终 schema”。

## 7. V2-only similarity corpus 矛盾

### 7.1 原始 specified 状态

V3 起始合同把 V2 accepted index 设为 bootstrap comparison base，直到 V3 有自己的 accepted index：

- `loops/v3_llm_wiki_loop_20260525/DRAFT_FIRST_PIPELINE_V3.md`
- `loops/v3_llm_wiki_loop_20260525/RUNBOOK.md`
- `loops/v3_llm_wiki_loop_20260525/LOOP_START_PROMPT.md`
- `loops/v3_llm_wiki_loop_20260525/CONTEXT_BOUNDARY.md`

所以 V2-as-base 不是 worker 私自越界，而是初始合同缺陷。后来的 loop 独立性原则重新判定它“从写下时就是 bug”，不能把后期原则伪装成原合同。

### 7.2 实际 executed 状态

`loops/v3_llm_wiki_loop_20260525/tools/similarity_top3.py` 的唯一比较常量是 V2 index；没有参数、V3 index 或 draft-vs-draft loop。171 个 similarity JSON 位于 `loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/similarity/`，且均满足：

- `comparison_base` = V2 card index；
- `comparison_base_card_count` = 15；
- Top-3 candidate paths 全部指向 V2 cards。

`loops/v3_llm_wiki_loop_20260525/task_templates/comparison_worker_prompt.md` 又要求 worker 只读 similarity 指定的 V2 Top-3，并禁止读其他 drafts。171 份 comparison 的决策分布是 163 `new_card`、8 `provenance_delta`、0 `merge_candidate`。因此：

- Top-3 mechanics：**executed 171/171**；
- cross-version comparison ledger：**executed 171/171**；
- intra-V3 duplication/fusion：**not executed**；
- “0 merge 证明 V3 无重复”：**contradicted**。

### 7.3 反证、根因与修复状态

`claude_code:claude-primary-v3:H026` 是直接反证：用户指出 comparison 应与 V3 自身运行并要求审计。`claude_code:claude-primary-v3:H027` 进一步要求溯源和下一 loop 防复发。`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md` 给出：

- V2 依赖在 V3 合同和工具诞生初期即进入，不是 late drift；
- batch parallelism 消除了“稍后自动切到累积 V3 index”的自然时刻；
- 切换承诺从未实现为代码；
- comparison contract 从未把 intra-V3 dedup 写成独立任务；
- 最强反例是 4 张围绕同一三层架构的 V3 cards，单卡均可解释为 V2 delta，但彼此从未比较。

修复方案包括 self-only corpus、显式 all-pairs/candidate pass、允许 comparison worker 读取 sibling Top-k、删除 V2 anchors 和跨 loop footnotes。然而当前 V3 outputs 没有重跑或去污染。`claude_code:claude-primary-v3:H027` 之后的审计和 future plans 是 **specified remediation**，不是 **executed remediation**。

## 8. 演化判断

V2 到 V3 的真实进步不是“FSJS 已经成熟”，而是审计对象从单卡正确性扩展到发布准入与跨工件一致性：

1. V2 证明了窄上下文、逐卡 source-grounded judge 和 revise/re-audit 闭环可工作。
2. V2 的吞吐与 knowledge-depth 反证促成 batch drafts、Top-3、comparison provenance 和更高信息密度合同，但这些大部分只在 V3 执行。
3. V3 把 publication checks 扩展到 171 张，并形成结构、decision、token、boundary、worker 和 pipeline 的后期审计面。
4. V3 仍缺少发布前的机械全量 filter、suspect-driven semantic shards、集合级 fusion judge 和多维 verdict；其最严重反例是 V2-only corpus 让“单卡都判得对”和“卡集存在重复”同时成立。
5. V3 后期形成的 questioning/reviewer/JJ/grep-first governance 与完整 pipeline contract，是从这些缺口推导出的下一版设计，不属于 V2/V3 原始执行。

因此按七阶段稳定模型，V2 是“窄 per-card judge + 局部 remediation”，V3 是“batch publication judge + post-hoc root-cause audits”；完整的 `contract -> mechanical filter -> shard judge -> synthesize -> adversarial probe -> root-cause -> remediation experiment` 闭环尚未在 V2 或 V3 单次运行中端到端成立。

## 9. 最小可复述事实集

1. V2 实际为 15 张 accepted cards 保存了 16 份逐卡审计报告；其中一张先 `revise`，修订后再 `pass`。这是 per-card semantic audit，不是后期 V2 Top-3/fusion 合同的执行证据。
2. V2 的 scoped-card、batch draft、Jieba/Jaccard Top-3、comparison 三问和 fusion audit 都是在吞吐与信息密度失败反馈后形成；V2 自身未闭环运行。
3. V3 确实执行 163 publication checks 与 8 fusion checks，并把 171 张卡发布到 loop-local KB；稳定 root KB promotion 未执行。
4. V3 发布前没有独立 mechanical filter 或 suspect-driven shard judge；pipeline/decision/token/boundary 等系统审计均在发布后形成。
5. V3 171/171 similarity 只比较 V2 的 15 张卡，V3 drafts 从未互比；`merge_candidate=0` 不能证明没有 V3 内部重复。
6. `claude_code:claude-primary-v3:H026`、`claude_code:claude-primary-v3:H027` 与 `loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md` 已确认并溯源该矛盾，但 current V3 outputs 没有执行 self-only 重跑或去污染。
7. V3 最终 unified-citation、footnote-derived related 和 integrity PASS 是后期迁移终态；它们不能证明 5 月 27 publication gate 使用了最终合同。
8. Questioner-reader、reviewer quit audit、Justification Journal 和 grep-first fusion 是 V3 后期为下一版形成的设计，不能作为 V2/V3 原始卡片质量背书。
