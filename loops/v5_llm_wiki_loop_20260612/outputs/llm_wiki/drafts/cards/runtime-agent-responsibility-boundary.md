---
id: runtime-agent-responsibility-boundary
title: 运行时与智能体职责边界
status: draft
card_type: design-principle
tags: [architecture, responsibility-separation, runtime, agent]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
evidence_basis: documentation
justification: ../justification/runtime-agent-responsibility-boundary.md
canonical_concept: runtime-agent-responsibility-boundary
aliases: [runtime owns vs agent owns, 运行时职责, agent 职责, runtime philosophy]
summary: >-
  runtime-agent-responsibility-boundary 运行时与智能体职责边界明确划分：
  runtime 负责 canonical paths/IDs、validation、deterministic writes、manifest tracking、wiki navigation；
  agent 负责 summarization、OCR/vision/profiling、synthesis、分类决策、持续改进。
  kb_prepare_source_bundle 是两层之间的桥梁接口。
related: []
---

## 运行时与智能体职责边界

llm-wiki-karpathy 明确划分了运行时与 agent 的职责 [^src-1]：

**Runtime owns**:
- canonical paths（规范路径）
- canonical IDs（规范标识）
- validation（校验）
- deterministic writes（确定性写入）
- manifest-backed representation tracking（清单驱动的表示追踪）
- generated wiki navigation（生成式导航）

**Agent owns**:
- summarization（摘要）
- OCR, vision, or profiling work（在 runtime 之外执行）
- synthesis（综合）
- 决定结果属于 output/concept/entity/synthesis 哪个类别
- 持续改进 wiki（而非让价值困在对话中）

`kb_prepare_source_bundle` 是两层之间的桥梁：它返回 agent 编译 source note 所需的全部元数据、资产引用、已存表示和就绪状态 [^src-2]。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" P105-118 -- "The runtime owns: canonical paths..."
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" P118 -- "kb_prepare_source_bundle is the bridge between those layers"
[^card-1]: [[representation-first-design]] — 此边界的具体体现：非文本资产的中间表示由 agent 生成，runtime 提供存储与验证
