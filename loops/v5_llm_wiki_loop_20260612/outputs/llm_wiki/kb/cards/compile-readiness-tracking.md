---
id: compile-readiness-tracking
title: 编译就绪度追踪机制
status: accepted
card_type: mechanism
tags:
- compile-readiness
- multimodal
- representation
- workflow
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- clawhub-llm-wiki-karpathy
evidence_basis: documentation
justification: ../justification/compile-readiness-tracking.md
canonical_concept: compile-readiness-tracking
aliases:
- compile readiness
- compile_readiness
- 编译就绪度
- ready/partial/needs_representation
summary: compile-readiness-tracking 编译就绪度追踪通过 kb_prepare_source_bundle 返回三种状态： ready（全部表示就位可编译）、partial（部分就位）、needs_representation（缺少必要中间表示），
  用于控制非文本资产何时可以编译为最终 source note。
related:
- representation-first-design
- kb-lint-deterministic-validation
- knowledge-compilation-paradigm
---

## 编译就绪度追踪机制

运行时通过 compile-readiness tracking 控制非文本资产的编译时机 [^src-1]，定义三种状态：

| 状态 | 含义 |
|------|------|
| **ready** | 所有必要的 representation trail 已就位，可编译最终 source note |
| **partial** | 部分中间表示已存储，但仍有缺失 |
| **needs_representation** | 尚未存储任何必要的中间表示 |

`kb_prepare_source_bundle` 返回 compile_readiness 字段，告知 agent 当前源的编译就绪状态 [^src-2]。agent 据此决定是继续生成表示还是开始编译。

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P22 -- "compile-readiness tracking with ready, partial, and needs_representation"
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" P21 -- "full compile context through kb_prepare_source_bundle, including asset refs, stored representations, and compile_readiness"
[^card-1]: [[representation-first-design]] — compile readiness 是 representation-first 路径的控制信号
