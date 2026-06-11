---
schema: v4_learnings
loop_id: v4_llm_wiki_loop_20260602
created: 2026-06-12
topic: design_decisions
purpose: retrospective
---

# 设计决策注册表

以下为 v4 中经证据验证的设计决策（非假设）。每项决策均有 v4 审计/执行中的实证支撑。

---

## 1. No cluster count targets

（详见 ./operational_lessons.md #2 — Cluster 治理制造知识边界）

- **decision**: governance clustering 使用启发式规则（topic/alias overlap），禁止数量目标。
- **rationale**: 数量约定（如"aim for 20-40 clusters"）会导致 agent 在自然 cluster 数不足时硬凑细分、过多时硬压合并，扭曲知识结构。Clustering 是粗糙建模（把可能有关系的卡放到 agent 面前），不是 ground truth classification。
- **evidence_from_v4**: v4 综合审计 Section 2 "Cluster count targets: NOT CONFIRMED"——8 个 created_time 聚类为批次生成的自然产物，无证据表明为凑数；19 张 comparison 卡均有实质区分点。cluster damage assessment 进一步证明集群没有形成硬边界（88.7% 链接跨前缀），但主题亲和性产生了温和聚类偏好（同前缀密度 5.7x）——这正是启发式自然聚类的预期行为，而非数量目标的人工产物。

---

## 2. Workflow load balancing

（详见 ./operational_lessons.md #4 — Workflow 负载不均衡）

- **decision**: parallel() 中所有 agent 的负载必须大致均等；若某 agent 工作量 >2x 平均值则拆分。
- **rationale**: parallel() 的完成时间 = 最慢 agent 的完成时间。负载不均浪费并发优势。
- **evidence_from_v4**: 深层审计部署了 10 个均衡 agent（每 agent 约 28 张卡或一个专项 topic），相比最初方案（全量 grep + 深读同在一个 agent 内导致超时），执行效率显著提升。v4 综合审计由 21 个 reporting agent 完成——工作分配证明了均衡策略的可行性和必要性。

---

## 3. Audit agent context control

- **decision**: 审计 agent 的阅读范围必须被显式限定；agent 不应依赖"自由探索整个 KB"来发现问题。
- **rationale**: 无边界阅读导致两个问题：(a) agent 上下文溢出，无法完成分配的审计任务；(b) 脚注叙事泄漏证明"读到什么就用什么"会引入未归因内容。
- **evidence_from_v4**: leakage trace 证明 governance agent 在读取 cluster 全部卡片时，脚注叙事中的外部概念被无归因地吸收（5/21 对比卡 = 24% 泄漏率）。修正：prompt 显式区分"卡正文 src 锚定内容"与"脚注跨引内容"；agent 被指示只使用有 footnote 锚定的内容作为 comparison tension 的输入。

---

## 4. Sequential vs parallel tradeoffs

- **decision**: extraction 可并行（提速），但 governance/fusion 必须在全部 draft 落地后顺序执行。
- **rationale**: 并行 extraction 没有"增量比累积"的时刻——同时生成的 draft 之间无法相互去重。governance 需要看到全集才能执行跨卡关系发现。
- **evidence_from_v4**: v4 的 248/280 张卡时间戳为同一批次（2026-06-05T10:00:00+08:00），intra-loop 去重从未发生（merge_candidate=0）。深层审计确认 KB 的问题是"缺失内容 vs 错误内容的不对称"——并行未引入错误，但因无 post-extraction fusion pass 而保留了可合并的重复/近似概念。

---

## 5. Comparison cards as pure sinks (by design)

- **decision**: comparison 卡是纯 sink 节点——引用 subject cards，但 subject cards 不需要 related 反引。
- **rationale**: comparison 是"关于两张卡的关系"的元知识，不是被引卡的属性。强制双向链接会给每张 subject card 的 related 字段注入大量 comparison slug，降低信噪比。
- **evidence_from_v4**: 深层审计确认 21 张 comparison 卡全部零入度，移除它们仅损失 6.8% 边——结构影响极小。但 comparison 卡同时是唯一的跨源连接载体（6.8% 多源卡），且静默分歧裁决表现优秀（19/21 NEUTRAL-ACKNOWLEDGED）。结论：sink 设计正确，但需补充轻量 see_also 反向链接以提高可发现性。

---

## 6. Editorial annotations vs card body edits

- **decision**: 审计发现的 editorial 超源内容用"编者注"标记，不修改卡正文。
- **rationale**: 卡正文代表从源材料提取的知识；审计层的判断（如"此处为合理推论"）属于元数据层，不应混入知识层。保持分层让消费者可以选择信任级别。
- **evidence_from_v4**: v4 审计的 m3 finding 列出 8 处 editorial 超源（tree-sitter-code-extraction "确定性"段、weight-internalization-aspiration "规模瓶颈"等），全部判定为"合理但未标注为编辑推论"。修复方案选择"为每处添加编者注标记"而非重写正文——保留了知识密度的同时增加了认识论透明度。

---

## 7. grep-friendly metadata over embedding

- **decision**: 召回质量来自一致的 metadata 纪律（canonical_concept / aliases / key_terms / summary），不来自重基础设施。grep 这种笨检索就够用。
- **rationale**: 与其"在笨卡片上建聪明检索（embedding/向量）"，不如"把卡设计成 grep-friendly，让 grep 就够用"。零基础设施依赖、可解释、agent 自主。
- **evidence_from_v4**: v4 全部审计工作（21 个 agent、280 张卡、400+ 脚注验证）均通过 grep + Read 完成，零 embedding 基础设施。mechanical audit 的 cross-link 验证（1021 条有向边解析）、slug 一致性检查、幽灵引用检测全部基于 frontmatter grep。唯一不足是"grep 审计有 false positive"（says-vs-implies 混淆），但修正方案仍是"grep 初筛 + agent semantic 复核"而非引入 embedding——保持了架构轻量性。

---

## 8. Zettelkasten no taxonomy

- **decision**: 卡片是原子 Zettels；card_type/tags 保持自由描述可选，不当受控分类网格。结构靠 footnote 链接 + governance 涌现。
- **rationale**: 预定义互斥分类体系（taxonomy）在知识复杂度高、用户会交互、无人维护的场景下是灾难。类别无法限定好。颗粒度的保证是"耗尽"（exhaust material 承载的不同 idea）而非体量。
- **evidence_from_v4**: v4 综合审计 "Zettelkasten 原子性: PASS"——35 标题连词疑似中 34 通过实质审查；19 多源卡全部为 comparison 类型（预期行为）。没有 taxonomy 不影响治理：governance 通过 canonical_concept 前缀自然聚类（11.3% 同前缀），alias overlap 驱动 comparison 发现（21 张 comparison 卡全部基于语义重叠而非类别标签）。card_type 字段保持自由（mechanism/concept/distinction/implementation 等无受控集），未观察到分类混乱。

---

## 9. Loop independence

- **decision**: 每个 loop 是独立的 0->1 过程。绝不依赖、比较、引用前序 loop 的 KB。
- **rationale**: 跨 loop 引用是污染。dedup/similarity 的比较基永远是本 loop 自己累积的 drafts/cards。
- **evidence_from_v4**: v4 综合审计 "Loop 独立性: PASS"——280 张卡无任何对 v0-v3 loop 的引用；grep 确认零跨 loop slug 引用。v4 KB 是完全独立产出，未继承 v3 的任何缺陷（如 v3 的 similarity base 指向 v2 这一 origin-defect 在 v4 中完全消除）。

---

## 10. Best-effort governance zen

- **decision**: 治理的目的不是解决所有问题，而是让问题更简单。governance/dedup/fusion 不必完备——每次让 KB 更简单（降熵）即可。
- **rationale**: O(N^2) 完备性追求在 280 张卡规模下不经济且不必要。园艺而非证明定理。可以心安理得放弃 edge case 的完美处理。
- **evidence_from_v4**: v4 governance 的实际表现验证了 best-effort 哲学：(a) 源忠实性零伪造引用（400+ 脚注全部追溯）——核心质量保障到位；(b) cross-link 54.3% 跨源——虽非 100% 但足够形成知识网络；(c) 残余问题（70 张 YAML bug、5 张孤儿、2 处泄漏）通过后续 audit pass 渐进修复——每轮降熵而非一步到位。cluster damage assessment 证明"集群未制造信息孤岛"（88.7% 跨前缀），best-effort 聚类已足够好。
