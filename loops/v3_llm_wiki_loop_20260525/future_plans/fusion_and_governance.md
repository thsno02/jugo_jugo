---
status: future_plan
stage: discussion_only
created: 2026-05-29
loop_id: v3_llm_wiki_loop_20260525
topic: fusion_and_governance
note: 本文档由 v3 审计衍生，面向"下一阶段（KB 成型后）"的治理设计，仅供讨论，尚未执行。scope 限于本 loop 的前瞻规划。
---

# Future Plan：Fusion + 治理子系统

> 分阶段 ingest→govern、嵌入召回为主、永不删除的 storage/view。
>
> 来源：本设计把同 capsule 内 `audits/loop_flow_expected_vs_actual_audit.md` §6/§8 与 `audits/comparison_corpus_drift_audit.md` §10 的结论，结合用户 2026-05-29 的决定，落成一份前瞻设计。**当前 ingestion 阶段不阻塞；本文是"KB 成型之后"的治理设计。**

## 0. 为什么需要它

v3 审计发现 fusion 环节从未发生：`tools/similarity_top3.py` 是 rule-based（jieba+jaccard）且语料硬编码指向 v2，没有任何 intra-self 去重/融合 pass，导致本该融成一张 hub 的卡（Karpathy "raw/wiki/schema 三层架构" ×4）以重复形态躺在 KB 里。用户要的不是"补一个 fusion 步骤"，而是一套**可 scaling、永不丢知识**的治理子系统。

核心约束与决定（2026-05-29 确认）：

- **分阶段**：init KB 阶段先入库后治理（ELT）；KB 成型后用统一治理方案做 fusion / 监督 / 分辨。
- **召回是手段，不是目的；选 grep 为主**：similarity / embedding / jieba / grep 都只是手段。本设计用 **agent 自主 grep** 召回，质量靠把卡设计成 **grep-friendly**（`canonical_concept` / `aliases` / `key_terms` / `summary`）来工程化——**把智能推进数据模型，而不是推进检索算法**。v1 **纯 grep**，embedding / jieba / 图全部不用——保持最 ai-native 的形式。**不追求完备**——直接放弃 O(N²) 的完备性焦虑。
- **治理的 zen**：治理的目的**不是解决所有问题，而是让问题更简单**。每次治理单调地降低 KB 的熵、不追求"完美状态"；增量、best-effort、像**园艺**而非证明定理。这正是可以心安理得放弃完备性的理由——目标是"更简单"，不是"全解决"。
- **永不删除**：知识卡只"移出可消费 view"，不从 library 删除——因为它过去代表了可溯源的知识。

## 1. 分阶段模型

- **Phase A — init KB / ingestion（route B / ELT）**：源忠实的卡立即入库，无 fusion gate；入库时**增量建召回索引**（embed-on-ingest）。库始终可溯源（可能暂时冗余）。这是单个 loop 的 ingestion 职责。
- **Phase B — mature KB / governance**：KB 成型后跑**统一治理 pass** —— fusion + supersession + 分辨。触发默认"每个 loop 的 ingestion 完成后跑一次"，也可按卡数阈值 / 按需。

> 关键：Phase B 必须**被真正设计出来**，不能默认它会自然发生——否则就是 v3 "similarity→fusion 断链"的同型错误（指望未实现的环节自动出现）。

## 2. 召回：纯 grep + agent 自主（ai-native，v1 不用 embedding/jieba/图）

similarity / embedding / jieba / grep 都只是**手段**。v1 选 **纯 grep**——透明、零基础设施、可解释、最 ai-native，且召回质量可以靠**把卡设计成 grep-friendly** 来工程化：**把智能推进数据模型，而不是推进检索算法**。grep-only 的代价是"同概念全异词、无共享 metadata"召不回——这个盲区交给 metadata 纪律（§2.1）压小、再交给治理 zen 吸收，不引入更重的检索去强解。

- **机制 = agent 自主**：fusion 由 agent 驱动——拿着一张卡，自主决定 grep 哪些词（`canonical_concept` / `aliases` / `key_terms` / `tag`），读命中的兄弟卡，再生成融合结果。agent 本身就是"召回 + 判断 + 生成"的闭环，而非固定阈值的流水线。
- **让 grep 准的关键 = grep-friendly metadata**（建卡 agent 在 **card-creation 时**写好）：`aliases`（同义别名）、`canonical_concept`（归一化概念 id）、`key_terms` / `tags`（可搜词）、一行稠密 `summary`。**recall 质量来自一致的 metadata 纪律，不来自向量模型。** 真正的设计功夫在这里。
- **不追求完备**：直接放弃 O(N²) 完备性焦虑。grep 只召回它能召回的；漏的（同概念、全异词、无共享 metadata）交给"治理 zen"吸收（best-effort + 增量），而不是用更重的检索去强解。
- **v1 只用 grep**：embedding / jieba / 图 co-citation 全部不用，保持最 ai-native 的形式。仅当远期 grep 被证明严重不足才再议 embedding（届时也只作 fallback）；当前**不作任何前置依赖**，也绕开"endpoint 有没有 embedding 模型"这个开放项。
- **决策分类仍由 LLM 判断**：候选读进来后，agent 判成 merge / distinction / contradiction / keep（反义/contrast 显式召回延后 v2）。
- **成本**：grep 近零；成本在 agent 读命中卡 + 生成，靠 best-effort + 增量控制。

## 2.1 grep-friendly metadata schema（v1 的核心设计）

grep-only 意味着 metadata 是**唯一**让 grep 生效的东西。但"限定"指的是**格式规则 + canonical 复用收敛**，**不是预定义/互斥 taxonomy**（exclusive taxonomy 是灾难、没人维护就失效；卡遵循 Zettelkasten 哲学）。grep 锚点是**描述这张卡内容的 per-card 字段**，不是把卡塞进分类：

- **`canonical_concept`（grep 锚点）**：每卡一个归一化概念 id。格式规则：kebab-case、英文、单数、受限字符集。建卡时 agent **先 grep 已有卡的 canonical_concept，命中则复用，无则新铸**——让概念集自收敛，KB 本身就是 tag registry（可 grep），不需要单独注册表。
- **`aliases`**：该概念的真实表层变体（含中英文、缩写、符号形式，如 `三层架构` / `raw/wiki/schema` / `three layers`），让 grep 任一变体都能命中。规则：列实际会被搜的表层串，不臆造。
- **`tags` / `card_type`**：自由描述、可选（Zettelkasten，**不设互斥 taxonomy**）。不充当受控分类网格；结构靠 footnote 链接 + 治理涌现，不靠分类。
- **`summary`**：见 §2.2。

**规则的执行分两段**（配合 §1 分阶段 + best-effort，把负担放对地方）：

- **建卡时（Phase A，并行）**：只守**格式规则**（cheap、确定性）+ 尽力复用 canonical / 选已有 tag。并行建卡无法完全收敛，**允许不完美**——保持低心智负担。
- **治理时（Phase B）**：agent grep summaries/aliases 找出变体簇，**归一化 canonical_concept + 合并**。受控词表的真正"对齐"发生在这里，而非建卡时。

## 2.2 summary metadata：要，且把它设计成"grep 靶子"

是否要 summary？**要。** 卡是 agent 生成的，顺手产一行 summary **零额外心智负担**；而且它能当召回的**主靶子**。

- **定位**：summary 不是给人看的摘要，而是**为 grep 优化的稠密一行**——刻意把 `canonical_concept` + 关键 `aliases` + 核心论断打包进一句话。于是"grep over summaries"成为**主召回**（高信噪比），body 作兜底。
- **与 title 区分**：title 是 headline（概念名）；summary 是 claim（这卡断言了什么）+ 召回信号。两者不冗余。
- **治理收益**：governance agent 可只 grep/读 summaries 找重复簇，不必打开全文——治理更便宜，token 边界更紧。
- **结论**：summary 可能是**单字段杠杆最高**的——既是主 grep 靶子，又是治理的廉价 skim 面。

## 3. fusion 决策空间（非二元 merge）

- **merge → hub card**：底层概念（如 llm-wiki 定义）随召回**密度涌现**为 hub，不预先指定 seed；hub 吸收被并卡的 provenance（论证从哪个源得到什么结论）。
- **link-as-distinction（分辨）**：同主题、不同/反立场 → 链成 tension，不合并。
- **subsume**：一张卡的知识折叠进另一张。
- **keep-separate**：保持独立。

## 4. 永不删除的 storage / view（文件系统改造）

- **STORAGE（library）**：所有卡永久留存；不 hard-delete；git history 是最终兜底。
- **VIEW（可消费）**：只含 active 卡 + 索引。
- **fusion 时**：被取代的卡打 `status: superseded` + `superseded_by: <hub-id>` + **物理移到 `kb/archive/`**，离开可消费 view 但留在 library（可溯源、可读、可 git 恢复）。
- 推荐布局：`kb/cards/` = active；`kb/archive/` = superseded；索引（view）只扫 active。

## 5. 实施时的关键文件（待执行阶段参考）

- `tools/similarity_top3.py` → 重写为 self-corpus + 召回（或拆出 `tools/recall.py`）；删除 v2 硬编码（当前 `:30/126/165`）。
- 新建 `tools/embed_cards.py` + 向量索引文件（embed-on-ingest）。
- 新建 `tools/govern.py`：治理 pass（召回 → LLM 判断 → merge/supersede/archive 落盘）。
- `tools/build_kb_index.py` → 改为"只索引 active 卡"（view = active）。
- 新建治理合同：下一个 loop 的 `FUSION_AND_GOVERNANCE.md`（分阶段、召回、决策空间、storage/view、触发条件）。
- 更新现有合同：去掉 v2 比较基、加入 governance 阶段与 storage/view（`DRAFT_FIRST_PIPELINE_V3.md`、`CONTEXT_BOUNDARY.md`、`SIMILARITY_MECHANISM_V3.md`、`RUNBOOK.md`、`LOOP_START_PROMPT.md`）。

**可复用**：`tools/derive_metadata_from_footnotes.py`（治理后重派生 `related:`）；`tools/build_kb_index.py`（索引/view 重建，改 active-only）；现有 `accepted_card_provenance.v3` schema（扩 `status`/`superseded_by` 字段即可承载 storage/view）。

## 6. 验证设想（待执行阶段）

1. **召回正确性**：嵌入现有 171 张卡，对 Karpathy 三层架构簇跑召回，确认 4 张被召回到一起。
2. **治理 dry-run**：在现有 v3 KB 上跑 `govern.py`，确认标出 ~15-20 张已知近重复、提出 hub 合并；superseded 卡移入 `kb/archive/`，索引只剩 active。
3. **token 边界**：测 LLM 判断 token = `O(candidates)`，确认有界；召回 token ≈ 0。
4. **可溯源**：确认 archived 卡仍可读 + git 可恢复 + provenance 完整（hub 吸收了被并卡的源）。

## 7. 待定 / 开放项

- **metadata schema 细化（最关键，主体见 §2.1/§2.2）**：待定的是 `tags` 受控词表的初始维度集、`canonical_concept` 命名细则、以及建卡时"grep 复用 canonical"步骤的具体提示词。
- **embedding 已移出 v1**：v1 纯 grep；embedding 仅在远期 grep 被证明严重不足时才重议（届时也只作 fallback）。
- **governance 触发条件**：默认"loop ingestion 完成后跑一次"，但"KB 成型"的判定标准（卡数阈值？按需？）待定。
- **archive 实现粒度**：物理移到 `kb/archive/`（推荐，匹配"放到其它地方"）vs 仅 status-flag + view 过滤；倾向物理移动 + status 双保险。
- **hub 涌现阈值**：召回密度到多少算 hub 候选，待校准。
