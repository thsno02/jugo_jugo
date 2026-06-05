---
id: production-scale-wiki-reference
title: 生产级 Wiki 参考实现
status: accepted
card_type: example_pattern
tags: [llm-wiki, production, scale, evidence, CompleteTech]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
justification: ../justification/production-scale-wiki-reference.md
canonical_concept: production-scale-wiki-reference
aliases: [生产级参考实现, BTTB wiki, Beyond the Token Bottleneck, 规模参考]
summary: >-
  production-scale-wiki-reference（生产级参考实现 / BTTB wiki / Beyond the Token Bottleneck / 规模参考）
  是 Karpathy LLM Wiki 模式的首个公开生产级实现：120 页、1400+ 交叉引用、27 源、13 实体、9 MOC、9 分析页，
  带完整工作流和双许可
related: [llm-wiki-pattern, llm-wiki-v2-agentmemory]
---

CompleteTech LLC 的「Beyond the Token Bottleneck」（BTTB）是 Karpathy LLM Wiki 模式[^card-1]的一个公开生产级实现，应用于潜空间推理与跨 agent 潜通信这一研究前沿[^src-1]。

**规模指标**[^src-2]：
- 120+ 页 wiki 页面
- 1400+ 内部交叉引用
- 27 个跟踪源（26 篇论文 + 1 个开源项目，2022.12 - 2026.04）
- 13 个研究组实体档案
- 9 个 Map of Content（引导阅读路径）
- 9 个分析/综合页面

**三层架构落地**[^src-3]：raw/ 存放 26 篇 arXiv/ACL/ICML/NeurIPS 论文 PDF 及来源索引；wiki/ 存放全部生成页面；AGENTS.md 作为 schema 文件定义页面类型、链接规范和完成标准。

**许可拆分**：代码部分（工作流、脚本、schema）为 Apache 2.0，内容部分（wiki 本身）为 CC-BY 4.0[^src-4]。

该实现的价值在于：相比又一篇关于「第二大脑」的思考文章，一个带审计工作流、插件列表、许可拆分和真实研究领域的 120 页实例更有说服力[^src-5]。该实现依赖人工审计工作流和摄入检查清单来保证质量，与 LLM Wiki v2 提出的自主代理无监督维护路线形成对照[^dist-1]。

## Footnotes

[^src-1]: `data/raw/webpage/complete-tech-live-frontier/text.txt` -- 开头摘要 -- "A 120-page Obsidian research wiki on latent-space reasoning and inter-agent latent communication — built using Andrej Karpathy's LLM Wiki pattern. 27 sources, 1400+ cross-references, schema-driven ingest. Apache + CC-BY."
[^src-2]: `data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "wiki/ — 120+ pages: source summaries, concept pages, entity profiles for 13 research groups, 9 Maps of Content (guided reading paths), 9 analysis/synthesis pages, an overview, a change log. 1400+ internal links knit the whole thing together."
[^src-3]: `data/raw/webpage/complete-tech-live-frontier/text.txt` -- "How Karpathy's pattern shows up in the build" -- "raw/ — 26 source PDFs from arXiv, ACL, ICML, NeurIPS, plus a per-paper provenance index, an ingest checklist, and a bulk arXiv downloader. Read-only by convention."
[^src-4]: `data/raw/webpage/complete-tech-live-frontier/text.txt` -- 结尾 -- "The repo is split-licensed: Apache 2.0 for code (workflows, scripts, schema), CC-BY 4.0 for content (the wiki itself)."
[^src-5]: `data/raw/webpage/complete-tech-live-frontier/text.txt` -- "Why we built it" 第三点 -- "Showing what a 120-page, 1400-link, schema-disciplined implementation looks like — with audit workflows, plugin lists, license splits, and a real domain — is more useful than another think-piece about second brains."
[^card-1]: [LLM Wiki 模式](llm-wiki-pattern.md) -- 本实现遵循的核心模式
[^dist-1]: [LLM Wiki v2 社区扩展与 agentmemory 模式](llm-wiki-v2-agentmemory.md) -- 本卡展示的生产级实现依赖审计工作流和人工摄入检查清单保证 120 页规模的质量，该卡主张自主代理无人工干预维护 wiki，区分点在于规模化路径是否需要人工监督环节
