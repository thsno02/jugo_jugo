# 出处论证：Schema 是 LLM Wiki 的配置文档

对应知识卡：`llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md`

## 事实从哪里来

本卡来自 `候选 10`，并只使用 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:33` 作为来源证据。候选陈述与来源行的核心信息一致：schema 是指导 LLM 组织 wiki、遵循约定并执行相关工作流的配置文档。

## 来源为什么能支撑它

第 33 行直接定义了 `The schema`。该行说明 schema 是一个文档，作用是告诉 LLM wiki 如何组织、有哪些约定，以及在摄取来源、回答问题和维护 wiki 时应遵循哪些工作流。该行还把 schema 称为关键配置文件，因此能够支撑“schema 是配置文档”这一整理后的事实陈述。

## 来源明说的部分

来源明说了三点：第一，schema 是一个文档；第二，它告诉 LLM wiki 的结构和约定；第三，它规定 LLM 在摄取来源、回答问题或维护 wiki 时遵循的工作流。来源还明说 schema 是关键配置文件。

## 整理后的表述

卡片把来源中的定义整理为一句中文原子事实：“在该来源的架构中，schema 是指导 LLM 如何组织 wiki、遵循约定以及执行摄取、问答和维护工作流的配置文档。”其中“组织 wiki、遵循约定、执行摄取、问答和维护工作流”是对来源列举内容的压缩转述；“配置文档”来自来源同时称其为文档和关键配置文件。

## 成立范围

该事实只在该来源对 schema 层的规定内成立。它不声称所有 wiki、所有 LLM agent 或其它知识管理系统都采用同样的 schema 概念。

## 采纳状态

审计报告给出 `audit_result: pass`，因此本卡已按任务包采纳到知识库；采纳后知识卡状态为 `accepted`。
