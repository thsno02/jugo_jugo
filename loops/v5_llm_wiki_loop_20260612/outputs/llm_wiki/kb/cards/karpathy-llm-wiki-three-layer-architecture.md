---
id: karpathy-llm-wiki-three-layer-architecture
title: Karpathy LLM Wiki 三层架构概念
status: accepted
card_type: concept
tags:
- llm-wiki
- knowledge-architecture
- karpathy
- three-layer
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- pypi-my-llm-wiki
evidence_basis: documentation
justification: ../justification/karpathy-llm-wiki-three-layer-architecture.md
canonical_concept: karpathy-llm-wiki-three-layer-architecture
aliases:
- LLM Wiki
- llm-wiki three layers
- Karpathy LLM Wiki
- three-layer architecture
summary: Andrej Karpathy 于 2026 年 4 月提出 LLM Wiki 概念：一种个人知识系统，包含三层架构——raw files（永不修改的原始文件）、compiled
  wiki（带交叉引用的编译 wiki）、schema（告诉 LLM 如何维护的模式）。核心洞察为 compile once query forever，wiki
  作为 persistent compounding artifact 持续积累而非每次查询重新推导。
related:
- karpathy-llm-wiki-concept
- karpathy-llm-wiki-pattern
- llm-knowledge-base-pattern
- llm-wiki-definition-and-core-value
- llm-wiki-knowledge-system
- llm-wiki-pattern
- llm-wiki-pattern-definition
- llm-wiki-pattern-overview
- llm-wiki-three-folder-architecture
- llmwiki-compile-first-architecture
- olw-llm-as-compiler
- raw-wiki-code-architecture
- three-layer-wiki-architecture
- llm-knowledge-base-three-layer-architecture
- memex-llm-kb-lineage
- my-llm-wiki-tool-overview
---

Andrej Karpathy 于 2026 年 4 月分享了 LLM Wiki 概念——一种个人知识系统，具有三层架构 [^src-1]：

1. **Raw files**（原始文件层）：永不修改的源文件
2. **Compiled wiki**（编译 wiki 层）：带交叉引用的知识编译产物
3. **Schema**（模式层）：告诉 LLM 如何维护整个系统的规则

核心洞察是"compile once, query forever"——一次编译，永久查询。Wiki 被定位为"persistent, compounding artifact"（持久的、复合增长的制品），而非每次查询时重新推导知识 [^src-2]。

[^src-1]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Project description" P100 -- "a personal knowledge system with three layers: raw files (never modified), a compiled wiki with cross-references, and a schema that tells the LLM how to maintain it"
[^src-2]: `data/raw/pypi/pypi-my-llm-wiki/text.txt` -- "Project description" P100 -- "compile once, query forever, and let the wiki grow with every session as a 'persistent, compounding artifact' rather than re-deriving knowledge on every query"
