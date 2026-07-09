---
id: llm-wiki-kit-wiki-architecture
title: llm-wiki-kit Wiki 目录架构
status: accepted
card_type: architecture
tags:
- wiki-structure
- knowledge-graph
- markdown-wiki
created_time: 2026-06-12 19:00:00+08:00
edited_time: 2026-06-12 19:00:00+08:00
edited_entity: llm
source_ids:
- repo-iamsashank-llm-wiki-kit
evidence_basis: code_implementation
justification: ../justification/llm-wiki-kit-wiki-architecture.md
canonical_concept: llm-wiki-kit-wiki-architecture
aliases:
- wiki directory structure
- concepts sources synthesis
- wiki architecture
summary: 'llm-wiki-kit 的 wiki 由三层目录组成: concepts/（概念页如 attention.md）、 sources/（源摘要页）、synthesis/（综合分析页），加上 index.md 目录和 log.md 操作日志。所有页面通过 [[wiki links]] 互联形成知识图谱。原始材料存于 raw/ 目录保持不可变。agent 负责维护 wiki 结构，用户不直接编辑。wiki_graph
  工具 可生成交互式 HTML 图谱可视化，节点按类型着色。'
related:
- llm-wiki-kit-persistent-agent-memory
- llm-wiki-kit-mcp-tool-surface
---

llm-wiki-kit 的知识库采用分层目录架构，由 agent 自主维护 [^src-1]。

## Wiki 层（agent 维护）

| 目录/文件 | 职责 |
|-----------|------|
| `concepts/` | 概念页面（如 `attention.md`），存储跨源抽象概念 |
| `sources/` | 源摘要页面（如 `paper-1.md`），对应单一原始材料 |
| `synthesis/` | 综合分析页面（如 `cache.md`），跨源比较与推理结论 |
| `index.md` | 目录索引 |
| `log.md` | 操作日志（何时发生了什么） |

所有页面通过 `[[wiki links]]` 互联，形成知识图谱结构 [^src-2]。

## Raw 层（不可变）

原始材料（`paper.pdf`, `article.html`, `transcript.md`）存于 `raw/` 目录，保持不可变。agent 从 raw 读取、向 wiki 写入 [^src-3] [^card-1]。

## 图谱可视化

`wiki_graph` 工具生成交互式 HTML 图谱，节点按类型（sources、concepts、synthesis）着色，可拖拽探索连接关系 [^src-4]。

[^src-1]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "How It Works" P169-192 -- "concepts/ | sources/ | synthesis/ | + index.md | + log.md"
[^src-2]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "How It Works" P181 -- "[[linked]]"
[^src-3]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "How It Works" P189-191 -- "RAW SOURCES (immutable) paper.pdf, article.html, transcript.md"
[^src-4]: `data/raw/github_repo/repo-iamsashank-llm-wiki-kit/repo/README.md` -- "Knowledge Graph" P199-205 -- "wiki_graph generates an interactive HTML visualization... Nodes are color-coded by type"
[^card-1]: llm-wiki-kit-persistent-agent-memory -- wiki 架构是持久记忆方案的内部结构
