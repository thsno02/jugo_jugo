---
status: future_plan
stage: discussion_only
created: 2026-05-30
loop_id: v3_llm_wiki_loop_20260525
topic: questioning_loop_design
note: 基于 reader↔questioner 对话的两模式知识抽取/综合设计。三个 design agent 的提案融合。仅讨论，未执行。
---

# Questioning Loop 设计：Mode A (建构) + Mode B (进化)

> 核心转变：不让 agent "抽取所有知识"（开放、模糊、显著性偏差），而是让一个 **questioner 持续提问，reader 回答，Q&A 对 → 原子卡**。材料通过"被问尽"而非"被抽尽"来 exhaust。

## 0. 为什么是两个模式

| | Mode A（建构） | Mode B（进化） |
|---|---|---|
| questioner 看到 | 单源的 **digest**（摘要+TOC+核心主张） | KB 内 **卡片簇摘要**（跨源） |
| 提问范围 | 源内（scope-bounded） | 跨源/逻辑推导（scope-free） |
| 收敛靠 | 源的边界（问完即止） | 4 道闸（entailment/novelty/depth/budget） |
| 产出 | 源忠实的原子卡 | 桥接卡/抽象卡 + collect-request（知识缺口） |
| 什么时候跑 | 每个新材料到达时 | governance 归一化后，KB 有密度时 |

两者共用同一套 **questioner ↔ reader 对话协议**，只是输入/技能/收敛机制不同——参数化，不是分叉。

---

## 1. Mode A：建构阶段（per-material extract）

### 1.1 Digest（摘要地图）

Reader 在对话前用一次轻量 pass 从全文产出 digest，包含四部分：

- **scope 声明**（1-2 句）：材料是什么、来自谁、覆盖什么、不涉及什么。
- **结构大纲（TOC）**：章节骨架，每节一行标题+一句话概述，不展开。
- **核心主张清单**（5-15 条）：材料声称了什么——方向，不是答案。
- **术语/实体索引**：关键术语、人名、模型名、数据集名，纯列表。

**"enough to scope, not enough to bias"**：digest 让 questioner 能问出"第四节剪枝机制的具体步骤"这样的定向问题，但问不出"该机制在 top-k=50 时 perplexity 降了 12%"——细节不在 digest 中，必须"问"才能获得。成本约为全文 token 的 1/10。

### 1.2 Questioning Skill（Mode A）

Questioner 拿到 digest 后按五阶段推进：

**Phase 1 — 广度扫描**：对 digest 中每个主要章节/主张提一个开放性问题。目标：最少轮次把材料全域触碰一次。

**Phase 2 — 深度追问**：根据 Phase 1 回答，识别"提到但未展开的机制/区分/条件"，逐一追问。每个追问链 1-3 层深。

**Phase 3 — 评判性提问**：对已有回答提评估性问题——局限、假设、与主流理解的差异。

**Phase 4 — 批判性/对比性提问**：追问材料**内部**的张力——"第三节和第五节是否矛盾？""作者对 X 的定义和通常理解有何差异？"（不引入材料外知识，那是 Mode B 的事。）

**Phase 5 — 覆盖率检查**：回顾 digest，逐条核对：每个 TOC 条目是否被问过、每个核心主张是否有 Q&A 覆盖、术语索引中是否有术语从未出现在任何问答中。遗漏项补问。

**SATISFIED 判定**（三个条件同时满足）：
- (a) digest 中每个核心主张都有至少一个 Q&A 覆盖；
- (b) 没有 Phase 2 追问链在"又提到新概念但未展开"状态下终止；
- (c) questioner 判断"再问下去不会产生新的原子 idea"。

### 1.3 对话机制

```
orchestrator (主会话):
  ① reader 读全文 → 产出 digest
  ② dispatch questioner(digest, "开始提问")
     → questioner 返回 Q1-Q5
  ③ reader 回答 Q1-Q5 (KV cache 暖, 定向读)
  ④ 即时 reframe 本轮 Q&A → draft 卡 (含 canonical grep)
  ⑤ SendMessage to questioner("答案 + 已产出 canonical 列表, 继续或 SATISFIED")
     → questioner 返回 Q6-Q8 或 SATISFIED
  ⑥ ...iterate...
  ⑦ SATISFIED → 收尾
```

- **轮次预期**：5-8 轮。Phase 1 约 1 轮，Phase 2 约 2-4 轮，Phase 3-4 约 1-2 轮，Phase 5 约 1 轮。
- **递减收益**：Phase 1-2 价值最高（主干知识）。Phase 3-4 不可跳过（挖边界条件——纯摘要最易遗漏的）。Phase 5 是兜底。
- **关键**：reframe 在每轮对话之间（非最后一步），这样 questioner 在下一轮看到"已产出的 canonical_concept 列表"，避免重复追问已覆盖概念。

### 1.4 Q&A → 卡片转化

**独立步骤，非 inline。** 三个变换：
- (a) 对话体 → 知识陈述体（"问：X 是什么？答：X 是..." → "X：一种...的机制"）。
- (b) 补 metadata：canonical_concept（grep 现有 KB 复用/新铸）、aliases（从回答变体词提取）、summary（稠密 grep 靶子）。
- (c) 脚注锚定：把回答中引用的源位置转化为 `## Footnotes`（`[^src-N]: data/raw/... — 行号/指针`）。

**一对一 vs 多对一**：默认一个 Q&A = 一张卡。Phase 1 广度问题的回答若含多个独立 idea → 拆多张；Phase 2 追问链若共同构成一个原子 idea → 合一张。判断标准：能否在不引用兄弟卡的情况下被理解。

### 1.5 Reader 角色

Reader 是**被动应答者**，不主动引导、不建议问什么、不评价问题质量。好回答四标准：
- **源忠实**：只基于手中材料，不注入外部知识。
- **定位精确**：引用具体位置（"第三节第二段"/"JSON pointer $.section.3"），使脚注锚定可操作。
- **卡片就绪**：信息量足以支撑一张原子卡——不过简也不过长。
- **显式标注不确定性**：材料未讨论 → 说"材料未直接讨论此点"，不编造。

### 1.6 独立 Reviewer 的去留

**不设独立 reviewer。** Questioner 的对话过程**天然包含审查功能**：它从 digest（非全文）出发，对 reader 回答进行交叉验证；Phase 5 覆盖率检查承担了"是否抽尽"的职责。Q&A 转卡时的 reframing 承担"卡是否自足/原子/有据"的最后检查。

独立 reviewer 的唯一残余价值是"抽查源忠实性"（卡的陈述是否被原文支撑）。若需要，可作为**可选的抽样 pass**（不是每张卡都查），成本极低。

---

## 2. Mode B：进化阶段（cross-material synthesis）

### 2.1 Questioner 的输入：卡片簇摘要

Questioner 不读任何原始材料，只看 KB 内部的卡片簇。簇的识别分两步：

**第一步**：复用倒排表（`canonical_concept → [card_ids]`），`count ≥ 2` 的概念自动形成簇。零成本。

**第二步**：跨簇桥接发现——对每卡的 `related` 做二跳展开：卡 A related 卡 B，B 属另一簇 → 两簇有桥接关系。纯脚本（grep related + 查倒排表），输出"簇间边列表"。**这张边列表是 Mode B 追问者最核心的输入**——它标出"哪些概念簇之间已有连接但尚未被显式表达"。

**Questioner 看到的**：每个簇只给 summaries（每卡一行），不给 body。Summary 是 grep 优化的信息靶子，信噪比高于 body。只在追问者主动请求某卡细节时，reader 才读 body。

### 2.2 Questioning Skill（Mode B）

Mode B 的提问方向与 Mode A 根本不同——面对的是**簇间关系**，不是单源内容。三种**追问姿态**（并行可用，非顺序阶段）：

- **桥接追问（connecting）**：两个簇各有卡但关系未显式表达。"X 和 Y 的关系是什么？互补、互斥、还是因果？"
- **张力追问（tensioning）**：两簇断言表面矛盾。"卡 A 说 schema 要先固定，卡 B 说 schema 应涌现——分界线在哪？"
- **空白追问（gap-probing）**：已有卡的逻辑推导显示某概念"应存在但不存在"。"KB 有原子性和可溯源两个约束，但没有卡讨论冲突时的优先级——偶然还是本质？"

关键区别：Mode A entailment 方向 = source → card；**Mode B entailment 方向 = cards → synthesis**。追问者只能在已有卡的逻辑凸包内综合。

### 2.3 递归循环（逐步映射）

以一个具体例子展开：

**Turn 1** — 追问者发桥接问题："`zettelkasten-atomicity` 和 `grep-friendly-metadata` 簇有 related 边但无显式讨论。关系是什么？"

**Turn 2** — Reader grep 两簇 body："卡 A 说一卡一概念，卡 B 说 summary 稠密包含 canonical+aliases+论断。" Reader 综合：原子性保证 summary 信噪比——一卡只有一个 canonical_concept，所以 summary 不会因混杂多概念而模糊。→ 可落卡的桥接断言。

**Turn 3** — 追问者读到回答后发现隐含问题："如果一张卡过粗跨两个概念，summary 就混杂。现有 KB 有没有卡讨论过粗卡的检测？" **（递归：回答暴露新空白。）**

**Turn 4** — Reader grep：没有。只有 governance 契约提 "过粗标 needs_split"。

**Turn 5** — 追问者判断：真实知识空白 + KB 内卡无法回答 → **emit collect-request**。

每轮模式：**追问 → 回答 → 回答暴露隐含前提 → 新追问**。递归燃料 = "回答总会暴露自身前提假设，这些假设可能尚未被 KB 覆盖。"

### 2.4 收敛：四道闸

Mode B 没有 Mode A 的"源读完即止"自然边界。四道闸同时是停止条件：

**Entailment 闸（最关键，反幻觉）**：Reader 生成综合回答时，必须对每个断言标注 `[来自 card-id-X]`。追问者落卡前检查：每断言有标注、被引 card-id 在当前簇内、综合推理的每步都有父卡支撑。不满足 → 不落卡 → 追问"这一步依据是什么？" → 找不到 → **collect-request**。

**Novelty 闸**：候选卡 summary 先 grep 现有 KB summaries。命中 → 降级为对已有卡的 related 补充（不落新卡）。

**Depth 闸（v1 = 1）**：`derived_from` 构成 DAG；archived 卡不可作父；v1 综合卡不可作另一综合卡的父。杜绝无限抽象塔与循环引用。

**Budget 闸**：每簇对固定 turn 预算（建议 v1 = 8 轮）。预算耗尽 → 未落卡的开放问题批量转为 collect-request（不丢线索）。

**追问者 SATISFIED**：簇对的所有追问分支都到达三种终态之一——(a) 成功落卡，(b) novelty 拒绝（已有卡覆盖），(c) 转为 collect-request（KB 无法回答）。无"继续挖"动力。

### 2.5 综合卡的 Provenance

```yaml
derived_from: [card-id-A, card-id-B, card-id-C]   # 直接父卡
root_sources: [source-x, source-y, source-z]       # 父卡 root_sources 的冻结并集（脚本自动算）
card_class: synthesis | bridge                      # 区别于 source-grounded
```

Footnotes 格式：`[^synth-N]` 指向父卡的具体断言，与 Mode A 的 `[^src-N]` 指向 raw 源形成对偶。

### 2.6 Gap → Collect-Request 桥接

当 reader 报告"KB 内无卡覆盖此问题"，追问者执行：

**真空白过滤**："如果此空白被填补，是否改变至少两张现有卡之间的关系理解？" 是 → 真空白；否 → `low_priority_gap` 存档。

**Collect-request 格式**：

```yaml
id: cr-<timestamp>-<slug>
type: collect-request
question: "过粗卡的自动检测机制：有哪些启发式或指标？"
context_cards: [card-id-A, card-id-B]
expected_contribution: "填补 atomicity 与 governance 之间的操作空白"
priority: high | medium | low
source_hints: ["Zettelkasten 社区实践讨论", "note-taking atomicity 研究"]
```

落盘到 `kb/collect_requests/`，不进 active view。下一轮 collect 获取新材料 → Mode A 产卡 → 新卡进倒排表 → Mode B 下轮召回 → 闭合循环。

Budget 耗尽时，所有未解决的开放追问**批量转为 collect-request**（priority=medium），保证不丢线索。

---

## 3. 整合：生命周期、共享基础设施、KV cache

### 3.1 生命周期：交错式

Mode A = 高频（每材料一次）。Mode B = 低频（批后一次 + 增量累积 ≥ 20 新卡触发）。**两者绝不并发**——Mode B 必须在当批 Mode A 全部入库 + governance 归一化后才启动（需要稳定 KB 快照）。

```
时间线：
  M1  M2  M3 ... Mn   ← 材料到达
  A1  A2  A3 ... An   ← Mode A 并行
  ──── ingest (脚本) ────
  ──── govern (dedup/canonical 归一化) ────
  ──── Mode B (全局，簇级) ────
  ──── ingest synthesis cards ────
  ──── govern again ────
  ...
  Mn+1 到达 → A(n+1) → ingest → scoped govern → (累积够?) → scoped Mode B
```

### 3.2 共享 vs 差异

**共享（同一套代码路径）**：对话协议（questioner 发问 → orchestrator 中继 → reader 答 → orchestrator 收集）、Q&A→卡 reframing、reader agent、orchestrator relay、ingest 脚本。

**差异（参数化）**：

| 维度 | Mode A | Mode B |
|---|---|---|
| questioner 输入 | source digest（~2-5K tok） | card-cluster summaries（~1-3K tok） |
| questioning skill | **scope-bounded**（5 阶段） | **scope-free**（3 姿态） |
| 收敛 | 自然（scope 有界，exhaust 即停） | 4-gate 强制（entailment/novelty/depth/budget） |
| provenance | `source → card`（`[^src-N]`） | `cards → synthesis`（`[^synth-N]`） |
| reader 缓存前缀 | source 全文 | cluster 内卡 body 拼接 |

### 3.3 KV Cache 策略

- **Mode A**：orchestrator 为每个 material 维护一个 reader session，prefix = 全文。同材料的所有对话轮次复用 → cache hit（第 2 轮起 ~95%）。
- **Mode B**：per-cluster reader session，prefix = cluster 内卡 body 拼接（按 canonical 排序，稳定）。同 cluster 的 M 轮对话复用。
- **跨模式无共享**：前缀语义完全不同，不尝试共享（正确——强行共享会污染 cache key）。

### 3.4 独立 Reviewer 的统一处理

**两个模式都不设独立 reviewer agent。** 审查功能分别内化在：
- **Mode A**：questioner 的 Phase 5 覆盖率检查 + reframing 时的质量检查。Questioner 的独立视角（从 digest 而非全文出发）天然是 independent review。
- **Mode B**：entailment gate 即是 review——检查综合卡的每个断言是否由源卡支撑。内建在对话循环中。

若需额外安全网：Mode A 可选"抽样源忠实性 spot-check"（reviewer 抽 3-5 张卡核验），低成本，非每张都查。

---

## 4. 完整 Loop 生命周期（伪代码）

```python
def run_loop(materials, kb):
    # ── Phase 1: Mode A (per-material) ──
    draft_cards = []
    for batch in chunk(materials, parallel=N):
        batch_results = parallel_map(batch, run_mode_a)
        draft_cards.extend(batch_results)

    # ── Phase 2: Ingest (脚本, 无 LLM) ──
    ingest(draft_cards, kb.cards_dir)

    # ── Phase 3: Governance (dedup / canonical 归一化) ──
    index = build_inverted_index(kb)
    clusters = [c for c in index if c.count >= 2]
    parallel_map(partition(clusters), run_governance)
    rebuild_index(kb, active_only=True)

    # ── Phase 4: Mode B (synthesis) ──
    cluster_summaries = extract_cluster_summaries(kb, index)
    synthesis_cards = []
    for cs in cluster_summaries:
        synthesis_cards.extend(run_mode_b(cs, kb))

    # ── Phase 5: Ingest synthesis cards + Governance pass 2 ──
    ingest(synthesis_cards, kb.cards_dir)
    index = build_inverted_index(kb)
    new_clusters = [c for c in index if c.has_new and c.count >= 2]
    parallel_map(partition(new_clusters), run_governance)
    rebuild_index(kb, active_only=True)


def run_mode_a(material):
    reader = create_session(prefix=material.full_text)
    digest = reader.produce_digest()
    questioner = spawn("scoped_questioning", input=digest)
    qa_pairs, cards = [], []

    for round in range(MAX_ROUNDS_A):  # 建议 8
        questions = questioner.ask(context=qa_pairs)
        if not questions:  # SATISFIED
            break
        answers = reader.answer(questions)
        new_qa = list(zip(questions, answers))
        qa_pairs.extend(new_qa)
        # 即时 reframe（questioner 下轮可见 canonical 列表）
        cards.extend(reframe(new_qa, provenance="source",
                             source_id=material.id))

    return cards


def run_mode_b(cluster_summary, kb):
    cluster_cards = kb.get_cards(cluster_summary.ids)
    reader = create_session(prefix=concat_bodies(cluster_cards))
    questioner = spawn("synthesis_questioning",
                       input=cluster_summary.text)
    qa_pairs, cards, budget = [], [], BUDGET_B

    for round in range(MAX_ROUNDS_B):  # 建议 6
        questions = questioner.ask(context=qa_pairs)
        answers = reader.answer(questions)
        for q, a in zip(questions, answers):
            if not pass_gates(q, a, cluster_cards):
                # entailment fail → collect-request
                # novelty fail → skip
                # depth/budget fail → stop
                continue
            qa_pairs.append((q, a))
            budget -= 1
        if budget <= 0:
            break

    return reframe(qa_pairs, provenance="entailed_from",
                   source_ids=cluster_summary.ids)
```

---

## 5. 成本模型

### Mode A（per-material）

| 项 | tokens | 说明 |
|---|---|---|
| reader session 启动（全文加载） | ~50K | 一次，后续 cache hit |
| digest 生成 | ~5K | 一次轻量 pass |
| questioner（digest + N 轮） | ~15K | digest ~3K + 每轮 ~2K × 5 |
| reader 回答 N 轮（增量） | ~25K | 每轮 ~5K output，prefix 不重计 |
| reframing Q&A → cards | ~10K | 每轮即时 |
| **Mode A / 材料** | **~105K** | |
| **Mode A / 卡**（~3 卡/材料） | **~35K** | v3 = ~60K/卡，**降幅 ~42%** |

降本来源：(1) KV cache 消除每卡独立重读全文的浪费；(2) 无 adoption/migration/comparison 阶段（出生即终态）；(3) ingest 是脚本。

### Mode B（per-cluster）

| 项 | tokens | 说明 |
|---|---|---|
| cluster body 拼接加载 | ~30K | 5-8 卡 × ~4K |
| questioner（summary + M 轮） | ~20K | |
| reader 回答 M 轮 | ~30K | cache 复用 |
| 4-gate 检查 | ~8K | |
| reframing | ~8K | |
| **Mode B / cluster** | **~96K** | |
| **Mode B / synthesis 卡**（~2 卡/cluster） | **~48K** | |

### 全 Loop 估算（init 64 材料）

```
Mode A:   64 × ~105K  = ~6.7M  →  ~192 张源卡
Govern1:  30 clusters × ~20K = ~0.6M
Mode B:   30 clusters × ~96K = ~2.9M  →  ~60 张综合卡
Govern2:  ~15 clusters × ~20K = ~0.3M
                                --------
总计:                           ~10.5M
产出:                           ~252 张卡
单卡成本:                       ~42K/卡（vs v3 ~60K/卡，降 ~30%）
```

同时多产出 ~60 张 synthesis 卡（v3 完全没有此环节）+ 自动发现知识缺口（collect-request）。

---

## 6. generate 与 governance 的关系

**Generate（Mode B）是 governance 的逆操作：**
- Governance：合并冗余、降熵。
- Generate（Mode B）：连接非冗余但相关的卡、增密。

两者同属 evolve 大阶段，先 governance 再 generate：必须在**已去重、canonical 已对齐**的语料上生成，否则在冗余输入上合成。

**Generate 永远 best-effort、可完全跳过**（init 首轮可不跑，无密度）。它只加分、不阻塞 ingest 的源忠实性。被它误伤的成本只是一张多余卡——而多余卡 never-delete，可 archive。

---

## 7. 开放决策

1. **Mode A 轮次上限 MAX_ROUNDS_A**：建议 8（best-effort zen：Phase 1-2 最高价值，Phase 5 兜底）。
2. **Mode B budget**：建议 8 轮 / 簇对。耗尽时批量转 collect-request。
3. **Mode B synthesis depth**：v1 锁 depth=1（综合卡不可再作父）。v2 可考虑 depth=2。
4. **Mode B 触发阈值**：init 后跑一次全局；增量 add 累积 ≥ 20 新卡再跑 scoped。
5. **Collect-request 自动化**：v1 只落盘存档（待人工审阅）；未来可自动 emit collect spec。
6. **Digest 格式精确化**：core claims 是几条？TOC 粒度到什么层级？—— 留给 skill 迭代。
7. **Optional spot-check reviewer**：Mode A 可选 3-5 张卡源忠实性抽查 pass，成本极低。是否启用？

---

## 8. 与其他 future_plans 文件的关系

- `next_loop_design.md`：本文件的 §1.1 extract 环节应指向此处（questioning loop 替代了原来的"单 agent exhaust"）。
- `fusion_and_governance.md`：本文件的 governance 环节不变；Mode B 的 synthesize 阶段是 governance 的后续 pass。
- `next_loop_optimization_and_landing.md`：B.1 Extract Agent spec 应替换为本文件的 Mode A 设计（reader + questioner 对话，非单体 drafter）。
