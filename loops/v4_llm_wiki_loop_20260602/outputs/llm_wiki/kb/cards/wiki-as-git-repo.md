---
id: wiki-as-git-repo
title: Wiki 即 Git 仓库
status: accepted
card_type: source_claim
tags: [llm-wiki, git, version-control, markdown]
created_time: 2026-06-05T00:00:00+08:00
edited_time: 2026-06-05T00:00:00+08:00
edited_entity: llm
source_ids: [karpathy-gist-llm-wiki]
justification: ../justification/wiki-as-git-repo.md
canonical_concept: wiki-as-git-repo
aliases: [Git 仓库, wiki as git repo, markdown 文件, 版本控制]
summary: >-
  wiki-as-git-repo（Git 仓库 / wiki as git repo / markdown 文件 / 版本控制）指 LLM Wiki
  选择纯 markdown 文件作为 wiki 层意味着 wiki 即 git 仓库，免费获得版本历史、分支和协作能力
related: [docs-as-code, three-layer-architecture]
---

LLM Wiki 的 wiki 层由纯 markdown 文件组成，这一设计选择带来一个重要推论：**wiki 就是一个 git 仓库**。用户免费获得版本历史、分支和协作能力[^src-1]。

这意味着 wiki 的每次变更都可追溯，支持回滚到任意历史版本，也使多人协作成为可能——与三层架构中 wiki 层的 markdown 文件设计一脉相承[^card-1]。

值得注意的是，Write the Docs 社区的 Docs as Code 理念从完全不同的出发点——文档应使用与代码相同的工具——独立将版本控制列为文档的五大工具支柱之一，两个社区在"知识制品属于 git"这一模式上形成了跨领域的收敛[^card-2]。

## Footnotes

[^src-1]: `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt` -- "Tips and tricks" P6 -- "The wiki is just a git repo of markdown files. You get version history, branching, and collaboration for free."
[^card-1]: [三层架构](three-layer-architecture.md) -- Wiki 层选择 markdown 文件使 git 版本控制成为自然结果
[^card-2]: [Docs as Code 理念](docs-as-code.md) -- 本卡从 LLM Wiki 的 markdown 存储选择推导出 wiki = git repo，该卡从技术写作社区的工具哲学独立主张版本控制是文档的五大工具支柱之一
