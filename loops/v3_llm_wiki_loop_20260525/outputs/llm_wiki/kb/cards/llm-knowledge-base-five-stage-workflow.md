---
id: llm-knowledge-base-five-stage-workflow
title: LLM 维护的知识库五阶段工作流
status: accepted
card_type: mechanism
tags: [#llm-wiki, #workflow, #knowledge-system, #operations]
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-28T11:32:00+08:00
edited_entity: llm
source_ids: [karpathy-x-launch-post]
provenance_card: ../provenance/llm-knowledge-base-five-stage-workflow.md
aliases: ["LLM KB 工作流", "Karpathy wiki 流水线"]
related: [obsidian-as-ide-llm-as-programmer, auto-index-replaces-rag-at-small-scale, file-outputs-back-as-compounding-loop]
---

Karpathy 把自己个人的"LLM 维护知识库"描述成五个先后衔接的操作[^src1]，而不是一步到位的"RAG"。每一阶段都有自己独立的产物和独立的 LLM 任务。正是因为五个阶段被分开处理，这套 wiki 才能在不断增长的同时不退化成原始文件堆。

- **Ingest（导入）。** 源文档（文章、论文、仓库、数据集、图片）先索引进一个 `raw/` 目录，然后由 LLM 增量地"编译"出一份 wiki —— 也就是一组 `.md` 文件：摘要、反向链接、概念分类、为每个概念写好的小文章。网页通过 Web Clipper 进入；相关图片通过一个快捷键批量下载到本地，方便 LLM 引用。
- **IDE（编辑器）。** 作者在 Obsidian 里同时打开三层视图：原始数据、编译出的 wiki、衍生的可视化。IDE 是人的"读"界面；几乎所有的"写"都是 LLM 完成的[^v3-1]。
- **Q&A（问答）。** 当 wiki 大到一定规模（示例：~100 篇文章 / ~400K 词）时，LLM 通过读取它自己维护的索引文件和每篇文档的简短摘要来回答复杂问题；在这种"小规模"下，这套机制替代了一个独立的 RAG 层[^v3-2]。
- **Output（输出）。** 答案不是终端里的纯文本，而是被渲染成 markdown 文件、Marp 幻灯或 matplotlib 图片，再回到 Obsidian 里查看。输出本身就是产物[^v3-3]。
- **Linting（健康检查）。** 周期性的 LLM "health check" 用来发现数据不一致、补全缺失字段（必要时配合 web search）、提示新文章候选、暴露有意思的跨链接。Linting 是"语料增长后不腐烂"的关键。

阶段顺序背后的逻辑：ingest 让这个 wiki 值得被查询；IDE 让人愿意继续维护它；Q&A 把 wiki 升级成研究工具；output 的多形态让 Q&A 可被复用；linting 是防止整体腐化的兜底。

边界：这是单用户、研究规模的设计，不是团队或产品规范。Q&A 阶段不需要显式 RAG 的判断只在"this ~small scale"成立；至于真正大规模，作者本人指向"合成数据 + 微调"作为后续方向。

## Footnotes

[^src1]: `data/raw/webpage/karpathy-x-launch-post/text.txt` — JSON 指针 `$.tweet.quote.text`，章节 "Data ingest:"、"IDE:"、"Q&A:"、"Output:"、"Linting:" 给出五阶段定义。
[^v3-1]: [obsidian-as-ide-llm-as-programmer](obsidian-as-ide-llm-as-programmer.md) — Obsidian 作为 IDE / LLM 作为程序员的展开。
[^v3-2]: [auto-index-replaces-rag-at-small-scale](auto-index-replaces-rag-at-small-scale.md) — Q&A 阶段"小规模下索引替代 RAG"规则的本卡。
[^v3-3]: [file-outputs-back-as-compounding-loop](file-outputs-back-as-compounding-loop.md) — Output 被回写形成复利循环的本卡。
