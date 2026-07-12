# V5 审计机制证据审计

## 结论摘要

V5 的审计机制不是一个单一、同时完成的控制面，而是三层证据叠加：预先写入 loop capsule 的控制设计（specified）、2026-06-12 主会话中报告的执行动作（executed），以及 2026-07-09 至 2026-07-12 由 Git 重排、事件归档和本次只读检查补强的事后证据（retrospective）。本审计不把工具文件存在、终态指标或后补提交等同于控制在原运行时按规定顺序执行。

最可靠的已执行结论是：V5 产生了可解析的 477 张 active cards；存在 source router、fusion、YAML、backlink/orphan 与 FSJS 相关工具和报告；主会话在被用户指出首轮审计未完成后，确实追加了机械审计和深层语义审计。最重要的否定性结论是：source completeness 的计数和状态未闭环，hedge preservation 没有做全量源卡逐对验证，163 对 fusion 缺少逐对裁决账本，YAML “每次修改后自动 gate”缺少触发日志，顺序治理的 `sorted(source_id, created_time)` 逐卡轨迹缺失，最终状态文件彼此冲突，且原审计合同没有覆盖 questioning 深度与信息密度退化。

## 证据口径

- **specified**：控制、阈值或失败动作写入 `task.md`、`LOOP_START_PROMPT.md`、skill 或审计方法，但没有足够证据证明按设计执行。
- **executed**：主会话事件明确记录动作或结果，并有对应运行产物；仍属于运行期报告（reported execution），不是原始命令日志。
- **retrospective**：由后补 Git 提交、回放事件、后验报告或本次只读检查确认；只能证明终态或后验判断，不能反推原运行顺序。
- Git `ca3865b7` 在 2026-06-12 一次性加入工具、卡片和审计档案，只能证明这些内容最迟在该提交时进入版本控制。2026-07-09 的 `1ed63fcc`、`226b2913`、`9e954607`、`ba6d5a56`、`2251069b` 按过程拆分提交，属于后验发布序列，不能单独证明 2026-06-12 的真实执行先后。
- `events.claude.primary-v5.v2.jsonl` 于 2026-07-12 生成，保留了用户锚定的助手窗口摘要，不是逐工具调用日志。`repo-loop-capsules` 和 `repo-git-history` 在 source registry 中均为 supporting evidence，不能替代原始交互顺序。

## Audit controls

### A. Source completeness

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| SC-1 来源路由完整性（source routing completeness） | `data/raw/{source_type}/{slug}` 的读取面与死源 | `source_router.py --scan-all`；按类型选择 bundle/markdown/text/README，并以 `<500B` 或 blocked/captcha/403 关键词拦截 | 每种 source type 至少一例路由正确；所有源均得到 `ok` 或可解释的 `failed` | failed 源不得进入 extraction；记录原因 | Phase 0，抽取前 | **specified + executed + retrospective**。H002 报告运行期为 74 total / 63 OK / 11 failed；本次只读复核得到相同结果 | H002 | `loops/v5_llm_wiki_loop_20260612/tools/source_router.py`; `.../LOOP_START_PROMPT.md`; `data/raw/` | `task.md` 仍全为未勾选项；没有保存当时 `--scan-all` 的机器可读 manifest。`repo2doc.py` 被规定为 Phase 0 条件但文件不存在，Git 后补说明也只加入 router 而非 repo2doc |
| SC-2 有效源消费完整性（source consumption） | routable source 是否至少产出一张 accepted card；失败源是否被状态表完整解释 | `audit_mechanical.py` D1/D2：比对 raw source、card `source_ids`、`loop_state.json` | 未消费源全部在失败清单中；未记录遗漏为 0；设计阈值 consumption >80% | 补录失败源及原因；对可路由但零产出的源重新抽取或显式豁免 | Phase 4 FILTER；发布前 | **executed（失败）+ retrospective**。机械报告为 62/74 consumed、12 unconsumed、12 unaccounted，D1 `pass:false` | H005, H006 | `.../tools/audit_mechanical.py`; `.../kb/audits/v5_mechanical_audit_report.json`; `.../kb/audits/v5_final_audit_report.md` | router 的 11 个 failed 之外，`repo-stanford-ares` 可路由但未消费；因此“63 valid/processed”与卡片实际覆盖 62 个 source_id 不同。终报虽列 D1 FAIL，又把 83.8% 纳入“6/6 核心通过”，判定口径冲突 |
| SC-3 失败源状态闭环（failed-source reconciliation） | `failed_sources` 数量、ID 列表、execution summary、version/source map | 交叉比对 `loop_state.json`、`execution_summary.md`、router 输出、version registry 与 source map | 数量与 ID 集合一致，修正保留版本关系而非覆盖；总源 = valid + failed 可复算 | 阻断 complete；保留冲突并指定权威字段/迁移规则 | 每次 source scan 后、Phase 5 固化前 | **specified + retrospective（未通过）** | H002, H005, H006 | `.../loop_state.json`; `.../learnings/execution_summary.md`; `docs/claude_interaction_replay/registry/version-registry.json`; `.../registry/source-map.json` | 当前同时存在 10/11/12 三种 dead-source 计数。`loop_state.failed_sources` 是整数 12，ID 却放在 `failed_source_ids`；`audit_mechanical.py` 只接受 `failed_sources` 列表，因此即使 ID 已补录仍报告 0 recorded。source map 正确标为 `confidence: conflicting`，未完成裁决 |

### B. Evidence basis and hedge

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| EH-1 `evidence_basis` 字段完整性 | 每张 card frontmatter 的证据类型 | YAML parser 读取；按枚举聚合；reframing/reviewer 检查字段 | 100% cards 有字段且值属于权威枚举；审计可按类别分层 | 阻断 ingest；回到 reframing 修复字段 | 每轮 reframe 后、ingest 前、Phase 4 | **specified + executed（字段已用于统计）+ retrospective** | H002, H005, H006 | `.../skills/reframing/PROMPT.md`; `.../tools/audit_mechanical.py`; `.../kb/audits/v5_mechanical_audit_report.json` | 设计文档称仅六类，但机械报告出现 `author_claim`、`normative_standard`、`documentation+code_implementation`，说明枚举未被强制。`yaml_lint.py` 与机械审计 C1 的 required keys 均未把 `evidence_basis` 作为必填 gate |
| EH-2 hedge preservation / authority flattening | 源中的 may/suggests/可能等限定是否在卡片保留；推断是否显式标注 | 设计要求 source-card 语义对照；实际主要以正文限定词词表统计 zero-hedge，并按 `evidence_basis` 分层；A4 says-vs-implies 由 agent shard 判断 | 源有 hedge 时卡片必须保留；EXTRAPOLATION 为 0；不适用类别应显式豁免而非用总体比例洗平 | 回到原文逐条修订；无法确认则降级为 caveat/hedged claim | reframe、reviewer quit-audit、Phase 4 JUDGE | **specified + executed（代理指标与分片语义审计）+ retrospective（合同不足）** | H003, H004, H005, H006, H008-H016 | `.../task.md`; `.../skills/reframing/PROMPT.md`; `.../kb/audits/audit_report.md`; `.../kb/audits/v5_final_audit_report.md`; `.../kb/audits/v5_info_density_diagnosis.md` | 79.8% zero-hedge 被改判 conditional pass，但没有全量“源含 hedge → 卡保留 hedge”的成对结果。机械报告当前分层数值又与初版报告不同。H014-H016 证明 citation/hedge 合规仍可产生未解释概念，原控制不覆盖解释充分性 |
| EH-3 源忠实与脚注锚定（evidence grounding） | `[^src-N]` 路径、位置、quote prefix 与原文语义；长段落是否有证据锚定 | 首轮每卡抽一条：431 条 grep；后续机械全量 848 条，705 matched、143 suspect；agent 抽样/语义判断；E2 无脚注段落筛查 | fabrication = 0；partial/false 源披露不可验证占比；无脚注长段落需 grounded 或 structural | suspect 进入 JUDGE；fail 修卡或降级 caveat；未验证子集不得宣称全量通过 | FILTER 后进入 SHARD/JUDGE，SYNTHESIZE 前 | **executed，但覆盖声明有争议** | H003-H006 | `.../kb/audits/filter_report.md`; `.../kb/audits/judge_faithfulness.md`; `.../kb/audits/v5_judge_results.md`; `.../kb/audits/v5_mechanical_audit_report.json` | 初版 431 是抽样，不是全脚注；终版把 848 全部称“机械 grep + 语义 JUDGE 双层验证”，但保存的语义明细只有 18 + 20 条 A1 样本，不足以证明 143 suspect 全量逐条 JUDGE。E2 仅抽 15/141 无脚注段落，终报已承认非全量 |

### C. Fusion

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| FU-1 fusion 候选召回 | 全量 draft 中跨 source 的 canonical/alias 重叠对 | `fusion_candidates.py` 建倒排索引，仅输出 source_ids 不相交的候选对 | 全量 extraction 落盘后扫描；候选可重现；不得与 extraction 并行 | 重跑全量 scan；解析失败或空 canonical 阻断裁决 | Phase 2 完成后、ingest 前 | **specified + executed（报告性证据）+ retrospective** | H002 | `.../tools/fusion_candidates.py`; `.../learnings/execution_summary.md`; `.../learnings/next_loop_prep.md` | 报告称 163 对，但没有保存候选清单、运行 stdout、输入 hash 或解析失败数；工具只用 exact normalized canonical/alias，不能证明语义重复召回完整 |
| FU-2 fusion 裁决与 anti-merge bias | 163 对候选的 duplicate / overlap_merge / distinct_link 决策及可追溯性 | agent 读卡裁决；superseded card 的 `superseded_by` 与 JJ；Git 比较 draft/active | 每对有 verdict、理由和目标；merge 信息无损；duplicate/merge 后 active 集合可复算 | 不确定时保留 distinct_link；缺理由不得 supersede；必要时恢复 draft | 候选生成后、ingest 前 | **executed（汇总）+ retrospective（终态可复核）** | H002, H007 | `.../outputs/llm_wiki/drafts/cards/`; `.../drafts/justification/`; `.../kb/cards/`; Git `ba6d5a56` / `ca3865b7` | 当前可见 488 top-level drafts、11 张 `status:superseded`、477 active cards；execution summary 另写“487 drafts，9 dup + 1 merge”，需要靠“1 fusion card”才能解释算术。153 个 distinct_link 与全部 163 对的逐对 ledger 未落盘，“审计未发现漏判 duplicate”也没有对应检查明细 |

### D. YAML

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| YA-1 frontmatter 解析与 related 格式 | 所有 active card 的 YAML、双格式 related、引用 slug | `yaml_lint.py --dir` 使用 `yaml.safe_load`；检测 inline/block 双格式及 invalid slug；机械审计 C1 再检查 | 0 parse error、0 dual-format、0 dangling related slug | 阻断 ingest/发布；由 parser 重写后重跑 | 设计为每次 frontmatter 修改后；至少在 Phase 3/4 gate | **specified + executed（终态报告）+ retrospective**。本次只读运行：477 files OK | H002, H005, H006 | `.../tools/yaml_lint.py`; `.../kb/audits/v5_mechanical_audit_report.json`; `.../kb/cards/` | 没有 pre-commit/hook 或逐次运行日志，不能证明“每次修改后自动验证”；只能证明保存报告和当前终态通过。task 的 22 个 checkbox 全部未勾选，无法作为阶段 gate 记录 |
| YA-2 schema 必填与类型一致性 | `id/title/source_ids/canonical_concept/related/summary/evidence_basis` 及枚举/类型 | YAML lint + schema-level validator | 必填字段齐全，列表/枚举类型正确，ID 与文件名策略明确 | 阻断 ingest；迁移不合规 frontmatter | reframe 后、ingest 前 | **specified + partially executed** | H002, H005 | `.../tools/yaml_lint.py`; `.../tools/audit_mechanical.py`; `.../skills/reframing/PROMPT.md` | `yaml_lint.py` 实际只验证 parse/related/ref；机械 C1 的必填字段也漏掉 `evidence_basis`。因此“YAML 0 error”不等于 schema contract 全通过 |

### E. Backlink / orphan

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| BO-1 dangling reference | `related` 与 body card refs 指向存在的 active card | 机械构图并检查目标 slug | 0 dangling | 修正 slug、恢复目标卡或移除错误边；重新 lint | 每轮 link mutation 后、Phase 4 | **executed + retrospective**：机械报告 1815 refs / 0 dangling | H002, H005, H006 | `.../tools/audit_mechanical.py`; `.../kb/audits/v5_mechanical_audit_report.json` | 报告只代表生成时终态；没有每次 mutation 后的 gate 记录 |
| BO-2 orphan 检测与补链 | 非 comparison 卡的出入度；`related:[]` 且无 inbound 的完全孤立卡 | 机械构图；orphan pass 对 canonical/aliases/key terms 全局 grep，人工判断后补 link | orphan rate <5%；设计目标通过补链趋近 0 | 对 orphan 与前 1/3 已处理卡回扫；无法合理链接则记录豁免 | batch link 后、backward backlink 前后、Phase 4 | **executed（报告）+ retrospective（冲突确认）** | H002, H005, H006 | `.../learnings/execution_summary.md`; `.../kb/audits/audit_report.md`; `.../kb/audits/v5_mechanical_audit_report.json` | execution summary/loop_state 写 0%，机械终报写 2/468（0.4%）；两者不能同时作为同一终态事实。81 张 orphan 的逐卡发现、候选和补链 ledger 未保存 |
| BO-3 backlink 对称性与修复 | 每条 A.related→B 是否有 B→A；comparison/distinction sink 例外 | `backward_backlink.py` parser 读写；机械审计 B3 复算 | 初始 task 阈值 <25%；终报采用 <5%；例外集合明确 | 自动补对称边；剩余单向边逐条说明例外 | batch link/orphan 后独立 pass；发布前复算 | **executed（报告）+ retrospective** | H002, H005, H006 | `.../tools/backward_backlink.py`; `.../tools/batch_link.py`; `.../kb/audits/v5_mechanical_audit_report.json`; `.../learnings/execution_summary.md` | 报告称补 423 条、最终 9/1815（0.5%）不对称，但没有修复前图快照或运行日志。脚本没有 dry-run/transaction/audit log，且会无条件为所有 related 边补反向边，未实现文档中的 comparison/distinction 例外判断 |

### F. FSJS

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| FS-1 FILTER | 全卡机械可检项：脚注、YAML、图、source coverage、JJ、跨源泄漏 suspect 等 | `audit_mechanical.py` + 初版 grep filter | 全量机械项有 denominator、suspect 清单和 pass/fail；grep miss 只标 suspect | FAIL 不得直接改写为 PASS；suspect 进入 JUDGE | Phase 4 起点 | **executed（分两轮补全）** | H003, H004, H005 | `.../kb/audits/filter_report.md`; `.../kb/audits/v5_mechanical_audit_report.json`; `.../kb/audits/v5_suspect_list.json` | H003 明确认定首轮只完整做了 FILTER/SYNTHESIZE，且 FILTER 当时仅每卡抽一条。后续扩展到 16 个机械维度，但 JSON 中 A1 与 D1/F2 仍为 `pass:false`，终报的“机械审计 PASS”表述过宽 |
| FS-2 SHARD | suspect 按 source affinity/source type 分片，限制每个判断上下文 | arxiv/webpage/github_repo/other 四 shard；后续 A4 与 leakage 另设 agent | 每个 suspect 唯一归属；分片输入、数量、模型和输出可追溯 | 重新分片；超上下文则继续拆分 | FILTER 后、JUDGE 前 | **specified；首轮未完整执行；H006 后报告 executed** | H003, H004, H006 | `.../task.md`; `.../learnings/execution_summary.md`; `.../kb/audits/v5_final_audit_report.md` | 没有 shard manifest、agent prompt、逐 shard 输入 hash 或完整结果文件。execution summary 说 18 suspects 分给 3 agents，每人 6 条；终报又说 4-shard says-vs-implies，属于不同任务但表述容易混同 |
| FS-3 JUDGE | grep suspect、上下文保真、says-vs-implies、跨源泄漏、无脚注段落 | agent 读原文语义判定 semantic-pass / caveat / fail | 所有 hard-gate suspect 关闭；抽样项明确抽样率和外推限制 | fail 回到卡片修复；未判项保持 open，不得由综合节点代判 | SHARD 后 | **executed（部分全量、部分抽样）** | H005, H006 | `.../kb/audits/judge_faithfulness.md`; `.../kb/audits/v5_judge_results.md`; `.../kb/audits/v5_final_audit_report.md` | 18 条初版 suspect 有逐条记录；20 条 A1 与15条 E2 是抽样。对 143 个扩展 A1 suspects、50 个 leakage suspects 和 A4 四 shard，终报给出整体结论但缺少同粒度逐条证据，不能验证是否全量关闭 |
| FS-4 SYNTHESIZE 与 gate | 所有机械/语义 finding、阈值、例外与 residual risk | 汇总 `audit_report.md` 和 `v5_final_audit_report.md`；按 severity 形成结论 | hard fail 为 0；conditional/marginal 不得计入无保留通过；结论与底层 JSON 一致 | 保持 Phase 4 未完成；修复后重跑，不可仅改文案 | JUDGE 后、Phase 5/发布前 | **executed，但判定一致性未通过** | H003-H006 | `.../kb/audits/audit_report.md`; `.../kb/audits/v5_final_audit_report.md`; `.../loop_state.json` | 初报 3/5 hard metrics，终报写 6/6；但底层 D1、A1 mechanical、F2 仍 false，终报自身又列 D1 FAIL、E2 conditional、B4/F2 marginal。`loop_state` 还写 orphan 0% 与所有域 bridge PASS，与终报 2 orphan/早期 HN marginal 不一致 |
| FS-5 质量合同完整性（quality-contract completeness） | 审计是否覆盖 questioning 深度、论证结构、概念解释充分性和 runtime skill 注入 | 后验六路 probe + synthesis；指定卡逐例检查；v4/v5/修正版 A/B | 审计必须能发现 Phase 3-4 questioning/quit-audit 未执行、空壳原子卡和引用存在但解释不足 | 质量 gate 失败；停止把 V5 视为合格基线，选择性重提取或治理降级 | 原应在 Phase 4；实际在用户质疑后 | **retrospective only（原审计漏检）** | H008-H016, H018-H020 | `.../kb/audits/v5_info_density_diagnosis.md`; `.../tools/extract_prompt_v2.md`; `.../drafts/cards/experiment/` | H010 修正此前说法：Workflow agent 只收到约 50 行骨架，完整 questioning/reader/reframing/reviewer 未进入运行上下文。原“26 子项全覆盖”没有覆盖 pipeline conformance 与信息密度，因此不能证明 V5 入库质量达到 v4 |

### G. 状态一致性与顺序治理

| ID | 审计对象 | 检查方法 / 工具 | 通过条件 | 失败动作 | 运行时机 | 状态 | 关联 event_id | artifact 路径 | 已知缺口 |
|---|---|---|---|---|---|---|---|---|---|
| ST-1 阶段状态一致性 | `task.md` frontmatter/checklist、`status.json`、`loop_state.json`、报告总判定 | 结构化读取并比较 phase/status/count/audit 字段 | 所有状态文件同一 phase；完成项有勾选或机器事件；底层 hard fail 时不得标 complete | 阻断 Phase 5/发布；由单一状态机原子更新所有视图 | 每阶段 transition、最终发布前 | **retrospective（未通过）** | H002, H005-H007 | `.../task.md`; `.../status.json`; `.../loop_state.json`; `.../kb/audits/v5_final_audit_report.md` | 当前 `task.md` frontmatter 为 complete 但 22 项全未勾选；`status.json` 仍是 setup；`loop_state.json` 是 complete；Git 只显示 loop_state 从 setup 直接到 complete，没有 `phase1_ready` 等中间状态。终报底层仍有 fail/marginal |
| ST-2 指标与 denominator 一致性 | 74/63/62 source、487/488/477 card、431/848 footnote、0/2 orphan、1813/1815 edge | 跨报告、JSON、文件计数、Git commit stat 复算 | 同一指标有名称、scope、timestamp、denominator；修订须 supersede 旧值并保留理由 | 标记 conflicting；禁止无限定复用指标 | 每次报告生成、registry 更新时 | **retrospective（未通过）** | H002, H005, H006, H013 | `.../learnings/execution_summary.md`; `.../kb/audits/*.md`; `.../kb/audits/v5_mechanical_audit_report.json`; `docs/.../registry/source-map.json` | 多组数字代表不同 scope，但原报告未稳定标注 scope/time。source map 只显式收录 dead-source 冲突，尚未收录 card/footnote/orphan/edge 分母冲突 |
| OR-1 阶段顺序（phase ordering） | setup → extraction → post-extraction fusion → ingest → governance → audit → docs | phase gate；Git/事件/产物时序交叉检查 | 前一阶段 gate 通过后才能进入下一阶段；保留 transition timestamp 与输入 hash | 回滚到上一逻辑阶段（不回退他人文件）；重跑缺失 gate | 每个 phase boundary | **specified + executed（主会话报告）+ retrospective（无法强证）** | H002, H003-H007 | `.../task.md`; `.../LOOP_START_PROMPT.md`; Git `624e52d0`, `ca3865b7`, `9e954607`, `ba6d5a56`, `2251069b` | 2026-06-12 的单一归档提交没有阶段粒度；2026-07-09 的拆分提交顺序合理但属后验。无 transition log、命令时间戳或 artifact hash，不能把设计顺序写成已证实运行顺序 |
| OR-2 fusion 与 extraction 隔离 | 全量 extraction 完成前不得运行跨源 fusion | 检查 fusion 输入集合冻结点、draft 数量和后续修改时间 | fusion 输入 manifest 固定；全量 draft 落盘后才扫描 | 若并行污染则废弃候选结果并重跑 | Phase 2/2b 边界 | **specified + executed（报告性证据）** | H002 | `.../task.md`; `.../LOOP_START_PROMPT.md`; `.../learnings/execution_summary.md`; Git `9e954607`→`ba6d5a56` | 缺少冻结 manifest 和原始运行时间；只能依据事件摘要与后补 Git 序列判断，不能排除 extraction 与 fusion 有交叠 |
| OR-3 逐卡顺序治理（sequential per-card governance） | `sorted(cards, key=(source_id, created_time))` 的逐卡 global grep、读命中、关系判断、写 footnote | 设计要求逐卡轨迹；实际工具 `batch_link.py` 按候选对批量写、`backward_backlink.py` 全图补边 | 每张卡有顺序号、查询词、命中集、判断与 mutation；前 1/3 回扫完成 | 缺轨迹则不得宣称按指定顺序治理；补做审计或改称 bulk graph repair | fusion/ingest 后、audit 前 | **specified；执行仅有汇总自述，证据不足** | H002 | `.../task.md`; `.../tools/batch_link.py`; `.../tools/backward_backlink.py`; `.../learnings/execution_summary.md` | 代码中没有 `(source_id, created_time)` 排序治理器，也没有逐卡 global-grep ledger。现有脚本按文件名/候选对排序并批量修改 metadata；这能证明 bulk link repair，不足以证明规定的 sequential per-card governance 已执行 |
| OR-4 mutation 后 gate 顺序 | fusion/ingest/link/orphan/backward 每步后运行 YAML、dangling、orphan、asymmetry 检查 | 每步产出 before/after report；失败即停止下一步 | 每次写入均有零 YAML error；最终图指标与最后一次 mutation 对齐 | 停止后续 mutation；修复并重跑全部下游 gate | 每个写操作后 | **specified；终态 executed；中间 gate 无证据** | H002, H005, H006 | `.../tools/yaml_lint.py`; `.../tools/audit_mechanical.py`; `.../kb/audits/` | backward 脚本本身会重写 YAML，但不调用 yaml_lint；batch_link 也不调用 gate。没有 orchestration wrapper 或 CI 记录，无法证明“写入→校验→再继续”的顺序纪律 |

## 总体判定

1. **可确认执行（executed with artifacts）**：source routing、active KB 落盘、fusion 后 supersede 终态、YAML 终态解析、机械图审计、首轮 18 条 faithfulness JUDGE、后补 FSJS 报告。
2. **仅能确认终态或后验（retrospective）**：477 cards 当前 YAML 全通过、74/63/11 router 结果、62 个 source_id 被消费、2 orphan、9 asymmetric edges、状态文件冲突、信息密度退化及 runtime skill 注入断点。
3. **不可写成已执行事实（specified but unproven）**：每次 frontmatter 修改后自动 lint、完整 `evidence_basis` 枚举 gate、全量 source-card hedge preservation、163 对 fusion 逐对裁决留痕、按 `(source_id, created_time)` 的逐卡顺序治理、每阶段 transition gate、143 个扩展 faithfulness suspects 的逐条语义关闭。
4. **V5 audit 的最终可信表述**：它充分证明了若干机械终态健康指标，但没有证明原 extraction/questioning 流程合规，也没有证明内容解释充分。因而“6/6 核心指标通过”只能视为当时的综合报告结论，不能升级为“V5 整体质量审计通过”。
