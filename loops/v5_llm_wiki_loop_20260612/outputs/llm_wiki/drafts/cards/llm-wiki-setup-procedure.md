---
id: llm-wiki-setup-procedure
title: LLM Wiki 搭建步骤
status: draft
card_type: how-to
tags: [llm-wiki, setup, obsidian, claude, tooling]
created_time: 2026-06-12T17:00:00+08:00
edited_time: 2026-06-12T17:00:00+08:00
edited_entity: llm
source_ids: [anthemcreation-en-guide]
evidence_basis: practitioner_report
justification: ../justification/llm-wiki-setup-procedure.md
canonical_concept: llm-wiki-setup-procedure
aliases: [wiki setup, initial setup, 5-minute setup]
summary: >-
  LLM wiki 搭建步骤 setup-procedure：5 分钟完成，无需开发技能。步骤：复制 Karpathy GitHub Gist → 粘贴到 LLM agent (Claude/Codex/Grok) → 创建空目录 → Obsidian 打开为 vault → 子文件夹放 raw sources → LLM 执行首次 ingestion。Obsidian 非必须，替代方案有 VS Code + Markdown Preview Enhanced、Logseq。
related: [llm-wiki-three-layer-architecture, agents-md-instruction-file, llm-wiki-cost-structure]
---

LLM wiki 初始搭建约需 5 分钟，无需高级开发技能 [^src-1]：

1. **复制 Gist**——获取 Karpathy 在 GitHub 上的原始 Gist
2. **粘贴到 LLM agent**——Claude、OpenAI Codex 或 Grok 均可
3. **创建空目录**——作为 wiki 根目录
4. **Obsidian 打开为 vault**——原生支持 wiki-style links 和连接图展示
5. **子文件夹放 raw sources**——如 `/sources/`，不与 wiki 文件混合
6. **首次 ingestion**——指示 LLM 创建初始页面：general index、entity pages、interconnected summaries

**工具选择**：Obsidian 被 Karpathy 推荐但非必须 [^src-2]。替代方案：
- VS Code + Markdown Preview Enhanced 扩展
- Logseq（支持双向 backlinks）
- 任何 flat markdown 兼容编辑器

核心要求是文件保持标准 markdown 格式，LLM 可自由读写。

[^src-1]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Setting up your LLM wiki with Claude and Obsidian" -- "The initial setup takes about 5 minutes and requires no advanced development skills."
[^src-2]: `data/raw/webpage/anthemcreation-en-guide/markdown.md` -- "Setting up your LLM wiki" -- "Obsidian is not mandatory, but it is recommended by Karpathy for its graphical display of links."
