---
id: morishige-kb-compile-mem0-overlay
title: 在 Mem0 + pgvector 之上叠 LLM Wiki：森茂的 /kb-compile 落地实践
status: accepted
card_type: example_pattern
tags: [#llm-wiki, #claude-code, #mem0, #practice]
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-28T11:50:00+08:00
edited_entity: llm
source_ids: [developersio-jp-pattern]
provenance_card: ../provenance/morishige-kb-compile-mem0-overlay.md
aliases: ["/kb-compile", "Karpathy pattern 实战", "Mem0 + wiki"]
related: [karpathy-llm-kb-three-layer-arch, karpathy-llm-kb-three-operations, mem0-extract-update-pipeline, file-outputs-back-as-compounding-loop, beyond-the-token-bottleneck-llm-wiki-case-study, my-llm-wiki-three-layer-implementation]
---

Classmethod 工程师森茂洋的实践提供了一个值得记住的 *retrofit* 模式：**在已经运行的 Mem0 + pgvector "记忆 / 检索"基础设施之上，再叠一层 LLM Wiki，而不是推倒重来**。这正面回答了一个普遍的工程顾虑——已经投入大量精力做了 RAG/Memory 的人，要不要为了 Karpathy 模式重建一切。

具体做法：

- **保留 Mem0 + pgvector 作为检索层**：用于 ad-hoc 查询、跨会话的 fact 抽取、向量检索。这一层不写人类可读的结构化文档。
- **新增 `workspace/wiki/` 作为编译产物**[^src1]：与 `workspace/knowledge/` raw 并列[^v3-1]，再加上各级 `CLAUDE.md` 作为 schema[^src2]。
- **新增 `/kb-compile` 自定义命令**[^src3]：对应 Karpathy 的 Ingest 操作[^v3-2]。支持 `/kb-compile blog` 只编译某项目，`/kb-compile --all` 全量更新，`/kb-compile --lint` 做 Karpathy 意义下的 Lint（矛盾检测、链断、过时记录）。
- **`_index.md` + `_recent.md` 两份索引**：前者是 30+ 项目的全景地图（表格 + frontmatter + backlinks），新会话开场只读这一份就能把握"现在每个项目走到哪"。

为什么这套混合架构在工程上合理：

1. **RAG 与 wiki 的使用场景互补**。森茂原话："アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利"[^src4]——前者像 Google，后者像目录索引。两个都保留比二选一更好。
2. **wiki 层让人类回得来**。Mem0 的 fact 是 LLM 给 LLM 看的；wiki 的 markdown 让人类（或新会话的 LLM）能从一个稳定入口快速 onboarding。
3. **Lint 在自定义命令里就能开始做**。即便没有自动化调度，`/kb-compile --lint` 至少给了一个"主动唤起的健康检查"动作；森茂坦承自动化还没完成，但这已经是可工作的最简形态。

可被复用的几个判断：

- **`_index.md` 作为入会议程**：每个新会话第一件事是读全景地图，比"让 LLM 自己 grep"更可靠。
- **手动唤起 > 自动隐式**：现阶段"hacky"是常态，依赖自动调度反而会让维护成本爆炸；自定义命令式 ingest 在能落地的范围内最实用。
- **跨项目 topic 文章可以晚做**：森茂明确说自己还没处理"跨项目的 topic 文章"，意味着 single-project wiki 已经能跑起来，topic 层可放在第二阶段。

边界与误读：

- 这是一份**个人工作流报告**，不是企业级或团队规模的设计；30 项目都是个人侧的活跃项目。
- Karpathy 与森茂都强调这仍是 "hacky collection of scripts"；不要把 `/kb-compile` 当成可以照抄上线的产品级方案。
- "Mem0 + wiki 互补"是经验判断，没有跑过 A/B 测试；引用应注明。

## References

- 整段实践见 §"自分は Claude Code でこう組み込んでいる"（`data/raw/webpage/developersio-jp-pattern/text.txt`，第 85–111 行）。
- 与 RAG 的折衷见 §"RAG とどう違うのか"末段（同文件 L83）。
- "hacky collection of scripts" 自评见 L66、L109、L121。

## Footnotes

- L97：目录结构 *"workspace/ ├── knowledge/ ├── wiki/ │ ├── _index.md │ ├── _recent.md │ └── projects/"*。
- L99：*"workspace/knowledge/ が Raw sources、各ディレクトリに置いた CLAUDE.md が Schema、 workspace/wiki/ が Compiled Wiki に相当します。"*
- L101：*"/kb-compile blog のように特定のプロジェクトだけをコンパイルすることも、 /kb-compile --all で全体を一括更新することもできます。Karpathy 氏の Lint に相当する --lint オプションもあって、矛盾検出やリンク切れチェック、古い記事の検出ができるようにしています。"*
- L83：*"アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利"*。
