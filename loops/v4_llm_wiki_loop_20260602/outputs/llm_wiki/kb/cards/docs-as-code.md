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
related: [documentation-merge-gate, documentation-shared-ownership, wiki-as-git-repo]
---

Docs as Code（Documentation as Code）是一种文档哲学，其核心主张是：**文档应使用与代码相同的工具来编写**[^src-1]。

该理念明确列举了五类工具支柱：

1. **Issue Tracker**（问题追踪器）
2. **Version Control / Git**（版本控制）
3. **Plain Text Markup**（纯文本标记语言，如 Markdown、reStructuredText、Asciidoc）
4. **Code Reviews**（代码评审）
5. **Automated Tests**（自动化测试）[^src-2]

采用 Docs as Code 意味着遵循与开发团队相同的工作流，并将文档工作整合到产品团队中[^src-3]。该理念在软件行业已被广泛实践，同时正在技术写作社区中获得更多采纳[^src-4]。开源工具链 docToolchain 是该方法的一个具体实现[^src-5]。

值得注意的是，Karpathy 的 LLM Wiki 从完全不同的出发点——选择 markdown 文件作为 wiki 层——独立得出了 wiki = git 仓库的相同结论[^card-1]。在工作流层面，合并门禁机制是该理念在激励设计上的具体落地[^card-2]，而文档共同所有权则是该理念在文化层面的核心成果[^card-3]。

## Footnotes

[^src-1]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "Docs as Code" L12 -- "Documentation as Code ( Docs as Code ) refers to a philosophy that you should be writing documentation with the same tools as code"
[^src-2]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "tool list" L13-21 -- "Issue Trackers / Version Control (Git) / Plain Text Markup (Markdown, reStructuredText, Asciidoc) / Code Reviews / Automated Tests"
[^src-3]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "workflows" L22 -- "This means following the same workflows as development teams, and being integrated in the product team."
[^src-4]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "adoption" L87 -- "The Docs as Code concepts are widely practiced in the software industry, and are gaining adoption in the writing community."
[^src-5]: `data/raw/webpage/writethedocs-docs-as-code/text.txt` -- "toolchain" L41-43 -- "there is an open source tool-chain which shows how the docs-as-code approach can be implemented / docToolchain"
[^card-1]: [Wiki 即 Git 仓库](wiki-as-git-repo.md) -- 本卡从文档哲学角度主张版本控制是五大工具支柱之一，该卡从 LLM Wiki 架构角度独立得出 wiki = git repo 的相同结论
[^card-2]: [文档合并门禁机制](documentation-merge-gate.md) -- 本卡描述 docs-as-code 的整体哲学，该卡展开其中一项关键激励机制：未附文档则阻止合并
[^card-3]: [文档共同所有权文化](documentation-shared-ownership.md) -- 本卡描述 docs-as-code 的整体哲学，该卡展开其核心文化成果：写作者与开发者共有文档所有权
