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
related: [llm-wiki-pattern, llm-wiki-v2-agentmemory, mcp-tool-skill-layering, my-llm-wiki-implementation, rag-wiki-complementarity, three-layer-architecture]
---

作者将 Karpathy 的 LLM Wiki 模式落地为 Claude Code 的自定义命令 `/kb-compile`，在已有的向量记忆基础设施上叠加了 wiki 编译层[^src-1]。

**目录映射**：`workspace/knowledge/`（日报、研究、会话日志）对应 Raw sources；各目录中的 `CLAUDE.md` 对应 Schema；`workspace/wiki/`（含 `_index.md`、`_recent.md`、`projects/`）对应 Compiled Wiki[^src-2]。

**混合架构**：与 Karpathy 的纯三层模型不同，作者在 raw 和 wiki 之间插入了 Memory MCP（Mem0 + pgvector）作为向量检索层，使 RAG 式检索与 wiki 浏览共存于同一系统[^src-3]。

**操作方式**：`/kb-compile blog` 可编译特定项目，`/kb-compile --all` 全量更新，`/kb-compile --lint` 执行矛盾检测、链接检查和过期文章识别[^src-4]。编译产出的 `_index.md` 包含 30 个项目的全景地图，新会话启动时首先阅读此文件即可掌握全局状态[^src-5]。

**已知局限**：需手动触发命令、跨项目主题文章尚未构建、Lint 自动化尚未实现。作者坦承仍处于「hacky collection of scripts」阶段[^src-6]。与 my-llm-wiki 的独立 pip 包路线相比，本实现选择在已有 Mem0 基础设施上叠加而非从零构建[^card-1]。llm-wiki-mcp 采用了更细粒度的工具/技能分离设计[^card-2]，而 LLM Wiki v2 的 agentmemory 模式则从概念层面探索了代理持续填充 wiki 的方向[^card-3]。

## Footnotes

[^card-1]: [my-llm-wiki PyPI 实现](my-llm-wiki-implementation.md) -- 本卡在 Mem0+pgvector 基础设施上叠加 wiki 层，my-llm-wiki 作为独立 pip 包从零构建（Tree-sitter + Docling + SHA256 缓存），体现「嵌入已有基础设施」与「独立工具」两种落地策略
[^card-2]: [MCP 工具与技能的双层设计](mcp-tool-skill-layering.md) -- 本卡以单一自定义命令 /kb-compile 封装全部逻辑，该卡将同类功能拆分为 4 个 MCP 工具原语 + 4 个技能编排，体现单体命令 vs 分层组合的架构选择
[^card-3]: [LLM Wiki v2 社区扩展与 agentmemory 模式](llm-wiki-v2-agentmemory.md) -- 本卡是 Claude Code agent 驱动的具体 wiki 编译实现，该卡从概念层面提出 agentmemory 持久化记忆引擎，两者分别代表工程实践与概念探索

[^src-1]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L93 -- "既存のメモリ基盤の上に wiki 層を載せる形で /kb-compile というカスタムコマンドを作り、いま試しているところです"
[^src-2]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L97 -- "workspace/ ├── knowledge/ # Raw — 日報、リサーチ、セッションログ ├── wiki/ # Compiled Wiki"
[^src-3]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L99 -- "自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて"
[^src-4]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L101 -- "/kb-compile blog のように特定のプロジェクトだけをコンパイルすることも、/kb-compile --all で全体を一括更新することもできます。Karpathy 氏の Lint に相当する --lint オプションもあって"
[^src-5]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L107 -- "30 プロジェクトの全体地図がひとつのファイルにまとまっていて、新しいセッションを始めるときにまずこれを見ると"
[^src-6]: `data/raw/webpage/developersio-jp-pattern/text.txt` -- L109 -- "Karpathy 氏と同じく「hacky collection of scripts」の域を出ていないのが正直なところです"
