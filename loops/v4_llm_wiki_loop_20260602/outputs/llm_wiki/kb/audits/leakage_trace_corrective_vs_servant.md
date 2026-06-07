---
schema: leakage_trace.v1
card: comparison-corrective-vs-servant-agency
leakage_concept: 确认优先规则
true_source: cognitionus-llm-wiki-guide
pathway: confirm-first-skill-capture → human-llm-role-division → comparison card
date: 2026-06-07
---

# Leakage Trace: 确认优先规则

## 1. 什么泄露了

`comparison-corrective-vs-servant-agency.md` 第 27 行：

> 这一分歧在实践中通过门控机制得到部分调和：**确认优先规则**和参与程度谱系允许系统在不同场景下调节 LLM 的自主程度，但根本问题——LLM 是否应拥有纠偏权——仍是知识系统架构的核心设计决策。

问题：
- 「确认优先规则」来自源 `cognitionus-llm-wiki-guide`（Cognition 的 confirm-first capture 设计）
- 但该 comparison 卡的 `source_ids` 仅声明 `[arxiv-memory-as-metabolism, karpathy-gist-llm-wiki]`
- 卡片正文对「确认优先规则」无任何 `[^card-*]` 或 `[^src-*]` 脚注锚定
- 概念在正文中以裸名出现，读者无法追溯其来源

附注：同一句中的「参与程度谱系」经调查为 **false positive**——Karpathy gist 第 37 行（Ingest 段）明确描述了 "I prefer to ingest sources one at a time and stay involved" vs "you could also batch-ingest many sources at once with less supervision" 的谱系，卡片是合理意译。

## 2. 执行链路追踪

### 2.1 Governance Workflow 架构

Comparison 卡由 `card-governance-wf_7019b6ac-72a.js` 生成，该 workflow 分三阶段：

1. **Scan**：一个 agent 读取全部 259 张卡的元数据（slug、canonical_concept、aliases、summary、tags、source），输出 synonym/antonym/cross-topic 聚类
2. **Govern**：每个 cluster 分配一个独立 agent。agent 接收 cluster 内的卡片列表，被指示 "Read ALL cards in this cluster using the Read tool"，然后执行 cross-link、comparison card 生成等治理任务
3. **Derive**：脚本从脚注反推 `related:` 字段

关键设计：Govern agent 的 prompt 明确列出 cluster 内卡片的文件路径，agent 被指示仅读取这些卡片。

### 2.2 推断的 Cluster 组成

`comparison-corrective-vs-servant-agency` 的 footnotes 仅引用两张卡：
- `[^card-1]`: `mirror-vs-compensate-principle.md`（source: arxiv-memory-as-metabolism）
- `[^card-2]`: `human-llm-role-division.md`（source: karpathy-gist-llm-wiki）

由于 Scan agent 的聚类是动态生成的（无持久化日志），cluster 的精确组成需从产物反推。鉴于该 comparison 卡的 card_type 为 distinction 且仅引用这两张卡，可高置信度推断 cluster 至少包含：

| 卡 | 来源 | 角色 |
|---|---|---|
| mirror-vs-compensate-principle | arxiv-memory-as-metabolism | 纠偏代理立场 |
| human-llm-role-division | karpathy-gist-llm-wiki | 仆人执行立场 |

cluster 可能还包含 `review-involvement-spectrum`、`confirm-first-skill-capture` 等相关卡（因为 Scan agent 的聚类规则允许 3-15 张卡），但即使不在 cluster 中，泄露仍会发生（见 2.3）。

### 2.3 泄露路径——逐步还原

**Step 1: Governance agent 读取 `human-llm-role-division.md`**

该卡是 cluster 的核心卡之一。Agent 读取其完整内容，包括第 32 行：

> 在实践中，角色边界的执行可通过门控机制实现——如 Cognition 的**确认优先规则**要求 LLM 产出须经人类明确批准[^card-4]，而参与程度本身也是可调节的[^card-3]。

以及脚注定义：

> `[^card-4]`: [确认优先的技能捕获规则](confirm-first-skill-capture.md) -- 本卡描述人机角色的宏观分工，该卡提供一种具体的门控机制实现角色边界

> `[^card-3]`: [人类参与程度谱系](review-involvement-spectrum.md) -- 本卡设定固定的人机角色边界，该卡将该边界描述为可调节的连续谱系

**Step 2: Agent 吸收脚注叙事中的跨卡概念**

`human-llm-role-division.md` 的正文和脚注叙事包含了对 `confirm-first-skill-capture`（源自 cognitionus-llm-wiki-guide）的描述性引用。Governance agent 在阅读 cluster 卡时，将这些脚注叙事中的概念纳入了工作记忆。

**Step 3: Agent 将吸收的概念写入 comparison card**

在生成 comparison 卡的「调和」段落时，agent 使用了从 `human-llm-role-division.md` 脚注叙事中吸收的「确认优先规则」和「参与程度谱系」概念，但未为这些概念添加 `[^card-*]` 脚注指向原始卡片。

**完整泄露链条**：

```
cognitionus-llm-wiki-guide（原始源材料）
  ↓ 提取
confirm-first-skill-capture.md（Phase 3 生成的 KB 卡，source_ids: [cognitionus-llm-wiki-guide]）
  ↓ [^card-4] 脚注叙事嵌入
human-llm-role-division.md（cluster 内卡，正文第 32 行引用「确认优先规则」）
  ↓ governance agent 阅读 cluster 卡
comparison-corrective-vs-servant-agency.md（第 27 行裸名引用「确认优先规则」，无脚注）
```

### 2.4 为什么 `review-involvement-spectrum` 也参与了传播

`review-involvement-spectrum.md` 在第 26 行同样引用了 confirm-first-skill-capture：

> 在谱系的高审批端，Cognition 的确认优先规则提供了一种具体的门控实现[^card-4]。

如果 `review-involvement-spectrum` 也在 cluster 中（其 related 字段包含 confirm-first-skill-capture），则 agent 通过两条路径接触到该概念，进一步强化了泄露。

## 3. 根因分析

### 3.1 直接原因：脚注叙事作为隐式上下文通道

Governance agent 的 prompt 限定了 "Read ALL cards in this cluster"，并仅提供 cluster 内卡片的文件路径。Agent 确实没有主动读取 cluster 外的卡片。

但 cluster 内的卡片已经过 Phase 3（卡片生成）和 Phase 4 前期（cross-link 添加），其正文和脚注中嵌入了丰富的跨卡引用叙事。这些叙事实际上构成了一个**隐式上下文通道**：

```
[^card-4]: [确认优先的技能捕获规则](confirm-first-skill-capture.md) 
           -- 本卡描述人机角色的宏观分工，
              该卡提供一种具体的门控机制实现角色边界
              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
              这段叙事携带了来自 cognitionus-llm-wiki-guide 的概念
```

Agent 合理地将所阅读内容视为可用上下文，而不区分「来自卡片声明源的内容」与「来自脚注跨引的内容」。

### 3.2 结构原因：Governance 在 Cross-link 之后运行

v4 的执行顺序为：
1. Phase 3: 卡片生成（每张卡仅引用自己的 source_ids）
2. Phase 4a: Cross-link 添加（cards 获得 [^card-N] 脚注指向其他卡）
3. Phase 4b: Governance（含 comparison card 生成）

Phase 4b 读取的卡片已经被 4a 注入了 cross-link 脚注。如果 governance 在 cross-link 之前运行，`human-llm-role-division.md` 的正文中不会有 `[^card-4]` 指向 `confirm-first-skill-capture`，泄露就不会发生。

但这并非可行的修复——cross-link 是 governance 的前置步骤，comparison 卡需要 cross-link 信息才能识别 tension。

### 3.3 设计原因：Comparison 卡的 source_ids 语义未明确

Governance prompt 中 comparison 卡的生成指令要求：
> The comparison card's body explains the tension/distinction with [^card-N] refs to both source cards

但未要求：
- comparison 卡的 `source_ids` 必须覆盖正文引用的所有概念的原始来源
- 正文中出现的每个非 cluster 概念必须有 `[^card-*]` 脚注锚定
- agent 区分「cluster 卡声明源中的内容」与「cluster 卡脚注跨引中的内容」

结果：agent 自由地使用了从 cluster 卡脚注中吸收的概念，但既未在 source_ids 中声明 cognitionus-llm-wiki-guide，也未添加 `[^card-3]` 或 `[^card-4]` 指向 confirm-first-skill-capture 和 review-involvement-spectrum。

## 4. 设计层面的缓解建议

### 4.1 Comparison 卡生成 prompt 增加脚注硬约束

在 `buildGovPrompt()` 中增加规则：

```
### E. Comparison Card Footnote Discipline
当 comparison 卡正文提及不属于 cluster 核心 tension 的概念时：
- 如果概念来自 cluster 内某张卡的 [^card-N] 引用，必须在 comparison 卡中
  添加自己的 [^card-N] 指向原始卡片
- 如果概念的原始来源不在 comparison 卡的 source_ids 中，
  要么添加该来源到 source_ids + [^src-N] 脚注，要么删除该概念
- 禁止在正文中裸名引用概念——每个概念必须有脚注锚定
```

### 4.2 Governance agent 阅读区分指令

在 prompt 中显式区分两层内容：

```
注意：你阅读的 cluster 卡中包含 [^card-N] 和 [^dist-N] 脚注引用其他卡。
这些脚注叙事是关于其他卡的描述，不是本 cluster 的核心内容。
在写 comparison card 时：
- 核心 tension 分析只使用 cluster 卡正文中有 [^src-N] 锚定的内容
- 如果你引用了脚注叙事中的概念，必须添加 [^card-N] 追溯
```

### 4.3 Post-hoc 检查脚本

在 Derive 阶段增加机械检查：

```python
# 检查 comparison 卡正文中出现但未被脚注锚定的概念名
for card in comparison_cards:
    body_concepts = extract_concept_names(card.body)  # NER or alias matching
    footnoted_concepts = extract_footnote_targets(card.footnotes)
    naked_concepts = body_concepts - footnoted_concepts
    if naked_concepts:
        warn(f"{card.id}: 裸名概念 {naked_concepts} 缺少脚注锚定")
```

### 4.4 Cluster 执行日志持久化

当前 Scan agent 的聚类结果未持久化，导致事后审计只能从产物反推 cluster 组成。建议将 `scanResult.clusters` 写入 `audits/governance_clusters.json`，使执行链路可完整重放。
