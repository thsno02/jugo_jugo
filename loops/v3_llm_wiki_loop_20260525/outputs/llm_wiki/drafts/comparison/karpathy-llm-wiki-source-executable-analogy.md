---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-llm-wiki-source-executable-analogy.md
draft_provenance: ../provenance/karpathy-llm-wiki-source-executable-analogy.md
similarity_result: ../similarity/karpathy-llm-wiki-source-executable-analogy.json
existing_cards:
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1667
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1667
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1667
decision: new_card
audit_required: false
created_time: 2026-05-26T12:18:00+08:00
edited_time: 2026-05-26T12:18:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选 jaccard 完全一致（0.1667）但每张只共享 `llm`、`wiki` 两个通用 token，没有共享 `源码`、`编译`、`产物`、`比作` 等核心概念词。候选都是 v2 内部 karpathy 卡片，触发 0.1667 完全是高频功能词。属于典型的"低分批 + 功能词撞分"。

## 2. draft 与候选在哪里不同

- **来源不同**：本 draft 取自 `anthemcreation-en-guide`（英文 LLM Wiki 实践指南）；v2 三张候选都出自 karpathy gist 家族。draft 是第三方对 karpathy 模式的转述与扩写。
- **类型与论点不同**：
  - 本 draft 是 `distinction` 卡，核心是"raw = source code、wiki = compiled executable、query = run executable"类比，并附 RAG vs LLM wiki 的二维对比表（每次 query 做什么 / 跨文档关系 / 多跳推理 / 规模适用）。
  - top1 `health-checks` 谈 LLM 健康检查事实；top2 `listed-use-cases` 谈应用场景清单；top3 `pattern-file` 谈"LLM Wiki 作为模式文件"。三者论点轴都与"源码/可执行"类比无任何重合。
- 本 draft 的关键贡献——"编译类比解释了为什么 100 篇规模不需要向量库"+"weak model 会传播错误而不 flag" 的 agents.md 风险警告——在 v2 都没有。
- 注意：本 draft 引用了 karpathy 的"100 articles / 400K words"实践规模锚（与 `auto-index-replaces-rag-at-small-scale` draft 重合），但论点轴不同：那张是"小规模下索引替代 RAG 的操作规则"，本卡是"源码/可执行编译类比"。

## 3. 下一步的核心依据

(1) 三张候选都不覆盖"source/executable 编译类比"；(2) draft 是 distinction 类，自带独立证据（行 80 类比原文 + 行 142-148 规模对比 + 行 152 模型质量警告）与边界声明（编译比源码编译宽松、依赖 agents.md 质量、几百文档以上 vector search 重新划算）；(3) 来源 v2 KB 中不存在。结论是 `new_card`。

不是 `provenance_delta`：本 draft 不是给 v2 任一卡补一段证据——它是另一个论点轴（编译类比）、另一个源、独立的 distinction 框架。也不是 `merge_candidate`：v2 没有 distinction 类卡或编译类比卡。不是 `revise_before_gate`：证据完整、边界明确（特别是 "编译比源码宽松" 的弱化声明）。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；建议在 sources 索引加入 `anthemcreation-en-guide`；与同批 `auto-index-replaces-rag-at-small-scale`（小规模下索引替代 RAG 的操作规则）做 related 互链——一个给类比，一个给阈值；与未来"LLM wiki vs RAG 切换点"卡（如出现）做主轴 cross-link。

## 5. 备注

- draft prov 备注里提到的"可考察是否要新增一张 LLM wiki vs RAG 在不同规模的切换卡"——这是 future work，本卡决策不依赖它。
- 对比表中"万级以上语料 → wiki 维护成本变高"这条与 Robin Cartier 卡（同批）的"~200 页天花板"主题邻近，可双向 cross-link 但不触发 provenance_delta。
