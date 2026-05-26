---
schema: comparison_provenance.v3
draft_card: ../cards/agents-md-as-schema-layer.md
draft_provenance: ../provenance/agents-md-as-schema-layer.md
similarity_result: ../similarity/agents-md-as-schema-layer.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.25
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-wiki-layer-generated-markdown-directory
    card_path: llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md
    score: 0.1765
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:33:00+08:00
edited_time: 2026-05-26T12:33:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-schema-configuration-document` 与 draft **真共享主题**：两者都讲"schema 层是什么、起什么作用"。

- v2 卡片由 Karpathy gist 第 33 行抽取，statement 是 schema 是配置文档，告诉 LLM wiki 结构 / 约定 / 摄取/查询/维护工作流。
- 本 draft 由 CompleteTech "Beyond the Token Bottleneck" 案例文章抽取，把 schema 这一抽象层落地为 `AGENTS.md` 文件，并列出四个具体配置维度（page types / linking conventions / depth standards / definition of done）。

共享 token `llm / schema / wiki / 的` 是高语义重合的体现，不是 token 误中。

top 2 `llm-wiki-three-layer-architecture` 是 schema 所属的三层架构卡，邻接相关；top 3 `llm-wiki-wiki-layer-generated-markdown-directory` 是 wiki 层（不是 schema 层），与 draft 关系弱。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 来源 Karpathy gist 第 33 行；draft 来源 CompleteTech BTTB 案例文章第 124–128 行（一个独立实践者的同主题陈述）。
- **覆盖维度（draft 更具体）**：v2 卡片只定义"schema 是配置文档"这一抽象事实；draft 给出 (a) 文件名建议（`AGENTS.md`）、(b) 四类配置内容、(c) `schema-self-audit` 作为审计 workflow 的一部分、(d) "为什么写进配置而不是 prompt"四条工程理由、(e) schema 的生命周期管理（修改时把不符合的 page 当 follow-up）。
- **决策粒度不同**：v2 卡片是"定义级"知识，draft 是"实施级"操作规则。
- **scope 不同**：v2 scope 仅限 Karpathy gist 对 schema 层的定义；draft scope 是"一个具体实践者对 schema 层的落地与边界"。
- 不是 v2 卡片的扩展，也不是同主题不同视角——是**同概念、不同源、更具体的实施级补强**。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 卡片故意限定在 Karpathy gist 一手来源；把 CompleteTech 实施细节合并进去会破坏 v2 卡片的"single-source"边界，也会让 v2 卡片从"定义级"漂移到"实施级"。
- 不是 `new_card`：核心概念（schema 是配置文档）与 v2 完全一致，独立成卡会形成两张几乎平行的 schema 概念卡。
- 不是 `duplicate_skip`：draft 带来的是 (i) 文件名 AGENTS.md 的命名约定、(ii) 四个配置维度的清单、(iii) `schema-self-audit` 工作流名称——这些是 v2 卡片当前 References 没有列出的新出处证据，应该反向链接进 v2 卡 provenance。
- 不是 `revise_before_gate`：draft 证据扎实、scope 清晰，边界（schema 太严 / 太宽 / 无 audit 则死）也都标注了。

正确决定是 `provenance_delta`：把这条 draft 作为 v2 schema 卡的实施级二手来源补强；audit 阶段决定要不要在 v2 卡 References 段追加 CompleteTech 引文。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：在 fusion/audit 阶段把 CompleteTech "AGENTS.md — the schema ..."一段作为 v2 `llm-wiki-schema-configuration-document` 卡的实施级二手出处补充；可考虑把"AGENTS.md 四个配置维度"独立成子卡（concept of schema → child: schema 配置维度），但默认本 draft 不直接写入 v2 卡 body。

## 5. 备注

- 本 draft 提到的 `idea-file-as-agent-era-artifact` 是 v2 已有卡片，但不在本 batch 的 similarity top-3 中——comparison 阶段无法对它进行评估；若 audit 阶段补建 related 链接需要另起评估。
- draft 自身预测的 `AGENTS.md / GEMINI.md / CLAUDE.md / spec-driven dev` 主题在 v2 当前 15 张卡中均不存在；只有 schema 概念卡是 v2 当前唯一可关联对象。
