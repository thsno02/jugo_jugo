---
schema: comparison_provenance.v3
draft_card: ../cards/nvk-llm-wiki-audit-and-librarian.md
draft_provenance: ../provenance/nvk-llm-wiki-audit-and-librarian.md
similarity_result: ../similarity/nvk-llm-wiki-audit-and-librarian.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1765
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: new_card
audit_required: false
created_time: 2026-05-26T12:08:00+08:00
edited_time: 2026-05-26T12:08:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top1/top2 共享通用 token `llm`、`wiki`、`的`，jaccard 0.2 / 0.1765 全部来自这些功能词；draft 标题里的 `nvk`、`audit`、`librarian`、`信任`、`workflow`等关键词在 v2 候选标题中都没出现。top3 `health-checks` 也只共享 `llm`、`wiki`。三者表面上是"都谈 LLM Wiki"，但论点轴不重合。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `llm-wiki-net`（nvk/llm-wiki 项目主站文档）；v2 top1/top2/top3 全部来自 karpathy 来源家族（gist + x post quote）。
- **抽象层不同**：本 draft 是 `operational_rule`，描述具体命令 `/wiki:librarian`（两层扫描、checkpoint recovery、JSON+report 输出）和 `/wiki:audit`（复用 librarian pass、跨 raw/wiki/output 追溯、detect drift、触发 fresh research 补 gap）的契约与组合 workflow，并给出 CI 类比与"每次 ingest 后跑 librarian / 每次生成 output 前跑 audit"等可复用规则。
- top1 `three-layer-architecture` 谈 karpathy 抽象三层；本 draft 是某具体项目里跨三层做 audit 的工作流，**借用**三层概念但贡献的是 workflow 设计而非分层定义。
- top2 `schema-configuration-document` 与 audit/librarian workflow 无直接对应。
- top3 `health-checks`：v2 谈"LLM health checks 寻找不一致、补缺、找候选文章"的抽象事实；本 draft 谈 nvk 的 `/wiki:lint --fix --deep` 命令实现，且 audit/librarian 范围远超 lint——audit 覆盖输出可信度回溯、不只是 wiki 自身健康。两者只在"健康检查"这一概念上有部分重叠，论点轴、来源、抽象层均不同。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖 nvk audit + librarian 的命令级 workflow；(2) draft 的核心贡献是"audit 触发 fresh research"这一闭环设计与 CI 类比，v2 没有；(3) 来源在 v2 KB 中不存在。结论是 `new_card`。

不是 `provenance_delta`：本 draft 与 v2 `health-checks` 有部分主题重叠（都涉及"健康检查"），但本 draft 是另一来源、另一抽象层（命令级 vs 概念级）的独立 operational_rule，不是给 v2 health-checks 卡补一条证据或边界。也不是 `merge_candidate`：v2 没有任何 audit / librarian / 命令级 workflow 卡可合并。不是 `revise_before_gate`：边界与证据完整，每段都引到原文行号或命令名。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `llm-wiki-net`；与 v2 `health-checks` 卡做 related 互链以呈现"karpathy 抽象 lint → nvk 命令级 audit/librarian"的演化路径。

## 5. 备注

- 注意 v2 health-checks 与本 draft 都谈"健康检查"，未来如果做"健康检查的不同实现"对比页时，应同时引这两张卡。
- "audit 触发 fresh research 的预算上限"是本卡引入的工程提醒（非原文），编辑/审稿可视情况裁定是否保留。
