---
id: companion-conformance-invariants
title: 伴侣系统合规不变量
status: accepted
card_type: operational_rule
tags: [companion-memory, conformance, specification, invariants, testing]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [arxiv-memory-as-metabolism]
justification: ../justification/companion-conformance-invariants.md
canonical_concept: companion-conformance-invariants
aliases: [伴侣合规不变量, companion conformance invariants, 合规边界, conformance boundary, 框架不变量]
summary: >-
  companion-conformance-invariants（伴侣合规不变量 / conformance boundary / 框架不变量）伴侣记忆框架为每个操作定义的规范性不变量集合，将"说服性框架"转变为"可测试的规范"；核心不变量包括：TRIAGE 禁止读取活跃 wiki、CONSOLIDATE 必须先缓冲区内评分、DECAY 不得衰减引力保护下限以上的条目、任何操作禁止永久删除对象
related: [audit-stress-test, companion-knowledge-system, spec-driven-conformance-testing, triage-shallow-filter]
---

伴侣记忆框架的合规不变量（Section 7.5）是规范的执行面——将"有说服力的框架"转变为"构建者可测试的东西"[^src-1]。

**关键跨操作不变量**[^src-2]：
- 活跃 wiki 在任何 CONSOLIDATE 或 AUDIT 运行期间必须保持可读——读路径不允许阻塞锁
- 联邦出站必须匿名化——个人身份内容不得跨设备边界
- 任何操作禁止永久删除任何对象——终态是 archived 或 expired，永不硬删除

**CONSOLIDATE 关键不变量**[^src-3]：
- 必须在对活跃 wiki 评分之前先对缓冲区条目互相评分——缓冲区内评分是非可选阶段；跳过它会重新引入缓冲区架构要防止的自密封失败模式
- 必须操作于定义的快照（特定 Git commit hash + 元数据索引高水位标记）
- 在固定模型版本和运行配置下给定相同缓冲区快照必须可复现
- 每次运行最多产生一个 Git commit
- 禁止永久丢弃少数派假设——矛盾集群转入分支而非删除

**DECAY 关键不变量**[^src-4]：
- 不得衰减基础引力 G_i^base 保持在引力保护下限以上的条目——下限基于 G_i^base 而非 G_i^eff 评估
- 必须压缩而非删除低于活力阈值的衰减合格条目

**实现自由度**：满足所有不变量的实现仍可在 CONTEXTUALIZE 的深度推断、DECAY 的权重调优、CONSOLIDATE 的提升阈值校准、AUDIT 的查询集等方面存在重大差异[^src-5]。

「规范先行」的方法论并非该框架独创——Microsoft Agent Governance Toolkit 独立采用了相同策略，为每个组件编写 RFC 2119 形式规范并配以合规测试[^card-1]。在操作层面，本卡定义的不变量构成了 AUDIT 等慢周期机制的合规边界：AUDIT 在不变量约束下通过悬挂高引力条目测试其功能必要性[^card-2]。

## Footnotes

[^src-1]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "The invariants are the spec's enforcement surface --- the point at which 'here is a persuasive framework' becomes 'here is something a builder can test against.'"
[^src-2]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "General" conformance invariants
[^src-3]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "CONSOLIDATE - MUST score buffer entries against each other before scoring against the active wiki --- buffer-internal scoring is a non-optional phase"
[^src-4]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "MUST NOT decay entries whose base gravity G_i^base remains above the gravity-protection floor"
[^src-5]: `data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "An implementation that satisfies all of the above invariants may still differ substantially from others"
[^card-1]: [规范驱动的合规测试](spec-driven-conformance-testing.md) -- 本卡聚焦伴侣记忆框架的操作级合规不变量，该卡聚焦 Microsoft 治理工具包的 RFC 2119 形式规范与 13,000+ 合规测试；两者共享「规范先行」方法论但应用于不同领域
[^card-2]: [AUDIT 结构性压力测试](audit-stress-test.md) -- 本卡定义所有操作必须满足的合规不变量边界，该卡描述运行于慢周期的 AUDIT 悬挂测试机制；AUDIT 在不变量约束下通过悬挂高引力条目测试功能必要性
