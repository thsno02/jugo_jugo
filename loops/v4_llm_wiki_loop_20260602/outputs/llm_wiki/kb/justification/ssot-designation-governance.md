---
schema: justification_journal.v1
card: ../cards/ssot-designation-governance.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：增量提取（falconer-enterprise-guide 第二轮）
来源：`data/raw/webpage/falconer-enterprise-guide/markdown.md`
源证据：
- "Step 3: Set sources of truth" 段 — "The enterprise equivalent is designating which documents are canonical for each domain: architecture decisions, runbooks, onboarding guides, product specs, API references."
- 同段 — "Once a doc is marked canonical, the system monitors it from that point forward and treats conflicting sources as supplementary context rather than competing truth."
- 比较表 Schema 行 — "SSOT designations and ownership metadata, enforced as a property of the system"
- "What Karpathy's LLM Wiki does" 段 — "And there's a CLAUDE.md schema file that tells the agent how to operate on the vault."
范围论证：现有 three-layer-architecture 卡描述个人 LLM Wiki 的三层结构（raw/wiki/schema），其中 raw 层是 "source of truth"——不可变输入的含义。本卡提取的是企业级的不同概念：SSOT 作为治理机制——为每个领域**指定**权威文档，附加所有权元数据，并对冲突来源做出声明式降级处理。这是从"个人操作指令"到"组织治理属性"的本质变化，值得独立成卡。与 continuous-drift-detection 的区分在于：偏移检测是执行层（怎么检测），SSOT 指定是策略层（检测什么、谁负责）。
