---
schema: comparison_provenance.v3
draft_card: ../cards/nvk-llm-wiki-parallel-multi-agent-research.md
draft_provenance: ../provenance/nvk-llm-wiki-parallel-multi-agent-research.md
similarity_result: ../similarity/nvk-llm-wiki-parallel-multi-agent-research.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.1667
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.15
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1053
decision: new_card
audit_required: false
created_time: 2026-05-26T12:22:00+08:00
edited_time: 2026-05-26T12:22:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 jaccard 0.1667 / 0.15 / 0.1053 都只共享 `llm`、`wiki`（top1/top2 多一个 `的`）——完全是高频功能词。draft 标题中的 `nvk`、`agent`、`gap`、`并行`、`研究`、`多轮` 等核心词在 v2 候选标题里都没出现。属功能词撞分。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `llm-wiki-net`（nvk/llm-wiki 项目主站文档）；v2 三张候选均出自 karpathy gist / x post 家族。
- **类型与论点不同**：
  - 本 draft 是 mechanism 卡，覆盖 `/wiki:research` 的四阶段流程（ask/topic → 5/8/10 并行 agent search → ingest + compile → gap report）、多种模式开关（`--plan` 多 path、`--deep`、`--retardmax`、`--new-topic`、`--min-time 1h`、`--mode thesis` 含 supporting/opposing/mechanistic/meta-review/adjacent agent 分工）、fuzzy router 衔接、以及 thesis mode 的反 confirmation bias 设计。
  - top1 `three-layer-architecture` 谈抽象 raw/wiki/schema 三层；top2 `schema-configuration-document` 谈 schema 角色；top3 `health-checks` 谈 LLM 周期性健康检查——三者都不涉及多 agent 研究流程。
- 关键数字（5/8/10 agent、--min-time 2h 多轮、`--plan` 多 path 并行 + 统一 compile）、关键短语（`act first, think later`、`focuses harder on the weaker side`、`Sources that don't relate to the claim's variables are skipped`）在 v2 完全没有。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖多 agent 研究流程；(2) draft 是来自全新源（llm-wiki-net）的独立 mechanism 卡，含完整证据链（行 214、276–296、350–366、466–478）；(3) thesis mode 的反 confirmation bias 设计、retardmax 的"act first"哲学等都是 v2 完全没有的新机制。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 任一卡补一段证据——它是另一个产品/项目的完整流程描述。不是 `merge_candidate`：v2 没有 mechanism 类的 nvk 研究流程卡可合并。draft prov 备注里曾考虑"是否合并为 nvk/llm-wiki 工具概览大卡"——但那是与同源的 `nvk-llm-wiki-hub-and-topic-wikis` 兄弟卡之间的内部分工问题，不涉及 v2 候选；维持分卡（流程 vs 结构）更利于下游引用。

不是 `revise_before_gate`：边界完整（依赖底层平台支撑并行 agent、retardmax 不适合严肃文献调研、thesis mode 跳过跨域反例的代价），证据全部回引行号。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；与同源同批 `nvk-llm-wiki-audit-and-librarian` 与 `nvk-llm-wiki-hub-and-topic-wikis`（如已存在）做 related 互链组成 nvk 工具三角；与 `llm-knowledge-base-five-stage-workflow` 的 Ingest 阶段做主轴 cross-link（"抽象 ingest" → "具体多 agent ingest"）。

## 5. 备注

- "thesis mode 跳过反例 → 损失 exploratory 价值" 是本卡的硬边界，未来下游使用 thesis mode 时必须保留这条提醒。
- `--retardmax` 的命名来自 "Elisha Long 的 retardmaxxing 哲学"，原文有引；如未来要做"研究模式哲学"卡可作为来源之一。
