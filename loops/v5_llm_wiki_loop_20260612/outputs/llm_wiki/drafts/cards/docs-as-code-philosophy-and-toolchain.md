---
id: docs-as-code-philosophy-and-toolchain
title: Docs as Code 理念与核心工具链
status: draft
card_type: concept-definition
tags: [documentation-philosophy, developer-workflow, toolchain]
created_time: 2026-06-12T18:00:00+08:00
edited_time: 2026-06-12T18:00:00+08:00
edited_entity: llm
source_ids: [writethedocs-docs-as-code]
evidence_basis: documentation
justification: ../justification/docs-as-code-philosophy-and-toolchain.md
canonical_concept: docs-as-code-philosophy-and-toolchain
aliases: [Docs as Code, Documentation as Code, docs-as-code, docs like code]
summary: >-
  Docs as Code (Documentation as Code) 是一种用与代码相同工具编写文档的哲学。核心工具链包括 Issue Trackers、Version Control (Git)、Plain Text Markup (Markdown, reStructuredText, Asciidoc)、Code Reviews、Automated Tests。遵循开发团队工作流，整合进产品团队，营造 writers 和 developers 共同拥有文档所有权的文化。
related: [docs-as-code-adoption-benefits]
---

Docs as Code（Documentation as Code）是一种文档编写哲学，主张使用与代码开发相同的工具和工作流来编写文档 [^src-1]。

其核心工具链包括五个要素 [^src-1]：

1. **Issue Trackers** — 用于跟踪文档任务与问题
2. **Version Control (Git)** — 对文档实施版本控制
3. **Plain Text Markup** — 使用 Markdown、reStructuredText、Asciidoc 等纯文本标记语言
4. **Code Reviews** — 文档变更经过代码审查流程
5. **Automated Tests** — 对文档执行自动化测试

该方法的文化目标在于：遵循开发团队相同的工作流，将文档工作整合进产品团队，使 writers 和 developers 双方都对文档产生所有权意识并协作提升其质量 [^src-1]。

[^src-1]: `data/raw/webpage/writethedocs-docs-as-code/markdown.md` -- "Docs as Code" P1 -- "Documentation as Code (Docs as Code) refers to a philosophy that you should be writing documentation with the same tools as code"
