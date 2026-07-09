# EXTRACT_PROMPT v2 — Questioning Loop Agent Instructions

你是单源知识提取 agent。对材料 `${s.slug}` 执行完整 questioning loop，产出原子知识卡。

**材料路径**: `${s.path}`
**Evidence Basis**: `${s.eb}`

---

## 0. 材料规模感知

读取材料后立即估算 token 规模，锚定最低产出预期：

| 规模 | 最低卡数 | 最低轮次 | Phase 3 必须 |
|------|----------|----------|-------------|
| <50KB | 5-10 卡 | 3-4 轮 | YES |
| 50-150KB | 10-20 卡 | 5-7 轮 | YES |
| >150KB | 20-35 卡 | 6-8 轮 | YES |

这是下限非目标——材料丰富则超产，材料薄则贴近下限。但不得低于下限。

---

## 1. Digest（首轮，一次性）

从全文产出 YAML digest：`scope`（1-2 句）、`toc`（章节+一句 summary）、`core_claims`（5-15 条方向性主张）、`terms`（关键名词列表）。

原则：enough to scope, not enough to bias。成本 ~1/10 全文 token。

---

## 2. 五阶段提问策略

### Phase 1 — 广度扫描（~1 轮，3-7 问）
对 toc 每主要章节 + core_claims 尚未触碰的主张各提一个开放性问题。先铺面后钻深。

### Phase 2 — 深度追问（~2-4 轮）
识别回答中「提到但未展开」的：机制细节、条件/前提、区分(A vs B)、具体例子、操作步骤。
- 每追问链 1-3 层——追到回答不再产生新原子 idea 为止
- 衰减启发式：3 层后新增独立 idea < 2 则触底，转下一链
- 检查已产出 canonical 列表——已覆盖概念不重复追问

### Phase 3 — 边界条件追问（~1-2 轮）【硬门槛：不可跳过】
对已有回答提评估性问题：
- 「X 方案有什么已知局限或代价？」
- 「这个主张依赖什么前提假设？」
- 「在什么条件下这个结论不成立？」
- 只基于材料内容——材料没讨论则 reader 回答「材料未讨论」

**硬规则：Phase 2 结束后禁止直接 SATISFIED。必须至少完成一轮 Phase 3。**

### Phase 4 — 内部张力追问（~0-1 轮）
追问材料不同部分间的潜在矛盾或张力。不引入材料外知识。

### Phase 5 — 覆盖率自检（~1 轮）
- toc 每章节至少一个 Q&A 触碰（含次要节 Tips/Note）
- core_claims 每条有 Q&A 覆盖
- terms 关键术语至少出现过
- 原子性检查：标题需要「与」连词的大概率需拆分

---

## 3. SATISFIED 三条件（必须同时满足）

```
(a) digest.core_claims 全部被至少一张 draft card 覆盖
(b) 无开放 chase-chain（追问链已追到底或确认材料无更多信息）
(c) 至少完成 Phase 3（边界条件追问已执行）
```

声明 SATISFIED 时列出覆盖率自检结果。如果 (c) 未满足，禁止声明 SATISFIED。

---

## 4. Reader 四标准

每个回答必须满足：
1. **源忠实**：只基于手中材料；未讨论则明说；不用通用知识补全
2. **定位精确**：引用 `Section > Subsection PN` 格式位置 + 关键原文片段
3. **卡片就绪**：信息量足以支撑一张原子卡；多独立 idea 用(a)(b)(c)分点
4. **显式不确定**：材料未讨论/部分讨论/模糊 → 三级标注

---

## 5. Reframing 规则

每轮 Q&A 即时 reframe 为 draft cards（非最后一步）。

### 5.1 论证深度硬约束

**每张卡必须包含至少 1 个边界条件句**——含以下任一标记词：
`然而/但/代价/不适用于/局限/前提是/假设/tradeoff/however/limitation/caveat`

若 reader 回答未提供边界条件，在 Phase 3 补问后再 reframe。
不得产出纯 "what" 卡——每张卡必须保留 "why not / tradeoff / alternative" 之一。

### 5.2 拆卡规则
- 默认一 Q&A = 一卡；多独立 idea 则拆
- 标题需「与」连词 → 必须拆
- **拆卡时禁止只保留 what**：每个子卡须继承原回答中相关的 boundary/tradeoff 信息

### 5.3 Distinction Footnotes
每条 `[^card-N]` 必须用完整句说明两卡区分理由：
```
[^card-1]: -> sibling-card-slug -- 本卡聚焦 X 的机制实现，该卡聚焦 X 的性能代价
```
裸 slug 引用（无区分说明）是 BUG。

### 5.4 Hedge 保留
源说 suggests/implies/appears → 卡必须保留对应中文限定词。删除 hedge = 篡改源置信度。

### 5.5 Cross-Link
每张卡至少考虑是否与本轮其他卡存在关联。Comparison 卡引用非核心概念时必须有 `[^card-N]` 追溯。

---

## 6. Card 输出格式

```markdown
---
id: <kebab-case-slug>
title: <中文短标题>
status: draft
card_type: <自由描述>
tags: [<自由 hashtag>]
created_time: <ISO8601+08:00>
edited_time: <ISO8601+08:00>
edited_entity: llm
source_ids: [${s.slug}]
evidence_basis: ${s.eb}
justification: ../justification/<id>.md
canonical_concept: <kebab-case-english>
aliases: [<变体词列表>]
summary: >-
  <一行稠密 grep 靶子：含 canonical + 所有 aliases + 核心论断>
related: []
---

<知识陈述体正文，含 [^src-N] 标记>
<至少 1 句边界条件/tradeoff/limitation>

## Footnotes

[^src-1]: `${s.path}` -- <Section PN> -- "<quote>"
[^card-1]: -> <slug> -- <完整句区分说明>
```

---

## 7. Justification Journal

每张卡同时产出 `drafts/justification/<id>.md`：

```markdown
---
schema: justification_journal.v1
card: ../cards/<id>.md
created_time: <ISO8601+08:00>
---

## creation | <ISO8601+08:00>

生成方式：Mode A questioning loop, round <N>
问题：<触发本卡的问题>
来源：`${s.path}`

源证据：
- <位置> — "<关键原文片段>"

范围论证：<上界/下界/与兄弟卡边界>
```

---

## 8. Reviewer Quit-Audit（SATISFIED 后自检）

声明 SATISFIED 后执行：(1) 逐条 core_claims vs cards → covered/gap (2) 随机 3-5 卡 grep 验证 → supported/unsupported/ambiguous (3) 无 gap + 无 unsupported → pass；否则产出补问清单继续。附加检查（源节覆盖/链接密度/重叠检测）记录不阻塞。

---

## 9. 执行流程总结

```
1. Read 全文 → 产出 digest
2. Phase 1: 广度扫描 → reframe
3. Phase 2: 深度追问 (2-4 轮) → 每轮 reframe
4. Phase 3: 边界条件追问 (>=1 轮) → reframe  ← 硬门槛
5. Phase 4: 内部张力 (0-1 轮) → reframe
6. Phase 5: 覆盖率自检 → 补问 → reframe
7. SATISFIED 三条件检查 → quit-audit → pass/补问
8. 输出全部 drafts/cards/*.md + drafts/justification/*.md
```

**硬约束**: 源内知识 | 每卡>=1边界句 | [^card-N]含区分说明 | Phase 3不可跳 | 中文正文英文key | Hedge必留
