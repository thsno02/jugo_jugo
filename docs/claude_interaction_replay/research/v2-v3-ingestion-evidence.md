# LLM Wiki V2-V3 入库机制证据审计

## 1. 审计范围与判定口径

本文审计 V2-V3 从本地来源到知识库的入库机制（ingestion mechanism），范围只包括：

- V2/V3 loop capsule 与产物；
- Codex V2 boundary、V2-V3 handoff 的 primary events；
- Claude V3 primary events；
- `version-registry.json`；
- Git 提交历史与当前工作树。

稳定阶段统一映射为：`source-route/acquisition`、`questioning-extraction`、`reframe-drafts`、`scripted-ingest/promotion`、`fusion-decision`、`graph-governance`、`publish-kb`、`failure-feedback`。这里的 `promotion` 必须区分两个目标面：

1. loop 内发布：`outputs/llm_wiki/drafts/` → `outputs/llm_wiki/kb/`；
2. 稳定产品发布：loop capsule → 仓库根 `llm_wiki/`。

证据状态使用四类标签：

- **specified**：用户输入、合同、prompt、runbook 或模板明确要求；只证明设计。
- **executed**：primary event、运行产物和 Git 快照能共同证明动作发生。
- **retrospective**：执行后形成的报告、审计、registry 或 future plan；可解释结果，不能倒写成原始运行合同。
- **contradicted**：规范、执行产物或后验审计互相冲突；必须并列保留，不静默选边。

事件短名沿用文件内编号，例如 V3 `H026` = `claude_code:claude-primary-v3:H026`；V2 handoff `H008` = `codex:codex-primary-v2-v3-handoff:H008`。Replay 目录在本次审计时整体仍是 Git 未跟踪内容，因此 event 与 registry 是当前工作树证据，不是既有提交本身；Git 事实另列。【证据：`docs/claude_interaction_replay/events/events.codex.primary-v2-boundary.v2.jsonl`；`docs/claude_interaction_replay/events/events.codex.primary-v2-v3.v2.jsonl`；`docs/claude_interaction_replay/events/events.claude.primary-v3.v2.jsonl`；`docs/claude_interaction_replay/registry/version-registry.json`；`git status --short`】

## 2. 总结论

1. **V2 实际跑通的是旧式逐卡链，不是后来定义的完整 scoped-card pipeline。** 原始链按单来源挖掘候选，再逐卡 `draft → audit → adoption`，约 7 小时采纳 15 张卡；之后才因吞吐和信息密度问题提出 batch draft、Jieba/Jaccard Top-3、comparison provenance 三问和 scoped card 合同。V2 结束时只有 1 张旧草稿进入 backlog，仍为 `similarity_pending`；没有 V2 similarity/comparison 产物，15 张 accepted 卡也没有迁移到 `CARD_CONTRACT_V2.md` 的 metadata。【证据：V2 handoff `H003`-`H010`、`H023`；`loops/v2_llm_wiki_loop_20260525/queues/draft_backlog.md`；`loops/v2_llm_wiki_loop_20260525/loop_state.json`；`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/`】

2. **V3 确实执行了 draft-first 批处理。** 首轮 1 个材料生成 4 张 draft；随后 72 个 material 全部获得状态，43 个可读来源产出 171 张 draft，22 个空源和 7 个上游阻塞未产卡；171 份 draft provenance、similarity、comparison 与 loop-local accepted KB 均存在。【证据：V3 `H001`、`H005`、`H006`、`H009`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`；`loops/v3_llm_wiki_loop_20260525/audits/pipeline_integrity_audit.md`】

3. **V3 的 Top-3 被执行了，但比较对象与后来确认的设计目标矛盾。** 171/171 similarity JSON 都只把 15 张 V2 卡作为比较基；工具硬编码 `V2_INDEX`，comparison worker 又禁止读兄弟 draft。`H026` 后验审计确认 V3 从未做 intra-V3 comparison/dedup。因此“171 次 Top-3 executed”成立，“V3 对自身做 duplication/fusion gate”不成立。【证据：V3 `H026`；`loops/v3_llm_wiki_loop_20260525/tools/similarity_top3.py`；`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`；`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/similarity/`】

4. **comparison provenance 完整落盘，但它主要记录跨版本比较，不是 V3 集合内去重 ledger。** 171 份 comparison 均回答三问，给出 163 `new_card`、8 `provenance_delta`、0 `merge_candidate`；8 个 delta 后续通过 fusion audit 并在 V3 provenance/body/related 中指向 V2。但 `merge_candidate=0` 的含义不是“检查后无融合”，而是 V3 兄弟卡根本没有进入候选池。【证据：V3 `H006`、`H026`；`loops/v3_llm_wiki_loop_20260525/outputs/llm_wiki/drafts/comparison/`；`loops/v3_llm_wiki_loop_20260525/audits/comparison_corpus_drift_audit.md`】

5. **V2/V3 都没有真正的 scripted ingest。** V2 `card_adoption_worker`、V3 六个 adoption workers 都由 agent 读工件、改状态并写 KB；脚本只负责 batch list、similarity、metadata/index 或 Git hook。V3 的 index 在 classifier 阻塞后甚至由 fallback agent 手工组装。不得把“有辅助脚本”表述为“内容通过确定性 ingest script 发布”。【证据：`loops/v2_llm_wiki_loop_20260525/task_templates/card_adoption_task.md`；`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/tools/build_adopt_batches.py`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`】

6. **Citation/related 的最终形态是执行后的迁移，不是原始 draft 合同。** 5 月 26 日先由 agent 手工为 drafts 形成 974 条 `related` 边；5 月 28 日才把 KB 迁到 unified Footnotes，加入 504+ 个 KB-internal footnotes，并由脚本规则或 fallback agent 派生 `related`。当前 171 张 drafts 仍同时保留 `## References`，171 张 KB cards 已没有 `## References`；draft 与 KB 是两个 schema 世代。【证据：V3 `H007`、`H019`、`H020`；`loops/v3_llm_wiki_loop_20260525/CARD_CONTRACT_V3.md`；`loops/v3_llm_wiki_loop_20260525/tools/derive_metadata_from_footnotes.py`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`】

7. **loop-local KB 发布已执行，稳定 KB promotion 未执行。** V2 有 15 张 loop-local accepted 卡，V3 有 171 张；两版都没有在本轮把候选产物 promotion 到仓库根 `llm_wiki/`。`version-registry.json` 的 “V2 未 promoted” 与 V3 “171 accepted”应按这两个发布层级解读。【证据：V2 handoff `H031`；V3 `H001`、`H009`；`loops/v2_llm_wiki_loop_20260525/README.md`；`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`；`docs/claude_interaction_replay/registry/version-registry.json`】

8. **Questioning-extraction 不属于 V2/V3 原始生产。** V2 是 source-mining fact candidates，V3 是 reader/batch worker 直接从全文写 draft；questioner↔reader、退出审计、Justification Journal 是 6 月 1-4 日的后验设计，进入 V4/future plan，不能用于为 171 张 V3 卡背书。【证据：V2 handoff `H001`-`H003`；V3 `H057`-`H079`；`loops/v3_llm_wiki_loop_20260525/future_plans/questioning_loop_design.md`】

## 3. 版本变化与证据强度

| 版本变化 | registry / 设计叙事 | 可证实执行 | 判定与缺口 |
|---|---|---|---|
| V1 → V2 | 主题 hub → bottom-up scoped knowledge cards；保留 provenance/source-driven；增加 control plane、brain mailbox、scoped-card contract。【证据：`version-registry.json` V2；V2 boundary `H046`-`H048`】 | 先按 `atomic_fact_card` 逐卡生产 15 张 accepted cards；每张有独立 provenance 与 audit chain。【证据：V2 handoff `H001`-`H004`；Git `f33dc4f1` 至 `237f5efc` 等 draft/audit/adoption commits】 | **contradicted**：15 张是 scoped-card 合同形成前的旧式产物；当前卡片 0/15 具备 V2 合同要求的 `id/title/card_type/tags/source_ids/provenance_card/aliases/related` 行首 metadata。registry 的 “scoped cards” 更接近最终设计标签，不是 15 张卡的执行态。【证据：`CARD_CONTRACT_V2.md`；`outputs/llm_wiki/kb/cards/`；`queues/draft_backlog.md`】 |
| V2 内部重构 | 写一张审一张 → material 先批量 draft，再 Top-3、comparison、publication/fusion audit。【证据：V2 handoff `H005`-`H010`、`H023`；`LOOP_DESIGN_V2.md`】 | 合同、runbook、brain mailbox 和 1 个 batch dispatch 被创建；candidate 11 进入 backlog。【证据：Git `992fdf1f`、`9c10bfab`；`iterations/iteration_20260525_0064_card_batch_drafting_karpathy_launch_remaining_a/`】 | **specified, not executed end-to-end**：batch iteration 只有 task/dispatch，无 delivery；candidate 11 仍 `similarity_pending`，无 similarity/comparison/fusion artifact。【证据：`queues/draft_backlog.md`；`loop_state.json`】 |
| V2 → V3 | 保留 scoped card/provenance，增加 draft-first、Top-3、fusion gate、统一 citation，替换重控制串行生产。【证据：`version-registry.json` V3；V2 handoff `H033`-`H044`】 | 171 drafts → 171 comparisons → interlinks → 171 loop-local KB cards；后做 unified citation migration。【证据：V3 `H001`、`H005`-`H009`、`H020`；`pipeline_integrity_audit.md`】 | **executed with drift**：draft-first 成立；Top-3 语料与 intra-V3 去重目标冲突；actual merge 为 0；citation 统一是后迁移；adoption 是 agent 操作而非 script-only ingest。【证据：V3 `H025`、`H026`、`H036`】 |
| V3 → future/V4 handoff | collect→extract→ingest→evolve；questioner-reader/reviewer；grep-first fusion；JJ 与 typed footnotes。【证据：V3 `H041`、`H057`-`H079`】 | 形成 future plan、questioning design、metadata/JJ contracts 与 V4 task/environment。【证据：Git `d1bfaa2c`、`df5751be`；`loops/v3_llm_wiki_loop_20260525/future_plans/`】 | **retrospective/future only**：不属于原始 171-card 生产，不可回填为 V3 executed mechanism。 |

## 4. 八阶段稳定映射

| 稳定阶段 | V2 状态 | V3 状态 | event_id / artifact / 缺口 |
|---|---|---|---|
| `source-route/acquisition` | **executed**：从本地 manifest 选 1 个 `status: ok` 来源，source-mining worker 产 fact candidates；不做网络 acquisition。【证据：V2 handoff `H001`、`H002`】 | **executed**：首轮精确路由到 1 个指定材料；后续对 72 条 material 排队，43 可读、22 empty、7 upstream blocked。没有 source-type router，也没有补采 blocked source。【证据：V3 `H001`、`H002`、`H005`；`queues/material_queue.md`】 | V2 artifact：`iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`、`iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`。V3 artifact：`queues/material_queue.md`、`source_access_log.jsonl`。缺口：acquisition 与 routing 混在 material queue；V3 blocked sources 仅记账。 |
| `questioning-extraction` | **executed extraction / not specified questioning**：source-mining 直接提取 12 个候选，再逐候选 draft。【证据：V2 handoff `H002`】 | **executed extraction / contradicted as questioning**：batch workers 直接全文读源并写卡；首轮防御性切片导致 14 篇 arXiv 后半段遗漏，revision pass 再补 34 张。【证据：V3 `H005`；`reports/loop_report.md`】 | Questioner-reader 是 `H057` 后的 future design。原始 V3 没有 per-source Q&A、SATISFIED、questioner quit 或 reviewer quit-audit artifact。【证据：V3 `H057`-`H071`；`future_plans/questioning_loop_design.md`】 |
| `reframe-drafts` | **executed old format; specified new format**：旧 worker 将 candidate 重构成 draft/provenance；15 张经审计采纳。V2 scoped-card metadata、自由正文和信息密度规则在生产后才落地。【证据：V2 handoff `H003`、`H008`-`H010`、`H023`】 | **executed**：material 先成 knowledge-dense drafts，不先读全 KB；4 → 171，并有同名 draft provenance。【证据：V3 `H001`、`H005`；`outputs/llm_wiki/drafts/{cards,provenance}/`】 | V2 新格式唯一 backlog card 仍待 metadata/Top-3/comparison。V3 draft 当前仍是 pre-unified-citation schema，不能当作最终 KB 的可重放输入。【证据：V2 `queues/draft_backlog.md`；V3 drafts 与 KB cards】 |
| `scripted-ingest/promotion` | **not executed as script; executed agent adoption**：adoption worker 在 audit pass 后写 card/provenance/index 并改 `accepted`。【证据：`loops/v2_llm_wiki_loop_20260525/task_templates/card_adoption_task.md`；`loops/v2_llm_wiki_loop_20260525/iterations/iteration_20260525_0062_card_adoption_wiki_health_checks/loop_delivery.md`】 | **not executed as script; executed agent adoption**：6 个 Opus workers 做 163 publication gates + 8 fusion audits，复制/改状态/写 accepted provenance；PostToolUse hook 只负责 commit。【证据：V3 `H008`、`H009`；`loops/v3_llm_wiki_loop_20260525/task_templates/adoption_worker_prompt.md`；`loops/v3_llm_wiki_loop_20260525/hooks/commit_card.sh`】 | `build_adopt_batches.py` 只分批，不 ingest；`build_kb_index.py` 因 classifier 阻塞未运行，index 由 fallback agent 组装。根目录 promotion 两版均未执行。【证据：`loops/v3_llm_wiki_loop_20260525/reports/loop_report.md`】 |
| `fusion-decision` | **specified, not executed in V2 design**：Top-3 后三问，动作含 `new_card/merge_candidate/provenance_delta/duplicate_skip`；merge/delta 必须审计并回链 A provenance。【证据：V2 handoff `H006`-`H008`；`LOOP_DESIGN_V2.md`】 | **partially executed / contradicted**：171 comparisons 对 V2 候选给出 163 new + 8 provenance delta；8 个 delta 过 fusion audit；实际 merge=0，intra-V3 fusion 未发生。【证据：V3 `H006`、`H009`、`H026`；`comparison_corpus_drift_audit.md`】 | V2 无 comparison ledger。V3 有完整 cross-version ledger，但没有 draft-vs-draft candidate/decision ledger；后验审计估计约 15-20 张近重复，最强簇是 4 张“三层架构”。 |
| `graph-governance` | **specified lightly / little executed**：V2 contract 有 optional `related`，fusion 后应回链 provenance；当前 15 cards 无 `related` metadata。【证据：`CARD_CONTRACT_V2.md`；V2 KB cards】 | **executed in two generations**：先 agent 手工添加 974 条 related 边；后将 KB-internal card citation 迁入 body Footnotes，再派生 related，170 张变更、1 张恒等、4 张合法空。【证据：V3 `H007`、`H019`、`H020`；`derive_metadata_from_footnotes.py`】 | **contradicted lineage**：初始 `related` 是手工治理，最终 `related` 才是 footnote-derived。Drafts 保留旧 related/References，KB 是统一 Footnotes；同一卡存在两个图版本。 |
| `publish-kb` | **executed loop-local / not promoted stable**：15 张进入 V2 capsule KB，未进入 root stable product。【证据：V2 handoff `H003`、`H031`；`outputs/llm_wiki/kb/`】 | **executed loop-local / not promoted stable**：171/171 accepted，index 已建；root `llm_wiki/`、registry/current-loop promotion 被明确留给人工。【证据：V3 `H009`；`reports/loop_report.md`】 | `version-registry.json` 的 accepted count 证明最终快照，不证明根目录发布。当前 loop-local KB 是 candidate product surface。 |
| `failure-feedback` | **executed**：delivery marker 缺失、路径边界、adoption template 等失败触发最小修复→独立审计→接受；最终吞吐问题触发整套 V2/V3 重构。【证据：V2 handoff `H002`-`H005`；Git `cce4cab4`、`eb47b963`、`bb965155`-`cd74a507`】 | **executed, mostly post-hoc**：全文截断触发 revision；英文标题/Jaccard miss 被复核；provider 额度中断后续跑；classifier 阻塞触发 fallback；V2-only corpus 在 `H026` 才被发现；citation 模型在发布后迁移。【证据：V3 `H008`-`H010`、`H020`、`H023`-`H026`】 | 修复并不都回写原始阶段：V3 self-comparison 缺口仍存在；draft schema 未同步 final KB；future questioning/JJ 只进入下一版设计。 |

## 5. 专项核对

### 5.1 V2 scoped cards：设计标签与产物世代不一致

**specified**：V2 scoped card 应是可独立理解的 bounded idea / distinction / mechanism / operational rule；要求固定 metadata，正文不应只是标题复述，References 为 source-level citation，Footnotes 为 inline locator。生产链应先 material→scoped draft+provenance，再 Top-3 与 comparison 三问。【证据：V2 handoff `H008`-`H010`、`H023`；`CARD_CONTRACT_V2.md`；`LOOP_DESIGN_V2.md`】

**executed**：15 张 accepted cards 来自此前的逐候选链，正文仍使用 `statement/fact_type/support/scope/status/provenance` 列表格式；例如 `llm-wiki-three-layer-architecture.md` 是一张 `known_fact`，没有 V2 新合同的 frontmatter。Git 在 03:01-09:49 之间持续记录 draft/audit/adoption，V2 设计直到 16:19 的 `9c10bfab` 才进入历史。【证据：Git `fa12054e`、`b8687a66`、`1ace57af` 至 `237f5efc`；Git `9c10bfab`；`outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md`】

**contradicted**：`version-registry.json` 把 V2 artifact 概括成 “候选 KB 和 v2 合同；未 promoted”，这在版本叙事上合理，但不能据此认定候选 KB 已遵守 scoped-card V2 合同。当前 15 张卡中没有任何一张具备 `id/title/card_type/tags/source_ids/provenance_card/aliases/related` 的合同字段；V2 backlog 还明确写 candidate 11 需要补 metadata、Top-3 和 comparison 后才能 publication。【证据：`version-registry.json`；`queues/draft_backlog.md`；`outputs/llm_wiki/kb/cards/`】

**结论**：安全表述是“V2 先证明逐卡可审计生产，后形成 scoped-card 设计并把它交给 V3”；不能写“V2 已用 scoped-card+Top-3 批量生产 15 张卡”。

### 5.2 V3 draft-first：主链成立，但 draft 不是最终格式

**specified**：首轮明确只做 `material → knowledge-dense draft cards → draft provenance → title similarity Top-3 → backlog/state`，禁止在同一 pass 中 adoption/fusion。Production 阶段不读 V2 body，只允许 similarity 读 V2 title index。【证据：V3 `H001`；`LOOP_START_PROMPT.md`；`CONTEXT_BOUNDARY.md`】

**executed**：首轮产生 4 卡；之后批量处理并 revision 到 171 卡。Git 先有大量 `v3 draft card: <id>` commits，随后 `29f41f3e` 固化 first-pass/revision bookkeeping，再由 `02715928` 固化 171 comparisons、`bf1e8101` 固化 interlinks。这一顺序支持 draft-first 确实先于 comparison/interlink。【证据：V3 `H001`、`H005`-`H007`；Git `2a44b0e4` 等 per-card commits、`29f41f3e`、`02715928`、`bf1e8101`】

**版本分叉**：当前 171 drafts 全部仍有 `## References` + `## Footnotes`，状态都是 `draft`；171 KB cards 全部 `accepted`、只有 `## Footnotes`。因此 V3 的最终 citation/related 状态不是“重跑 adoption 即可由 draft 再生”的确定性产物；需要重放 5 月 28 日迁移才能得到当前 KB。【证据：`outputs/llm_wiki/drafts/cards/`；`outputs/llm_wiki/kb/cards/`；`task_templates/citation_migration_worker_prompt.md`】

### 5.3 Similarity Top-3 与 comparison provenance

**specified**：标题用 Jieba 分词，按 Jaccard set similarity 排序取 Top-3；similarity 只是 pre-check，不判断 truth、duplicate、fusion 或 publication。影响路由的比较必须回答“为何相同、哪里不同、下一步依据”。【证据：V2 handoff `H006`-`H010`；`SIMILARITY_MECHANISM_V3.md`；`PROVENANCE_CONTRACT_V3.md`】

**executed**：171 个 similarity JSON 都记录 tokenizer、metric、Top-3、score/shared tokens 与 comparison base；171 个 comparison Markdown 都有三问和 decision。代表性工件 `karpathy-llm-kb-three-layer-arch` 得分 0.5，对 V2 三层架构卡判为 `provenance_delta`，并留下来源、scope 与决策排除理由。【证据：`outputs/llm_wiki/drafts/similarity/karpathy-llm-kb-three-layer-arch.json`；`outputs/llm_wiki/drafts/comparison/karpathy-llm-kb-three-layer-arch.md`】

**contradicted**：

- `similarity_top3.py` 只有 `V2_INDEX`，无参数、无 V3 index、无 draft-vs-draft 循环；171 JSON 的 `comparison_base_card_count` 均为 15。【证据：`tools/similarity_top3.py:26-30`、`:116-166`；`comparison_corpus_drift_audit.md`】
- 初始合同写 V2 是 bootstrap 默认，直到 V3 有 accepted index；但切换逻辑从未实现。【证据：`DRAFT_FIRST_PIPELINE_V3.md`；`comparison_corpus_drift_audit.md`】
- `H026` 用户明确纠正 comparison 应与 V3 自身跑；后验审计进一步按 loop 0→1 独立性推翻 V2 secondary base。但当前 similarity、8 个 V2 anchors、body `[^v2-1]` 与 `related` 仍保留，修复没有回写生产结果。【证据：V3 `H026`；`audits/comparison_corpus_drift_audit.md`；`audits/pipeline_integrity_audit.md`】

**缺口**：Top-3 文件数量完整、语义覆盖不完整；3 张真实 V2 邻居漏出 Top-3，V3 自身近重复完全未召回。Top-3 只能作为候选检索证据，不能当 dedup/fusion coverage 证据。【证据：`reports/loop_report.md` “comparison 阶段的发现”；`decision_quality_audit.md`】

### 5.4 Fusion：有 fusion audit 名称，没有实际 card merge

**specified**：V2/V3 都将 `merge_candidate` 与 `provenance_delta` 送独立 audit；通过后应把 comparison provenance 接回 A 卡 provenance。V3 设计强调 material 先成 draft，再做昂贵融合。【证据：V2 handoff `H006`；`LOOP_DESIGN_V2.md`；`PROVENANCE_CONTRACT_V3.md`】

**executed**：8 张 `provenance_delta` 由一个 fusion worker 全部审计通过；V3 accepted provenance 带 `v2_anchor`，body 有 V2 footnote，related 含 anchor id。`enterprise-llm-wiki-drift-detection-loop` 的错误 top-1 anchor 还在 gate 中被纠正到实际 top-3。【证据：V3 `H009`；`reports/loop_report.md`；`audits/pipeline_integrity_audit.md`】

**not executed**：没有 `merge_candidate`、`duplicate_skip` 或 superseded card；没有两张 V3 draft 合成新卡，也没有 V3 self-fusion ledger。V3 写入边界禁止修改 V2，因此设计要求的 “comparison provenance 链回 A 卡 provenance” 实际降级为仅在 V3 一侧记录 anchor，V2 卡没有反向更新。【证据：`task_templates/adoption_worker_prompt.md`；`audits/boundary_compliance_audit.md`；`comparison_corpus_drift_audit.md`】

**retrospective**：`H025` 才把 draft→KB 重排为 Fork/Weave/Derive，`H036` 又明确 adoption 是 schema 修补而非正式阶段、真正缺口是 set-level dedup/fusion gate；`H037`-`H040` 的 grep-first/best-effort fusion 属于 future governance。【证据：V3 `H025`、`H036`-`H040`】

### 5.5 Citation 与 related：最终统一，但 lineage 不可直接重放

**V2 specified/executed**：V2 后期把 References 定义为来源级说明、Footnotes 定义为 inline citation locator；旧 15 卡普遍有 References/Footnotes，但不是统一 typed footnote，也没有 related graph metadata。【证据：V2 handoff `H010`；`CARD_CONTRACT_V2.md`；V2 KB cards】

**V3 generation 1 executed**：在 publication 前，6 个主题 worker 手工为 drafts 选择 related，形成 974 条边、0 dangling、0 orphan。该轮 related 不是从 citation 派生。【证据：V3 `H007`；Git `bf1e8101`；`reports/loop_report.md`】

**V3 generation 2 executed**：`H019` 决定 related 不单独维护，而应从 Footnotes 派生；`H020` 后把 References 内容并入唯一 `## Footnotes`，支持 raw/v3/v2/URL targets，加入 504+ KB-internal footnotes，再重算 related。最终 4 张卡因只引 raw/URL 而合法 `related: []`。【证据：V3 `H019`、`H020`；`CARD_CONTRACT_V3.md`；`derive_metadata_from_footnotes.py`；`pipeline_integrity_audit.md`】

**contradicted**：adoption worker 的原 gate 要求 `## References` 存在且 `related` 非空；最终合同却删除 References，并允许 4 张合法空 related。两者分别是 5 月 27 日 adoption 合同和 5 月 28 日迁移后合同，不应合并成一个同步执行的 gate。【证据：`task_templates/adoption_worker_prompt.md`；`CARD_CONTRACT_V3.md`；`reports/loop_report.md`】

**缺口**：`derive_metadata_from_footnotes.py` 存在，但原运行被 classifier 阻塞，171 张卡实际由 fresh agent 以 Read+Edit 模拟脚本规则；所以最终 related 符合规则的证据来自后验完整性审计，不是该脚本的成功运行日志。【证据：`reports/loop_report.md`；`audits/hook_and_classifier_audit.md`】

### 5.6 Publish KB：candidate publication 与 stable promotion

V2 和 V3 的 `outputs/llm_wiki/kb/` 都是 loop capsule 内候选产品面。V2 handoff `H031` 明确规定，只有 human promotion 后仓库根才形成稳定 `llm_wiki/`；V3 start prompt 也禁止首轮提前 adoption，并在最终 report 把 root promotion 留作人工决定。【证据：V2 handoff `H031`；V3 `H001`；`reports/loop_report.md`】

因此：

- V2 loop-local publish：**executed**，15 accepted；stable promotion：**not executed**。
- V3 loop-local publish：**executed**，171 accepted；stable promotion：**not executed**。
- `version-registry.json` 是 replay 展示层的版本注册，不等于根产品目录已被发布或切换。【证据：`version-registry.json`；V2/V3 `outputs/llm_wiki/kb/`】

## 6. 关键事件时间线

| event_id | 触发 / 版本变化 | 证据性质 |
|---|---|---|
| `codex:codex-primary-v0-v2-boundary:H046` / `H047` / `H048` | 明确无预设 topic、目标是 agent 自主 bottom-up 卡片而非 hub；draft 必须 audit 后交付。 | **specified**：V2 入口边界。 |
| `codex:codex-primary-v2-v3-handoff:H001` | 启动旧式 source-mining→单卡 drafting→audit→adoption 链。 | **specified + executed start**。 |
| V2 handoff `H003` / `H004` | 15 张卡已采纳；用户指出 7 小时吞吐过低。 | **executed + failure feedback**。 |
| V2 handoff `H005`-`H010` | 提出 batch draft、Top-3、comparison 三问、scoped knowledge 与 References/Footnotes。 | **design transition**。 |
| V2 handoff `H023` | V2 设计正式固化。 | **specified**；Git `9c10bfab`。 |
| V2 handoff `H031` | loop output 是候选，root stable KB 需 human promotion。 | **specified publication boundary**。 |
| V2 handoff `H033`-`H044` | 建 V3 capsule、上下文白名单与 Claude CLI start prompt。 | **specified handoff**。 |
| `claude_code:claude-primary-v3:H001` | 首轮 1 material→4 drafts/provenance/similarity，不 adoption。 | **executed**。 |
| V3 `H005` | 全量材料状态与 171 张中文 draft。 | **executed**。 |
| V3 `H006` / `H007` | 171 comparisons；随后 974 related edges。 | **executed**。 |
| V3 `H008` / `H009` | provider 中断后恢复；171 cards/provenance 进入 loop-local KB。 | **executed with interruption**。 |
| V3 `H019` / `H020` | related 改为 Footnotes 派生；171 KB cards 做 unified-citation migration。 | **executed post-publication migration**。 |
| V3 `H025` / `H026` | 用户指出 draft 需 dedup/link/citation/fusion 加工，并纠正 comparison 应跑 V3 self；审计确认 171 drafts 从未互比。 | **contradicted + retrospective audit**。 |
| V3 `H036` | 更正：batch 是刻意的 material-consumption 策略，adoption 是 schema fix，缺的是 set-level gate。 | **retrospective correction**。 |
| V3 `H041`、`H057`-`H079` | 设计 collect→extract→ingest→evolve、questioner-reader/reviewer、JJ、grep-first fusion，并交给下一 loop。 | **future specification, not V3 execution**。 |

## 7. Git 证据与版本进入历史

### 7.1 V2

- 2026-05-25 03:01-09:49 的提交清楚分离多个 draft、audit、adoption 动作，证明旧式逐卡链真实执行，而非只存在于总结。【证据：Git `fa12054e`、`601f5191`、`b8687a66`、`1ace57af`，以及后续同类 commits】
- `992fdf1f`（10:42）才切到 atomic draft-first；`9c10bfab`（16:19）才正式 “Adopt loop design v2”。因此 15 张 accepted cards 的主体生产先于 scoped V2 设计。【证据：Git `992fdf1f`、`9c10bfab`】
- `d95fa619` / `ac4968ca` 关闭并归档 V2，`396eca13` 才采用当前 loop capsule layout。归档路径改写不能改变原执行时序。【证据：Git 上述 commits】

### 7.2 V3

- per-card draft commits 出现在 2026-05-26 10:49-11:27；`29f41f3e` 在 11:34 固化完整 first-pass/revision bookkeeping；`02715928` 11:57 固化 comparisons；`bf1e8101` 12:16 固化 interlinks。该提交序列支持 draft→comparison→interlink 的阶段顺序。【证据：Git 上述 commits】
- 当前完整 V3 contracts、adoption/citation tools、audits 与最终 outputs 多数在 2026-05-29 的 `b796a370`、`0bbc2f89`、`36808a9b`、`da9d00a5` 中成组固化。它们能证明最终快照，不应替代 5 月 25-28 primary events 作为运行时顺序证据。【证据：Git 上述 commits】
- Questioning/JJ/future pipeline 于 2026-06-04 的 `d1bfaa2c`、`df5751be` 才进入 Git，进一步确认这些机制不是原始 V3 ingestion。【证据：Git `d1bfaa2c`、`df5751be`】

## 8. 已知冲突与缺口台账

| ID | 状态 | 冲突 / 缺口 | 安全表述 |
|---|---|---|---|
| G1 | **contradicted** | V2 registry/core 称 scoped cards，但 15 张 accepted 卡是新合同前的旧 metadata 世代。 | “V2 形成 scoped-card 设计；旧链已产 15 张候选 KB 卡，但未迁移到该合同。” |
| G2 | **specified-not-executed** | V2 Top-3/comparison/fusion pipeline 已写合同，唯一 backlog card 仍 `similarity_pending`。 | “V2 把机制交给 V3 验证，V2 自身未跑完整。” |
| G3 | **contradicted** | V3 Top-3 171/171 完整，但全部只比 V2 的 15 张卡；后来要求 V3 self-only。 | “Top-3 机械执行完整，comparison corpus 错位且未修复。” |
| G4 | **executed-with-gap** | 171 comparison provenance 完整，但没有 intra-V3 comparison。 | “它是 cross-version decision ledger，不是 V3 set-level dedup ledger。” |
| G5 | **contradicted metric** | `merge_candidate=0` 看似无融合需求，实际兄弟 drafts 从未互比。 | “0 表示该候选池内无 merge，不表示 V3 无重复。” |
| G6 | **partial execution** | 8 个 fusion audit 实际都是 V2 provenance delta，没有 card merge；V2 side 不能回写。 | “执行了单向跨版本 delta anchoring，未执行真正 fusion。” |
| G7 | **generation drift** | drafts 有 References+Footnotes，KB 只有 Footnotes；重跑 adoption 会回退 schema。 | “当前 KB 需要 post-adoption migration 才可再生。” |
| G8 | **contradicted contract** | adoption gate 要 References 和非空 related；最终合同删除 References，并允许 4 张空 related。 | “分别报告 5 月 27 gate 与 5 月 28 migration 后合同。” |
| G9 | **executed-via-fallback** | `derive_metadata_from_footnotes.py` 存在，但全量 related 更新由 agent fallback 完成。 | “规则是脚本化的，实际全量写入不是脚本执行。” |
| G10 | **not executed** | V2/V3 都没有内容层 script-only ingest；均由 agent adoption worker 写卡。 | “有脚本辅助与 Git hook，不等于 deterministic ingest。” |
| G11 | **not executed** | 两版都只发布到 loop-local KB，没有 root `llm_wiki/` promotion。 | “candidate KB published locally; stable product promotion pending.” |
| G12 | **retrospective-only** | Questioner-reader、quit review、JJ、grep-first fusion 在 V3 后期设计。 | “它们解释下一版方向，不证明 171 张卡采用这些机制。” |
| G13 | **artifact gap** | V3 `source_access_log.jsonl` 只有 bootstrap 行，无法逐材料重放实际 read path/时间。 | “material queue 与 card provenance 能证明来源绑定，不能替代完整访问日志。” |
| G14 | **governance gap** | 初始 974 related 边没有逐边 decision ledger；迁移后 related 可由 footnotes解释，但 drafts 仍保留旧图。 | “最终 KB 图可从 citation 派生，原 draft 图与边选择过程不可完整重放。” |

## 9. 可复述的最小事实集

1. V2 先用严格逐卡链生产并审计 15 张卡，随后才定义 scoped-card、batch draft、Top-3 和 comparison provenance；后者未在 V2 内完整执行。【证据：V2 handoff `H003`-`H010`、`H023`；Git `9c10bfab`】
2. V3 draft-first 真实执行：43 个可读材料产出 171 drafts，最终形成 171 份 draft/provenance/similarity/comparison 和 171 张 loop-local accepted KB cards。【证据：V3 `H005`-`H009`；`pipeline_integrity_audit.md`】
3. V3 171 次 Top-3 全部比较 V2 的 15 张 accepted cards；没有任何 draft-vs-draft 或 V3-self dedup pass。【证据：V3 `H026`；`similarity_top3.py`；`comparison_corpus_drift_audit.md`】
4. 171 comparison provenance 给出 163 new cards 与 8 provenance deltas；8 个 delta 通过 fusion audit，但没有实际 card merge，`merge_candidate=0` 不能证明无重复。【证据：`outputs/llm_wiki/drafts/comparison/`；`audits/pipeline_integrity_audit.md`】
5. V3 related 先由 agent 手工治理，后在 unified Footnotes migration 中改为 citation-derived metadata；当前 drafts 与 KB 属于不同 citation schema 世代。【证据：V3 `H007`、`H019`、`H020`；`derive_metadata_from_footnotes.py`】
6. V2/V3 的 adoption 都由 agent worker 完成，不是确定性 ingest script；脚本与 hook 只承担召回、派生、分批、索引或提交辅助。【证据：两版 adoption templates；V3 `reports/loop_report.md`】
7. V2 的 15 张、V3 的 171 张都发布在 loop capsule 内；稳定 root KB promotion 没有执行。【证据：V2 handoff `H031`；V3 `reports/loop_report.md`】
8. Questioner-reader、reviewer quit gate、Justification Journal 与 grep-first fusion 是 V3 执行后的下一版设计，不属于原始 V2/V3 入库事实。【证据：V3 `H057`-`H079`；Git `d1bfaa2c`、`df5751be`】
