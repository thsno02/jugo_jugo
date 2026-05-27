---
id: nvk-llm-wiki-hub-and-topic-wikis
title: nvk/llm-wiki 的 Hub + Topic-Wikis 结构——一题一库，互不污染
status: accepted
card_type: concept
tags: [#llm-wiki, #nvk, #obsidian, #topic-isolation, #plugin]
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-27T15:12:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
provenance_card: ../provenance/nvk-llm-wiki-hub-and-topic-wikis.md
aliases: ["nvk llm-wiki architecture", "topic-wiki isolation"]
related: [llm-knowledge-base-five-stage-workflow, nvk-llm-wiki-audit-and-librarian, nvk-llm-wiki-parallel-multi-agent-research, robin-cartier-scale-ceiling, karpathy-gist-three-layers]
---

`nvk/llm-wiki`（由 nvk 开发的、Karpathy LLM Wiki gist 的工具化实现）把"wiki"拆成 **Hub + 多个 Topic-Wiki** 的两级结构，而不是一个大库装一切。这是它最重要的设计决策之一，也是它能多 topic 同时维护而互不污染的关键。

**目录结构（默认在 `~/wiki/`）：**

```
~/wiki/                # Hub — 轻量、无内容
├── wikis.json         # 所有 topic wikis 的 registry
├── _index.md          # 列出 topic wikis 与统计
├── log.md             # 全局活动日志
└── topics/            # 每个 topic 是一个独立 wiki
    ├── nutrition/
    │   ├── .obsidian/     # Obsidian vault 配置
    │   ├── inbox/         # 该 topic 的 drop zone
    │   ├── inventory/     # items / candidates / corpora / views
    │   ├── datasets/      # 大型 / 外部数据的 manifest
    │   ├── raw/           # 不可变源
    │   ├── wiki/          # 编译出的文章（concepts / topics / references）
    │   ├── output/        # 生成的可交付物
    │   ├── _index.md
    │   ├── config.md
    │   └── log.md
    ├── woodworking/   # 另一个 topic wiki
    └── .archive/      # 归档的 topic wikis（默认隐藏）
```

**Hub 的角色（极轻）：**

- 只装 registry (`wikis.json`)、列表索引 (`_index.md`)、活动日志 (`log.md`)；
- **不装任何内容**——所有 raw / wiki / output 都在 topic 子目录里；
- 切换或合并机器时只需要同步 hub，topic 文件夹本身可独立移动。

**Topic-Wiki 的不变量：**

- 每个 topic 一个独立的 Obsidian vault，可以 `open ~/wiki/topics/nutrition/` 直接打开；
- `raw/` 是 **immutable**：一旦 ingest，永不修改。Articles 在它上面合成；retract 时同时移除两者，保持 audit trail；
- `inventory/` 是 *state* 而非 evidence——存可清点的"事物"：items, source candidates, corpora, entities, open questions, watch items, next actions；明示不作为事实证据；
- `datasets/` 只放 manifest（路径、samples、profile、query recipe）——大型外部数据不进 `raw/`，wiki 充当"索引界面"；
- `wiki/` 文章分三类目录：concepts（基础理念）/ topics（具体专题、状态报告）/ references（工具表、数据表）；每个目录都有 `_index.md` 作为"派生缓存"，agent 永远不"blindly scan"。

**为什么 isolation 这件事这么重要：**

> "Each research area is isolated. No cross-topic noise. Queries stay focused. A multi-wiki peek finds overlap when relevant."

- nutrition 的 query 不会被 woodworking 的内容污染；
- "deep query" 仍可显式跨 wiki（命令支持 `--with <wiki>`、`--include-archived`）；
- archive 是 topic 级，不是 page 级：把整个 topic 移到 `topics/.archive/` 让它"安静"但不删除。

**操作含义：**

- 在设计自己的 LLM Wiki 时，**先决定 topic 边界**，再 ingest；
- topic 之间的 cross-link 用 archive registry + `_index.md` 派生缓存维持，而不是把所有 page 都倒进同一个 vault；
- 不要把"项目"或"客户"硬塞成 topic——topic 是"研究域"维度，"项目"用 `output/projects/<name>/` 子目录承载更合适。

**边界：**

- topic 隔离意味着同一概念可能在多个 topic 里重复出现——`/wiki:query --with` 是显式抢救机制，但维护成本要承认；
- archive 是 *quiet*，不是 *delete*：archived topic 仍占磁盘；要彻底删除需要手动；
- hub 的 `wikis.json` 应当存"逻辑路径"（如 `topics/bitcoin`）而不是某台机器的绝对路径，否则跨机器同步会失败。

## References

- `nvk/llm-wiki` 主站文档：`data/raw/webpage/llm-wiki-net/text.txt`，目录树在行 140；hub 与 isolation 段在行 142–168；commands 部分行 174。
- iCloud / 同步章节里关于"portable hub path"的劝告：行 332–334。

## Footnotes

- 目录树原文见行 140（单行密集排版）。
- "One topic, one wiki ... Each research area is isolated."——行 142–144。
- "Raw is immutable"段（行 150–152）：
  > "Once a source is ingested it is never modified. Articles synthesize on top. Retraction removes both cleanly."
- "Inventory is state" 段（行 154–156）；"Datasets stay external" 段（行 158–160）；"Archive is quiet" 段（行 162–164）。
- Hub 与 wikis.json 同步劝告（行 332–334）：
  > "Shared wikis.json entries should store topic paths such as topics/bitcoin , not /Users/alice/.../topics/bitcoin ."
