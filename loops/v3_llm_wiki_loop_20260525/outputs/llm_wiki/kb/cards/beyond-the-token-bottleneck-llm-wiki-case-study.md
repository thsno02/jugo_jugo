---
id: beyond-the-token-bottleneck-llm-wiki-case-study
title: Beyond the Token Bottleneck——120 页 Obsidian 实现 Karpathy LLM Wiki 模式的案例
status: accepted
card_type: example_pattern
tags: [#llm-wiki, #obsidian, #case-study, #completetech, #latent-reasoning]
created_time: 2026-05-26T11:20:00+08:00
edited_time: 2026-05-27T14:34:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
provenance_card: ../provenance/beyond-the-token-bottleneck-llm-wiki-case-study.md
aliases: ["BTTB case study", "CompleteTech LLM Wiki implementation"]
related: [llm-knowledge-base-five-stage-workflow, agents-md-as-schema-layer, karpathy-llm-wiki-obsidian-plugin-overview, my-llm-wiki-three-layer-implementation, anthemcreation-llm-wiki-setup-cost-envelope, morishige-kb-compile-mem0-overlay]
---

CompleteTech LLC 把 Karpathy 的 LLM Wiki 模式应用到一个真实研究前沿（latent-space reasoning + inter-agent latent communication），开源仓库 `github.com/CompleteTech-LLC-AI-Research/beyond-the-token-bottleneck`（镜像 `ctech.llc/bttb`）。这是一份**有规模数据的生产参考实现**，对验证"模式是否真的能压住 bookkeeping 成本"很有意义。

**规模事实（2026/04/06 Field Note）：**

- 27 个源（26 篇论文 + 1 个开源项目，Dec 2022 – Apr 2026）；
- 120+ 页 wiki：source summaries、concept pages、13 个研究组的 entity profiles、9 个 Maps of Content (MoC)、9 个 analysis / synthesis 页、overview、change log；
- **1400+ internal links** 把所有页面织在一起；
- 仓库 split-license：代码 Apache 2.0，内容 CC-BY 4.0。

**架构上如何映射 Karpathy 三层（raw / wiki / schema）：**

- `raw/` — 26 篇源 PDF，外加 per-paper provenance index、ingest checklist、bulk arXiv downloader。**惯例上只读**，LLM 不编辑这一层；
- `wiki/` — 120+ 页 LLM 生成内容；
- `AGENTS.md` — **schema 层**：page types、linking conventions、depth standards、每类 page 的"完成"定义。这是让 LLM 多轮 ingest 之间输出保持可预测、wiki 可维护的关键；
- `workflows/` — maintainer playbooks：create（ingest / batch-ingest / synthesize）、enrich、audit（gap-analysis / verification / lint / plugin-audit / schema-self-audit）、query、meta；决策树在 `workflows/README.md`。

**核心循环——ingest 一篇论文的副作用：**

> "A new paper drops into raw/pdf/ ; the LLM reads it and writes a source summary against the schema; entities and concepts get extracted and given their own pages or extended on existing ones; cross-references get threaded through every page that mentions the new work; Maps of Content get updated so the new piece sits in a guided reading path, not just an orphan node. One paper, ten to fifteen page touches, hundreds of new and updated links."

也就是说：**一篇新论文 ≈ 10–15 页 touches、数百条新增 / 更新 link**——这就是 Karpathy 所说的"bookkeeping"被实际数字化后是什么样。

**作者总结的"做这件事的三个理由"：**

1. 文献变化速度超过人类策展能力；
2. 框架（如 10-level communication-depth taxonomy）只有当每个方法都被映射到它上面、并且每个方法都反向 link 到 MoC 时才有意义；
3. Karpathy 的 gist 值得有一个真实领域的生产参考实现，而不是另一个"second brain" 想象。

**对其他人复用这一模式的启示：**

- 必须先固定 schema（`AGENTS.md` 类）再 ingest，否则多轮 LLM 写出的 page 会发散；
- maintainer playbook 不是 nice-to-have——`audit` workflow（gap analysis、lint、verification、provenance、schema self-audit）是把 wiki 撑过去 100+ 页的关键；
- raw 必须只读，否则 provenance 链条断裂。

**边界：**

- 这是单团队报告，未公开 ingest 总耗时 / 成本；
- 它是面向**研究文献** 的，不是面向产品文档、代码 docs 或 PKM；要照搬到其他领域，必须重写 schema。

## References

- "Beyond the Token Bottleneck — Building Karpathy's LLM Wiki on a Live Frontier"，CompleteTech LLC, 2026-04-06：`data/raw/webpage/complete-tech-live-frontier/text.txt`，行 81–148。
- 仓库 `github.com/CompleteTech-LLC-AI-Research/beyond-the-token-bottleneck`，镜像 `ctech.llc/bttb`（行 94、150）。

## Footnotes

- 规模事实：行 90、94、122–130。
- 三层架构映射：行 120–128。
- ingest 循环原文："One paper, ten to fifteen page touches, hundreds of new and updated links."——行 130。
- Karpathy "the tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping"——行 92。
- License split：行 148。
- 三条理由：行 136–140。
