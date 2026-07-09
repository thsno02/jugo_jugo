---
id: llm-wiki-ingestion-workflow
title: LLM Wiki Ingestion 工作流
status: accepted
card_type: process-description
tags:
- llm-wiki
- ingestion
- workflow
created_time: 2026-06-12 17:00:00+08:00
edited_time: 2026-06-12 17:00:00+08:00
edited_entity: llm
source_ids:
- anthemcreation-en-guide
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-ingestion-workflow.md
canonical_concept: llm-wiki-ingestion-workflow
aliases:
- ingestion phase
- wiki ingestion
- document ingestion
summary: LLM wiki ingestion 工作流 ingestion-workflow：添加新文档时 LLM 执行四类操作——创建新 entity page、更新已有页面、识别与综合来源间矛盾、创建自动 backlinks。Raw sources 保持不可变，职责分离严格。
related:
- llm-wiki-three-layer-architecture
- llm-wiki-query-phase
- llm-wiki-two-step-cot-ingest
- llm-wiki-v2-agent-memory
---
Ingestion 是 LLM wiki 的核心写入操作。当添加新文档时，LLM 读取源文件、提取关键思想，然后整合至已有 wiki [^src-1]。具体可执行四类操作：

1. **创建新 entity page**——为尚不存在的概念建立页面（如 "Phi-2" 页面详述其 27 亿参数在 1.4 万亿 token 上训练）
2. **更新已有页面**——补充新信息至现有实体
3. **识别并综合矛盾**——当来源间存在冲突时进行标注和综合
4. **创建自动 backlinks**——在相关页面间建立双向链接

Raw sources 保持不可变。LLM 写 wiki，用户读 wiki——职责分离严格 [^card-1]。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Ingestion phase" -- "When you add a new document, the LLM reads the source, extracts the key ideas, and then integrates them into the existing wiki."
[^card-1]: 参见 [[llm-wiki-three-layer-architecture]] 关于三层架构的职责分离
