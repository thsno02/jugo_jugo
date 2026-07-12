# V4 审计机制演化证据审计

## 1. 范围、口径与结论

本文把 V4 的审计实践投影到当前稳定七阶段：`audit-contract`、`mechanical-filter`、`shard-judge`、`synthesize-verdict`、`adversarial-probe`、`root-cause-audit`、`remediation-experiment`，并按当前十项控制复核实际覆盖。七阶段和十项控制是后验稳定模型，不假定 V4 当时已经用这些名称完整实现。

事实状态严格区分：

- **`specified`（规定）**：prompt、skill、task 或 fix plan 写了应做什么；不证明执行。
- **`executed`（执行）**：归档事件、当时 Git 快照或运行产物证明动作发生。
- **`observed_failure/contradicted`（观察失败/矛盾）**：用户反证、审计发现、状态冲突或后续语义复核推翻了原结论。
- **`retrospective`（复盘）**：后写 learnings、当前计数或研究文档；只能解释历史，不能回填原执行。

覆盖标签也按分母解释：

- **`full`（全量）**：在明确快照上，目标集合每一项都进入该检查；只对该检查成立。例如 280/280 YAML parse 不等于 280 张卡语义正确。
- **`suspect`（嫌疑集）**：机械信号先召回候选，仅候选进入语义判断；不能外推到未召回项。
- **`sample`（抽样）**：只检查预先选定或随机子集；通过不能外推全库。
- **`not measured`（未测）**：没有可核验分母或运行账本。

**总判定**：V4 在 280-card 快照上真实形成了 FSJS（Filter-Shard-Judge-Synthesize）和“用户反证→根因追踪→修复→再验证”的闭环，这是其最重要的机制进化；但它没有形成一个覆盖原始生产合同、知识解释充分性和最终 328-card 快照的统一审计。V4 的强项是后验发现与修复，弱项是发布前门禁和逐运行证据。最终修复快照证明“后来变好”，不能证明 43-source 原始 pipeline conformant。

## 2. 七阶段对照

| 稳定阶段 | V4 中的实际形态 | 事实状态 | 审计判定 |
|---|---|---|---|
| `audit-contract` | seed 的 reviewer quit-audit 定义 coverage 全查、source faithfulness 随机 3-5 卡抽查；随后提出十个审计 topic，最后才稳定为 FSJS | `specified`：`loops/v4_llm_wiki_loop_20260602/skills/reviewer/PROMPT.md`；`executed`：`claude_code:claude-primary-v4:H019`、`claude_code:claude-primary-v4:H029` | 合同持续演化，初始不是一个冻结后执行的统一 control inventory |
| `mechanical-filter` | 对 280 cards 扫 YAML、字段、footnote、slug、related、loop isolation，并输出 defect/suspect 清单 | `executed`：`claude_code:claude-primary-v4:H031`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/mechanical_report.json`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/suspect_lists.json` | 在 280 分母上真实全量；报告间有 69/70 dual-format 的口径冲突 |
| `shard-judge` | 21 个 source-affinity agents，每组 1-2 sources、约 5-15 cards；comparison 另作 11+10 数量分片 | `executed`：`claude_code:claude-primary-v4:H031`；方法说明见 `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md`，该文件是 `retrospective` | card assignment 可称全量，具体语义维度并非全部 claim 全量；原始逐 shard ledger 未保留在当前仓库 |
| `synthesize-verdict` | 汇总 196 findings，给 8 个设计不变量 5 PASS / 3 PARTIAL，并列出 CRITICAL/MAJOR/MINOR | `executed`：`claude_code:claude-primary-v4:H031`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md` | 是 280-card 条件 verdict，不是 328-card 终态 verdict；后续有 finding 翻转 |
| `adversarial-probe` | 用户连续挑战绝对路径、缺失 fusion、cluster 数量锚、mega-agent、grep leakage、cluster 边界、source pipeline 和 partial repo fix | `executed`：`claude_code:claude-primary-v4:H012`、`claude_code:claude-primary-v4:H015`、`claude_code:claude-primary-v4:H018`、`claude_code:claude-primary-v4:H029`、`claude_code:claude-primary-v4:H033`、`claude_code:claude-primary-v4:H036`、`claude_code:claude-primary-v4:H045`、`claude_code:claude-primary-v4:H049` | V4 最强的一环；新问题多由用户阅读和操作观察进入，而非初始合同自动发现 |
| `root-cause-audit` | 追到并发 direct publish 跳过顺序 ingest/fusion、正则写 YAML、脚注叙事泄漏、扁平 source fallback、repo 无阅读面、HTML→text 有损 | `executed`：`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015`、`claude_code:claude-primary-v4:H034`、`claude_code:claude-primary-v4:H036`、`claude_code:claude-primary-v4:H042`、`claude_code:claude-primary-v4:H049`；产物见 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/leakage_trace_corrective_vs_servant.md`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md` | 覆盖 governance 和 collection 根因，但没有系统核验 43-source execution nodes 是否收到完整四技能合同 |
| `remediation-experiment` | 22 项 fix plan→脚本/定点/agent 修复→280-card verification；随后 arXiv、bridge、2 repo demo、webpage markdown 和增量重提取 | `executed`：`claude_code:claude-primary-v4:H037`、`claude_code:claude-primary-v4:H038`、`claude_code:claude-primary-v4:H044`、`claude_code:claude-primary-v4:H045`、`claude_code:claude-primary-v4:H051`、`claude_code:claude-primary-v4:H053`；产物见 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_plan.md`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/scrape_lossiness_flags.yaml` | 修复分阶段、分分母执行；没有把 43-source 原批次按修正后合同重跑，也没有对 328 cards 重跑完整 FSJS |

## 3. 分批演化

### 3.1 Seed：Karpathy gist

**`specified`**：`loops/v4_llm_wiki_loop_20260602/LOOP_START_PROMPT.md` 要求 reader、questioner、reframing、reviewer 与 quit-audit。`loops/v4_llm_wiki_loop_20260602/skills/reviewer/PROMPT.md` 明确：digest core claims 做全量 coverage check；source faithfulness 只随机抽 3-5 张；`unsupported` 才阻塞退出；通过后每张 JJ 应追加 `## review |`。

**`executed`**：`claude_code:claude-primary-v4:H001` 记录独立 reader/questioner/reviewer 调用、15 cards、15 JJ、quit-audit pass，并在后续质量复核中发现 17 项链接密度、原子性、脚注和内容缺口。Git `2df61ddb` 固化 15 份 draft、15 份 accepted card 及四项 skills。

**实际覆盖**：

- coverage against digest：`full`，但只覆盖一个 seed source。
- source faithfulness：`sample`（3-5/15），不是全量。
- schema、graph、fusion、state：只有局部人工检查或产物存在，没有稳定全量报告。
- pipeline conformance：角色调用有事件证据，但完整 skill 注入、逐轮 transcript 和 reviewer verdict 未落盘，属于 `not measured`。
- knowledge depth：17 项后续复核是 `sample/qualitative`，并且 task 在当时仍保留“在 gist 上重新运行”未完成。

**`contradicted`**：reviewer contract 要求每张通过卡追加 review event，但 Git `2df61ddb` 和当前 328 JJ 均检索不到 `## review |`。因此 transcript 可证明 reviewer 调用和 pass 声明，不能证明 per-card review ledger 实际写入。

### 3.2 43-source full batch

**`executed`**：`claude_code:claude-primary-v4:H010` 记录 43/43 materials 完成、240 张新增卡、总计 259 cards；Git `d36f6f7a` 固化 240 张新增 accepted cards/JJ。它是生产批次，不是审计批次。

**实际覆盖**：来源处理状态在 workflow 汇总中是 `full`（43/43），但十项审计控制几乎均为 `not measured`。agents 直接写 `kb/cards/`，同批并发不可见，未形成逐源 immutable run ledger、draft→review→promotion ledger 或 inline fusion verdict。

**`observed_failure/contradicted`**：

- `claude_code:claude-primary-v4:H013`、`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015` 确认 240/259 cards 使用绝对 source path、链接覆盖约 45%，并认定顺序 ingest、fusion 和治理被跳过。
- Git 固化能证明文件产生，不能证明 reviewer、fusion、schema gate 或完整 questioning contract执行。
- “43/43 success”只表示 workflow 节点返回成功，不等于 43/43 source eligibility 或 knowledge quality 通过。

### 3.3 Post-publication governance

**`executed`**：`claude_code:claude-primary-v4:H011` 对 259 cards 做 canonical/cross-link 治理，但 source faithfulness 仅抽查 8 张，结果 8/8；`claude_code:claude-primary-v4:H016` 运行 37-cluster governance，新增 295 card footnotes、54 distinction footnotes、21 comparison cards，KB 到 280 cards；Git 边界为 `f4ec89b6` 与 `b26dafc3`。

**实际覆盖**：

- canonical/related/graph bookkeeping：面向当时全库，属于 `full` mechanical pass。
- source faithfulness：`sample`（8 cards）。
- fusion boundary：只对 cluster/candidate 集合做 agent judgment，属于 `suspect`，没有全库 pair ledger、skip/merge 账本或 pre-promotion gate。
- graph relation semantics：候选经 agent 读卡判断，但 cluster 数量锚改变了召回边界，不能称语义全量。

**`observed_failure/contradicted`**：`claude_code:claude-primary-v4:H017` 与 `claude_code:claude-primary-v4:H018` 发现 prompt 中存在“20-40 clusters”数量锚，用户否定以目标数量驱动聚类。后续 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md` 证明 post-hoc derive-related 的单行替换制造了 dual-format YAML、孤儿和跨域稀疏。治理确实执行过，但它同时制造了新缺陷。

### 3.4 FSJS：280-card 综合审计

**`specified`→`executed`**：`claude_code:claude-primary-v4:H019` 先列十个审计 topic；`claude_code:claude-primary-v4:H020`、`claude_code:claude-primary-v4:H023`、`claude_code:claude-primary-v4:H024`、`claude_code:claude-primary-v4:H026`、`claude_code:claude-primary-v4:H028` 暴露 topic-level mega-agent、错误 restart/resume 和“语义全库由单 agent 阅读”问题；`claude_code:claude-primary-v4:H029` 才明确机械检查全量、语义判断分片；`claude_code:claude-primary-v4:H031` 完成 22-agent FSJS、196 findings 和综合报告。

**机械 `full`（280 snapshot）**：

- 280 cards 的必填字段、status、JJ 对应关系、source/card/dist footnote presence、related target、loop reference 和 YAML 双格式进入全量 grep/计数；184 个 unique card-footnote targets 被全量交叉核对。
- `id==filename` 与 valid footnote prefix 在 `mechanical_report.json` 中明确带有 sampling 表述，只能标 `sample`，不能因同一报告的其他检查全量而升级为 `full`。
- `mechanical_report.json` 报 70 个 dual-format defects，其中 11 张全损；`audit_methodology.md` 和 `cluster_damage_assessment.md` 写 69/280。该 69/70 冲突必须保留，不能择一覆盖。
- 35 个标题连词、19 个多源卡、6 个长正文等只是 atomicity `suspects`，不是 confirmed failures。

**语义 coverage**：

- source-faithfulness：按 source-affinity 将 280-card 集合分派给 agents，可称 **card-set `full`**；但 10 张 knowledge-compounding cards 因 PDF 无法 section-level 验证，comparison cards 缺直接 source footnotes，且报告没有保留逐 claim 的完整公开 ledger。因此不能称 claim-level 全量证明。
- atomicity：机械召回后对 `suspects` 判断。
- cross-source leakage：概念/grep 初筛后只对具体 suspects 做语义判断。
- knowledge depth：标题、长度、coverage gap 是代理信号；没有“机制/边界/因果/反例/tradeoff 是否讲清”的全量 rubric。

**综合 verdict**：`v4_comprehensive_audit.md` 的 5 PASS / 3 PARTIAL 对 280 cards 和当时定义的 8 invariants 成立。它没有验证完整 extraction prompt propagation，也没有验证后增 48 cards。

### 3.5 Findings 的语义翻转

1. **Leakage 翻转**。`claude_code:claude-primary-v4:H032` 延续 grep 初判，把 `comparison-corrective-vs-servant-agency` 的“参与程度谱系”和“确认优先规则”都作为疑似泄漏。`claude_code:claude-primary-v4:H033` 在用户要求全文复核后翻转为：前者是 Karpathy gist 的合理意译，属 false positive；后者为 true leakage；GraphRAG 案例改判 provenance gap。`claude_code:claude-primary-v4:H034` 将协议改为 `grep miss → suspect → full-text semantic review`。修订记录在 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md` 第 8 节和 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/leakage_trace_corrective_vs_servant.md`。
2. **Cluster 假设翻转**。`claude_code:claude-primary-v4:H035` 与 `claude_code:claude-primary-v4:H036` 的专项审计没有确认“cluster 是硬边界”或“comparison 被限制在同域”；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md` 反而确认 69/280 dual-format、5 个孤儿、5/21 comparison leakage/provenance 问题，并部分确认跨域稀疏。正确结论不是“cluster 全面有害”，而是数量锚和局部实现造成特定损伤。
3. **Source balkanization 翻转**。`v4_deep_audit_blind_spots.md` 后验区分：wikibase 是真实 scope gap，knowledge-compounding 是 false alarm，ALCE 才是 bridge-link failure。高同源率不能机械等同治理失败。

这些翻转证明 `mechanical-filter` 的输出只能是 suspect；没有 semantic JUDGE 的 grep verdict 不应进入最终事实。

### 3.6 Source-pipeline audits

**`executed`**：`claude_code:claude-primary-v4:H038`、`claude_code:claude-primary-v4:H039`、`claude_code:claude-primary-v4:H040` 在首次 synthesis stalled 后重新分片完成 8-topic deep audit；`claude_code:claude-primary-v4:H042` 与 `claude_code:claude-primary-v4:H043` 把 scrape、repo、arXiv route 和 cross-family links 追到 pipeline stage；`claude_code:claude-primary-v4:H047`、`claude_code:claude-primary-v4:H048`、`claude_code:claude-primary-v4:H049` 再审计 collection pipeline，形成 74-source inventory 和 fix plan。

实际 coverage 分层如下：

| 检查 | 覆盖 | 说明 |
|---|---|---|
| 74 source directories 是否产卡、是否有可用 reading surface | `full` inventory | 发现 30/74 phantom sources；`data_collection_fix_plan.md` 后验评估约 44/74 有可靠阅读面 |
| authority hedge 词 | `full` proxy + `sample` semantic | 280 cards 全量词法统计得 174/280 零限定词；语义只抽 5 cards |
| says-vs-implies | `sample` | 两批共 10 cards、49 source footnotes；首批 13/26 reasonable inference，第二批 23/23 direct |
| silent disagreement | `full` within subtype | 21/21 comparison cards；19 neutral-acknowledged，2 neutral-but-framed |
| scrape lossiness | `sample`→定量扩展 | deep audit 先抽 5 sources；`pipeline_gaps_report.md` 再统计 1261 个结构元素损失，但不等于每个丢失元素均做语义影响判断 |
| graph balkanization/backlink asymmetry | `full` mechanical at 280 | 1021 edges、411 single-direction、40 zero-indegree；拓扑全量不等于每条边语义正确 |
| arXiv low-quality route、repo gaps、citation bridges | `suspect/full inventory` | 路径/引用统计全量召回 affected sets；对受影响卡没有逐张按全文重提取和再审 |
| extraction contract conformance | `not measured` | 审计追到 source router 和 governance，但没有逐 43-source 比较完整 skills、实际 prompt、轮次和 reviewer exit evidence |

`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md` 是重要 executed artifacts；`loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md` 则是 6 月 12 日 `retrospective`，其中“280 cards 完全按 script ingest”“四角色如设计执行”等表述与 `claude_code:claude-primary-v4:H010`、`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015` 及 0 review events 冲突，不能作为原始执行证明。

### 3.7 Remediation

**结构与内容修复**：`claude_code:claude-primary-v4:H037` 先形成 22 项 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_plan.md`，再执行 ScriptFix→TargetedEdit→AgentFix→Verify。当前 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json` 对 280 cards 记录：YAML 280/280 pass、orphan 0、JJ creation header 280/280；但当时仍有 2 broken related、3 footnote-integrity failures、1/21 comparison 无 source footnote。`claude_code:claude-primary-v4:H038` 随后要求修最后断链；Git `5d7586fc` 固化最后两条 related 修复。

**来源修复**：`claude_code:claude-primary-v4:H044` 报告 arXiv 路径、scrape flags、citation bridges 和 repo bundle/card 修复；`claude_code:claude-primary-v4:H045` 随即揭示 20 repos 中实际只处理 2 个，15 张新卡来自这两个 repo，原“repo 修复”只能标 `sample/partial`。`claude_code:claude-primary-v4:H046` 又明确 material bundle 只是 demo，repo→doc→card 尚未实现。

**collection remediation**：`claude_code:claude-primary-v4:H051` 修死源标记和 arxiv-ragas bundle，Reddit 仍因 403/OAuth 停止；`claude_code:claude-primary-v4:H052` 与 `claude_code:claude-primary-v4:H053` 将有效 webpage 的 raw HTML 转为 markdown，并对 19 个来源做增量重提取，13 sources 新增 33 cards、6 sources 判定已覆盖。Git `044312a2` 固化 23 份 markdown，具体路径包括 `data/raw/webpage/aillm-wiki-directory/markdown.md` 和 `data/raw/webpage/wikibase-data-model/markdown.md`，并固化新增 cards/JJ。

这些是 **新的修复运行**，不是对原 43-source 运行的追溯补证。尤其“增量只补遗漏”没有重跑完整 questioning/reviewer/fusion，也没有保存逐源 reviewer ledger。

### 3.8 Final 328-card snapshot

**`retrospective/current observation`**：当前 `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/cards/` 有 328 个 Markdown files，`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/justification/` 也有 328 个；`claude_code:claude-primary-v4:H053` 和 Git `044312a2` 支持 295→328 的增量。`claude_code:claude-primary-v4:H055` 的后验总结声称 328 active cards、1022 links，并生成 7 份 learnings。

**`contradicted`**：终态不是一个一致、全量验收过的 snapshot：

- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/indexes/cards.md` 仍写 `total_cards: 280` 和 861 links。
- `loops/v4_llm_wiki_loop_20260602/status.json` 仍为 `setup`。
- `loops/v4_llm_wiki_loop_20260602/loop_state.json` 仍为 `materials_processed: 0`、`cards_produced: 0`。
- 328 JJ 中当前只有 313 份标准 `## creation |`，`## review |` 为 0。
- `loops/v4_llm_wiki_loop_20260602/learnings/kb_health_snapshot.md` 明确 1022 links、264/280 linked ratio 和 3.3 density 都沿用 280-card governance 分母，后增 48 cards 尚未完全链接。
- 没有 328-card `mechanical_report`、`suspect_lists`、source-affinity JUDGE ledger 或综合 verdict。

因此“328 cards 存在”是终态文件事实；“328 cards 通过 V4 完整审计”是无证据命题。

## 4. 十项控制的 V4 实际覆盖

| Control | 最强实际覆盖 | 关键证据 | V4 总判定 |
|---|---|---|---|
| `source-eligibility` | source-pipeline 阶段对 74 directories 做 `full` inventory；原 43-source 入口无可靠 gate | `claude_code:claude-primary-v4:H049`、`claude_code:claude-primary-v4:H051`、`claude_code:claude-primary-v4:H053`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md` | 晚期发现并部分修复；原生产批次 `contradicted` |
| `source-faithfulness` | seed `sample` 3-5；Phase 4 `sample` 8；FSJS card assignment `full` 但 claim-level 有 PDF/ledger caveat；leakage 走 `suspect` | `claude_code:claude-primary-v4:H001`、`claude_code:claude-primary-v4:H011`、`claude_code:claude-primary-v4:H031`、`claude_code:claude-primary-v4:H033`、`claude_code:claude-primary-v4:H034`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md` | `partial`，不能表述为全库逐 claim 证明 |
| `inference-boundary` | 280-card hedge 词 `full` proxy；10 cards/49 footnotes `sample` semantic | `claude_code:claude-primary-v4:H040`、`claude_code:claude-primary-v4:H042`、`claude_code:claude-primary-v4:H043`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md` | `partial`；发现 174/280 零 hedge，未全库语义修复 |
| `schema-validity` | 280-card mechanical + repair verification `full` | `claude_code:claude-primary-v4:H031`、`claude_code:claude-primary-v4:H037`、`claude_code:claude-primary-v4:H038`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/mechanical_report.json`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json` | 280 snapshot 强；328 snapshot `not measured` |
| `fusion-boundary` | post-publication cluster/candidate `suspect` judgment；无逐对 ledger | `claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015`、`claude_code:claude-primary-v4:H016`、`claude_code:claude-primary-v4:H018`、`claude_code:claude-primary-v4:H035`、`claude_code:claude-primary-v4:H036`、`claude_code:claude-primary-v4:H037`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md` | 原 pre-promotion fusion `missed`，后置补救 `partial` |
| `graph-integrity` | 280-card graph `full` mechanical；关系语义和 328 增量未全审 | `claude_code:claude-primary-v4:H031`、`claude_code:claude-primary-v4:H037`、`claude_code:claude-primary-v4:H038`、`claude_code:claude-primary-v4:H040`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md` | 280 snapshot `partial/pass-with-scope`；328 `not measured` |
| `cross-source-leakage` | grep/concept `suspect`，全文语义只落到具体 comparison cases；15 comparison semantic TODO 中仅 2 已覆盖 | `claude_code:claude-primary-v4:H032`、`claude_code:claude-primary-v4:H033`、`claude_code:claude-primary-v4:H034`；`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/leakage_trace_corrective_vs_servant.md` | `partial`；发生至少 1 true leakage + 1 provenance gap |
| `state-consistency` | 当前可做 `full` 文件对账，但结果失败 | `claude_code:claude-primary-v4:H011`、`claude_code:claude-primary-v4:H031`、`claude_code:claude-primary-v4:H055`；`loops/v4_llm_wiki_loop_20260602/status.json`、`loops/v4_llm_wiki_loop_20260602/loop_state.json`、`loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/indexes/cards.md` | `contradicted`：328/280/0 多真值并存 |
| `pipeline-conformance` | 仅对 governance 和 collection 做局部 root cause；43-source 完整 skills/phase/quit-audit `not measured` | `claude_code:claude-primary-v4:H010`、`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015`、`claude_code:claude-primary-v4:H042`、`claude_code:claude-primary-v4:H049` | 核心漏检；最终文件不能替代 run evidence |
| `knowledge-depth` | atomicity/length/coverage suspects，deep audit samples 和用户阅读 probe | `claude_code:claude-primary-v4:H001`、`claude_code:claude-primary-v4:H031`、`claude_code:claude-primary-v4:H040`、`claude_code:claude-primary-v4:H042`、`claude_code:claude-primary-v4:H043` | `sample/proxy only`；从未成为发布 hard gate |

## 5. 为什么最终修复不能证明原始 pipeline conformance

1. **时间方向不可逆**：`fb7b4060`、`5d7586fc`、`d2ebcf41`、`044312a2` 都发生在 `d36f6f7a` 的 direct-to-KB 批次之后。后写正确 YAML 或 source path 不能证明原 agent 当时走过 draft、review、promotion、fusion。
2. **对象已变更**：FSJS 的核心分母是 280；终态是 328。修复、补卡和重提取改变了 cards、JJ、links 与 source surfaces，不能把终态 pass 投射到历史对象。
3. **结果证据不等于过程证据**：一个 accepted card、JJ 或 citation 只能证明文件存在。没有 per-source prompt、skill injection、round Q&A、SATISFIED、reviewer verdict、fusion verdict 和 promotion ledger，就不能证明生产合同执行。
4. **修复选择有偏**：repo remediation 最初表述为 repo 修复，`claude_code:claude-primary-v4:H045` 才揭示只处理 2/20；webpage 是增量补遗漏，不是全量重跑。局部成功不能外推未处理集合。
5. **语义结论会翻转**：参与程度谱系从 leakage 翻为 supported paraphrase；knowledge-compounding 从 source balkanization suspect 翻为 false alarm。最终修正文案不能抹除初始审计方法的误判率。
6. **状态与账本仍冲突**：328 files、280 index、0 state counters、313 standard creation headers、0 review headers同时存在。若终态尚不能自洽，它更不能作为历史过程的替代证明。
7. **后验设计文档会合理化历史**：`loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md` 把 full batch 描述成四角色、script ingest 和完整 JJ；这是 `retrospective`，并与 `claude_code:claude-primary-v4:H010`、`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015` 及仓库 ledger 缺口矛盾。后写“as-built”不是原始 run trace。

## 6. 可安全进入 Module Recall 的结论

1. V4 的 seed reviewer 是“coverage 全量 + source faithfulness 抽样”，不是全量语义审计。
2. 43-source full batch 是 43/43 production completion，不是 43/43 audit pass；它跳过了可证明的顺序 ingest/fusion/reviewer ledger。
3. Post-publication governance 扩大了图连接，也因 cluster 数量锚和非结构化 YAML 写入制造了新缺陷。
4. V4 在 280-card 快照上真实执行了 mechanical full scan、source-affinity shard/JUDGE 和 synthesis；对 source faithfulness 应表述为“card-set 分派全量、claim-level 有 caveat”，而不是无条件全量验证。
5. V4 的方法论关键进步是把 grep 结果降级为 suspect，并要求 full-text semantic review；至少一项 leakage finding 因此翻转。
6. Deep audit 把控制面从卡片格式扩展到 source eligibility、inference boundary 和 pipeline root cause，但 full extraction-contract conformance 与 knowledge depth 仍未成为稳定 gate。
7. Remediation 改善了 280-card 结构和部分 source surfaces；2-repo demo、Reddit failure、19-source webpage increment 都必须保留各自分母。
8. 328-card 只是最终修复快照，不是原始 pipeline conformance 的证明，也没有同级 FSJS 终验。

## 7. 主要证据索引

### Primary archived events

- Seed：`claude_code:claude-primary-v4:H001`
- 43-source full batch：`claude_code:claude-primary-v4:H010`
- 初始 governance 与用户反证：`claude_code:claude-primary-v4:H011`、`claude_code:claude-primary-v4:H012`、`claude_code:claude-primary-v4:H013`、`claude_code:claude-primary-v4:H014`、`claude_code:claude-primary-v4:H015`、`claude_code:claude-primary-v4:H016`、`claude_code:claude-primary-v4:H017`、`claude_code:claude-primary-v4:H018`
- 审计合同、负载失败与 FSJS：`claude_code:claude-primary-v4:H019`、`claude_code:claude-primary-v4:H020`、`claude_code:claude-primary-v4:H021`、`claude_code:claude-primary-v4:H022`、`claude_code:claude-primary-v4:H023`、`claude_code:claude-primary-v4:H024`、`claude_code:claude-primary-v4:H025`、`claude_code:claude-primary-v4:H026`、`claude_code:claude-primary-v4:H027`、`claude_code:claude-primary-v4:H028`、`claude_code:claude-primary-v4:H029`、`claude_code:claude-primary-v4:H030`、`claude_code:claude-primary-v4:H031`
- Leakage semantic review：`claude_code:claude-primary-v4:H032`、`claude_code:claude-primary-v4:H033`、`claude_code:claude-primary-v4:H034`
- Cluster adversarial/root-cause/remediation：`claude_code:claude-primary-v4:H035`、`claude_code:claude-primary-v4:H036`、`claude_code:claude-primary-v4:H037`、`claude_code:claude-primary-v4:H038`
- Deep audit 与 pipeline gaps：`claude_code:claude-primary-v4:H039`、`claude_code:claude-primary-v4:H040`、`claude_code:claude-primary-v4:H041`、`claude_code:claude-primary-v4:H042`、`claude_code:claude-primary-v4:H043`、`claude_code:claude-primary-v4:H044`、`claude_code:claude-primary-v4:H045`、`claude_code:claude-primary-v4:H046`、`claude_code:claude-primary-v4:H047`、`claude_code:claude-primary-v4:H048`、`claude_code:claude-primary-v4:H049`
- Source remediation 与 328 snapshot：`claude_code:claude-primary-v4:H050`、`claude_code:claude-primary-v4:H051`、`claude_code:claude-primary-v4:H052`、`claude_code:claude-primary-v4:H053`、`claude_code:claude-primary-v4:H054`、`claude_code:claude-primary-v4:H055`

### Repository artifacts

- `loops/v4_llm_wiki_loop_20260602/skills/reviewer/PROMPT.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/mechanical_report.json`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/suspect_lists.json`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_comprehensive_audit.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/leakage_trace_corrective_vs_servant.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/cluster_damage_assessment.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_plan.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/fix_verification.json`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/v4_deep_audit_blind_spots.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/pipeline_gaps_report.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/data_collection_fix_plan.md`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/audits/scrape_lossiness_flags.yaml`
- `loops/v4_llm_wiki_loop_20260602/outputs/llm_wiki/kb/indexes/cards.md`
- `loops/v4_llm_wiki_loop_20260602/status.json`
- `loops/v4_llm_wiki_loop_20260602/loop_state.json`
- `loops/v4_llm_wiki_loop_20260602/learnings/audit_methodology.md` (`retrospective`)
- `loops/v4_llm_wiki_loop_20260602/learnings/pipeline_actual.md` (`retrospective`, 部分 claim 被 primary evidence 反驳)
- `loops/v4_llm_wiki_loop_20260602/learnings/kb_health_snapshot.md` (`retrospective`)
