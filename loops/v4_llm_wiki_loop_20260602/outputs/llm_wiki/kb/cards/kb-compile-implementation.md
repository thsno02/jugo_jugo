---
id: kb-compile-implementation
title: kb-compile 实现模式
status: accepted
card_type: example_pattern
tags: [llm-wiki, claude-code, implementation, mem0, kb-compile]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
justification: ../justification/kb-compile-implementation.md
canonical_concept: kb-compile-implementation
aliases: [kb-compile命令, kb-compile实现, Claude Code wiki编译]
summary: >-
  kb-compile-implementation（kb-compile命令 / Claude Code wiki编译）是一种将 LLM Wiki
  模式落地的具体实现：通过 Claude Code 自定义命令 /kb-compile 触发 wiki 编译，在已有 Mem0+pgvector
  向量检索层之上叠加 wiki 层，形成四组件混合架构
related: [llm-wiki-pattern, three-layer-architecture, rag-wiki-complementarity]
---

作者将 Karpathy 的 LLM Wiki 模式落地为 Claude Code 的自定义命令 `/kb-compile`，在已有的向量记忆基础设施上叠加了 wiki 编译层[^src-1]。

**目录映射**：`workspace/knowledge/`（日报、研究、会话日志）对应 Raw sources；各目录中的 `CLAUDE.md` 对应 Schema；`workspace/wiki/`（含 `_index.md`、`_recent.md`、`projects/`）对应 Compiled Wiki[^src-2]。

**混合架构**：与 Karpathy 的纯三层模型不同，作者在 raw 和 wiki 之间插入了 Memory MCP（Mem0 + pgvector）作为向量检索层，使 RAG 式检索与 wiki 浏览共存于同一系统[^src-3]。

**操作方式**：`/kb-compile blog` 可编译特定项目，`/kb-compile --all` 全量更新，`/kb-compile --lint` 执行矛盾检测、链接检查和过期文章识别[^src-4]。编译产出的 `_index.md` 包含 30 个项目的全景地图，新会话启动时首先阅读此文件即可掌握全局状态[^src-5]。

**已知局限**：需手动触发命令、跨项目主题文章尚未构建、Lint 自动化尚未实现。作者坦承仍处于「hacky collection of scripts」阶段[^src-6]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L93 -- "既存のメモリ基盤の上に wiki 層を載せる形で /kb-compile というカスタムコマンドを作り、いま試しているところです"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L97 -- "workspace/ ├── knowledge/ # Raw — 日報、リサーチ、セッションログ ├── wiki/ # Compiled Wiki"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L99 -- "自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L101 -- "/kb-compile blog のように特定のプロジェクトだけをコンパイルすることも、/kb-compile --all で全体を一括更新することもできます。Karpathy 氏の Lint に相当する --lint オプションもあって"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L107 -- "30 プロジェクトの全体地図がひとつのファイルにまとまっていて、新しいセッションを始めるときにまずこれを見ると"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/developersio-jp-pattern/text.txt` -- L109 -- "Karpathy 氏と同じく「hacky collection of scripts」の域を出ていないのが正直なところです"
