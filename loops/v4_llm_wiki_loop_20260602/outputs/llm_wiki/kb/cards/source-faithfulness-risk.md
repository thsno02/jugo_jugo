---
id: source-faithfulness-risk
title: 源忠实性风险与不可变锚点
status: accepted
card_type: distinction
tags: [llm-wiki, faithfulness, drift, verification]
created_time: 2026-06-04T22:45:00+08:00
edited_time: 2026-06-04T22:45:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/source-faithfulness-risk.md
canonical_concept: source-faithfulness-risk
aliases: [源忠实性, faithfulness drift, 知识漂移风险]
summary: >-
  source-faithfulness-risk（源忠实性 / faithfulness drift / 知识漂移风险）指 LLM Wiki
  中 wiki 内容经多轮变换后偏离来源的风险；raw sources 不可变提供锚点，lint 仅查时效性非忠实度
related: [audit-provenance-tracing, compilation-gap, entrenchment-under-user-coupled-drift, lint-operation, model-quality-error-propagation, three-layer-architecture]
---

LLM Wiki 的 wiki 层完全由 LLM 生成，每次操作（摘要、综合、交叉引用、更新）都是有损变换。多轮迭代后，wiki 内容可能逐渐偏离原始来源的实际陈述——这是一种潜在的**知识漂移风险**。

材料的设计提供了一个**结构性锚点**：raw sources 层是不可变的——LLM 只读取不修改，它们是整个系统的 source of truth[^src-1]。这意味着理论上任何时候都可以回溯核查。

然而，材料未定义系统性的**忠实度验证机制**。Lint 操作检查的是时效性问题（「过时的主张」「缺失的交叉引用」），而非 wiki 内容是否偏离了原始来源的本意[^src-2][^card-2]。Raw sources 的不可变性是三层架构的核心设计决策[^card-1]。源忠实度的保障在实践中可能依赖于人类的抽查——作者描述了自己 「跟随链接、检查图谱视图、阅读更新后的页面」的实践[^src-3]——但这不是一个形式化的验证步骤。

LLM Wiki 的审计机制部分回应了这一缺口——它沿制品图遍历检测漂移，但其复用的 librarian 评分通道主要关注时效性而非语义忠实度[^card-6]。编译缺口描述了一种互补的失败模式：即使单次编译步骤也可能灾难性地丢弃关键事实，失败率高达 53-60%[^card-3]。在用户耦合的记忆系统中，漂移还会受到结构性固化的加剧——主导解释获得保护，矛盾证据被边缘化，知识库退化为范式维护系统[^card-4]。此外，模型自身能力不足是忠实性风险的另一根源：弱模型可能在不发出告警的情况下静默传播错误[^card-5]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Architecture > Raw sources" -- "These are immutable — the LLM reads from them but never modifies them. This is your source of truth."
[^src-2]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Operations > Lint" P1 -- "stale claims that newer sources have superseded"
[^src-3]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "The core idea" P4 -- "I browse the results in real time — following links, checking the graph view, reading the updated pages"
[^card-1]: [三层架构](three-layer-architecture.md) -- raw sources 的不可变性是三层架构的第一层设计
[^card-2]: [巡检操作](lint-operation.md) -- 巡检检查时效性但不检查源忠实度，本卡分析这一缺口
[^card-3]: [编译缺口](compilation-gap.md) -- 本卡聚焦多轮变换的渐进性漂移，该卡聚焦单次编译步骤的急性事实丢失（53-60% 灾难性失败率）
[^card-4]: [用户耦合漂移下的固化](entrenchment-under-user-coupled-drift.md) -- 本卡聚焦技术层面的有损变换漂移，该卡聚焦用户耦合的结构性范式固化（库恩式僵化）
[^card-5]: [模型能力不足导致的错误传播风险](model-quality-error-propagation.md) -- 本卡聚焦多轮变换的漂移风险，该卡聚焦模型能力不足作为错误静默传播的根因
[^card-6]: [审计与溯源追踪](audit-provenance-tracing.md) -- 本卡识别缺乏忠实度验证的风险，该卡描述沿制品图遍历检测漂移的审计机制，但其 librarian 通道侧重时效性而非语义忠实度
