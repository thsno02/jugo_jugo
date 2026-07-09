---
id: conflict-routing-matrix
title: 冲突路由矩阵
status: draft
card_type: decision-procedure
tags: [conflict-routing, mirror-compensate, sycophancy, safety-override, companion-memory]
created_time: 2026-06-12T16:00:00+08:00
edited_time: 2026-06-12T16:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
evidence_basis: theoretical_paper
justification: ../justification/conflict-routing-matrix.md
canonical_concept: conflict-routing-matrix
aliases: [conflict routing matrix, 冲突路由矩阵, routing legend]
summary: >-
  conflict routing matrix 冲突路由矩阵将 mirror-vs-compensate 程序规则逐案实例化为七种冲突类型的路由决策。
  路由图例：Mirror（不变异规范条目的用户对齐行为）、Compensate（通过CONSOLIDATE高摩擦路由）、
  Buffer（进入少数分支不立即整合）、AUDIT override（优先路由至AUDIT）、External correction（标记待下次CONSOLIDATE审查）。
  关键行：Row 3 谄媚失败模式——用户持续强化有害声明但报告效用稳定时，无论效用信号如何补偿，
  因为效用信号在此不可靠。Row 5 多周期多元源矛盾触发正式晋升评估。Row 7 基座模型更新依赖架构可分离性。
  矩阵不定义校准参数（周期数、源多样性阈值），明确留给实现和实证验证。
related: [mirror-vs-compensate-principle, audit-operation, consolidate-operation, minority-hypothesis-retention]
---

冲突路由矩阵将 mirror-vs-compensate 程序规则逐案实例化为七种冲突类型的路由决策。[^src-1]

路由图例：
- **Mirror** = 不变异规范条目的用户对齐行为
- **Compensate** = 通过 CONSOLIDATE 以升高摩擦路由
- **Buffer** = 进入少数分支不立即整合
- **AUDIT override** = 优先路由至 AUDIT 并应用引力减少路径
- **External correction** = 标记待下次 CONSOLIDATE 审查 [^src-2]

关键行：
- Row 1-2：用户词汇偏离——无效用退化时镜像并保留偏离标记，有效用退化时重分类为补偿（效用信号是域重分类的桥梁）。
- Row 3（谄媚失败模式）：用户持续强化外部安全/认知信号标记为有害的声明，但用户报告效用稳定——无论效用信号如何都补偿。效用信号在此不可靠因为用户对有害模式报告满意度。
- Row 4-5：单源单周期矛盾默认 Buffer；多元源多周期矛盾触发正式晋升评估。
- Row 6：高引力条目跨多个 AUDIT 周期牵涉不良结果——AUDIT override 剥夺保护。
- Row 7：基座模型更新矛盾——标记外部修正，结构依赖架构可分离性。[^src-3]

局限：Row 7 命名基座模型矫正通道，但完全新颖坏信念（既未在基座模型中表示也未被后续经验矛盾）不被矩阵任何行捕获。矩阵在相关冲突信号存在时规定行为；不制造外部源未提供的信号。[^src-4]

[^src-1]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.0 Conflict routing matrix" P1 -- "The mirror-vs-compensate principle is procedural rather than algorithmic...The matrix below specifies routing for seven such cases."
[^src-2]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.0 Routing legend" -- "Mirror = apply user-aligned behavior...Compensate = route through CONSOLIDATE with elevated friction...Buffer = store in minority branch...AUDIT override...External correction"
[^src-3]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.0 Matrix Rows 1-7" -- "Row 3...This is the sycophancy failure mode. The utility signal is unreliable here...Safety requires an explicit override"
[^src-4]: data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt -- "5.0 Limitation" -- "the structural residual --- fully novel bad beliefs not represented in the base model and not contradicted by subsequent experience --- is not captured by any row in this matrix."

[^card-1]: mirror-vs-compensate-principle — 矩阵是原则的逐案实例化
[^card-2]: audit-operation — Row 6 路由至 AUDIT override
[^card-3]: minority-hypothesis-retention — Row 4-5 路由至 Buffer 和晋升评估
