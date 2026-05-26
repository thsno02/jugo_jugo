---
schema: comparison_provenance.v3
draft_card: ../cards/idea-file-as-agent-era-artifact.md
draft_provenance: ../provenance/idea-file-as-agent-era-artifact.md
similarity_result: ../similarity/idea-file-as-agent-era-artifact.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.3
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0.1818
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1429
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:22:00+08:00
edited_time: 2026-05-26T12:22:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `idea-file-abstract-vague` (0.3)**：共享 `file / idea / 的`。这是**真共享**：v2 top1 statement "idea file 被有意保持得略微抽象和模糊，因为这个想法可发展的方向很多" 与本 draft "刻意欠规格化反而是优点：它为个性化留出空间" 谈的是**同一个 Karpathy 推文事实**（`$.tweet.text` 的 "intentionally kept a little bit abstract/vague"）。
- **top 2 `idea-file-share-the-idea` (0.182)**：共享 `file / idea`。这也是**真共享**：v2 top2 statement "在 LLM agents 时代，相比分享具体代码或应用，发布者只需分享想法，接收者的 agent 可以按其具体需求定制并构建" 与本 draft 主张"分发载体从代码转移为想法、接收者的智能体补齐本地细节"完全是同一事实。
- **top 3 `llm-wiki-schema-configuration-document` (0.143)**：仅共享 `是 / 的`，主题完全无关（v2 这张谈 schema 是配置文档，与 idea file 概念不沾边）。低分误中。

## 2. draft 与候选在哪里不同

- **来源完全相同**：draft 与 v2 top1、v2 top2 全部取自同一 `$.tweet.text`（同一条 Karpathy 推文文本）。draft 不引入新来源、不增加新证据、不补新边界数值。
- **scope 与抽象层级不同**：
  - v2 top1 = 一条 known_fact，只陈述 idea file "被有意保持抽象 / 同时可在 Discussion 贡献";
  - v2 top2 = 一条 known_fact，只陈述 "分享 idea 而非 code，接收者 agent 定制构建";
  - draft = 一张 concept 卡，把这两条 known_fact **综合成"agent 时代分发载体"的概念**，并加入：
    - "分发出来的物件看起来小但做了完整 repo + 安装说明才能做的事"——这是对原文的引申归纳，原文未直接表述；
    - "三个条件依赖"（接收者 agent 通用编码能力 / 想法杠杆率 / 刻意欠规格化优点）——原文未列举；
    - **边界澄清** "idea file ≠ README ≠ 设计文档；当成 spec 会消除其价值来源"——原文未做此区分，draft provenance 已显式声明这是引申。
- 没有论点冲突，draft 是在 v2 两张 known_fact 之上**做了一层综合解释**。

## 3. 下一步的核心依据

- (1)(2) 显示：draft 与 v2 top1、v2 top2 共享完全相同的源材料和核心事实，但 draft 把两条 known_fact 综合到一个 concept 层次，并补了一组合理引申（杠杆率、欠规格化优点、与 README/spec/设计文档的边界）。
- 选 `provenance_delta`：
  - draft 没有引入新来源（与 v2 top1/top2 同一份 tweet），所以严格意义上不是为 v2 卡补新证据；
  - 但 draft 携带的"边界澄清（idea file ≠ README ≠ 设计文档）"和"三个成立条件"是 v2 两张 known_fact 在工程使用时需要的下游边界，audit 阶段可以把这两条边界以"下游解读"形式反向链接进 v2 top1 / top2 的 provenance，作为 v2 卡的"使用边界"补丁；
  - draft 自身作为 concept 卡留下，承担"综合层"的角色。
- 不选 `merge_candidate`：v2 两张 known_fact 各自的 scope 严格限定在原文的一句话；合并到 draft 会破坏 v2 known_fact 的紧致性，并让"事实"与"综合解读"混淆。
- 不选 `new_card`：忽略 draft 与 v2 两张卡的事实重叠会失去回链机会；v2 卡在"如何被工程化引用"上需要 draft 的边界注脚。
- 不选 `duplicate_skip`：draft 的综合视角与边界澄清是 v2 KB 当前缺失的，值得入库。
- 不选 `revise_before_gate`：draft 的范围、边界、引用都已完备，draft provenance 也已显式声明"边界澄清来自引申，非原文"。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：作为新 concept 卡入库；audit 阶段把 draft 的边界澄清（idea file ≠ README ≠ 设计文档）和"三个成立条件"作为下游使用边界，反向链接进 v2 `idea-file-abstract-vague` 与 `idea-file-share-the-idea` 的 provenance。

## 5. 备注

- v2 top1、top2 是同一推文的两条平行 known_fact，draft 是它们的合成视角；这是 v3 loop 中典型的"事实-综合"层级关系，audit 可考虑同时为两张 v2 卡都加一条"对应综合视角见 idea-file-as-agent-era-artifact"的注脚。
- draft 内提到的 Karpathy gist 链接（idea file 本身）在本轮 draft provenance 已声明未读取，audit 阶段也不强求读取。
