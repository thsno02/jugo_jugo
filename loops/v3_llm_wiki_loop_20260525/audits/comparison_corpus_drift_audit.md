---
schema: audit.v3
topic: comparison_corpus_drift
loop_id: v3_llm_wiki_loop_20260525
created_time: 2026-05-29T15:40:00+08:00
auditor: llm
status: complete
---

# V3 Loop 比较语料漂移审计（intra-v3 去重缺口）

> 范围：审计 v3 draft-first pipeline 的 similarity / comparison 阶段所用的"比较语料"（comparison corpus）。核心问题：comparison/dedup 阶段是否按设计对 **v3 KB 自身**（draft-vs-draft / draft-vs-accumulated-v3）做了去重，还是错误地只对 **旧 v2 KB** 做了比较，从而导致 v3 内部重复从未被检查。

## 0. TL;DR

- **确认：intra-v3 去重从未发生过。** 全部 171 张 v3 draft 的 similarity 比较基 100% 是 v2 索引（`comparison_base` 字段在 171/171 个 JSON 里完全一致），且 `comparison_base_card_count` 恒为 **15**——即每一张 v3 draft 都只跟同一组 **15 张 v2 卡** 比，从未和任何 v3 兄弟卡比过。
- **更糟：这 15 张 v2 卡全部来自 2 个 Karpathy 源**（gist + X launch post），主题只覆盖"Karpathy 原始 LLM Wiki 概念"。而 v3 跨 43 个源、覆盖 memory / RAG / 安全 / 治理等主题。对约 150 张 arxiv/工具类 draft 而言，这个 v2 语料**结构上不可能**提供有意义的去重候选——它们的 "top-3" 基本是 jieba 噪声命中。
- **`merge_candidate = 0` 是"从没看过"，不是"确实没有重复"。** comparison worker 被合同**明确禁止读其他 draft 卡**（`comparison_worker_prompt.md:33`），所以两张 v3 draft 在结构上不可能进入同一次比较。
- **根因（三因叠加）**：(c) `tools/similarity_top3.py` 把 v2 索引**硬编码**为唯一语料，没有任何 v3 自比路径或切换逻辑；(b) 171 张 draft 一次性批量生成 + 批量比较，从未出现"拿新 draft 比累积 v3"的增量时刻，导致合同里"等 v3 有自己的 accepted 索引后再切换"的切换点永远不会触发；(a) v2-as-base 本身是 bootstrap 阶段（首轮无 v3 KB）的**有据可查的默认选择**（`DRAFT_FIRST_PIPELINE_V3.md:31`），不是私自漂移。
- **影响**：保守估计 ~15-20 张卡是彼此的近重复（约 10-15% KB 膨胀），集中在 cluster A（LLM Wiki 概念，49 张）。最强证据是 **Karpathy "raw/wiki/schema 三层架构" 一个概念被 4 张卡重复承载**。按 ~60K token/卡的 v3 全 pipeline 单卡成本估算，这些冗余卡的下游处理浪费约 **0.7-1.1M token（占 ~10M 总量的 ~7-11%）**。
- **不是数据损坏**：footnote 图没有断链、related 边都有效、知识本身正确。这是"重复卡未被发现"+"图里有一簇冗余近重复节点"，不是"图坏了"。讽刺的是 interlink 阶段把这些重复卡织成了一个看似健康的 related 簇，反而掩盖了重复。
- **判定**：真实缺口，YES。严重度 **MEDIUM（偏 medium-high）**。一句话修复：**让 `similarity_top3.py` 对每张 draft 额外输出一份"对其他 v3 draft 全配对打分"的候选列表，并在 adoption 前加一道 draft-vs-draft 的 merge_candidate 复核 pass。**
- **设计原则修正（2026-05-29，用户）**：每个 loop 是独立的 0→1 过程，v3 不应以任何形式依赖 v2。据此 §6 / §7 中"保留 v2 作为 SECONDARY 跨 KB provenance"的建议被**推翻**——正确做法是比较基**只用 v3-self**，v2 完全移除（含 8 张 `v2_anchor` 卡 + body `[^v2-1]` footnote 的去污染）。**溯源**（v2 依赖何时进入）见 §9；**修复与下一轮预防**见 §10。

---

## 1. 设计意图（DESIGN INTENT）：合同到底要求拿什么做比较基？

逐一核对五份合同，结论是：**合同从未把"对 v3 兄弟卡去重"列为一项明确需求**；它明确写的是"对 accepted 卡索引比较"，且**默认基就是 v2**。

### 1.1 `DRAFT_FIRST_PIPELINE_V3.md` — 唯一明确点名语料的合同

- 第 28 行（Stage 2）："tokenize accepted card titles from **the configured comparison index**" —— "配置好的比较索引"，单数、可配置。
- **第 31 行（关键句）**："The default comparison base is `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md` **until v3 has its own accepted index**." —— 明确把 v2 索引设为**默认**比较基，并用 "until v3 has its own accepted index" 暗示**本意是等 v3 有了自己的 accepted 索引后切换过去**。

这一句是整个审计的轴心：v2-as-base 是**写进合同的、有意为之的 bootstrap 默认**（不是私自漂移）；但它附带了一个"之后要切到 v3"的承诺，而这个承诺**从未被实现**（见 §2、§4）。

- 第 46-51 行（Stage 4 decisions）：`merge_candidate`（"draft and A should likely become one card"）、`duplicate_skip`（"draft is already covered"）——这套决策词汇读起来像**语料内部去重**，但合同里的 "A" / "accepted cards" 从未限定是 v2 还是 v3。词汇是语料无关的；接线却只指向 v2。

### 1.2 `SIMILARITY_MECHANISM_V3.md` — 对"哪个 KB"保持沉默

- 第 7 行："It narrows the comparison set for a new draft card so agents do not repeatedly read **the whole KB**." —— "the whole KB" 未限定 v2/v3。
- 第 16 行（Input）："accepted card title index" —— **没有点名 v2 还是 v3**。这是一处沉默/歧义：bootstrap 时唯一的 accepted 卡就是 v2，于是"accepted index"自然=v2，但合同没有强制说明 v3 自身的 accepted 卡（adoption 之后产生）也应进入这个索引。

### 1.3 `CONTEXT_BOUNDARY.md` — 读范围其实**允许 v3 自比**（反而不是"只准读 v2"的铁证）

- similarity_top3 读 allowlist（第 72-78 行）同时允许：
  - 第 77 行：`outputs/llm_wiki/kb/indexes/cards.md`（**这是 v3 自己的索引**，相对 loop root）；
  - 第 78 行：`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`（v2 索引）。

  **重要**：read-scope 并没有把语料锁死成 v2-only——它**显式允许读 v3 自身索引**。所以"只比了 v2"**不是** boundary 逼出来的；恰恰相反，boundary 给了 v3 自比的许可，但工具（`similarity_top3.py`）忽略了这个许可（见 §2.1）。这一点很关键：它把根因从"合同禁止"排除掉，定位到"工具未实现"。

- comparison_provenance 读 allowlist（第 86-94 行）："only the top 3 existing card bodies named by the similarity result"——comparison 阶段**只读 similarity 给出的 top-3**，自身没有独立的 v3 自比通道。similarity 只吐 v2，comparison 就只能比 v2，缺口逐级传递。

### 1.4 `PROVENANCE_CONTRACT_V3.md` — "draft vs A card"，A 未定义

- 第 18 行：comparison provenance 解释"a new draft card and an existing A card"之间的决策。"A card" 全程未定义为 v2 还是 v3，语料无关。

### 1.5 `CARD_CONTRACT_V3.md` — 数据模型**区分** intra-v3 与 cross-v2，但那是"链接"不是"去重"

- 第 50 行、第 86-89 行：footnote/`related:` 显式支持 "v3 KB card (same loop)" 与 "v2 KB card (cross-loop)" 两种 target。所以数据模型**知道** intra-v3 和 cross-v2 的区别——但这是为了 **interlink（"see also"链接）**，**不是 dedup（"同一主张，合并"）**。这正是题目要求区分的关键：链接 ≠ 去重。合同把"链接到相关 v2 卡 / 跨 KB provenance"做得很细，却**从未**把"在 v3 内部去重"写成一项任务。

### 1.6 Q1 结论

| 问题 | 答案 | 证据 |
|---|---|---|
| 合同有没有说比较基应是 v3-self？ | **没有明确说** | similarity/provenance 合同对"哪个 KB"沉默 |
| 合同有没有说比较基应是 v2？ | **有，作为默认 bootstrap 基** | `DRAFT_FIRST_PIPELINE_V3.md:31` |
| 合同有没有说应该 both？ | **隐含**："v2 until v3 has its own index" 暗示先 v2 后切 v3 | `DRAFT_FIRST_PIPELINE_V3.md:31` |
| "对 v3 兄弟卡去重"这个真实需求被明确指定过吗？ | **从未** | 五份合同均无 |
| read-scope 是否把语料锁死成 v2-only？ | **没有**，反而允许读 v3 索引 | `CONTEXT_BOUNDARY.md:77` |

**一句话**：设计意图对 intra-v3 去重是**沉默/未指定**的；它明确选了 v2 作为**默认 bootstrap 比较基**并承诺"之后切 v3"。所以这不是"合同要求 v3-self 却被改成 v2"的漂移，而是"合同承诺要切 v3 却从未兑现 + 从未把 intra-v3 去重写成需求"的**漏实现型缺口**。

---

## 2. 实现现实（IMPLEMENTATION REALITY）：实际跑的是什么？

### 2.1 `tools/similarity_top3.py` —— 单一最重要证据：v2 被硬编码为唯一语料

逐行钉死：

- **第 30 行**：`V2_INDEX = REPO_ROOT / "loops" / "v2_llm_wiki_loop_20260525" / "outputs" / "llm_wiki" / "kb" / "indexes" / "cards.md"` —— v2 路径被**硬编码**，是脚本里**唯一**的语料常量。
- **第 117-119 行**：`if not V2_INDEX.exists(): print("ERROR: v2 index missing"); return 2` —— v2 索引是**硬性必需**前置。
- **第 126 行**：`existing = parse_v2_index(V2_INDEX)` —— 装载的语料**只有** v2。
- **第 129 行**：`drafts = sorted(p for p in DRAFT_CARDS_DIR.glob("*.md") ...)` —— 一次性 glob **所有** draft，批量跑。
- **第 141 行**：`for row, ex_tokens in existing_tokens:` —— 每张 draft **只**对 v2 行打分。**脚本里不存在任何 draft-vs-draft 的循环**。
- **第 165 行**：输出里硬编码 `"comparison_base": "loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md"`。
- **全脚本无任何对 v3 索引（`outputs/llm_wiki/kb/indexes/cards.md`）的引用**：没有 flag、没有 fallback、没有 merge、没有"如果 v3 索引存在就切换"的逻辑。

→ **假设 (c) 直接坐实**：脚本把 v2 索引硬编码为语料。合同第 31 行承诺的"等 v3 有自己的索引后切换"——**脚本里根本没有能执行这个切换的代码**。

### 2.2 数据层验证：171/171 全是 v2，且语料只有 15 张卡

对 `outputs/llm_wiki/drafts/similarity/*.json`（171 个文件）聚合：

- `comparison_base` 字段：**171 次**全部 = `loops/v2_llm_wiki_loop_20260525/.../cards.md`（无第二种取值）。
- `comparison_base_card_count` 字段：**171 次**全部 = **15**。
- 全部候选 `card_path` 都指向 `llm_wiki/kb/cards/<v2-id>.md`（v2 卡）；**没有一个 v3 候选**。最高频候选：`idea-file-abstract-vague`(114)、`llm-wiki-three-layer-architecture`(106)、`llm-wiki-schema-configuration-document`(100)、`llm-wiki-health-checks`(66)。

v2 语料本体（`loops/v2_.../kb/indexes/cards.md`）实测 **15 行卡**，且全部来自 **2 个源**：`karpathy-gist-llm-wiki`（12 张）+ `karpathy-x-launch-post`（3 张：idea-file-share-the-idea / idea-file-abstract-vague / llm-wiki-health-checks）。

→ **结构性后果**：v3 跨 43 个源（mem0、memgpt、ARES、GraphRAG、OWASP、Wikibase、Zep……），却只拿一组"纯 Karpathy 原始概念"的 15 张卡当去重基。对那 ~150 张 arxiv/工具/安全类 draft，这个语料**不可能**给出真去重候选——它们的 top-3 只是 jieba 在"的/LLM/wiki"等高频中文 token 上的噪声命中（loop_report.md:108 自己也承认这是"token 误中"）。能找到真 v2 邻居的只有约 20 张"LLM Wiki 概念"类 draft，而这恰恰是 intra-v3 重复聚集的地方——但它们也只跟 v2 比，没跟彼此比。

### 2.3 `task_templates/comparison_worker_prompt.md` —— worker 被告知比 v2，且被禁止读兄弟 draft

- 第 30 行：top-3 候选是 "**v2 accepted-card body**"，文件在 `loops/v2_llm_wiki_loop_20260525/.../cards/<id>.md`。
- 第 31 行：必要时读 top-3 的 **v2** provenance。
- **第 33 行（结构性铁证）**：「**禁止**：通读 v2 KB；为推断意图去读 v2 iterations/...；**读其他 draft 卡片**。」—— comparison worker 被**明确禁止读其他 draft 卡**。这意味着 intra-v3 去重在 comparison 阶段**结构上不可能发生**。
- 第 102 行：`provenance_delta` 定义为"反向链接进 **v2 卡** provenance"——delta 的对象写死是 v2。

### 2.4 comparison 文件实测

`outputs/llm_wiki/drafts/comparison/*.md`（171 个）：

- 决策分布：**163 new_card / 8 provenance_delta / 0 其他**（与 loop_report 一致）。
- `audit_required`：163 false / 8 true。
- `existing_cards` 里的 `card_id` 全部是 v2 id，且与 similarity 的 15 张同源（最高频 idea-file-abstract-vague 114、llm-wiki-three-layer-architecture 106……完全继承 similarity 的 v2-only 候选池）。

→ comparison 阶段 100% 继承了 similarity 的 v2-only 候选池，自身没有任何 v3 自比。

---

## 3. intra-v3 去重缺口（INTRA-V3 DEDUP GAP）

### 3.1 有没有任何阶段做过 draft-vs-draft 去重？——没有

- **similarity**：只比 v2（§2.1）。
- **comparison**：只读 similarity 的 v2 top-3，且被禁止读兄弟 draft（§2.3）。
- **interlink**：**在 v3 内部运行**（填 `related:`，974 条边），但它是 **"see also" 链接，不是去重**。`interlink_worker_prompt.md:42` 甚至把重复的三层架构卡当作"跨源同概念"related 的**典范示例**："karpathy-gist 的'三层架构'和 anthemcreation 的'三层架构落地'"。也就是说——**interlink 把重复卡发现了，却把它们框定为"值得互链"而非"应当合并"**，反而把重复织成了一个看似健康的 related 簇。
- **fusion_audit / publication_gate**：只处理 comparison 已给出的决策（8 prov_delta + 163 new_card），不重新做 v3 自比。

**结论**：没有任何阶段做过 draft-vs-draft 去重。

### 3.2 171 张里有多少是彼此的重复？（catalog-first 估算 + 抽样确认）

以 `outputs/llm_wiki/kb/indexes/cards.md` 标题清单扫近重复簇，只对最强簇做 full-read 确认：

**簇 1：Karpathy "raw/wiki/schema 三层架构" —— 4 张，已 full-read 确认为近重复（最强证据）**

| id | source_id | card_type | v2_anchor |
|---|---|---|---|
| `karpathy-gist-three-layers` | karpathy-gist-llm-wiki | distinction | llm-wiki-three-layer-architecture |
| `karpathy-llm-kb-three-layer-arch` | developersio-jp-pattern | concept | llm-wiki-three-layer-architecture |
| `karpathy-llm-wiki-three-layers` | marvin-hn-persistent-knowledge | concept | llm-wiki-three-layer-architecture |
| `anthemcreation-llm-wiki-three-layer-architecture` | anthemcreation-fr-guide | concept | llm-wiki-three-layer-architecture |

四张卡的**核心知识完全相同**：raw 不可变 / LLM 拥有 wiki 层 / schema 是规则文件 / 所有权严格分离。差别只在"是哪个二手源转述了 Karpathy 的 gist"（gist 原文 / 日文博客 / HN-Marvin 帖 / 法文指南）。**四张卡各自的 `[^v2-1]` footnote 都自述为"本卡是该 v2 卡的 delta：从 X 视角再次确认三层架构"**——它们全部被独立判定为"对同一张 v2 卡的 delta"，却**没有任何一张被拿来和其他三张兄弟卡比较**。它们之间还互相 `related:` 链接（anthem 的 related 里有 karpathy-gist-three-layers）。
- 细微但诚实的限定：`karpathy-llm-wiki-three-layers` 额外补了"三操作 Ingest/Query/Lint + index.md/log.md"，`karpathy-llm-kb-three-layer-arch` 补了森茂的目录映射 + Mem0 overlay——所以并非 4→1 全塌，但"三层架构"这个核心被**四重陈述**。合理去重应是 4 → 1~2 张（1 张 canonical 三层卡 + 各源独有 delta 折叠为段落或更细的卡）。

**簇 2：schema 是最关键的东西 —— 4 张，强烈疑似**

`aillm-wiki-schema-as-bottleneck`（挑 schema 才是瓶颈）/ `llm-wiki-schema-is-most-important`（schema.md 是最重要文件）/ `robin-cartier-schema-as-product-doc`（真正创新是 schema 文件）/ `agents-md-as-schema-layer`（AGENTS.md 充当 schema 层）。后两张共享 v2_anchor=`llm-wiki-schema-configuration-document`。核心主张高度重叠（"schema/规则文件才是 LLM Wiki 的关键杠杆"），可约简 2-3 张。

**簇 3：LLM Wiki vs RAG —— ~5 张，疑似 2-3 真重复**

`anthemcreation-llm-wiki-vs-rag-multi-hop` / `karpathy-llm-wiki-vs-rag` / `hn-llm-wiki-is-just-rag-debate` / `karpathy-wiki-full-context-vs-rag` / `auto-index-replaces-rag-at-small-scale`。其中 `anthemcreation-llm-wiki-vs-rag-multi-hop`（差距在推理深度）与 `karpathy-llm-wiki-vs-rag`（wiki 是 compiled artifact、RAG 是 transient）框架重叠最高，疑似可并。其余几张角度确有差异（HN 争论 / 小规模 index / full-context 立场），多半 legit。

**簇 4：四个定义性属性 —— 2 张**

`aillm-wiki-four-defining-properties` vs `enterprise-llm-wiki-four-properties`（capture/link/compound/stay-current）。可能可约简 1 张，也可能是 aillm vs falconer 两种 framing。

**簇 5：编译类比** `karpathy-llm-wiki-source-executable-analogy` 与三层架构各卡正文的"编译类比"段落重叠。

**估算**：intra-v3 去重会标记的近重复，**保守 ~15-20 张**（约 10-15% 膨胀），集中在 cluster A（LLM Wiki 概念，49 张）。arxiv 论文类卡（mem0/memgpt/ARES…）大多是不同论文的不同机制，**真正独立**——所以重复集中在"LLM wiki 概念"那批二手源（karpathy gist + 各博客/指南），不在 arxiv 语料。

---

## 4. 根因（ROOT CAUSE）：为什么漂到了 v2？

| 假设 | 证据支持？ | 证据 |
|---|---|---|
| **(a) Bootstrap**：首轮无 v3 KB，v2 被设为种子基，之后没切回 v3 | **支持** | `DRAFT_FIRST_PIPELINE_V3.md:31` "until v3 has its own accepted index"；journey §3.1 首轮在 karpathy-x-launch-post 上跑时确实无 v3 KB。v2-as-seed 是合理 bootstrap |
| **(b) 批量并行生成**：171 张 draft 一次性生成 + 比较，从无"拿新 draft 比累积 v3"的增量时刻 | **支持** | `similarity_top3.py:129` 一次 glob 全部 draft；journey §3.3"全部 171 张 draft 跑 comparison"为一批。"切到 v3 索引"的触发点永不到来 |
| **(c) `similarity_top3.py` 硬编码 v2 索引** | **支持（最强）** | `similarity_top3.py:30/117/126/165`，全脚本无 v3 路径、无切换逻辑 |
| **(d) 合同把"跨 KB provenance 链到 v2"和"v3 内去重"混为一谈** | **部分支持** | 决策词汇（merge_candidate/duplicate_skip）读着像语料内去重，实际语料是跨 KB 的 v2；provenance 合同"draft vs A"对语料沉默。但合同没有把两件事写在同一阶段——更准确说是**(d) 漏写**而非混写 |

**主因 = (c)+(b)+(a) 三因叠加，(d) 使缺口无人察觉：**
- 设计选了 v2-as-bootstrap-base（(a)，**有据、可辩护**）；
- 执行把所有 draft 一批跑完，"切到 v3 索引"的增量触发点从未出现（(b)）；
- 而那个本该执行切换的工具，**根本没写能切到 v3 的代码**（(c)）；
- 合同从未把"intra-v3 去重"列为独立需求（(d)），所以没有任何检查会发现这个缺口。

**所以这不是"被人改成 v2"的漂移，而是"合同承诺先 v2 后切 v3，结果只实现了前半句"的漏实现型缺口。** v2-base 这一步本身是诚实的 bootstrap；缺陷在于"从未对 v3 自身比较过"这件事偏离了 `DRAFT_FIRST_PIPELINE_V3.md:31` 自己声明的意图。

---

## 5. 影响（IMPACT）

### 5.1 `merge_candidate = 0` 是"从没看过"，不是"确实没有重复"——判定：从没看过

证据链：
1. similarity 候选池是固定的 15 张 v2 卡，**无任何 v3 候选**（§2.2）；
2. comparison worker 被**明确禁止读兄弟 draft**（§2.3，prompt:33）；
3. 两张 v3 draft 在结构上从不进入同一次比较；
4. §3.2 的 4 张三层架构卡是 intra-v3 重复**确实存在**且**未被标记**的直接物证。

→ `merge_candidate=0` 这个"看起来 KB 很干净"的头条指标具有**误导性**：它的真实含义是"v3 内部从未被检查过重复"。

### 5.2 膨胀与 token 估算

- 卡数膨胀：~15-20 张可约简（~10-15%），主要在 cluster A。
- token 浪费：按 `token_consumption_audit.md:372`"单卡产出成本 ≈ 60 K token/张（含全 pipeline）"：
  - 全口径：60K × ~18 ≈ **~1.08M token**；
  - 仅算 draft 之后的下游（similarity+comparison+interlink+adoption+citation migration，约 40K/卡，因为读源产 draft 这步本身不算白费）：40K × ~18 ≈ **~0.72M token**；
  - **区间 ~0.7-1.1M token，约占 ~10M 总量的 7-11%。**
- 注意：浪费主要在**下游每卡 pipeline**（对本该合并的卡重复跑了 comparison/interlink/adoption/migration），不是 draft 创建本身（读每个源是合理的）。

### 5.3 是否腐蚀互链/footnote 图？——否（仅留下未被发现的重复卡）

- footnote 图**没有断链**、related 边都有效、`[^id]` 都能解析、知识本身正确。
- 但语义上图被**稀释**：4 张近重复卡互相 related，形成一簇冗余节点，读者/agent 必须自行消歧。
- 准确表述："**重复卡未被发现** + 图里有一簇冗余近重复节点"，而非"图坏了"。**interlink 阶段反而把重复粉饰成了健康的 related 簇**（§3.1），让缺口更隐蔽。

---

## 6. 正确设计（CORRECT DESIGN，简要建议）

这是**两个不同的问题，需要两套语料/两个 pass**：

1. **PRIMARY — intra-v3 去重**（draft-vs-draft / draft-vs-accumulated-v3）：这是真正缺失的需求。因为生成是**批量并行**的，它不能用"逐张拿新 draft 比累积 v3"的增量方式，必须用**全配对（all-pairs）或 catalog 聚类** pass：对 171 张 draft 标题做 all-pairs jieba-jaccard，对高分对做 merge_candidate 复核。
2. **SECONDARY — 跨 KB provenance**（draft-vs-v2）：附加 v2_anchor / provenance_delta。这正是 v3 实际做了的事——**就它本身的目的而言是合法有效的**（8 张 v2-anchored delta 都成立），只是它被误当成了去重。

**与批量并行的交互（关键）**：增量式"每张新 draft 比累积 v3"在"所有 draft 一次生成"时**不成立**。要么 (i) 串行化 adoption 让 v3 索引逐步增长、后来的 draft 比已采纳的 v3，要么 (ii) 在 draft 生成之后、comparison 之前，加一道**专门的 intra-v3 全配对聚类 pass**。鉴于 v3 已选择批量并行，(ii) 更契合。

**一句话修复**：扩展 `similarity_top3.py`，让它对每张 draft 输出**两份带标签的候选列表**——一份对其他 v3 draft 全配对打分（PRIMARY 去重），一份对 v2 索引打分（SECONDARY 跨 KB），并在 adoption 前加一道 draft-vs-draft 的 merge_candidate 复核 pass。

---

## 7. 最终判定（VERDICT）

### (i) 这是漂移吗？ —— **是（真实缺口），但属"漏实现型"而非"私自改语料型"**

- v2-as-comparison-base 本身是**写进合同的、可辩护的 bootstrap 默认**（`DRAFT_FIRST_PIPELINE_V3.md:31`），不是私自漂移；
- 真正的缺陷是：合同声明"v2 until v3 has its own accepted index"，但 (a) 工具从未实现切到 v3 的代码（`similarity_top3.py` 无 v3 路径），(b) 批量并行让切换触发点永不到来，(c) 合同从未把"intra-v3 去重"写成独立需求；
- 净效果：**intra-v3 去重从未发生**，偏离了合同自己声明的"之后切 v3"意图。**所以判定为真实缺口/缺陷：YES。**

### (ii) 根因

`tools/similarity_top3.py` 硬编码 v2 为唯一语料、无 v3 自比路径、无切换逻辑（最强）；叠加 171 张 draft 批量并行生成+比较，消除了任何增量"比累积 v3"的时刻；再叠加合同从未把 intra-v3 去重列为独立需求，使缺口无人察觉。

### (iii) 严重度：**MEDIUM（偏 medium-high）**

- 不是 critical：知识正确、图没坏、v2 provenance 工作有效、KB 可用、重复是近重复不是矛盾；
- 不是 low：~15-20 张冗余卡（~10-15% 膨胀）+ ~0.7-1.1M token 下游浪费 + `merge_candidate=0` 这个"质量信号"具误导性 + **该盲点会在每一次批量 production pass 中复发**，除非修复；
- 综合定 **MEDIUM**，因复发性 + 可量化浪费 + 误导性指标而偏 medium-high。

### (iv) 一句话修复

**让 `similarity_top3.py` 对每张 draft 额外产出一份"对其他 v3 draft 全配对打分"的候选列表（PRIMARY 去重），与现有的 v2 跨 KB 比较（SECONDARY）并列，并在 adoption 前加一道 draft-vs-draft 的 merge_candidate 复核 pass。**

---

## 8. 审计验证（证据可复现）

- 设计意图：`DRAFT_FIRST_PIPELINE_V3.md:28/31/46-51`、`SIMILARITY_MECHANISM_V3.md:7/16`、`CONTEXT_BOUNDARY.md:72-78/86-94`、`PROVENANCE_CONTRACT_V3.md:18`、`CARD_CONTRACT_V3.md:50/86-89`。
- 实现：`tools/similarity_top3.py:30/117-119/126/129/141/165`；`task_templates/comparison_worker_prompt.md:30/31/33/102`；`task_templates/interlink_worker_prompt.md:42`。
- 数据（聚合自 `outputs/llm_wiki/drafts/similarity/*.json` 与 `outputs/llm_wiki/drafts/comparison/*.md`）：`comparison_base` 171/171=v2；`comparison_base_card_count` 171/171=15；候选 card_path 全部 v2；decision 163 new_card / 8 provenance_delta / 0 其他。
- v2 语料：`loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/indexes/cards.md`，实测 15 张卡，全部来自 karpathy-gist-llm-wiki + karpathy-x-launch-post 两源。
- 重复簇：full-read 确认 `karpathy-gist-three-layers` / `karpathy-llm-kb-three-layer-arch` / `karpathy-llm-wiki-three-layers` / `anthemcreation-llm-wiki-three-layer-architecture` 四张卡正文，核心三层架构主张重复，各自 `[^v2-1]` 自述为同一 v2 卡的 delta。
- token 基准：`audits/token_consumption_audit.md:372`（~60K token/卡）。
- 叙事佐证：`docs/v3_loop_journey.md:202`（最高 jaccard 0.500 = karpathy-llm-kb-three-layer-arch ↔ v2 三层架构）、`reports/loop_report.md:84/106-108`（v2 高频干扰卡、token 误中自述）。

---

## 9. 溯源（ORIGIN TRACING）：v2 依赖在哪个时刻、怎么进来的

> 证据：git history（`similarity_top3.py` 仅 1 个 commit `29f41f3`；最早 draft+similarity 提交 2026-05-26 10:49:02 +0800）+ 文件 mtime + 叙事时间线交叉验证。

| 时刻 | 事件 | v2 依赖状态 |
|---|---|---|
| 2026-05-25 20:54:47 | v3 capsule 创建 | — |
| **2026-05-25 20:57** | 三份核心合同写出（SIMILARITY / DRAFT_FIRST / PROVENANCE，mtime） | **v2-as-default-base 在此刻写进 `DRAFT_FIRST_PIPELINE_V3.md:31`——v3 诞生第 3 分钟** |
| 2026-05-25 21:09 | CONTEXT_BOUNDARY.md 写出（mtime） | 第 78 行把 v2 索引列入 similarity 读 allowlist（同时第 77 行也允许 v3 自身索引——这条许可从未被工具使用） |
| **2026-05-25 21:41** | `similarity_top3.py` 创建（mtime） | **v2 路径硬编码进脚本，无任何 v3 自比/切换代码；此后再未修改（单 commit）** |
| 2026-05-26 10:49:02 | 首批 batch draft + similarity 提交进 git | **v2-only 比较首次大规模运行；自此每张 draft 都继承 v2-only 候选池** |

**三个关键结论：**

1. **这是 origin-defect，不是 late drift。** v2 依赖在 v3 诞生第 3 分钟就写进合同（20:57），第 47 分钟硬编码进工具（21:41）。它从一开始就在，不是后期跑偏。
2. **"切到 v3"的承诺从未被写成代码。** `similarity_top3.py` 在 git 里只有 1 个 commit（`29f41f3`），从创建起只有 v2 路径，从未被修订加入 v3 切换逻辑。合同第 31 行 "until v3 has its own accepted index" 是一句**没有任何代码兑现**的承诺。
3. **小订正**：`docs/v3_loop_journey.md` §3.2 把 `similarity_top3.py` 记为 2026-05-26（day 2）创建，但 mtime 显示 2026-05-25 21:41（bootstrap 当晚）。无论哪天，它从创建起就 v2-硬编码且从未改过——只会让 origin-defect 的结论更硬。

**用户独立性原则下的重新定性**：§1–§7 把缺陷描述为"承诺先 v2 后切 v3，却只实现前半句"。但按用户 2026-05-29 确立的 loop 独立性原则，更准确的定性是：**v2 在任何时刻被当作比较基，本身就是缺陷**——不是"忘了切"，而是"根本不该把 v2 列为 base"。`DRAFT_FIRST_PIPELINE_V3.md:31` 从写下那一刻起就是 bug：哪怕切换代码写全，也只是把"错误依赖 v2"换成"先错误依赖 v2 再切走"。独立 loop 的正确起点是——**第一张 draft 的比较基是空集（此时 v3 尚无兄弟卡），随 draft 累积而增长，永不引用任何外部 loop。**

---

## 10. 修复方案与下一轮预防

### 10.1 修正的设计原则（覆盖 §6 / §7-iv）

> **每个 loop 是独立的 0→1 过程，绝不依赖、绝不比较任何前序 loop 的 KB。** —— 用户 2026-05-29

据此 §6 "PRIMARY v3-self + SECONDARY 保留 v2 跨 KB provenance" 中的 SECONDARY 部分**被推翻**。正确设计：**比较基只有 v3-self；v2 完全移除**（similarity base、comparison 候选、8 张卡的 `v2_anchor` 字段、body 里的 `[^v2-1]` v2 footnote、`related:` 指向 v2 id 的边，全部清除）。

### 10.2 现有 v3 KB 怎么修（两部分，比初版建议更大）

**(a) intra-v3 去重**：对 171 张做 v3-self 全配对（all-pairs jieba-jaccard）→ 高分对走 merge_candidate 复核 → 合并 ~15-20 张近重复。
- **免费起手式**：`v2_anchor` 字段意外地**就是一份现成的重复信号**——4 张卡共享 `v2_anchor=llm-wiki-three-layer-architecture`，正说明它们讲同一件事。先按 v2_anchor 聚类，是 remediation 第一刀。

**(b) v2 去污染**（独立性原则新增的必做项）：8 张 v2-anchored 卡，剥掉 `v2_anchor` frontmatter + body `[^v2-1]` v2 footnote + `related:` 里的 v2 id。**卡的知识全部保留，只移除跨 loop 引用。** 171 份判定-against-v2 的 comparison provenance 作为历史 audit trail 可保留，但不再代表有效去重判定。
- **关键洞察**：这 8 张被判 `provenance_delta` 的依据正是"扩展了某张 v2 卡"。独立性原则下"扩展 v2 卡"不是有意义的关系——它们应重判为"要么独立 v3 卡、要么彼此 intra-v3 重复"。三层架构那 4 张正是后者：全被判成"同一张 v2 卡的 delta"，而这恰是"它们彼此重复"的信号。**(a) 与 (b) 在这 8 张上是同一个问题。**

> 现有 KB 修 or 不修，仍是成本决定（forward-only vs remediate-now）。若 remediate，用 catalog-first：只读标题+statement 做配对，只对高分对回读全文，把回溯开销压到最低。

### 10.3 下一轮 loop 怎么避免（prevention，具体改动）

1. **`similarity_top3.py` 重写**：语料 = v3-self（对累积 drafts/cards 全配对 jaccard），**删除 `V2_INDEX` 常量与所有 v2 路径**；输出候选 = 兄弟 draft。
2. **`DRAFT_FIRST_PIPELINE_V3.md:31` 改写**：删掉"default base v2 until..."，改为"comparison base 永远是本 loop 自己累积的 drafts/cards；loop 之间永不互比"。
3. **`CONTEXT_BOUNDARY.md` 收紧**：从 similarity / comparison 读 allowlist 删除 v2 索引与 v2 卡（当前第 78 行），让 boundary **强制**独立性（而非现在"既允许读 v3 也允许读 v2"，结果工具选了 v2）。
4. **`comparison_worker_prompt.md:33` 反转**：当前"**禁止**读其他 draft 卡"恰恰是去重做不成的结构性原因。改为"读你被分到的兄弟-draft top-k 候选"以支持受控的 intra-v3 去重。
5. **新增 intra-v3 去重 pass**：在 draft 与 adoption 之间插一道专门的全配对聚类 + merge_candidate 复核（批量并行生成没有"增量比累积 v3"的时刻，所以必须显式补一道）。
6. **泛化为 scaffold 规则**：任何未来 loop 起步即以 self 为唯一语料；任何跨 loop 引用视为 lint 错误（可在 hook 加一条检查：footnote/related/similarity 出现 `v[0-9]+_*_loop_*` 外部路径即告警）。

### 10.4 严重度重估（独立性原则下）

初版定 MEDIUM（偏 medium-high），只算 ~15-20 张未去重卡。独立性原则下污染面扩大：**+8 张 v2_anchor 卡 + 171 份 against-v2 的 comparison 判定**也属污染（答错了问题，而非只答得不全）。知识仍正确、可恢复、无数据损坏。综合 → **medium-high**。仍非 critical，但受污染工件面比初版评估更大。
