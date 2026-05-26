---
id: docs-as-code-merge-block-incentive
title: 把"无文档不合并"写进 CI 是 Docs as Code 的关键激励机制
status: draft
card_type: operational_rule
tags: [#docs-as-code, #ci, #pull-request, #incentive, #process]
created_time: 2026-05-26T11:16:00+08:00
edited_time: 2026-05-26T11:16:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
provenance_card: ../provenance/docs-as-code-merge-block-incentive.md
aliases: ["block merging without docs", "PR docs gating"]
related: [docs-as-code-five-pillars, enterprise-llm-wiki-drift-detection-loop, llm-wiki-karpathy-lint-grounding-trail, wicer-cegar-compile-evaluate-refine, wicer-recovery-distribution-exceeds-fc-raw]
---

Write the Docs 社区列举 Docs as Code 三条收益时，第三条不是"工具更好"或"质量更高"，而是一种**激励机制**：

> "You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh."

这条规则之所以单独成卡，是因为它是 Docs as Code 工程化的"门控点"：前两条收益（writer 整合更紧密、developer 顺手写第一稿）是软现象，第三条是**硬约束**——CI 检测到 PR 改了功能代码却没改文档，pipeline failed，merge 被阻止。

**为什么"fresh"是关键词：**

- 文档腐烂的高峰期是"功能合并后 1–4 周"——那时候开发者还在脑里，但开始切下一件事；
- 如果文档可以推后写、由"文档冲刺"补齐，开发者切换上下文的成本会使内容质量退化（甚至写成事实错误）；
- 在 PR 那一刻强制写文档，可以在记忆最完整时落字——这是"fresh" 一词承担的设计意图。

**实现要点（来自社区其他演讲的归纳）：**

- CI 规则不必非黑即白——常见做法是"代码改动但文档目录没动" → 警告；"代码改动且 schema/接口变化" → 阻止；"refactor / 重命名" → 跳过；
- 阻止策略要给出"为何被拒"和"如何修复"——否则开发者会绕过（加假注释、把改动拆得很碎）；
- 与 *review* 支柱配合：文档变更也要被 review；只检测"有没有动"不能保证质量；
- 与 issue tracker 支柱配合：文档缺失生成 follow-up issue 而不只是阻止，把"债务"显性化。

**边界与误用：**

- 这条规则只在**面向开发者的内部文档**上稳定有效。面向终端用户的 release notes / tutorial 节奏不同，强制阻断可能压死功能发布；
- 把"docs 改动行数 > 0"当唯一检测项，会让开发者写空话凑数；更好的检测是"改动了哪些函数/接口 → 这些 entry 在 docs 里有没有更新引用"；
- 在 Docs as Code 不完整（缺 review、缺 issue tracker）的团队里，单独引入"merge block" 容易被视作 *官僚化* 而被绕过。

**与 LLM 写作器的衔接：**

这条规则原本针对人写文档；但同样适用于"由 LLM 维护的 wiki / 知识库"——CI 可以检查"raw 改动 vs wiki 改动"的对应关系，让 ingest 流程必须把新 raw 体现到 wiki 上才算 merge 通过。这与 Karpathy LLM Wiki 中 *linting* 阶段、`llm-wiki by nvk` 的 `/wiki:lint --fix` 想法同源。

## References

- "Docs as Code — Write the Docs"：`data/raw/webpage/writethedocs-docs-as-code/text.txt`，行 25–31。

## Footnotes

- 原话（行 31）：
  > "You can block merging of new features if they don't include documentation, which incentivizes developers to write about features while they are fresh"
- 与其他两条收益（行 27、行 29）合并在同一列表里。
