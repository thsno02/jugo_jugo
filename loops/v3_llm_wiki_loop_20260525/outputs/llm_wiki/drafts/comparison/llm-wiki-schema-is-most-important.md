---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-schema-is-most-important.md
draft_provenance: ../provenance/llm-wiki-schema-is-most-important.md
similarity_result: ../similarity/llm-wiki-schema-is-most-important.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.3333
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.2
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2
decision: new_card
audit_required: false
created_time: 2026-05-26T12:12:00+08:00
edited_time: 2026-05-26T12:12:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-schema-configuration-document` (0.333)**：共享 `llm / schema / wiki / 是 / 的`。两张卡都谈"schema 在 Karpathy LLM Wiki 中的地位"——v2 给静态定义（schema 是配置文档），draft 给经验主张（schema 是**最重要**的文件，Karpathy gist underplay 了它）。
- **top 2 `llm-wiki-pattern-file` (0.2)**：共享 `llm / wiki / 文件`。v2 这张是"LLM Wiki 作为模式文件"，谈的是 idea-file 的整体定位；draft 提的"schema.md / CLAUDE.md / AGENTS.md"是 wiki 实例内部的规则文件，不是同一种"文件"。token 共享是"文件"二字的偶然命中。
- **top 3 `llm-wiki-three-layer-architecture` (0.2)**：只共享 `llm / wiki / 的`。三层中 schema 是其中一层，所以主题相邻；论点不冲突也不重叠。

## 2. draft 与候选在哪里不同

- **来源不重叠**：v2 top1 来自 Karpathy gist `raw.txt:33`；draft 来自 `openaitoolshub-six-months/text.txt`（Jim Liu 在 Obsidian 上跑该模式 6 个月、35 页后的反思文章）。Rohit Ghumare 的二次引用 "Schema is the most important file" 在 draft 内被复述，但 v2 top1 完全不引用这两个来源。
- **论点轴对立**：
  - v2 top1：schema 是配置文档，与 raw / wiki 并列（**平等的一层**）。
  - draft：实际部署中 schema 比 raw / wiki **更重要**，缺 schema 会"a graveyard within two months"（Karpathy gist 的相对强调比例被 underplay 了）。
  - 这是 draft **明确反对**了 v2 top1 隐含的"三层并列"框架。
- **scope 不同**：v2 是 known_fact（仅限源对 schema 层的规定）；draft 是 operational_rule（含 Pitfall #4 双 slug 案例、schema-first 实操字段清单、"任何工具切换前重读 schema"操作规则）。
- **fact_type 不同**：v2 是 known_fact（事实陈述），draft 是 operational_rule（基于个人经验的工程主张，sample size = 1）。

## 3. 下一步的核心依据

- (1) 与 (2) 显示：draft 与 v2 top1 共享"schema"这个实体，但 draft 是个独立的、来源不同的、论点相反方向的 operational_rule 卡。v2 top1 的 statement（"schema 是配置文档"）本身不被 draft 推翻或修正，但 draft 在事实层之上叠了一层**经验性强调主张**。
- 选 `new_card`：因为 draft 不为 v2 top1 提供新证据 / 新边界 / 新数值——它是一个独立主张（"schema 在三层中地位最高"），与 v2 top1 的事实陈述并列存在，没有必要回写进 v2 top1 的 provenance。
- 不选 `provenance_delta`：draft 内容是另一个论点，不是 v2 top1 statement 的补充证据。强行把 draft 的 Jim Liu / Rohit Ghumare 主张写进 v2 top1 的 provenance，会破坏 v2 top1 "fact_type: known_fact / scope: 仅限该来源对 schema 层的规定" 的边界。
- 不选 `merge_candidate`：v2 top1 是事实卡，draft 是 operational_rule 卡；合并会让两种 fact_type 混杂、scope 失控。
- 不选 `revise_before_gate`：draft 已显式标注 sample size = 1 的边界、"相对强调不否认内容也重要"的语义边界，结构完整。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可在 draft `related` 加 `llm-wiki-schema-configuration-document`，建立"定义"与"经验主张"之间的导航。

## 5. 备注

- v2 top1 的 token "是"被 jaccard 计入共享，加上"schema"是高密度概念词，导致 0.333 这个看上去高的分数；但论点轴不同，分数实际是误高。
- Jim Liu 的 Pitfall #4（双 slug 案例）若以后想入 v2 KB，应另开一张"slug 规则跨工具迁移"卡，而非塞进 v2 top1。
