---
schema: comparison_provenance.v3
draft_card: ../cards/nvk-llm-wiki-hub-and-topic-wikis.md
draft_provenance: ../provenance/nvk-llm-wiki-hub-and-topic-wikis.md
similarity_result: ../similarity/nvk-llm-wiki-hub-and-topic-wikis.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2143
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.1875
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1333
decision: new_card
audit_required: false
created_time: 2026-05-26T12:43:00+08:00
edited_time: 2026-05-26T12:43:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张 v2 候选与 draft 共享 token 仅 `llm / wiki / 的`，纯属误中：

- v2 三张候选讲 Karpathy gist 的 raw/wiki/schema 三层架构 / schema 配置 / health checks——所谓"层"是 gist 的逻辑分层。
- 本 draft 讲 `nvk/llm-wiki` 这个工具实现的 **Hub + Topic-Wikis 两级目录结构**——所谓"层"是文件系统层级与"一题一库"的隔离策略。

虽然都有"分层"字面，但所指对象完全不同：v2 是 conceptual layers，draft 是 directory structure + topic isolation。

## 2. draft 与候选在哪里不同

- **对象不同**：v2 是 Karpathy gist 概念定义；draft 是 `nvk/llm-wiki` 工具的具体目录布局（`~/wiki/topics/<topic>/{inbox,inventory,datasets,raw,wiki,output}` + 全局 `wikis.json` 注册表 + `_index.md` 派生缓存）。
- **抽象层不同**：v2 是概念；draft 是工程实现（目录树 + 不变量 + 多 wiki 隔离机制 + portable path 注意事项）。
- **覆盖维度全新**：Hub（极轻、只装 registry 与 log）+ Topic 五个不变量（raw immutable / inventory = state / datasets = manifest / wiki 三类目录 / `_index.md` 派生缓存 / archive 是 quiet 不是 delete）+ "deep query 支持 `--with` 跨 wiki" + iCloud portable path 劝告 —— 都不在 v2 任何卡片中。
- **决策粒度不同**：draft 给出操作规则（先决定 topic 边界 / topic = 研究域不是项目 / cross-link 用 archive registry 维持）。

不是 v2 卡片的扩展，是**关于另一个工具（nvk/llm-wiki）的全新事实卡**。

## 3. 下一步的核心依据

- 不是 `merge_candidate` / `provenance_delta`：v2 没有 nvk/llm-wiki 工具或任何 hub+topic 多 wiki 实现的内容。
- 不是 `duplicate_skip`：未被 v2 覆盖。
- 不是 `revise_before_gate`：draft 证据扎实（目录树与所有不变量都对应原文行号）、scope 清晰、边界（同概念跨 topic 重复 / archive 仍占磁盘 / wikis.json 须存逻辑路径）都标注。

正确决定是 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：走 publication_gate；audit 阶段建议与 `beyond-the-token-bottleneck-llm-wiki-case-study`（如存在）形成"工具 vs 案例"对比，与 `llm-knowledge-base-five-stage-workflow`（如存在）形成"工具 vs 抽象 workflow"对比，但这两张目标卡都不在本 batch top-3，仅作为后续 related 提示。

## 5. 备注

- v2 中"三层架构"卡里的"层"与本 draft 的"Hub+Topic 两级"完全是不同 ontology 的"层"——audit 阶段可在 v2 卡 Note 段补一句"本概念分层与具体工具实现（如 nvk/llm-wiki 的 Hub+Topic）属不同维度"，避免读者混淆。
- jaccard 把不同"层"概念拉到同一 top-3 是典型 surface-level 误中。
