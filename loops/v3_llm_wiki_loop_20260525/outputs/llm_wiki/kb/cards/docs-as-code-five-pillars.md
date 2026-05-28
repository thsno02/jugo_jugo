---
id: docs-as-code-five-pillars
title: Docs as Code 的五条工程工具栈定义
status: accepted
card_type: concept
tags: [#docs-as-code, #documentation, #write-the-docs, #toolchain]
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-28T12:30:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
provenance_card: ../provenance/docs-as-code-five-pillars.md
aliases: ["Docs as Code 五大支柱", "Documentation as Code"]
related: [docs-as-code-merge-block-incentive, wicer-cegar-compile-evaluate-refine]
---

Write the Docs 社区把 "Docs as Code"（Documentation as Code）定义为**一种文档应当与代码使用同一套工具链的工作哲学**[^src1]。这套哲学不只是"用 git 管 markdown"，它在原始定义里被拆成五条具体工具栈支柱[^src2]：

1. **Issue Trackers**——文档的需求、缺陷、改进都进同一个 issue 系统，而不是独立的"文档 backlog"。
2. **Version Control (Git)**——文档纳入版本控制，跟代码同源。
3. **Plain Text Markup (Markdown, reStructuredText, Asciidoc)**——文档以纯文本标记格式存储，不依赖 Word/Confluence 这类二进制或专有平台。
4. **Code Reviews**——文档改动走 PR / merge request，由人 review；既审内容也审格式。
5. **Automated Tests**——文档纳入 CI 自动测试（链接检查、构建、风格 lint、示例可执行性等）。

**含义不只是"工具"，更是"流程与文化"：**

> "This means following the same workflows as development teams, and being integrated in the product team. It enables a culture where writers and developers both feel ownership of documentation, and work together to make it as good as possible."[^src3]

也就是说，五条支柱合在一起的本质是把"文档"从一个独立交付物变成"开发流程的副产物"——它跟代码同 repo、同 PR、同 review、同 CI；维护者可以是工程师也可以是 writer，不再是分而治之的"扔过墙"模式。

**典型收益（社区列出的三条）：**

- writer 和开发团队的整合更紧密；
- 开发者经常会顺手写出第一稿文档；
- 可以**在 PR 没有附带文档时拒绝合并**，从机制上奖励"功能新鲜时把文档写出来"[^v3-1]。

**边界与误用：**

- "Docs as Code" 不等于"所有文档都必须放 git 里"——更准确地说是"和代码同源、同工具"。营销文案、法律文档不一定适用；
- "Markdown 就是 Docs as Code"是常见的概念稀释——五大支柱里 Markdown 只是工具维度，缺了 review / CI / issue 这几条，纯 Markdown 项目仍可能复刻"Word 时代"的痛点；
- 这套哲学是面向"开发者文档 / 技术文档"的，对面向终端用户的产品文档、tutorial、视频脚本，需要补充内容设计、本地化等流程，不能 1:1 套用。
- LLM 时代的"知识库 / wiki" 也可以套这五条——WiCER 的诊断重写循环本质上是把"评测信号"接进 CI 风格的合并门控[^v3-2]。

## Footnotes

[^v3-1]: [docs-as-code-merge-block-incentive](docs-as-code-merge-block-incentive.md) — 第三条收益的展开：把"无文档不合并"作为 CI 硬约束
[^v3-2]: [wicer-cegar-compile-evaluate-refine](wicer-cegar-compile-evaluate-refine.md) — LLM-wiki 编译的 CEGAR 闭环，可视作把 Docs as Code 的 "automated tests" 支柱挪到 LLM 编译器后侧
[^src1]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` 行 11："Documentation as Code (Docs as Code) refers to a philosophy that you should be writing documentation with the same tools as code"。Eric Holscher 与 Write the Docs 社区原文，整页参见行 7–32
[^src2]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` 行 13–21（五条支柱明确列举）。社区参考三本书与 docToolchain 工具链见行 33–43
[^src3]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` 行 23（关于"文化与所有权"的引文）；三条收益列在行 25–31
