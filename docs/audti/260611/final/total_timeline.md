# Codex/Claude 开发时间线审计总报告

```yaml
status: final_synthesis
scope_start: 2026-05-21
scope_end: 2026-06-08
timezone: Asia/Shanghai
input_policy: only accepted daily reports, independent audits, repair records, and main-agent acceptance records
output_language: 中文为主，关键术语用中文（English）锚定
```

## 一页结论

本报告只合并 `day_queue.md` 中已验收（accepted）且存在主控验收记录（main-agent acceptance）的日期：`2026-05-21` 到 `2026-06-08`。`2026-06-09` 到 `2026-06-11` 不进入历史每日梳理正文；其中 `2026-06-11` 只作为队列外风险（queue-out risk）被显式记录。

总线可以概括为四段：

1. `2026-05-21` 到 `2026-05-22`：从空壳仓库进入原始来源采集（raw source acquisition）和覆盖驱动循环（coverage-driven loop）固化，建立 raw corpus、source manifest、coverage framework 和 loop runner。
2. `2026-05-24` 到 `2026-05-29`：从 v0/v1 的 topic hub skeleton（主题中枢骨架）纠偏到 v2/v3 的 bottom-up knowledge-card pipeline（自下而上知识卡流水线），完成 v3 草稿、采纳、统一引用迁移（unified-citation migration）、capsule 收束与登记。`2026-05-29` 经过返修后通过，必须保留 no `Co-Authored-By` rule（无署名 trailer 规则）的分段事实。
3. `2026-05-30` 到 `2026-06-03`：不是连续开发主线，而是过渡和空窗：`2026-05-30` 是 transition_window_pass（过渡空窗通过），`2026-05-31` 和 `2026-06-03` 是 empty_window_pass（空窗日通过），`2026-06-01` 是 transition_planning_pass（过渡规划通过），`2026-06-02` 是 transition_runtime_pass（过渡运行通过）。
4. `2026-06-04` 到 `2026-06-08`：v4 正式进入实验、全量生产、治理补救、FSJS 审计修复和 deep audit / pipeline repair。`2026-06-08` 经过返修后通过，必须拆分 `data_collection_fix_plan.md` 的 `2026-06-08` execution artifact（运行产物）与 `2026-06-11` git solidification（git 固化）。

需要特别保留的三条边界：

- `2026-05-29`：14:53-14:54 +0800 确立 no `Co-Authored-By` rule（无署名 trailer 规则），但不能反推全天提交均无 trailer。14:32 的七个 v3 固化 commits 含 trailer，`779e045` 与 `0eccb9d` 未见 trailer。
- `2026-06-08`：`d2ebcf4` 是本地 6/8 最后一个 git commit，但不是最后一个 6/8 execution / artifact event（运行/产物事件）。`data_collection_fix_plan.md` 在 6/8 02:46-02:58 +0800 生成，6/11 `044312a2` 才首次提交。
- `2026-06-11`：当前 git history 中存在 `94aefbd6` 与 `044312a2` 两个 LLM Wiki 后续实质提交。除 `data_collection_fix_plan.md` 的 6/8 运行归属外，6/11 webpage re-extraction（网页重提取）和 295 -> 328 card expansion（卡片扩展）不回填到 6/8；是否扩展 day queue（日期队列）需主控或用户另行裁决。

## 证据包索引

本报告只使用以下已审计或已验收材料，不直接从未审计 transcript（会话记录）或 loop artifacts（循环产物）生成新事实：

| 证据包 | 路径 | 用途 |
| --- | --- | --- |
| 执行协议（execution protocol） | [`../protocols/execution_protocol.md`](../protocols/execution_protocol.md) | 日期归属、证据优先级、角色边界、空窗门禁 |
| 证据目录（source inventory） | [`../source_inventory.md`](../source_inventory.md) | 盘点证据源、覆盖矩阵和 6/9-6/11 排除背景 |
| 日期队列（day queue） | [`../day_queue.md`](../day_queue.md) | accepted / excluded 状态、验收类型和下一步说明 |
| 已验收日报（accepted daily reports） | [`../daily/`](../daily/) | 每日事实、边界、问题、证据地图 |
| 独立审计（independent audits） | [`../audits/`](../audits/) | pass / repair_required 判定、残余风险、门禁建议 |
| 返修记录（repair records） | [`../repairs/`](../repairs/) | 20260529 与 20260608 的 required changes 落实情况 |
| 主控验收（main-agent acceptance） | [`../decisions/`](../decisions/) | accepted 状态、acceptance_type、最终可合并口径 |

关键返修链路：

| 日期 | 初审 | 返修 | 复审 / 验收 | 最终合并口径 |
| --- | --- | --- | --- | --- |
| `2026-05-29` | [`20260529...audit.md`](../audits/20260529_v3_capsule_solidification_uploads_memory_feedback_audit.md) | [`20260529_repair_round1.md`](../repairs/20260529_repair_round1.md) | [`20260529...reaudit_round1.md`](../audits/20260529_v3_capsule_solidification_uploads_memory_feedback_reaudit_round1.md), [`20260529_acceptance.md`](../decisions/20260529_acceptance.md) | no `Co-Authored-By` rule 的规则事实与 commit trailer 事实分段表达 |
| `2026-06-08` | [`20260608...audit.md`](../audits/20260608_v4_deep_audit_pipeline_repair_audit.md) | [`20260608_repair_round1.md`](../repairs/20260608_repair_round1.md) | [`20260608...reaudit_round1.md`](../audits/20260608_v4_deep_audit_pipeline_repair_reaudit_round1.md), [`20260608_acceptance.md`](../decisions/20260608_acceptance.md) | `data_collection_fix_plan.md` 的 6/8 运行生成与 6/11 git 固化拆开 |

## 总体时间线

| 日期 | 类型 | 主线摘要 | 证据边界 |
| --- | --- | --- | --- |
| `2026-05-21` | 实质开发日（substantive development day） | 项目初始化、raw-source acquisition workspace、45 seed sources、coverage framework；21:03-21:39 的 corrected coverage-driven loop 有 transcript 强证据但当天未 git 固化。 | 5/22 继续追踪 loop artifacts 的 git 固化。 |
| `2026-05-22` | 固化日（git solidification day）/实质固化 | `ec5ecd3` 固化 5/21 晚间 corrected loop；`e09ea2a`、`c14a93e` 扩展 arXiv / GitHub / webpage corpus；`41e8693` 固化报告层。 | `goal_satisfaction_audit.md` 与 `judgment_status.md` / `loop_state.json` 状态不一致，作为 stale report（过期报告）风险。 |
| `2026-05-23` | empty_window_pass | 本项目未确认实质开发；Codex 活动属于项目外 `agent_skills/skill-manager` / `user-insights` 工作。 | 空窗通过，不补写开发事实。 |
| `2026-05-24` | 实质开发日，无当天 git commit | v0 meta KB demo、v1 topic hub skeleton、context isolation / focus drift audit；确认 v1 是 attention map / hub skeleton，不是 bottom-up atomic KB。 | 5/25 凌晨 commit 只作为后验固化；active atomic loop 文件化落地跨到 5/25。 |
| `2026-05-25` | 实质开发日 | v2 bottom-up loop、draft-first 转向、brain mailbox smoke test、user-insights bootstrap、Codex 到 Claude Code 的 v3 handoff；v3 first pass 运行但 git 固化在 5/26。 | user-insights 只作 secondary index（二级索引）；v3 首轮英文 draft 与中文主语言冲突由 5/26 处理。 |
| `2026-05-26` | 实质开发日 | v3 中文化、full-source read（全文读取）纠偏、171 draft cards / provenance / similarity / comparison、interlink 974 edges；adoption 因 API quota 未落地。 | 不把 5/27 adoption 和 5/28 unified-citation 迁移回填。 |
| `2026-05-27` | 实质开发日 | 171 张 v3 KB cards 文件级 adoption、3 张 similarity miss 复核、引用模型讨论、user-insights 提炼。 | 全局 state/status 未同步；5/28 迁移只作为后续。 |
| `2026-05-28` | 实质开发日 | v3 unified-citation migration：删除 `References`，统一 `Footnotes`，`related:` 从 footnotes 派生；672 个 `v3 adopt:` commits 是 171 张既有卡的多轮 migration edits。 | 合同/脚本/状态文件多在 5/29 才 git 固化；不能把 672 写成新增卡。 |
| `2026-05-29` | 固化/补账日（solidification / bookkeeping day） | v3 capsule closure、合同/脚本固化、status/registry 补账、active candidate 登记、uploads、comparison corpus drift 发现、memory feedback、next-loop design 讨论。 | 经 round1 repair 通过；no `Co-Authored-By` rule 必须分段表达。 |
| `2026-05-30` | transition_window_pass | 00:00:02-00:02:43 +0800 的 Claude transcript spillover，属于 5/29 晚间设计讨论尾声；无 git、loop、docs/user-insights 落盘。 | 不是实质开发日，也不是纯内容空窗。 |
| `2026-05-31` | empty_window_pass | 无本仓库 git、Claude/Codex 本项目 cwd、loop mtime、docs/user-insights 落盘证据。 | 外部 GitLab workspace 自动化排除。 |
| `2026-06-01` | transition_planning_pass | v4 前置规划：questioning loop、Mode A/B、pipeline contract、reviewer grep access；`questioning_loop_design.md` 与 `pipeline_spec.md` 初稿落盘。 | 无 git commit；v4 初始化不属于 6/1。 |
| `2026-06-02` | transition_runtime_pass | `docs/present_doc/intro_*.html` 演示材料制作和 5 张 PNG 导出；不是 v4 loop 初始化日。 | `docs/present_doc/` 未跟踪，只能用 transcript / mtime / 导出记录支撑。 |
| `2026-06-03` | empty_window_pass / external transition | 本项目空窗；Codex 活动属于外部 workspace 或工具索引噪声。 | 不能写成 v4 前置开发日。 |
| `2026-06-04` | 实质开发日 | v3 future plans git 固化、v4 capsule 初始化、`LOOP_START_PROMPT.md`、Phase 1-2、karpathy-gist 实验、15 张初始 KB cards。 | `loop_state.json` / `status.json` stale；`2df61dd` 只证明 local git solidification。 |
| `2026-06-05` | 实质开发日 | Phase 2 targeted remediation、Phase 4 全量 extraction、259 cards、governance pass、P0 绝对路径修复、full governance remediation、21 comparison cards、FSJS 方案形成。 | 不是最终质量闭环；state/status 仍 stale。 |
| `2026-06-06` | empty_window_pass | Claude / Codex / git / loop mtime / memory / user-insights 均无本项目实质开发证据。 | 保留 6/5 与 6/7 之间的空窗。 |
| `2026-06-07` | 实质开发日 | FSJS audit -> fix plan -> repair -> verification；`fb7b406` 主修复提交，`5d7586f` 修最后 2 条断裂引用；deep audit 只在本日晚间启动。 | `fix_verification.json` 停在 `fb7b406`，6/7 末态断链归零需由 `5d7586f` git snapshot 支撑。 |
| `2026-06-08` | 实质开发日 | deep audit blind spots、pipeline gaps report、partial pipeline repair；`a13d02f`、`4ec3b45`、`d2ebcf4` 三个 6/8 commits；`data_collection_fix_plan.md` 6/8 生成但 6/11 才提交。 | 经 round1 repair 通过；6/11 后续提交是队列外风险，不回填。 |

## 阶段划分

### 阶段一：来源采集与覆盖框架（2026-05-21 至 2026-05-22）

本阶段把仓库从空壳推进到 raw knowledge database（原始知识库）工作区。5/21 的核心是 source acquisition（来源获取）、arXiv source-first（源码优先）和 coverage framework（覆盖框架）；5/22 的核心是把 5/21 晚间 corrected coverage-driven loop 的 runner、manifest、claims 和 coverage records 通过 git 固化。

阶段边界：

- `2026-05-21` 的 21:03-21:39 corrected loop 是运行事实（execution fact），不是当天 git 固化事实。
- `2026-05-22` 的 `ec5ecd3` 是前一晚运行结果的 git solidification（git 固化），不是当天新跑 research loop（研究循环）。

### 阶段二：从 topic skeleton 到 bottom-up KB（2026-05-24 至 2026-05-29）

本阶段完成核心对象的连续纠偏：v0/v1 证明了 filesystem-backed loop（文件系统支撑循环）和 topic hub skeleton（主题中枢骨架）可以运行，但被审计和用户反馈降级为 attention map（注意力地图），不是最终 bottom-up atomic KB（自下而上原子知识库）。5/25 到 5/29 将生产对象改为 scoped knowledge card（有范围的知识卡），并形成 v3 的 draft-first、comparison provenance、adoption、unified footnote model、candidate registration。

阶段边界：

- v2 / v3 的 user-insights（用户洞察）只作为 secondary index（二级索引），不能替代 transcript、git 和 loop artifacts。
- 5/28 的 unified-citation migration 是运行与多轮卡片编辑，5/29 才固化合同、脚本、状态补账和上传类提交。
- 5/29 的 no `Co-Authored-By` rule 是规则事实，不是全天 commit trailer 事实。

### 阶段三：过渡、空窗与 v4 前置规划（2026-05-30 至 2026-06-03）

这一段不是连续实质开发。5/30 是跨午夜尾声，5/31 和 6/3 是空窗，6/1 是规划落盘，6/2 是演示材料运行产出。它们在最终总线中必须保留，因为它们防止后续读者把 6/4 v4 初始化倒填到 6/1-6/3。

阶段边界：

- `2026-06-01` 可写 planning discussion（规划讨论）和 future plan artifact landing（规划产物落盘），不可写 v4 production（v4 生产）。
- `2026-06-02` 可写 presentation material runtime output（演示材料运行产出），不可写 v4 initialization（v4 初始化）。
- `2026-06-03` 是本项目 empty window（空窗），Codex 外部活动只作为排除证据。

### 阶段四：v4 实验、治理和审计修复（2026-06-04 至 2026-06-08）

本阶段从 v4 capsule 初始化开始，先在 karpathy-gist 上完成 Phase 1-2，再在 6/5 进入全量 extraction（提取）与 governance remediation（治理补救），6/7 用 FSJS（Filter-Shard-Judge-Synthesize）执行大规模审计与修复，6/8 进一步用 deep audit（深度审计）暴露 pipeline gaps（流水线缺口）并做局部修复。

阶段边界：

- 6/4 的 `loop_state.json` / `status.json` 滞后，不能代表实际 Phase 1-2 状态。
- 6/5 的 governance pass 和 spot-check 不是最终质量闭环，6/7 继续发现结构缺陷。
- 6/8 的 pipeline repair 是 partial pipeline repair（局部流水线修复），不是 repo2doc / source router / scrape re-extraction 全闭环。

## 关键转折点

| 转折点 | 日期 | 支撑材料 | 总线意义 |
| --- | --- | --- | --- |
| 从 raw acquisition 到 coverage-driven loop | `2026-05-21` / `2026-05-22` | [`20260521 daily`](../daily/20260521_project_initialization_source_discovery.md), [`20260522 daily`](../daily/20260522_loop_manifests_expanded_corpus.md) | 项目不只是收集文件，而是开始用 coverage satisfaction（覆盖满足）作为停止条件。 |
| 从 meta KB / topic skeleton 转向 bottom-up atomic/scoped cards | `2026-05-24` / `2026-05-25` | [`20260524 daily`](../daily/20260524_v0_v1_loop_capsules_context_audits.md), [`20260525 daily`](../daily/20260525_v2_v3_handoff_user_insights.md) | v0/v1 被降级为 demo / attention map，生产对象改为知识卡。 |
| 从串行 acceptance 低吞吐转向 draft-first | `2026-05-25` | [`20260525 daily`](../daily/20260525_v2_v3_handoff_user_insights.md) | 7 小时 15 张 accepted cards 的吞吐问题推动 draft-first 与后置 gate。 |
| 中文主语言与全文读取成为硬约束 | `2026-05-26` | [`20260526 daily`](../daily/20260526_v3_draft_interlink_full_source_chinese.md), [`20260526 audit`](../audits/20260526_v3_draft_interlink_full_source_chinese_audit.md) | 纠正英文 first pass 和防御性 `limit:2000` 截断，影响后续卡片密度与相似度。 |
| `related` 从手写元数据转为 footnote-derived view | `2026-05-27` / `2026-05-28` | [`20260527 daily`](../daily/20260527_v3_adoption_citation_discussion_user_insights.md), [`20260528 daily`](../daily/20260528_unified_citation_migration.md) | 引用模型从 References/Footnotes 二分转为统一脚注和派生图。 |
| loop independence 暴露 v3 comparison corpus drift | `2026-05-29` | [`20260529 daily`](../daily/20260529_v3_capsule_solidification_uploads_memory_feedback.md), [`20260529 reaudit`](../audits/20260529_v3_capsule_solidification_uploads_memory_feedback_reaudit_round1.md) | 发现 v3 similarity/comparison 只比较 v2 的 15 张卡，未做 intra-v3 dedup。 |
| v4 采用 JJ、typed footnotes、grep-only、init-not-special | `2026-06-04` | [`20260604 daily`](../daily/20260604_v4_initialization_phase1_2_karpathy.md), [`20260604 acceptance`](../decisions/20260604_acceptance.md) | v4 从 v3 future plan 固化为新 capsule 和可执行实验。 |
| governance 从抽检转向结构性补救 | `2026-06-05` | [`20260605 daily`](../daily/20260605_v4_phase4_governance_remediation_audit_design.md), [`20260605 audit`](../audits/20260605_v4_phase4_governance_remediation_audit_design_audit.md) | 绝对路径 P0、link density、近义/反义 cluster 和 comparison cards 进入治理层。 |
| FSJS 让 280 卡审计可分片执行 | `2026-06-07` | [`20260607 daily`](../daily/20260607_v4_fsjs_audit_fix_verification.md), [`20260607 acceptance`](../decisions/20260607_acceptance.md) | Filter / Shard / Judge / Synthesize 成为大规模语义审计的执行框架。 |
| deep audit 从 bug 修复推进到 pipeline gap | `2026-06-08` | [`20260608 daily`](../daily/20260608_v4_deep_audit_pipeline_repair.md), [`20260608 reaudit`](../audits/20260608_v4_deep_audit_pipeline_repair_reaudit_round1.md) | 盲点审计把问题上升到 source routing、repo digestion、scrape lossiness 和 source authority。 |

## 决策链

1. 原始来源优先（source-first preservation）：5/21 确立 raw source、metadata、hash、fetch time 优先，arXiv 走 TeX/source bundle 优先，PDF 只作为 fallback（兜底）。
2. 覆盖满足优先于结构校验（coverage satisfaction over structural verify）：5/21 晚 corrected loop 明确 `verify` 不能替代 coverage satisfaction，5/22 固化 runner 和 records。
3. main-agent 作为控制面（control plane）：5/24 暴露 main-agent 越界和 audit worker 写入问题后，v2/v3 继续强调 main-agent 调度、worker 执行、独立审计。
4. 从 topic node 到 scoped knowledge card：5/24 晚和 5/25 将生产对象从 topic/hub 改为有信息密度的 scoped knowledge card（有范围知识卡）。
5. draft-first 与后置 gate：5/25 以后，生产先形成 draft backlog（草稿积压），再做 similarity、comparison、publication/fusion gate。
6. 中文主语言和全文读取：5/26 把中文主语言（Chinese primary language）和 full-source read（全文读取）变成 worker 合同核心约束。
7. 引用模型统一：5/27-5/28 将 `references` / `footnotes` / `related` 重新界定为统一脚注模型，`related` 成为 citation-derived graph（引用派生图）。
8. loop independence：5/29 用户纠偏每个 loop 独立，暴露 v3 comparison base 错误依赖 v2。
9. v4 pipeline 简化：6/1-6/4 的设计链条选择 questioning loop、grep-only recall、Justification Journal（JJ）、typed footnotes、no O(N) comparison、init is not special。
10. 治理先补结构，再做语义：6/5-6/7 从 absolute path、YAML related、orphan、broken refs 等机械问题进入 FSJS 语义审计。
11. pipeline gap 优先级：6/8 将 deep audit 发现收束为 arxiv source routing、citation eval cross-links、scrape lossiness、GitHub repo digestion 四类可执行缺口。

## 坑与修复模式

| 模式 | 出现位置 | 修复/降级方式 | 残余状态 |
| --- | --- | --- | --- |
| 运行时间与固化时间混淆 | 5/21-5/22、5/28-5/29、6/1-6/4、6/8-6/11 | 总线统一拆分 execution time（运行发生时间）与 git solidification time（git 固化时间）。 | `data_collection_fix_plan.md` 是最重要的双日期案例。 |
| 二级材料诱导后验补史 | user-insights、docs、memory、summary | 只作 secondary index（二级索引），关键事实回到 accepted daily / audit / decision。 | 仍需防止当前文件状态污染历史日。 |
| 目标对象漂移 | v0/v1 topic skeleton | 审计降级为 demo / attention map，5/25 转入 bottom-up KB。 | v1 不证明 atomic fact reliability。 |
| 读取不足与语言不一致 | 5/25 first pass、5/26 batch workers | 用户纠偏中文主语言与 full-source read，修 worker template。 | 5/26 prompt 中仍有局部 `limit:2000` 残余指令。 |
| 状态文件滞后 | 5/27、6/4、6/5 | 用 transcript、git tree、task snapshot 替代 stale `loop_state.json` / `status.json`。 | 自动化总线不能盲读 state/status。 |
| comparison base 错误 | 5/29 v3 comparison corpus drift | 审计记录 v2-only base，列为流程债。 | 未在 5/29 完成 remediation。 |
| commit message 规则反推过度 | 5/29 no Co-Authored-By | round1 repair 后改为规则事实和提交事实分段表达。 | 必须保留首轮审计和返修 provenance。 |
| 初次治理门禁过度乐观 | 6/5 governance pass | 6/7 FSJS 继续审计并修复结构缺陷。 | 6/5 不等于最终质量闭环。 |
| 验证 artifact 与末态不同步 | 6/7 `fix_verification.json` | 用 `5d7586f` git snapshot 证明 broken refs 归零。 | JSON 仍停在 `fb7b406` 时点。 |
| source routing 泛化错误 | 6/8 arxiv `text.txt` | card 层改为 `agent_source_bundle.txt`，并形成 data collection fix plan。 | JJ 仍有 19 处旧 `text.txt`，repo2doc 未执行。 |

## 未解决问题

- 来源覆盖缺口：Reddit blocked（Reddit 受阻）、AICritique/network intercept（网络拦截）、enterprise governance（企业治理）、empirical evaluation（实证评估）等问题从 5/21 开始即存在，后续未在本范围内完全补齐。
- raw corpus 内容质量：多日审计确认了采集、目录、计数、提交边界和代表样例，但没有逐篇全文审计所有 raw source（原始来源）。
- stale reports / stale state：`goal_satisfaction_audit.md`、`loop_state.json`、`status.json`、`fix_verification.json` 等多次出现时点滞后，最终读者必须看对应审计说明。
- v3 comparison corpus drift：5/29 已确认 v3 comparison 错依赖 v2-only base，未完成已有 171 张 KB 的系统性修复。
- registry/status/current_loop 不一致：5/29 v3 active candidate、candidate_ready、candidate_in_progress 和 stale next_action 并存。
- v4 Phase 1-2 质量验证缺口：6/4 首跑后发现 17 项问题，只迭代 skills，没有同日完整 rerun。
- v4 state/status 滞后：6/4、6/5 的 `loop_state.json` / `status.json` 不能代表实际进展。
- 6/7 末态仍有未解决结构问题：3 张卡脚注定义缺失，1 张 comparison card 缺直接 `[^src-*]` 脚注，knowledge-compounding PDF / section-level 验证盲区仍在。
- 6/8 pipeline repair 是局部修复：arxiv card path 已修，但 JJ 仍有旧 source line；repo extraction 只覆盖 2 个 repo；scrape lossiness 主要被标记为 flags；source authority flattening 只形成诊断，没有完成 schema 级修复。
- `2026-06-11` 队列外提交：`94aefbd6` 与 `044312a2` 已挑战 source_inventory / day_queue 的旧口径；本报告不扩展队列，只记录风险。

## 未纳入内容

- `2026-06-09`、`2026-06-10`、`2026-06-11` 不纳入历史每日梳理正文；6/11 只作为 queue-out risk（队列外风险）说明。
- 未审计 transcript（会话记录）、未验收 loop artifacts（循环产物）和当前工作树状态不直接产生新事实。
- `docs/present_doc/` 在 6/2 作为 transition runtime output（过渡运行产出）纳入，但它是 untracked directory（未跟踪目录），不作为 git 固化事实。
- 外部 Codex workspace，如 `2604-llm-analysis`、`2606-trinity`、`2605-qunfen`、`agent_skills/skill-manager`，只作为排除证据，不进入本项目 LLM Wiki 主线。
- 本报告不重新审计 171 / 280 / 295 / 328 张卡的语义质量，不复算所有 graph edges（图边），不评估最终产品质量。
- 本报告不修订 `day_queue.md`、`source_inventory.md`、daily、audits、repairs 或 decisions。

## 风险与残余不确定性

| 风险 | 影响 | 本报告处理 |
| --- | --- | --- |
| 证据等级差异 | 有些日期有 git + transcript + artifacts 三角校验；有些日期只有 transcript / mtime / negative evidence。 | 在时间线中标注实质开发日、固化日、过渡日、空窗日。 |
| 运行与固化双日期 | 同一 artifact 可能运行在一天、提交在另一天。 | 明确 execution time（运行时间）和 git solidification time（git 固化时间）。 |
| 文件内日期（in-file date）误导 | `created: 2026-06-02`、`date: 2026-06-07` 等可能与本地日窗冲突。 | 以 accepted daily / audit 的归属为准，不用 frontmatter 单独定日。 |
| 当前工作树后续污染 | 6/11 后续提交和未跟踪目录可能让当前文件状态不同于当日状态。 | 只合并已审计的 commit snapshot / daily 结论，不按 HEAD 重新推断。 |
| 空窗不是“没有思考” | empty_window_pass 只证明可审计证据中没有本项目开发事实。 | 不声称用户没有离线思考或未记录讨论。 |
| 6/11 队列外风险 | `source_inventory.md` / `day_queue.md` 的“6/8 最后实质开发记录”口径被后续 git history 挑战。 | 明确交由主控或用户决定是否扩展 day queue。 |

## 范围边界

本报告的时间范围是 `2026-05-21 00:00:00 +0800` 到 `2026-06-09 00:00:00 +0800`，实际已验收开发线截止 `2026-06-08`。日期归属采用 Asia/Shanghai 本地日窗。

本报告的事实来源仅限：

- 已验收日报（accepted daily reports）
- 通过的独立审计（independent audits / reaudit）
- 返修记录（repair records）
- 主控验收记录（main-agent acceptance records）
- 执行协议、source inventory 和 day queue 的边界说明

本报告不直接读取未审计 transcript 来补新事实；即使某些日报和审计引用了 transcript lines、git commits、mtime 或 loop artifacts，本报告也只采用其已经审计通过的表述。

## 附录：每日索引

| 日期 | 验收类型 | 日报 | 审计 / 复审 | 主控验收 |
| --- | --- | --- | --- | --- |
| `2026-05-21` | substantive development | [`daily`](../daily/20260521_project_initialization_source_discovery.md) | [`audit`](../audits/20260521_project_initialization_source_discovery_audit.md) | [`decision`](../decisions/20260521_acceptance.md) |
| `2026-05-22` | git solidification / substantive | [`daily`](../daily/20260522_loop_manifests_expanded_corpus.md) | [`audit`](../audits/20260522_loop_manifests_expanded_corpus_audit.md) | [`decision`](../decisions/20260522_acceptance.md) |
| `2026-05-23` | empty_window_pass | [`daily`](../daily/20260523_gap_or_transition_day.md) | [`audit`](../audits/20260523_gap_or_transition_day_audit.md) | [`decision`](../decisions/20260523_acceptance.md) |
| `2026-05-24` | substantive development, no same-day commit | [`daily`](../daily/20260524_v0_v1_loop_capsules_context_audits.md) | [`audit`](../audits/20260524_v0_v1_loop_capsules_context_audits_audit.md) | [`decision`](../decisions/20260524_acceptance.md) |
| `2026-05-25` | substantive development | [`daily`](../daily/20260525_v2_v3_handoff_user_insights.md) | [`audit`](../audits/20260525_v2_v3_handoff_user_insights_audit.md) | [`decision`](../decisions/20260525_acceptance.md) |
| `2026-05-26` | substantive development | [`daily`](../daily/20260526_v3_draft_interlink_full_source_chinese.md) | [`audit`](../audits/20260526_v3_draft_interlink_full_source_chinese_audit.md) | [`decision`](../decisions/20260526_acceptance.md) |
| `2026-05-27` | substantive development | [`daily`](../daily/20260527_v3_adoption_citation_discussion_user_insights.md) | [`audit`](../audits/20260527_v3_adoption_citation_discussion_user_insights_audit.md) | [`decision`](../decisions/20260527_acceptance.md) |
| `2026-05-28` | substantive development | [`daily`](../daily/20260528_unified_citation_migration.md) | [`audit`](../audits/20260528_unified_citation_migration_audit.md) | [`decision`](../decisions/20260528_acceptance.md) |
| `2026-05-29` | solidification / bookkeeping, repaired | [`daily`](../daily/20260529_v3_capsule_solidification_uploads_memory_feedback.md) | [`first audit`](../audits/20260529_v3_capsule_solidification_uploads_memory_feedback_audit.md), [`repair`](../repairs/20260529_repair_round1.md), [`reaudit`](../audits/20260529_v3_capsule_solidification_uploads_memory_feedback_reaudit_round1.md) | [`decision`](../decisions/20260529_acceptance.md) |
| `2026-05-30` | transition_window_pass | [`daily`](../daily/20260530_gap_or_transition_day.md) | [`audit`](../audits/20260530_gap_or_transition_day_audit.md) | [`decision`](../decisions/20260530_acceptance.md) |
| `2026-05-31` | empty_window_pass | [`daily`](../daily/20260531_gap_day.md) | [`audit`](../audits/20260531_gap_day_audit.md) | [`decision`](../decisions/20260531_acceptance.md) |
| `2026-06-01` | transition_planning_pass | [`daily`](../daily/20260601_v4_planning_and_future_plan_landing.md) | [`audit`](../audits/20260601_transition_planning_future_plan_audit.md) | [`decision`](../decisions/20260601_acceptance.md) |
| `2026-06-02` | transition_runtime_pass | [`daily`](../daily/20260602_v4_loop_id_rejected_presentation_materials.md) | [`audit`](../audits/20260602_v4_loop_id_presentation_materials_audit.md) | [`decision`](../decisions/20260602_acceptance.md) |
| `2026-06-03` | empty_window_pass / external transition | [`daily`](../daily/20260603_transition_empty_external_codex.md) | [`audit`](../audits/20260603_transition_empty_external_codex_audit.md) | [`decision`](../decisions/20260603_acceptance.md) |
| `2026-06-04` | substantive development | [`daily`](../daily/20260604_v4_initialization_phase1_2_karpathy.md) | [`audit`](../audits/20260604_v4_initialization_phase1_2_karpathy_audit.md) | [`decision`](../decisions/20260604_acceptance.md) |
| `2026-06-05` | substantive development | [`daily`](../daily/20260605_v4_phase4_governance_remediation_audit_design.md) | [`audit`](../audits/20260605_v4_phase4_governance_remediation_audit_design_audit.md) | [`decision`](../decisions/20260605_acceptance.md) |
| `2026-06-06` | empty_window_pass | [`daily`](../daily/20260606_empty_window_timezone_boundary_review.md) | [`audit`](../audits/20260606_empty_window_timezone_boundary_review_audit.md) | [`decision`](../decisions/20260606_acceptance.md) |
| `2026-06-07` | substantive development | [`daily`](../daily/20260607_v4_fsjs_audit_fix_verification.md) | [`audit`](../audits/20260607_v4_fsjs_audit_fix_verification_audit.md) | [`decision`](../decisions/20260607_acceptance.md) |
| `2026-06-08` | substantive development, repaired | [`daily`](../daily/20260608_v4_deep_audit_pipeline_repair.md) | [`first audit`](../audits/20260608_v4_deep_audit_pipeline_repair_audit.md), [`repair`](../repairs/20260608_repair_round1.md), [`reaudit`](../audits/20260608_v4_deep_audit_pipeline_repair_reaudit_round1.md) | [`decision`](../decisions/20260608_acceptance.md) |
