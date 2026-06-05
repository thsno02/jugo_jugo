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
related: [spec-driven-conformance-testing, triage-shallow-filter, companion-knowledge-system]
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

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "The invariants are the spec's enforcement surface --- the point at which 'here is a persuasive framework' becomes 'here is something a builder can test against.'"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "General" conformance invariants
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "CONSOLIDATE - MUST score buffer entries against each other before scoring against the active wiki --- buffer-internal scoring is a non-optional phase"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "MUST NOT decay entries whose base gravity G_i^base remains above the gravity-protection floor"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/arxiv/arxiv-memory-as-metabolism/agent_source_bundle.txt` -- "Section 7.5" -- "An implementation that satisfies all of the above invariants may still differ substantially from others"
