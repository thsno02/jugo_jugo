---
schema: audit.v3
topic: loop_flow_expected_vs_actual
loop_id: v3_llm_wiki_loop_20260525
created_time: 2026-05-29T16:30:00+08:00
auditor: llm
status: complete
---

# V3 Loop 流程审计：期望流程 vs 实际流程（端到端对照）

> 范围：把 v3 draft-first loop 的**三层流程**放在一份文档里互相对照——(1) 经 2026-05-29 用户原则修正后的**理想流程**（THE CORRECTED IDEAL）、(2) 五份合同**实际声明的流程**（AS-CONTRACTED）、(3) v3 这一轮**真正跑出来的流程**（AS-EXECUTED）。目标是让读者清楚看到"意图"在哪一步、因为什么、偏离成了"现实"。
>
> 主语言中文；schema 字段 / 文件路径 / 代码 / id / 决策枚举保留英文。
>
> **更正说明（2026-05-29 补）**：§8 根据项目作者的说明，还原了若干被 §0/§3/§5 误判为"缺陷"的**设计意图**——批处理为何是刻意选择、adoption 实为一次 schema 修补、similarity 为何粗糙（rule-based 非 semantic）、以及"入口治理 vs 入库后治理"这条尚未想清的开放岔路。阅读前五节的"缺陷"定性时，请一并参考 §8。前面各节的**事实**（只比 v2、去重 pass 缺位、merge=0）依然成立，需要还原的是**动机与定性**。
>
> 本文是 synthesis（综合）审计，建立在以下既有审计之上，不重复其细节，只做连接：`comparison_corpus_drift_audit.md`（语料漂移，中心）、`token_consumption_audit.md`（成本）、`pipeline_integrity_audit.md`（完整性）、`decision_quality_audit.md`（决策质量）、`boundary_compliance_audit.md`（边界）、`worker_dispatch_audit.md`（派单）、`hook_and_classifier_audit.md`（hook/分类器）。

---

## 0. TL;DR — 期望与实际最大的几条裂缝

- **裂缝 1（最严重）：比较语料的"自指 vs 外指"。** 理想要求"比较基只用本 loop 自己累积的 drafts/cards，永不引用任何外部 loop"；合同却把**默认比较基写成 v2 索引**（`DRAFT_FIRST_PIPELINE_V3.md:31`、`RUNBOOK.md:71`、`LOOP_START_PROMPT.md:81-82/108-109`），工具又把 v2 路径**硬编码为唯一语料**（`tools/similarity_top3.py:30/126/165`）。实际跑出来的结果：171/171 张 draft 全部只跟同一组 **15 张 v2 卡** 比，**intra-v3 去重从未发生**，`merge_candidate=0` 是"从没看过"而非"确实无重复"。详见 `comparison_corpus_drift_audit.md` §2/§9。
- **裂缝 2：去重 pass 整个缺位。** 理想要求一道**显式的 intra-loop 全配对（all-pairs）去重/合并 pass** 在 adoption 之前发生；合同从未把"对本 loop 兄弟卡去重"写成任何一项需求（五份合同皆无），`comparison_worker_prompt.md:33` 甚至**明令禁止 worker 读其他 draft 卡**——使 draft-vs-draft 比较在结构上不可能。实际后果：~15-20 张近重复卡进入 KB（最强物证：Karpathy "raw/wiki/schema 三层架构"一个概念被 **4 张卡**重复承载，`comparison_corpus_drift_audit.md` §3.2）。
- **裂缝 3：unified-citation 是"出生自带"还是"事后迁移"。** 理想要求 draft 从**第一张卡**就生于单一 `## Footnotes` 引用枢纽、`related:` 由脚本派生；实际是先用 `## References` + `## Footnotes` 二分模型跑完全流程，**adoption 之后**才做了一次覆盖 171 张卡的大型迁移（`docs/v3_loop_journey.md` §3.5、`reports/loop_report.md:34-36`），并额外烧掉 ~1.42M 的 citation migration token + 623K 的 derive_metadata fallback（`token_consumption_audit.md` §3.3/§4）。
- **裂缝 4：批量并行消灭了"增量切换点"。** 理想/合同都隐含"等 v3 有自己的索引后切到 v3-self"，但 171 张 draft **一次性批量生成 + 批量比较**（`similarity_top3.py:129` 一次 glob 全部 draft），从未出现"拿新 draft 比累积 v3"的增量时刻，那个切换点**永不到来**。这是把"语料 bug"从潜在变成必然的执行级原因（`comparison_corpus_drift_audit.md` §4(b)）。
- **裂缝 5：成本结构由"分阶段横扫"决定。** 理想的"产一张卡、判一张卡"被实现成"全部 draft → 全部 similarity → 全部 comparison → 全部 interlink → 全部 adoption → 全部 migration"的多趟横扫，每张卡在不同阶段被反复 Read，单卡全 pipeline 成本 ≈ **60K token**（`token_consumption_audit.md:372`），其中相当一部分是同一文件的重复 read（`token_consumption_audit.md` §5：~540K 结构性重复）。

一句话：**v3 的执行非常干净（边界 0 越界、计数 6/6 全过、决策抽样 29/29 通过），但它干净地执行了一个在合同层面就已偏离理想的流程——偏离集中在"和谁比"这一个支点上。**

---

## 1. 期望的 loop 流程（THE CORRECTED IDEAL）

这是按用户 2026-05-29 原则修正后的理想流程。贯穿全程的**不变量（invariants）**有四条，必须在每个阶段被保持：

- **INV-1 loop 独立性**：每个 loop 是独立的 0→1 过程。比较/去重/引用的语料**只能是本 loop 自己**累积的 drafts/cards；**永不**依赖、比较、引用任何外部 loop（v2/v1/v0）的 KB。第一张 draft 的比较基是**空集**，随 draft 累积而增长。
- **INV-2 intra-self 去重**：去重是"本 loop 内部、draft 之间"的事。因为生成是批量的，去重必须是一道**显式的全配对（all-pairs）/聚类 pass**，而非依赖"逐张比累积"的增量假设。
- **INV-3 footnote 单一真理源**：从第一张卡起，引用就只有一种机制——body 内 `[^id]` marker + 末尾单一 `## Footnotes` 枢纽；`related:` 永远是**脚本派生的视图**，不手工维护。没有 `## References` 与 `## Footnotes` 的二分，也没有任何 v2 target。
- **INV-4 步步留痕（provenance）**：每个判断（相似、比较、去重、发表门）都落成可恢复的工件，不只留在 chat / task result 里。

逐阶段（input → action → output → 保持的不变量）：

**Stage 0 — material 入队.** input：raw 源（论文/博客/repo）。action：登记进 `queues/material_queue.md`，标 `drafting`。output：material queue 行。不变量：INV-4。

**Stage 1 — material_to_draft.** input：单个完整源（**一次性 full read**，1M context 足够，不防御性截断）。action：抽出 2-5 张知识密集 draft 卡 + draft provenance；**卡一出生就用 `## Footnotes` 单一引用枢纽**（target = raw 源 / 已有兄弟 v3 卡 / URL；**无 v2 target**）。output：`drafts/cards/*.md` + `drafts/provenance/*.md`。不变量：INV-3（出生即统一引用）、INV-4。

**Stage 2 — similarity（候选检索）.** input：draft 标题 + **本 loop 已累积的 drafts/cards 标题索引**（首张 draft 时该索引为空集）。action：jieba 分词 + Jaccard，取 top-k 候选；只是缩小比较集的廉价预检，不判真理/重复。output：`drafts/similarity/*.json`，其 `comparison_base` 字段指向 **v3-self 索引**。不变量：INV-1（语料自指）、INV-4。

**Stage 3 — intra-self 去重（全配对/聚类）.** input：全部 draft 标题 + 高分相似对。action：对所有 draft 做 all-pairs jieba-jaccard（或 catalog 聚类），对高分对 full-read 复核，回答三问，给 `merge_candidate` / `duplicate_skip` / `new_card` / `revise_before_gate`。**这一道是理想流程里真正的去重，对象是兄弟 draft，不是任何外部卡。** output：comparison provenance + 合并/跳过决策。不变量：INV-2（intra-self 全配对去重）、INV-1、INV-4。

**Stage 4 — interlink.** input：经去重后的卡集。action：在卡 body 里为自然 cross-card 提及加 `[^id]` footnote；`related:` 由脚本从 footnote 派生。output：带 KB-internal footnote 的卡 + 派生的 `related:`。不变量：INV-3（footnote 驱动、related 派生）、INV-1（footnote target 只指 v3-self）。

**Stage 5 — publication gate / fusion audit.** input：去重后的 new_card / merge 结果。action：轻量发表门（知识密度、源支撑、非标题复述）；merge 才走 fusion audit。output：通过的卡 + accepted provenance（含 gate 块）。不变量：INV-4。

**Stage 6 — adoption.** input：过门的卡。action：`status: draft → accepted`，写入 `kb/cards/` + `kb/provenance/`。output：v3 KB。不变量：INV-1（KB 自包含）、INV-4。

**Stage 7 — index / citation 一致性.** input：已采纳的卡。action：脚本建 `kb/indexes/cards.md`、脚本派生 `related:`、脚本校验 footnote 1:1。**注意：这里不该有"unified-citation 迁移"——因为卡在 Stage 1 就生于统一格式。** output：索引 + 一致的图。不变量：INV-3。

关键点：理想流程里**没有 v2 出现的任何位置**，且去重（Stage 3）是一道独立、显式、对兄弟 draft 全配对的 pass。

---

## 2. 合同声明的流程（AS-CONTRACTED）——以及合同自身的偏离

五份合同（`DRAFT_FIRST_PIPELINE_V3.md` / `CARD_CONTRACT_V3.md` / `SIMILARITY_MECHANISM_V3.md` / `PROVENANCE_CONTRACT_V3.md` / `CONTEXT_BOUNDARY.md`）加上 `RUNBOOK.md` / `LOOP_START_PROMPT.md` 声明的流程**骨架**与理想一致：material → draft → similarity top-3 → comparison provenance（三问）→ decision（五选一）→ publication_gate / fusion_audit → adoption（`DRAFT_FIRST_PIPELINE_V3.md:5-13`）。但合同在三处**与 §1 理想明确分歧**，必须点破而非抹平：

**分歧 A（致命）：v2-as-base 被写进合同，违反 INV-1。**
- `DRAFT_FIRST_PIPELINE_V3.md:31`：「The default comparison base is `loops/v2_llm_wiki_loop_20260525/.../indexes/cards.md` **until v3 has its own accepted index**」——把 v2 索引设为默认比较基，并承诺"之后切 v3"。
- `RUNBOOK.md:71`：「default comparison base: `loops/v2_.../kb/indexes/cards.md`」——同一缺陷在 runbook 复述。
- `LOOP_START_PROMPT.md:81-82` 与 `:108-109`：启动 prompt 直接指示"similarity 用 v2 accepted-card title index"。
- `CONTEXT_BOUNDARY.md:7`：「V2 candidate cards may be used **only as** accepted-card comparison material.」——边界合同的"原则"段就把 v2 写成合法比较材料。

按 INV-1，这一句**从写下那刻起就是 bug**（`comparison_corpus_drift_audit.md` §9 的重新定性）：不是"忘了切到 v3"，而是"根本不该把 v2 列为 base"。哪怕切换代码写全，也只是把"错误依赖 v2"换成"先错误依赖 v2 再切走"。

**分歧 B：References/Footnotes 二分先于 unified-citation，违反 INV-3。**
- v3 起草版的 card 模型曾把 `## References`（卡级"refer to 某 idea/源"）与 `## Footnotes`（句级 inline locator）分开。`CARD_CONTRACT_V3.md:74-81` 的"Why one mechanism"段是**事后**才把二分批为 artifact 并统一的——也就是说，合同里 unified-citation 是后来补写进去的，不是起草时就有（佐证：`docs/v3_loop_journey.md` §3.5/§4.4 把 unified-citation 列为 2026-05-28 的大型重构，发生在 adoption 之后）。

**分歧 C：intra-self 去重在任何合同里都没有被指定（INV-2 完全缺位）。**
- `DRAFT_FIRST_PIPELINE_V3.md:46-51` 的决策枚举（`merge_candidate` "draft and A should likely become one card"、`duplicate_skip` "draft is already covered"）**读起来**像语料内部去重，但合同里的 "A" / "accepted cards" 从未限定语料；接线只指向 v2。
- `SIMILARITY_MECHANISM_V3.md:7/16`、`PROVENANCE_CONTRACT_V3.md:18` 对"哪个 KB"保持**沉默**——bootstrap 时唯一的 accepted 卡是 v2，于是"accepted index"默认=v2。
- `CONTEXT_BOUNDARY.md:77` 其实**允许**读 v3 自身索引（不是被边界锁死成 v2-only），但**没有任何合同把"对 v3 兄弟卡去重"写成一项任务**。`comparison_worker_prompt.md:33` 反而明令"禁止读其他 draft 卡"。
- 净结论（`comparison_corpus_drift_audit.md` §1.6）：合同把"链接到相关 v2 卡 / 跨 KB provenance"做得很细（`CARD_CONTRACT_V3.md:50/86-89` 区分 v3-card 与 v2-card target），却**从未**把"在 v3 内部去重"写成需求。**链接 ≠ 去重**，合同混淆了这两件事的优先级。

所以：合同声明的流程在骨架上对，但在"和谁比 + 去不去重 + 引用从何时统一"这三处，**合同本身就已偏离 §1 理想**。这不是执行跑偏，是设计起点的缺陷。

---

## 3. 过去实际跑的流程（AS-EXECUTED）

真实跑出来的流程（带真实数字与真实行为，证据来自 `docs/v3_loop_journey.md`、`reports/loop_report.md` 与各审计）：

**Stage 1 实际：批量并行生成 171 张 draft。** 8 个 batch worker（model:opus）处理 64 条材料产 129 张卡；首轮**防御性 `limit:2000` 截断**漏掉 14 篇 arxiv 后半段，事后派 4 个 revision worker 全文重读补 34 张卡（`docs/v3_loop_journey.md` §3.2、`worker_dispatch_audit.md` §5.1）。draft **生于 References/Footnotes 二分模型**，不是统一枢纽。代价：batch 1.45M + arxiv revision 1.24M token（`token_consumption_audit.md` §1.2）。

**Stage 2 实际：v2-only similarity，语料仅 15 张卡。** `similarity_top3.py` 一次 glob 全部 171 张 draft（`:129`），每张只对**硬编码的 v2 索引**打分（`:30/126`）；输出 `comparison_base` 171/171 = v2，`comparison_base_card_count` 171/171 = **15**（`comparison_corpus_drift_audit.md` §2.2）。这 15 张 v2 卡全部来自 2 个 Karpathy 源，主题只覆盖"Karpathy 原始 LLM Wiki 概念"，对 ~150 张 arxiv/工具/安全类 draft 结构上不可能给出真候选。中文化（2026-05-26）意外解开跨语言 jaccard 死结，让 39 张产生 ≥0.15 的分布（`reports/loop_report.md:88`），但比的仍是 v2。**更根本地**：similarity 是 rule-based（标题 token 集合）而非 semantic，这是它粗糙的根因，也直接导致"similarity → fusion"的自然衔接断掉、fusion 环节没能长出来（详见 §8.3）。

**Stage 3 实际：去重 pass 不存在。** comparison 阶段 8 个 worker 处理 171 张 draft，**100% 继承 similarity 的 v2-only 候选池**，且被 `comparison_worker_prompt.md:33` 禁止读兄弟 draft。决策分布：**163 new_card / 8 provenance_delta / 0 merge_candidate / 0 duplicate_skip / 0 revise_before_gate**（`pipeline_integrity_audit.md` §2.3）。`merge_candidate=0` 不是"无重复"，是"从没在 v3 内部看过"（`comparison_corpus_drift_audit.md` §5.1）。8 张 provenance_delta 全部锚向 v2 三类卡（三层架构 5 / schema 配置 2 / idea-file 1，后修正 1 张到 health-checks）。

**Stage 4 实际：interlink 在 v3 内部跑，但是"链接"不是"去重"。** 6 个 cluster worker（A49/B7/C47/D21/E27/F20）填 `related:`，产 **974 条边**，平均 5.70/卡，0 孤立、0 dangling（`reports/loop_report.md:28`、`worker_dispatch_audit.md` §3.3）。讽刺的是 interlink **把重复卡织成了健康的 related 簇**——4 张三层架构卡互相 related，反而掩盖了重复（`comparison_corpus_drift_audit.md` §3.1）。

**Stage 5+6 实际：171/171 全采纳，0 reject。** 6 个 adoption worker（1 fusion_audit + 5 publication_gate）：163 new_card 全过 gate，8 provenance_delta 全过 fusion（`reports/loop_report.md:66-68`）。决策质量抽样 29/29 通过（`decision_quality_audit.md` §7）——**单卡质量很高，但这是在"从未做 intra-v3 去重"的前提下的高质量**，两件事不矛盾。代价：adoption 1.74M token（最大单阶段，`token_consumption_audit.md` §3.1，其中 kb body 是 draft body 的逐字复制，~50% output token 是重打一遍）。**注**：adoption 本身是一次针对早期 schema 问题的**修补**，而非设计里的正式准入阶段；它的存在恰恰印证"正式发表门从一开始就缺席"（详见 §8.2）。

**Stage 7 实际：unified-citation 作为 LATE 迁移 + 索引手工兜底。** 全流程跑完、171 张卡已在 KB 后，2026-05-28 才做 unified-citation 大型迁移：6 个 cluster worker 砍 `## References` 并入 `## Footnotes`、加 504+ KB-internal footnote、8 张 v2-anchored 卡的 anchor 移到 body `[^v2-1]`（`reports/loop_report.md:35`）。`related:` 改脚本派生，但 **bash classifier 持续阻塞 python**，被迫派 fresh agent 用 Read+Edit 重写 171 张卡（单笔 **623K token**，全 loop 最贵，`token_consumption_audit.md` §4）；`build_kb_index.py` 同样被阻塞，fallback 手工组装索引（125K）。

**贯穿全程的横向特征：**
- **批量并行 + 分阶段横扫**：每个阶段都是"把 171 张卡全过一遍"，同一文件在不同阶段被多个独立 worker 反复 Read（`token_consumption_audit.md` §5：kb index 被 6 worker 各读一次浪费 ~150K；结构性重复总计 ~540K）。
- **classifier 阻塞 → fallback agent**：≥40 次命令被 reject，两次大 fallback 烧掉 ~750K（`hook_and_classifier_audit.md` §4）。
- **工程隔离是胜利**：PostToolUse hook 自动 commit 1374 次、0 lock 冲突、0 越界写入（`boundary_compliance_audit.md` §2、`hook_and_classifier_audit.md` §2/§6）。
- **总成本 ≈ 10M token，单卡 ≈ 60K**（`token_consumption_audit.md` §10）。

---

## 4. 逐阶段差异表

| 阶段 | 期望（IDEAL，§1） | 合同（AS-CONTRACTED，§2） | 实际（AS-EXECUTED，§3） | 差异 / 后果 |
|---|---|---|---|---|
| 0. material 入队 | 登记 + 标记，留痕 | 同左（`RUNBOOK.md:25`） | 一致；72 源 / 43 drafted / 22 empty / 7 blocked | 无差异（`pipeline_integrity_audit.md` §9） |
| 1. material→draft | full read；**卡出生即 unified-footnote** | full read 是后补规则；卡用 References/Footnotes 二分 | 首轮防御性截断漏 14 篇→补 34 卡；卡用二分模型 | 1.24M revision 重读债（INV-3 未在出生满足）|
| 2. similarity | 语料 = **v3-self**（首张为空集，渐增） | 默认基 = **v2**（`DRAFT_FIRST:31` 等多处） | v2 硬编码唯一语料，base=15 张卡，171/171 全 v2 | **INV-1 破**：自指变外指（`drift_audit` §2）|
| 3. intra-self 去重 | **显式 all-pairs 去重 pass**，对兄弟 draft | **完全未指定**；`comparison_worker:33` 禁读兄弟 draft | 不存在；comparison 继承 v2 候选；merge=0 | **INV-2 破**：~15-20 近重复入 KB（`drift_audit` §3）|
| 4. interlink | footnote 驱动，related 派生，target 仅 v3-self | related 起初手工；footnote target 含 v2 | v3 内 974 边；但把重复织成健康 related 簇 | 链接≠去重；重复被粉饰隐蔽（`drift_audit` §3.1）|
| 5. gate / audit | 轻量发表门 + merge 才 fusion | 同左（`DRAFT_FIRST:53-57`） | 163 gate + 8 fusion，全过；抽样 29/29 通过 | 决策质量高，但去重前提缺失 |
| 6. adoption | 写入自包含 v3 KB | 同左 | 171/171 采纳；kb body 逐字复制 draft | 一致；~855K 复制 output token（`token_audit` §3.1）|
| 7. index / citation | 脚本建索引 + 派生 related；**无迁移** | unified-citation 后补进合同 | **LATE 迁移**：504+ footnote + 623K fallback | **INV-3 时序破**：迁移本可避免（`token_audit` §4）|

---

## 5. 根因与教训（跨审计综合）

把各审计的发现连起来，而不是各自重复：

**根因 1：一个支点缺陷（"和谁比"）+ 三因叠加，造成 INV-1/INV-2 同时失守。** 语料漂移审计（§4）已锁定三因：(a) v2-as-base 是写进合同的 bootstrap 默认（`DRAFT_FIRST:31`，可辩护但按 INV-1 本身即 bug）；(b) 171 张 draft **批量并行**生成+比较，消灭了"拿新 draft 比累积 v3"的增量切换时刻；(c) `similarity_top3.py` 把 v2 **硬编码**为唯一语料，没有任何切到 v3 的代码。三者叠加 + 合同从未把 intra-self 去重写成需求（INV-2 缺位），使缺口**无人察觉**。教训：**当"切换"只是合同里一句话承诺而没有任何代码兑现路径时，它等于不存在**；尤其在批量并行执行下，任何依赖"渐进状态变化"的设计假设都会失效——必须把它实现成一道显式 pass。

**根因 2：批量并行 + v2 硬编码 + 沉默合同 = 去重缺口的合谋。** 单看任一因素都不致命：批量并行本身是吞吐胜利（`worker_dispatch_audit.md`：42 worker 全 WORKER_DONE，wall-clock 压到 max-cluster）；v2-as-bootstrap 是诚实选择；合同沉默看似无害。但三者合谋的结果是：生成阶段没给去重留增量窗口 → 工具没给去重留 v3 语料 → 合同没给去重留需求条目 → **去重在每一层都被悄悄省略**，最终 `merge_candidate=0` 这个"看起来 KB 很干净"的头条指标具有**误导性**（`drift_audit` §5.1）。教训：throughput 优化（批量并行）与 quality gate（去重）必须**显式解耦**——批量化的生产必须配一道批量化的去重，不能指望增量去重自然发生。（注：批处理本身是刻意且合理的 ingestion 选择，"合谋"指的是三者叠加让去重无人实现，而非批处理有错；设计意图还原见 §8.1。）

**根因 3：成本浪费的两大驱动都来自"流程时序错位"。** `token_consumption_audit.md` 列的三大可省成本（~1.8M）几乎全是时序问题：(i) 首轮防御性截断 → 1.24M arxiv 重读，因为"省 token"的截断规则**早于**"1M 够用"的认知（INV：full read 应是出生规则）；(ii) unified-citation 作为**事后迁移** → 1.42M migration + 623K fallback，因为统一引用**晚于** adoption 才确立（INV-3 时序破）；(iii) 分阶段横扫导致同一文件被反复 Read（~540K 结构性重复），因为流程被切成多趟"全 171 张过一遍"而非"一张卡走完全程"。教训：**把规则提前到卡的出生时刻**（full read、unified-footnote），以及**减少横扫趟数**，是最大的成本杠杆——比任何 prompt 压缩都有效。

**根因 4：决策质量高，恰恰掩盖了流程缺陷。** `decision_quality_audit.md` 抽样 29/29 通过，worker 多处主动质疑上游（fusion 改 anchor、interlink 清 dangling、comparison 主动暴露 similarity miss）。这是真实的优点，但它制造了一种**虚假的安全感**：每一张卡都判得对，不代表"卡集整体无冗余"。三层架构那 4 张卡，**每一张的 provenance_delta 判定单独看都成立**（都是"对同一张 v2 卡的 delta"），但"它们彼此重复"这件事，因为没有任何阶段让它们互相照面，**永远不会被任何单卡决策发现**（`drift_audit` §3.2/§10.2）。教训：**单点决策质量审计无法替代集合级去重审计**；前者答"这张判对了吗"，后者答"这堆有没有重复"，是正交的两个问题。

**根因 5：工程隔离的成功证明缺陷不在执行层。** 边界 0 越界、完整性 6/6、hook 1374 次 0 冲突——执行层近乎完美。这把缺陷**精确定位到设计层**：v3 完美地执行了一个起点就偏离 INV-1 的流程。教训：**当执行无可挑剔而结果仍有缺口时，问题一定在合同/设计，不在 worker**。

---

## 6. 下一轮 loop 的目标流程（PRESCRIPTIVE）

把 §1 理想与 §5 教训合并，下一轮应跑的**固化流程**：

1. **比较语料从第 1 张卡起就只用 self。** 重写 `similarity_top3.py`：**删除 `V2_INDEX` 常量与所有 v2 路径**（当前 `:30/117-119/126/165`），语料 = 本 loop 累积的 drafts/cards 全配对 jaccard；第一张 draft 的 base 是空集。改写 `DRAFT_FIRST_PIPELINE_V3.md:31` / `RUNBOOK.md:71` / `LOOP_START_PROMPT.md:81-82/108-109`：删掉"default base v2 until..."，改为"comparison base 永远是本 loop 自己累积的 drafts/cards；loop 之间永不互比"。（INV-1）

2. **在 draft 与 adoption 之间插一道显式 intra-loop all-pairs 去重/合并 pass。** 因为批量并行没有增量去重的时刻，必须显式补：对全部 draft 标题做 all-pairs jieba-jaccard + catalog 聚类，对高分对 full-read 复核 → `merge_candidate` / `duplicate_skip` 决策 → 合并。反转 `comparison_worker_prompt.md:33`：从"禁止读兄弟 draft"改为"读你被分到的兄弟-draft top-k 候选"，让 intra-self 去重在结构上成为可能。（INV-2）

3. **draft 出生即 unified-footnote 格式，取消迁移阶段。** 卡在 Stage 1 就只用 `## Footnotes` 单一引用枢纽（target 仅 raw 源 / 兄弟 v3 卡 / URL，**无 v2 target**），`related:` 全程由 `derive_metadata_from_footnotes.py` 派生、视为只读。这样省掉整个 citation migration 阶段（实测 1.42M + 623K fallback）。（INV-3）

4. **边界 ENFORCE 独立性，而非仅允许。** 从 `CONTEXT_BOUNDARY.md` 的 similarity/comparison 读 allowlist **删除 v2 索引与 v2 卡**（当前 `:78`），删除 `:7` 的"V2 candidate cards may be used as comparison material"原则句。加一条 lint/hook：footnote / related / similarity 中出现 `v[0-9]+_*_loop_*` 外部路径即告警。让边界**强制**独立性（当前是"既允许读 v3 也允许读 v2，结果工具选了 v2"）。（INV-1 强约束化）

5. **阶段合并，减少横扫趟数。** 把"全 171 张过一遍"的多趟横扫，尽量合并为"一张卡尽量一次走完 draft→similarity→去重→interlink→gate"，减少同一文件被不同阶段重复 Read（当前 ~540K 结构性重复）。配合：full read 作为 draft 出生规则（消除 arxiv 重读债）、classifier reject 第 1 次即切 fallback 且拆 N 个小 agent（消除 623K 单笔大 fallback）。

6. **去重审计与决策审计并列为两道独立验收。** 下一轮收尾必须同时跑：(i) 单卡决策质量抽样（沿用本轮 29/29 的方法）；(ii) 集合级 intra-self 近重复扫描（all-pairs，确认 `merge_candidate` 计数反映"真看过"）。两者正交，缺一不可。

一句话概括 §6 目标流程：**一个从第 1 张卡起就 self-only 语料、unified-footnote 出生、在采纳前强制做一道兄弟 draft 全配对去重、并由边界 lint 强制 loop 独立性的、横扫趟数更少的 0→1 流程。**

---

## 7. 证据索引

- 理想/原则：用户 2026-05-29 loop 独立性原则（`comparison_corpus_drift_audit.md` §0/§9/§10）；unified-citation 真理源原则（`CARD_CONTRACT_V3.md:70-119`、`docs/v3_loop_journey.md` §4.4）。
- 合同 v2-base 缺陷：`DRAFT_FIRST_PIPELINE_V3.md:31`、`RUNBOOK.md:71`、`LOOP_START_PROMPT.md:81-82/108-109`、`CONTEXT_BOUNDARY.md:7/78`。
- 去重缺位：`comparison_worker_prompt.md:33`（禁读兄弟 draft，转引自 `drift_audit` §2.3）；五份合同无 intra-self 去重需求（`drift_audit` §1.6）。
- 工具硬编码：`tools/similarity_top3.py:30/117-119/126/129/141/165`（转引自 `drift_audit` §2.1）。
- 实际数据：171/171 v2 base、count=15（`drift_audit` §2.2、`pipeline_integrity_audit.md` §2.3）；163/8/0 决策（`reports/loop_report.md:63-65`）；974 边（`reports/loop_report.md:28`）；171/171 采纳（`reports/loop_report.md:66`）；4 张三层架构重复卡（`drift_audit` §3.2）。
- 成本：~10M 总 / 60K 单卡（`token_consumption_audit.md:371-372`）；adoption 1.74M / migration 1.42M / batch 1.45M / arxiv revision 1.24M（`token_consumption_audit.md` §1.2）；derive_metadata fallback 623K（§4）；结构性重复 ~540K（§5）。
- 执行干净度：0 越界（`boundary_compliance_audit.md` §2/§9）；6/6 完整性（`pipeline_integrity_audit.md` §10）；29/29 决策（`decision_quality_audit.md` §7）；42/42 worker（`worker_dispatch_audit.md` §0）；1374 commit 0 冲突（`hook_and_classifier_audit.md` §2）。
- 时序佐证：unified-citation = 2026-05-28 事后迁移（`docs/v3_loop_journey.md` §3.5）；v2 依赖在 v3 诞生第 3/47 分钟即写入合同/工具（`drift_audit` §9）。

---

## 8. 更正与补充：设计意图还原与开放问题

> 本节据项目作者 2026-05-29 的说明补写，纠正 §0–§5 把若干**深思熟虑的权衡**误判为"缺陷"的地方。前面各节的**事实**（语料只比 v2、去重 pass 缺位、merge=0、unified-citation 是事后迁移）依然成立，需要还原的是其**动机与定性**。

### 8.1 批处理不是执行偶然，而是刻意选择

§0 裂缝4 / §5 根因1-2 把"批量并行生成"当作消灭增量去重时机的负面因素。这个因果链在事实上成立（批量确实没给增量去重留窗口），但把批处理本身说成缺陷是错的——批处理是针对当前阶段的合理选择，理由有三：

1. **增量 draft→KB 会造成 material 的重复消耗。** 若每张 draft 直接入库，逻辑上变成"读一个 raw material → 跑完整套流程 → 再回头重跑去消费这张卡"——同一份 material 被反复读取，流程不通畅。批处理"一次读尽一个 source、一次产出该 source 的全部卡"恰好避免了这种 re-consumption（与 §1 Stage 1 的 full-read 出生规则同源）。

2. **seed card / root card 无法预先指定。** 有些知识相对底层、彼此可融合——典型如"llm wiki 的定义"。理想上它应当**融合成一张卡（或一张 hub card）**，由多个 raw material 共同喂养，并在 provenance 里论证"从哪个源得到什么结论"。但**哪些 topic 是 seed / hub 无法事先划定**——强行指定 seed topic 既困难又武断。因此这本质上**依赖 agent 自主判断**；而 agent 要自主判断"什么该融合成 hub"，前提是它能**同时看到一批卡**，而非一张一张孤立地流过。批处理为这种"集合级自主融合"留出了可能（尽管本轮没真正实现 fusion，见 §8.3）。

3. **当前阶段的核心任务是"知识入库"（ingestion）。** v3 这一轮聚焦于把分散在 72 个源里的知识可靠地变成卡。在这个目标下，批处理是恰当的吞吐模型。

**修正后的定性**：批处理是对的；缺的不是"别批处理"，而是"批处理之后必须显式补一道**集合级**的 intra-self 去重/融合 pass"（§6.2 处方不变）。§5 根因2 的措辞应从"批量并行是去重缺口的合谋者"理解为"批量并行是正确的 ingestion 模型，但它要求去重必须实现成一道显式的集合级 pass，而这道 pass 缺位"。

### 8.2 adoption 不是正式流程，而是一次 schema 修补

§3 Stage 5+6 与 §4 表第 6 行把 adoption 当作管线里的一个正式阶段来审计。实际上 adoption 是因为**早期 schema 存在问题**而做的一次**修正/补丁**——是当初 design 不够清晰留下的债，不是设计里有意安排的正式准入阶段。

但要点在于：作者**认可**审计指出的结构性结论——draft 进 KB 确实**缺一个像样的 gate / 准入门槛**。所以这里不是给 adoption"平反"，而是更准确地命名它：它是一次**事后修补**，填补的正是那个本该存在却从一开始就缺席的 gate。"adoption 是补丁"这个事实，恰恰印证了"正式发表门从未被设计好"。

### 8.3 similarity 粗糙（rule-based 而非 semantic）→ 直接导致 fusion 缺席

§3 Stage 2 已指出 similarity 是 jieba+jaccard。这里补一层因果：similarity 不仅"只比了 v2"，它本身**是基于规则（标题 token 集合）而非基于语义的**——这才是它粗糙的根因。正因为它粗糙到只能做"标题撞词"级判断，**fusion 这个环节就没能长出来**。

逻辑上，**similarity 计算之后本应紧跟一道 fusion**：similarity 找出"可能是同一件事"的候选 → fusion 决定是否融合成一张（hub）卡。本轮因为 similarity 退化为规则级 + 语料指向 v2，这条"similarity → fusion"的自然衔接整个断掉。这与 §8.1.2 的 hub-card 设想是同一件事的两面：要把"llm wiki 定义"这类底层知识融成 hub，必须有一个**语义级 similarity** 把分散在多源的同义卡聚到一起，再 fuse——规则级 similarity 做不到。（本轮 4 张三层架构卡正是"本应 fuse 成一张 hub 却各自独立入库"的实例。）

### 8.4 开放问题：入口治理 vs 入库后治理（尚未想清）

审计 §1/§6 默认了一种哲学：**在入口处就 gate / 去重 / 融合**（"产一张、判一张、该融则融再入库"）。但还有另一种哲学值得摆上台面：

- **先不管，直接入库**——所有 draft 无门槛进 KB，把去重、依赖、hub 融合等问题**全部推迟到后续的"治理 / 迭代"环节**去解决。

这条"先入库后治理"的路线**与当前声明的流程相违背**（当前是入口 gate 哲学）。更关键的是：**后续的治理 / 迭代环节本身还没想清楚**——它要怎么发现重复、怎么把分散卡融成 hub、怎么维护依赖，目前都没有明确设计。

所以这是一个**真正悬而未决的设计岔路**，不是已有答案的"应该怎么做"：

- **路线 A（入口治理）**：§6 的处方——self-only 语料 + 采纳前强制一道 intra-self 去重/fusion pass。优点是 KB 始终自洽；代价是入口处要做语义级 similarity + fusion，复杂度高。
- **路线 B（入库后治理）**：入口极简，靠迭代治理收敛。优点是 ingestion 吞吐最大、不阻塞；代价是 KB 在治理跟上之前是"带重复的草稿态"，且治理环节必须被真正设计出来（当前空缺）。

本审计**不替这个岔路下结论**。它需要作者在"KB 何时必须自洽"与"治理环节能否被设计出来"之间权衡后决定。一个折中观察：在治理环节成型之前，路线 A 更安全（至少 KB 不会越长越脏）；但若 ingestion 吞吐是当前唯一目标、且接受 KB 暂为草稿态，路线 B 也成立——前提是**承认并补上**那个尚不存在的治理环节，而不是默认它会自然发生（这正是本轮 similarity→fusion 断链的同型错误：不能指望未实现的环节自动出现）。
