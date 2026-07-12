# V4 查询级里程碑时间线（提案）

> 状态：研究提案（proposal），供后续人工写入 `registry/query-timeline.json` 时使用；本文件本身不改 registry。

## 1. 范围与证据规则

- 主时间轴来自 `docs/claude_interaction_replay/events/events.claude.primary-v4.v2.jsonl` 的 59 条 user-anchored events，顺序采用归档中的 `sequence` / `times.source_recorded_at`。
- `docs/claude_interaction_replay/events/events.codex.retro-v4-v5-research.v2.jsonl` 仅作后验对照；其中 `codex:codex-retro-v4-v5-research:H001` 是 2026-06-15 的 V4/V5 风格归因研究，不是 V4 当时执行节点，因此不列入里程碑。
- **规定（specified）**：用户要求、启动 prompt 或设计文档说明了应当怎样运行；不代表对应机制实际进入 execution node。
- **执行（executed）**：归档 event 的 assistant window 记录了实际动作或同时期 Git 快照；只证明该窗口可见的执行范围。
- **观测失败/矛盾（observed_failure/contradicted）**：后续用户质疑、运行结果或审计反证了先前完成声明或设计假设。
- **复盘（retrospective）**：后续 audit、learnings、修复后文件或最终快照对早期运行作解释；不能倒填为原始执行证据。
- 当前 `loops/v4_llm_wiki_loop_20260602/task.md`、`learnings/*.md` 和 328-card KB 均为后验/修复后状态。它们只能证明终态或复盘认识，不能证明 H010 的 43-source 批次曾完整执行 questioning、reviewer、顺序 ingest 或 inline fusion。
- 数量必须按阶段读取：seed `15 -> 19`，原始 full batch `19 + 240 = 259`，post-hoc governance `259 -> 280`，局部 repo 修复约 `280 -> 295`，webpage 增量修复约 `295 -> 328`。**328 不是一次成功 run 的产量。**

## 2. 建议里程碑注释（20 条）

### 01. Seed：启动合同并完成 15-card 首轮

- `event_id`: `claude_code:claude-primary-v4:H001`
- 建议 `role`: `origin`; 证据状态：`specified` + `executed`
- `module_ids`: `ingestion`, `audit`
- 注释：启动要求引入 questioning、reader、reframing、reviewer；归档窗口可见 Karpathy gist 的分角色多轮问答、quit-audit、15 张 draft/accepted card 与 JJ。它证明 seed 角色结构真实运行，但 prompt 仅注入 skill 摘要，reframing 由 main agent 写文件，不能外推为全量四角色合同。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/LOOP_START_PROMPT.md`; `loops/v4_llm_wiki_loop_20260602/skills/questioning/SKILL.md`; `loops/v4_llm_wiki_loop_20260602/skills/reader/PROMPT.md`; `loops/v4_llm_wiki_loop_20260602/skills/reframing/PROMPT.md`; `loops/v4_llm_wiki_loop_20260602/skills/reviewer/PROMPT.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/drafts/cards/`
- 边界：同时期 Git `2df61ddb` 支持 seed 产物；当前 skill/task 文件可能含后续迭代，不是原始 prompt 的逐字快照。

### 02. Seed：质量返工后扩到 19 cards

- `event_id`: `claude_code:claude-primary-v4:H003`
- 建议 `role`: `validation`; 证据状态：`executed`
- `module_ids`: `ingestion`
- 注释：在 H002 的 ConnectionRefused 后，main agent 直接补 cross-links、aliases、脚注格式、拆卡和缺失主题，seed 从 15 增至 19；这是一轮 seed repair，不是 full batch。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/task.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards/`
- 边界：同时期 Git `1b92f941` 记录 `15 -> 19`；当前 card 目录是最终 328-card 快照，只能与 Git/event 联合使用。

### 03. Full batch：43-source 并行直写形成 259-card 快照

- `event_id`: `claude_code:claude-primary-v4:H010`
- 建议 `role`: `action`; 证据状态：`executed` + `contradicted`
- `module_ids`: `ingestion`
- 注释：43 个 extraction agents 报告 43/43 完成、240 张新增卡、KB 共 259 张。实际 prompt 把 reader/questioner/reframe 合并进单 agent，reviewer 缺席，输出直接写 accepted KB；所谓 Ingest 仅重建 index，不是顺序 promotion/fusion。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/task.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`
- 边界：同时期 Git `d36f6f7a` 支持 `43 materials -> 259 cards`；两份 learnings 是后验解释，且 `pipeline_actual.md` 中“主批次入库/完整管线”的表述不能覆盖归档中的 direct-publish 反证。

### 04. Path/governance failure：绝对路径与低链接暴露

- `event_id`: `claude_code:claude-primary-v4:H013`
- 建议 `role`: `failure`; 证据状态：`observed_failure`
- `module_ids`: `ingestion`, `audit`
- 注释：卡住状态调查确认 240/259 张卡使用绝对路径，V4 link coverage 约 45%，显著低于 V3；并行 extraction 与未落实的后置治理成为首个运行层根因。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md`
- 边界：artifact 是后续归因/量化；失败首次被观测的主证据是本 event，而不是修复后的零绝对路径终态。

### 05. Path/governance failure：纠正 related，并确认 fusion 缺席

- `event_id`: `claude_code:claude-primary-v4:H015`
- 建议 `role`: `correction`; 证据状态：`specified` + `contradicted`
- `module_ids`: `ingestion`, `audit`
- 注释：用户纠正“grep 命中即可 related”的错误理解：grep 只召回候选，agent 必须读卡判断 merge、related-but-distinct 或 keep，typed footnotes 才是关系依据。该追问同时确认顺序 ingest、inline fusion 与 evolve/governance judgment 没有在 full batch 落实。
- `artifact_refs`: `loops/v3_llm_wiki_loop_20260525/future_plans/fusion_and_governance.md`; `loops/v3_llm_wiki_loop_20260525/future_plans/pipeline_spec.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`
- 边界：V3 文档证明原合同（specified），H015 证明原合同与 H010 执行不一致；后来的补链不能把 full batch 改写成已执行 fusion。

### 06. Post-hoc fusion：37-cluster 补救生成 21 张 comparison cards

- `event_id`: `claude_code:claude-primary-v4:H016`
- 建议 `role`: `action`; 证据状态：`executed` + `retrospective`
- `module_ids`: `ingestion`
- 注释：发布后 governance 扩展到近义、反义/张力和跨域候选，运行 37 clusters，新增 card/distinction links 与 21 张 comparison cards，使 KB 从 259 到 280、264 张有链接。这是 **post-publication fusion/governance rescue**，不是 pre-promotion fusion。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/task.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards/comparison-incremental-vs-batch-ingest.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`
- 边界：同时期 Git `b26dafc3` 支持 280-card 补救快照；当前 task/cards 已含后续修复。

### 07. Post-hoc governance：取消 cluster 数量目标

- `event_id`: `claude_code:claude-primary-v4:H018`
- 建议 `role`: `correction`; 证据状态：`observed_failure/contradicted`
- `module_ids`: `ingestion`, `audit`
- 注释：用户否定“20-40 clusters”数量锚，要求按 canonical/alias 重叠、观点张力、跨域机制与上下文容量做启发式分组；cluster 只能压缩候选，不能成为 taxonomy 或 exploration boundary。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`
- 边界：cluster damage report 是 H036 后的专项复核；它支持损伤机制，但不是 H016 当时执行正确的证明。

### 08. FSJS：从审计堵塞中形成方法

- `event_id`: `claude_code:claude-primary-v4:H029`
- 建议 `role`: `decision`; 证据状态：`specified` + `retrospective`
- `module_ids`: `audit`
- 注释：H019-H028 多次暴露 mega-agent、错误 resume 与语义全量遍历问题后，agent team 提出 Filter-Shard-Judge-Synthesize：机械 filter 全量，语义 suspect/样本按 source/card affinity 分片，结构化输出后统一 synthesize。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/run_audit.py`
- 边界：本 event 形成方案；`audit_methodology.md` 是 H055 的复盘固化，不能单独证明 H029 已完整执行 FSJS。

### 09. FSJS：22-agent 综合审计产出 196 findings

- `event_id`: `claude_code:claude-primary-v4:H031`
- 建议 `role`: `action`; 证据状态：`executed` + `observed_failure`
- `module_ids`: `audit`
- 注释：FSJS 审计执行完成；归档 assistant window 报告 22 agents、196 findings、8 个设计不变量中 5 PASS / 3 PARTIAL，发现 YAML dual-format related、引用/JJ/材料缺口及疑似 leakage。当前报告 frontmatter 则记为 `agents_reporting: 21`，应保留“22 启动/归档汇总、21 reporting”的口径差异。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/mechanical_report.json`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/suspect_lists.json`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md`
- 边界：当前 `v4_comprehensive_audit.md` 已在 H033/H034 后把初始 leakage 结论修正为 1 true leakage、1 provenance gap、1 false positive；不能把当前修订文本当成 H031 原始报告快照。

### 10. Semantic false-positive correction：全文复核翻转 grep 判定

- `event_id`: `claude_code:claude-primary-v4:H033`
- 建议 `role`: `correction`; 证据状态：`contradicted` + `executed`
- `module_ids`: `audit`
- 注释：用户指出 grep miss 不等于原文无证据，并要求 agent team 读全文。复核把“参与程度谱系”从 leakage 翻转为 false positive，同时保留“确认优先规则”为 true leakage，并把 GraphRAG 案例降为 provenance gap/editorial。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/leakage_trace_corrective_vs_servant.md`; `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md`
- 边界：修正证明的是“suspect 必须语义复核”，不是 grep 无价值；也不能静默保留 H031 的两个 confirmed leakage 旧说法。

### 11. Cluster damage：专项审计区分确认与反证

- `event_id`: `claude_code:claude-primary-v4:H036`
- 建议 `role`: `validation`; 证据状态：`executed` + `contradicted`
- `module_ids`: `ingestion`, `audit`
- 注释：专家 team 先追溯 cluster 设计，再以 workflow 验证六项损伤预测；结果确认孤儿遗漏、YAML derive-related bug、脚注叙事泄漏，部分确认跨域桥梁稀疏，同时反证“链接硬隔离”和“comparison 只限同域”。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md`
- 边界：专项报告说明 cluster 带来偏置而非绝对边界；不能把所有图缺陷都归因于 cluster。

### 12. FSJS remediation：修图后仍显式保留缺口

- `event_id`: `claude_code:claude-primary-v4:H037`
- 建议 `role`: `action`; 证据状态：`executed` + `validation`
- `module_ids`: `ingestion`, `audit`
- 注释：agent team 先形成 22 项 fix plan，再按 ScriptFix -> TargetedEdit -> AgentFix -> Verify 执行；280/280 YAML 可解析、孤儿和 dual-format related 清零，但仍保留 2 条断裂引用与 1 张 comparison 源脚注缺口。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_plan.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md`
- 边界：同时期 Git `fb7b4060` 是修复后快照；它证明 remediation，不证明 H010/H016 从未产生这些缺陷。

### 13. Source pipeline diagnosis：深审先发现症状

- `event_id`: `claude_code:claude-primary-v4:H040`
- 建议 `role`: `validation`; 证据状态：`executed` + `retrospective`
- `module_ids`: `audit`
- 注释：8-topic 深审量化 authority flattening、scrape loss、30 个 phantom sources、source balkanization、零入度与单向边；这一步把“卡片问题”推进到 source/reframing/graph 各阶段，但尚未完成 collection root-cause 审计。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md`
- 边界：报告针对 280-card 治理快照，不代表后增 48 cards 接受了同级审计。

### 14. Source pipeline diagnosis：量化四类 pipeline gaps

- `event_id`: `claude_code:claude-primary-v4:H043`
- 建议 `role`: `validation`; 证据状态：`executed` + `observed_failure`
- `module_ids`: `ingestion`, `audit`
- 注释：定量 workflow 确认 1,261 个 HTML 结构元素损失、8 个高优先 repo 未消化、跨家族桥梁不足，以及 62/626 arXiv footnotes 落在摘要级 `text.txt` 的低质量路由面。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/scrape_lossiness_flags.yaml`
- 边界：报告反证 flat `text.txt` fallback 的可靠性；不能用后来的路径替换倒推原卡曾读取 TeX/full bundle。

### 15. Source remediation：先做路径、桥梁与两仓库 demo

- `event_id`: `claude_code:claude-primary-v4:H044`
- 建议 `role`: `action`; 证据状态：`executed` + `contradicted`
- `module_ids`: `ingestion`
- 注释：workflow 修 arXiv 引用路径、记录 scrape flags、补 citation bridges，并只为 graphrag 与 nvk-llm-wiki 两个 repo 生成 bundle/15 张实践卡。它是 partial fix，不是 20-repo 全量覆盖；arXiv 路径替换也不等于重新 extraction。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/scrape_lossiness_flags.yaml`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`
- 边界：同时期 Git `d2ebcf41` 支持这次局部修复；H045 明确仍有 18/20 repos 未处理。

### 16. Source remediation correction：bundle demo 不等于 repo2doc

- `event_id`: `claude_code:claude-primary-v4:H046`
- 建议 `role`: `correction`; 证据状态：`contradicted` + `specified`
- `module_ids`: `ingestion`
- 注释：用户否定“repo 文件拼 bundle -> card”作为最终方案，要求 repo -> structured doc -> standard doc2card；bundle 仅是 demo，缺少架构、接口、配置与实现模式的语义中间层。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`; `loops/v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md`
- 边界：这些文件后验记录 repo2doc TODO；V4 没有通用 repo2doc 执行证据。

### 17. Source pipeline diagnosis：按 source type 重审 collection

- `event_id`: `claude_code:claude-primary-v4:H049`
- 建议 `role`: `action`; 证据状态：`executed` + `retrospective`
- `module_ids`: `ingestion`, `audit`
- 注释：Understand -> per-source-type Audit -> Plan 形成数据采集修复计划：74 个源约 44 个有可靠阅读面，12 个 broken/empty，18 个需要 repo2doc；正确方向是 source-type dispatch，而非统一 `text.txt` fallback。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`
- 边界：fix plan 是 diagnosis/plan；不能把其中“期望阅读面”写成 H010 已执行的 source router。

### 18. Source remediation：执行窄范围修复并观测 Reddit 失败

- `event_id`: `claude_code:claude-primary-v4:H051`
- 建议 `role`: `failure`; 证据状态：`executed` + `observed_failure`
- `module_ids`: `ingestion`
- 注释：执行死源标记与 arxiv-ragas bundle 去污染（约 46MB -> 46KB）；Reddit JSON、old Reddit 等端点均返回 403，因无 OAuth2 停止。repo2doc 与 webpage 转换仍未完成。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`; `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/scrape_lossiness_flags.yaml`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`
- 边界：event 是执行/失败证据；learnings 是 H055 后验汇总。

### 19. Source remediation：webpage 全量转 markdown 后增量提取至 328

- `event_id`: `claude_code:claude-primary-v4:H053`
- 建议 `role`: `action`; 证据状态：`executed` + `retrospective`
- `module_ids`: `ingestion`
- 注释：raw.html 经 trafilatura 生成 `markdown.md`，19 个既有来源进入增量重提取；13 个源新增 33 张卡、6 个判定已覆盖，使约 295-card 快照增至 328。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/indexes/cards.md`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`; `loops/v4_llm_wiki_loop_20260602/learnings/kb_health_snapshot.md`
- 边界：同时期 Git `044312a2` 支持 `295 -> 328`；328 是 seed、full batch、post-hoc governance、repo demo 与 webpage repair 的累积终态，不是单次 pipeline 成功，也没有证据表明新增 48 cards 完整重跑 280-card 级 fusion/FSJS。

### 20. Learnings：把失败链固化，并保留未完成项

- `event_id`: `claude_code:claude-primary-v4:H055`
- 建议 `role`: `retrospective`; 证据状态：`retrospective` + `validation`
- `module_ids`: `ingestion`, `audit`
- 注释：按“agent team 讨论 -> workflow 执行 -> agent team 审计 -> workflow 修复 -> 独立总结”固化 7 份 learnings，并明确 repo2doc、hedging、Reddit、sequential governance 与 source router 仍未完成。
- `artifact_refs`: `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md`; `loops/v4_llm_wiki_loop_20260602/learnings/design_decisions.md`; `loops/v4_llm_wiki_loop_20260602/learnings/kb_health_snapshot.md`; `loops/v4_llm_wiki_loop_20260602/learnings/next_loop_prep.md`; `loops/v4_llm_wiki_loop_20260602/learnings/operational_lessons.md`; `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md`; `loops/v4_llm_wiki_loop_20260602/learnings/skill_iteration_log.md`
- 边界：同时期 Git `5f2824e9` 支持文档固化；learnings 是对前述事件的复盘，不是 full batch 原始执行日志。

## 3. 建议因果边（causal edges）

以下 relation 均使用 `query-timeline.schema.json` 已允许的枚举。

| from_event_id | relation | to_event_id | label |
|---|---|---|---|
| `claude_code:claude-primary-v4:H001` | `triggered_rework` | `claude_code:claude-primary-v4:H003` | seed 首轮的 17 项质量问题触发 15→19 修复 |
| `claude_code:claude-primary-v4:H003` | `caused` | `claude_code:claude-primary-v4:H010` | seed 被接受后扩展到 43-source full batch |
| `claude_code:claude-primary-v4:H010` | `contradicted` | `claude_code:claude-primary-v4:H013` | 43/43 完成声明被绝对路径和低链接覆盖反证 |
| `claude_code:claude-primary-v4:H013` | `caused` | `claude_code:claude-primary-v4:H015` | path/link 症状追到顺序 ingest、fusion 与治理缺席 |
| `claude_code:claude-primary-v4:H015` | `triggered_rework` | `claude_code:claude-primary-v4:H016` | related/fusion 边界纠正触发发布后治理补救 |
| `claude_code:claude-primary-v4:H016` | `challenged` | `claude_code:claude-primary-v4:H018` | 37-cluster 结果暴露 cluster 数量锚的不合理性 |
| `claude_code:claude-primary-v4:H018` | `caused` | `claude_code:claude-primary-v4:H029` | 治理偏差与后续审计堵塞共同推动通用 FSJS 设计 |
| `claude_code:claude-primary-v4:H029` | `caused` | `claude_code:claude-primary-v4:H031` | FSJS 方法进入 22-agent 综合审计执行 |
| `claude_code:claude-primary-v4:H031` | `contradicted` | `claude_code:claude-primary-v4:H033` | 首轮 leakage suspect 被 full-text semantic review 部分翻转 |
| `claude_code:claude-primary-v4:H033` | `caused` | `claude_code:claude-primary-v4:H036` | semantic false-positive 修正推动 cluster 假设也接受独立证伪 |
| `claude_code:claude-primary-v4:H036` | `triggered_rework` | `claude_code:claude-primary-v4:H037` | cluster damage 的确认项进入修复/验证 workflow |
| `claude_code:claude-primary-v4:H037` | `caused` | `claude_code:claude-primary-v4:H040` | 结构修图后转向认知、来源与图健康盲点深审 |
| `claude_code:claude-primary-v4:H040` | `caused` | `claude_code:claude-primary-v4:H043` | phantom source/scrape loss 等症状追到 source pipeline 根因 |
| `claude_code:claude-primary-v4:H043` | `triggered_rework` | `claude_code:claude-primary-v4:H044` | 四类 pipeline gaps 触发 arXiv、bridge、repo 局部修复 |
| `claude_code:claude-primary-v4:H044` | `contradicted` | `claude_code:claude-primary-v4:H046` | 两仓库 bundle demo 被纠正为非最终 repo2doc 方案 |
| `claude_code:claude-primary-v4:H046` | `caused` | `claude_code:claude-primary-v4:H049` | repo2doc 分层要求推动按 source type 重审 collection |
| `claude_code:claude-primary-v4:H049` | `caused` | `claude_code:claude-primary-v4:H051` | fix plan 收敛为死源、arxiv-ragas 与有限 Reddit 执行 |
| `claude_code:claude-primary-v4:H051` | `triggered_rework` | `claude_code:claude-primary-v4:H053` | Reddit 受阻且 repo 暂缓后，修复资源转向 webpage markdown |
| `claude_code:claude-primary-v4:H053` | `caused` | `claude_code:claude-primary-v4:H055` | 多轮增量修复后的累积终态触发独立 learnings 固化 |

## 4. 不应生成的叙事

1. 不应写“V4 一次运行 43 个来源并成功产出 328 张卡”。可证实的是 H010 到 259，H016 后置治理到 280，H044 局部 repo 修复到约 295，H053 webpage 增量修复到 328。
2. 不应把 `learnings/pipeline_actual.md` 的理想化 as-built 描述当作 H010 的 execution trace。H010 的 full batch 是角色折叠、direct accepted publish、无独立 reviewer/顺序 fusion 的执行。
3. 不应把 current `v4_comprehensive_audit.md` 当作 H031 原始审计文本；它已吸收 H033/H034 的 semantic false-positive correction。
4. 不应把 arXiv footnote 路径替换当作重新阅读 TeX/full bundle 的证明，也不应把两个 repo bundle demo 当作通用 repo2doc。
5. 不应把 280-card FSJS/graph verification 外推到后增 48 cards；终态 link/card 数只证明当前快照，不证明所有增量卡经过同级治理。
