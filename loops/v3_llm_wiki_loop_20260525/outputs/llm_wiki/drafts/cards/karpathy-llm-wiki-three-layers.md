---
id: karpathy-llm-wiki-three-layers
title: Karpathy LLM Wiki 的三层 + 三操作：raw / wiki / schema + Ingest / Query / Lint
status: draft
card_type: concept
tags: [#karpathy-llm-wiki, #architecture, #three-layers, #ingest-query-lint]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
source_ids: [marvin-hn-persistent-knowledge]
provenance_card: ../provenance/karpathy-llm-wiki-three-layers.md
aliases: [raw + wiki + schema, ingest query lint, three layers three operations]
related: [karpathy-llm-wiki-vs-rag, obsidian-as-ide-llm-as-programmer, llm-wiki-mcp-skills-vs-tools-workflow, llm-knowledge-base-five-stage-workflow]
---

## 三层架构

Karpathy 在 gist 里把整套系统分成三个**职责正交**的层：

1. **Raw sources（原始源层）**：immutable 的 article / paper / transcript / image / dataset。是 ground truth，**不被 LLM 改写**。
2. **Wiki（编译层）**：LLM-authored markdown 页，含 summaries / concepts / entities / comparisons / 更宏观的 synthesis。这是 LLM 的"工作区"。
3. **Schema（规则层）**：一份 AGENTS.md 或 CLAUDE.md，告诉 agent "这个 wiki 应该长什么样、怎么维护"。

任何一层缺失都会失效：缺 raw → 无可追溯证据；缺 wiki → 退化为 RAG；缺 schema → 退化成另一堆笔记。

## 三个核心操作

在三层之上，gist 规定 agent 必须能做三件事，对应 wiki 的全生命周期：

| 操作 | 含义 | 触发时机 |
|---|---|---|
| **Ingest** | 读新源 → 讨论 → 写摘要 → 更新 index → 触达相关页 → append log | 有新源进入 raw/ |
| **Query** | 拿问题对 wiki 做问答，可选地把分析结果回灌成新页 | 用户提问 / agent 自查 |
| **Lint** | 周期性检查矛盾、过期声明、孤儿页、弱 cross-reference、缺失概念 | 手动 / 周期触发 |

这三者与"数据库的 CRUD"不是 1:1 对应——Ingest 不是"INSERT"，它必然附带 UPDATE 多个旧页；Query 不是"SELECT"，它可能 INSERT 新页；Lint 不是 housekeeping，它是 wiki 的健康闭环。

## 两个特殊文件

- `index.md`：内容导向的导航地图（"wiki 里有些什么主题"）。
- `log.md`：时序导向的演化记录（"什么时候做了什么"）。

两个文件**功能正交**：index 让人 / agent 在概念空间里找路；log 让人 / agent 在时间维度上回溯。**两个都缺的 wiki 等于没有元数据**。

## 操作含义

- 项目起步：先写 schema.md（哪怕只有 5 行），再做第一次 ingest。
- 周期性 lint 是**非可选**——多人 / 多 agent 写过同一片区域后矛盾会快速堆积。
- 不要把 raw/ 和 wiki/ 混在同一个目录或 .gitignore 规则里，否则不可逆操作会发生。

## References

- 三层架构原文：`data/raw/webpage/marvin-hn-persistent-knowledge/text.txt:29`。
- 三操作原文：`text.txt:31`。
- index / log 双特殊文件：`text.txt:31`。

## Footnotes

- 三层原文：`text.txt:29` —— "Karpathy frames the system in three layers. The first is raw sources... The second is the wiki, a directory of LLM-authored markdown pages... The third is the schema, a rules document such as AGENTS.md or CLAUDE.md that tells the agent how the wiki should be structured and maintained."
- 三操作原文：`text.txt:31` —— "Ingest means reading a new source, discussing it, writing a summary, updating the index, touching related pages, and appending to the log. Query means answering questions against the wiki itself, then optionally filing the resulting analysis back into the knowledge base as a new page. Lint means periodically checking for contradictions, stale claims, orphan pages, weak cross-references, or missing concepts."
- 两特殊文件原文：`text.txt:31` —— "Two special files, index.md and log.md, help navigation by separating the content-oriented map of the wiki from the chronological record of how it evolved."
