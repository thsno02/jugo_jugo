---
id: anthemcreation-llm-wiki-setup-cost-envelope
title: LLM wiki 个人版的 5 分钟搭建路径与成本上限
status: accepted
card_type: operational_rule
tags: [#llm-wiki, #setup, #cost, #obsidian, #claude]
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-28T10:44:00+08:00
edited_entity: llm
source_ids: [anthemcreation-fr-guide]
provenance_card: ../provenance/anthemcreation-llm-wiki-setup-cost-envelope.md
aliases: [LLM wiki setup, Karpathy wiki cost, Obsidian Claude workflow]
related: [anthemcreation-llm-wiki-three-layer-architecture, karpathy-llm-wiki-obsidian-plugin-overview, beyond-the-token-bottleneck-llm-wiki-case-study, my-llm-wiki-three-layer-implementation, robin-cartier-scale-ceiling]
---

法语指南给出的 LLM wiki 落地路径异乎寻常的轻：5 分钟、零开发能力、个位数欧元，就能跑起来一个 Karpathy 风格的个人知识基。把这套数字记牢有助于劝退两类常见的伪需求："要先搭一个 RAG 后端"和"要先选一个 vector DB"。

**最小可行流程（5 步，原文 ordered list）**：

1. 把 Karpathy 的原始 Gist 复制到一个 LLM agent（Claude / OpenAI Codex / Grok 都行）；
2. 在本地新建一个空目录，这个目录就是你的 wiki；
3. 用 Obsidian 把这个目录开成一个新 vault；
4. 把第一批原始源放进**独立的子目录**（建议 `/sources/`），不要和 wiki 文件混在一起；
5. 让 LLM ingest 第一篇源，生成 index、entity pages 与互相链接的摘要。

工具替换余地：Obsidian 不强制——VS Code + Markdown Preview Enhanced、Logseq 都能用，关键是文件保持 flat markdown，方便 LLM 读写[^src1]。

**成本封顶（原文成本表）**[^src3]：

| 配置 | Setup 成本 | 维护成本 |
| --- | --- | --- |
| Obsidian + Llama 3（开源 LLM） | 免费 | 0 €/月 |
| Obsidian + Claude API | 免费 | **~0.01–0.10 € / 篇 ingest** |
| 100 篇文档的 Claude wiki | **< 10 €** | 增量 ingest，成本低 |

读出三条操作信号：

1. **个人版可以"先用 Claude API 起步，省下迁移成本后再换 Llama"**——上限 10€ 量级，迁移风险低；
2. **每篇 ingest 成本是常量 0.01–0.10€ 量级**，因此 wiki 不会因为规模 doubling 就成本爆炸，只随文档数量线性；
3. **零循环费用版本可达**——Obsidian + 本地 Llama 3 在第一档表里直接写 "0 €/mois"，意味着隐私场景或长期持有者可以做到完全自费 = 0。

**风险与限制（同篇 FAQ）**：

- 个人量级 10–几百篇之后，跨页链接维护会变贵，应考虑切换或叠加 vector search[^2]；
- 弱 LLM 会把源中的错误悄无声息地写进 wiki，因此**前几周建议人工抽查关键页面**；
- Karpathy 没有发布官方实现，落地仍需基于 Gist 手动配置（这正是这套教程能存在的原因）。

把这套数字与"三层架构"（见 `anthemcreation-llm-wiki-three-layer-architecture`）合在一起：你只需要"一个空文件夹 + 一份 agents.md + 一份 Gist 提示"，技术栈就完整了；剩下的工作是反复 ingest，让 wiki 自己 compound。

## References

- Anthem Création 法语博客 §"Configurer votre LLM wiki" 第 114–126 行（五步流程）、§"Coûts réels du système" 第 128–137 行（成本表）、FAQ §"Quelles sont les limites" 第 208–210 行（限制）。本卡的步骤、价格区间与风险条款均出自这些段落。

## Footnotes

[^1]: `data/raw/webpage/anthemcreation-fr-guide/text.txt` 第 126 行：
    > "Obsidian n'est pas obligatoire, mais il est recommandé par Karpathy pour son affichage graphique des liens. Des alternatives viables existent : VS Code avec une extension Markdown Preview Enhanced, ou Logseq qui gère aussi les backlinks bidirectionnels. L'essentiel reste que vos fichiers soient en markdown plat, compatible avec n'importe quel éditeur."
[^2]: 同文件第 210 行：
    > "Le système excelle à échelle personnelle, typiquement de 10 à quelques centaines de documents. Au-delà, la gestion des interliens peut devenir coûteuse en tokens et une vector search devient plus adaptée."
[^3]: 同文件第 130–136 行（成本表）：
    > "Obsidian + LLM open source (Llama 3) Gratuit 0 €/mois / Obsidian + Claude API Gratuit ~0,01 à 0,10 € par doc ingéré / Wiki de 100 documents (Claude) Moins de 10 € Faible (ingestions incrémentales)"
