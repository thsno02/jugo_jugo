---
id: agents-md-as-schema-layer
title: AGENTS.md 充当 LLM Wiki 的 schema 层——让多轮 ingest 不发散
status: accepted
card_type: concept
tags: [#llm-wiki, #agents-md, #schema, #convention, #predictability]
created_time: 2026-05-26T11:21:00+08:00
edited_time: 2026-05-28T10:00:00+08:00
edited_entity: llm
source_ids: [complete-tech-live-frontier]
provenance_card: ../provenance/agents-md-as-schema-layer.md
aliases: ["AGENTS.md schema", "wiki schema config"]
related: [beyond-the-token-bottleneck-llm-wiki-case-study, llm-knowledge-base-five-stage-workflow, robin-cartier-schema-as-product-doc, llm-wiki-schema-is-most-important, aillm-wiki-schema-as-bottleneck, anthemcreation-llm-wiki-three-layer-architecture]
---

CompleteTech 的 BTTB 案例[^v3-1]把 Karpathy LLM Wiki 三层架构里那一层最容易被忽视的 `schema` 显式落地为一个 `AGENTS.md` 文件[^v2-1]。这张卡专门讨论"schema 层"的角色，因为它是决定 LLM 多轮写入是否会**发散成 slop** 的设计杠杆。

**`AGENTS.md` 在 BTTB 里承载的内容：**

> "AGENTS.md — the schema. Page types, linking conventions, depth standards, what counts as 'done' for each page class. This is what makes the LLM's output predictable and the wiki maintainable across many ingest passes."[^src1]

四个具体配置维度：

- **Page types**：声明 wiki 中允许出现的页面类别（如 source summary / concept / entity / MoC / analysis），LLM 写新页时必须落到某一类；
- **Linking conventions**：跨页 link 怎么写、双向 link 是否必须、是否允许 wiki-link `[[...]]` + markdown link 双书写；
- **Depth standards**：每类页面的最小 / 最大长度、必含字段、必引 raw；
- **Definition of "done"**：每类 page 在什么条件下可以从 draft 转 published（如：引用 ≥ 2 个 raw、被至少一个 MoC link）。

**为什么把这些写进配置文件而不是 prompt：**

- prompt 在每次调用都重新构造，标准容易跨 session 漂移；
- `AGENTS.md` 是仓库内的不可变约定，多个 ingest workflow 共享同一份；
- 它可以被 `audit` workflow 反向校验（`schema-self-audit`）——schema 本身也有人来 lint 它[^src2]；
- LLM 在执行任何写动作前可以先 grep `AGENTS.md` 拿到本类 page 的"完成"判据，避免靠常识猜。

**实践含义（操作规则）：**

- 在 LLM Wiki 项目里**先固定 schema 再开始 ingest**——否则前 10 篇 raw 的写入风格会"污染"后续；
- schema 文件应该被 LLM 视作高优先级输入；可以在 `AGENTS.md` 顶部直接写"This file is the schema. Read it before any wiki write action."；
- 改 schema 时把"已有 page 不符合新 schema 的列表"当 follow-up 任务，而不是默默让旧页发散；
- 与 `idea-file-as-agent-era-artifact` 卡[^v3-2]呼应：idea-file 是 LLM 阅读的对象，schema 是 LLM 写作的合同。

**边界与误用：**

- schema 太严会让小 raw 难写（每个 page 都要凑齐 5 个必填字段），降低 ingest 吞吐；
- schema 太宽则形同虚设，回到"靠 prompt 撑住一切"的状态——不可持续；
- 在没有 `audit / lint` 这条 workflow 之前，schema 是死的——它需要执行层把它当真。

## Footnotes

[^src1]: `data/raw/webpage/complete-tech-live-frontier/text.txt` 行 124–126 — "AGENTS.md — the schema. Page types, linking conventions, depth standards, what counts as 'done' for each page class. This is what makes the LLM's output predictable and the wiki maintainable across many ingest passes."
[^src2]: `data/raw/webpage/complete-tech-live-frontier/text.txt` 行 128 — workflows audit 列表中包含 `schema-self-audit`，说明 schema 本身也是 audit 对象。
[^v3-1]: [beyond-the-token-bottleneck-llm-wiki-case-study](beyond-the-token-bottleneck-llm-wiki-case-study.md) — 本卡讨论的 `AGENTS.md` schema 实例来自 BTTB 案例。
[^v3-2]: [idea-file-as-agent-era-artifact](idea-file-as-agent-era-artifact.md) — schema 是写作合同、idea-file 是阅读对象，两者是对偶角色。
[^v2-1]: v2 anchor [llm-wiki-schema-configuration-document](../../../../../v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md) — 本卡是该卡的 delta：把"schema = 配置文档"具体化到 `AGENTS.md`，并补出 BTTB 的四个配置维度与 `schema-self-audit` workflow。
