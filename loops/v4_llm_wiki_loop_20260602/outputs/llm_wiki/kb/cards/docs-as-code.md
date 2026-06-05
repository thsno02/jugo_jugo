---
id: docs-as-code
title: Docs as Code 理念
status: accepted
card_type: concept
tags: [documentation, development-workflow, toolchain, write-the-docs]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
justification: ../justification/docs-as-code.md
canonical_concept: docs-as-code
aliases: [Documentation as Code, 文档即代码, docs like code]
summary: >-
  docs-as-code（Documentation as Code / 文档即代码 / docs like code）指一种文档哲学：用与代码相同的五类工具（Issue Tracker、版本控制、纯文本标记、代码评审、自动化测试）和相同的开发工作流来编写文档
related:
  - wiki-as-git-repo
  - documentation-merge-gate
  - documentation-shared-ownership
---

Docs as Code（Documentation as Code）是一种文档哲学，其核心主张是：**文档应使用与代码相同的工具来编写**[^src-1]。

该理念明确列举了五类工具支柱：

1. **Issue Tracker**（问题追踪器）
2. **Version Control / Git**（版本控制）
3. **Plain Text Markup**（纯文本标记语言，如 Markdown、reStructuredText、Asciidoc）
4. **Code Reviews**（代码评审）
5. **Automated Tests**（自动化测试）[^src-2]

采用 Docs as Code 意味着遵循与开发团队相同的工作流，并将文档工作整合到产品团队中[^src-3]。该理念在软件行业已被广泛实践，同时正在技术写作社区中获得更多采纳[^src-4]。开源工具链 docToolchain 是该方法的一个具体实现[^src-5]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "Docs as Code" L12 -- "Documentation as Code ( Docs as Code ) refers to a philosophy that you should be writing documentation with the same tools as code"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "tool list" L13-21 -- "Issue Trackers / Version Control (Git) / Plain Text Markup (Markdown, reStructuredText, Asciidoc) / Code Reviews / Automated Tests"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "workflows" L22 -- "This means following the same workflows as development teams, and being integrated in the product team."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "adoption" L87 -- "The Docs as Code concepts are widely practiced in the software industry, and are gaining adoption in the writing community."
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "toolchain" L41-43 -- "there is an open source tool-chain which shows how the docs-as-code approach can be implemented / docToolchain"
