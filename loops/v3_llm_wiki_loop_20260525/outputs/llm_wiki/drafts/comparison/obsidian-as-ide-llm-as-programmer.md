---
schema: comparison_provenance.v3
draft_card: ../cards/obsidian-as-ide-llm-as-programmer.md
draft_provenance: ../provenance/obsidian-as-ide-llm-as-programmer.md
similarity_result: ../similarity/obsidian-as-ide-llm-as-programmer.json
existing_cards:
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.3077
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.25
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1538
decision: new_card
audit_required: false
created_time: 2026-05-26T12:20:00+08:00
edited_time: 2026-05-26T12:20:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- **top 1 `llm-wiki-schema-configuration-document` (0.308)**：共享 `llm / wiki / 是 / 的`。token 高分主要来自基础词，外加 `是`、`的` 两个虚词。v2 谈 schema 定义；draft 谈 "Obsidian 是 IDE / LLM 是程序员 / wiki 是 codebase" 类比——topic 完全无关，jaccard 误中。
- **top 2 `llm-wiki-three-layer-architecture` (0.25)**：共享 `llm / wiki / 的`。draft 提"三层架构"作为 related，但本张卡专门讲类比，不讲三层。token 共享同样是高频词，主题相邻但不重叠。
- **top 3 `llm-wiki-health-checks` (0.154)**：仅共享 `llm / wiki`。draft 提到 "lint = code review" 的类比映射但只一句话，主题完全不在一个轴上。低分误中。

## 2. draft 与候选在哪里不同

- **来源不同**：v2 三张候选全部来自 Karpathy 原 gist / quote text；draft 来自 `marvin-hn-persistent-knowledge/text.txt:35-37`（HN 讨论中的总结性段落，引用了 Karpathy 的 IDE / 程序员 / codebase 类比）。
- **主张完全不同**：
  - v2 top1 = schema 是配置文档；
  - v2 top2 = 架构分三层；
  - v2 top3 = LLM 跑 health checks 清理 wiki；
  - draft = **Karpathy 显式提出的角色类比**：Obsidian / LLM / wiki = IDE / 程序员 / codebase，三个承诺（角色重定位、人机分工反转、工具栈框定），加上 "重复 bookkeeping 任务在结构上同构"的命中理由。
- **scope 不同**：draft 是 concept 类，专门解释这个类比"承诺了什么 / 边界在哪 / 操作含义"；v2 三张都是 known_fact，仅陈述源对各自字段的描述。
- 没有任何一张 v2 卡涉及"角色类比"，更没有 IDE / 程序员 / codebase 这组词，draft 的主轴在 v2 KB 完全空缺。

## 3. 下一步的核心依据

- (1)(2) 显示：draft 与三个 v2 候选的 token 重合都是基础词 + 虚词带来的，主题没有任何实质相邻。draft 的核心主张（Karpathy IDE 类比）在 v2 KB 完全未被覆盖。
- 选 `new_card`：这是一个全新的概念卡，引入了 v2 KB 不曾出现的核心隐喻；不会修改 v2 任何卡的 body 或 provenance。
- 不选 `provenance_delta`：draft 不为任何 v2 卡补证据 / 新边界 / 新数值。
- 不选 `merge_candidate`：v2 没有任何对得上的卡可合并。
- 不选 `duplicate_skip`：draft 的主张 v2 完全没有覆盖。
- 不选 `revise_before_gate`：draft 自带边界（类比非函数对应、Obsidian 非必需、LLM 写作能力假设）、引用与操作含义。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate；可在 draft `related` 保留与 `karpathy-llm-wiki-three-layers`、`karpathy-llm-wiki-vs-rag` 的互链以形成"Karpathy gist 主题集合"。

## 5. 备注

- 三个候选的 jaccard 高分（0.308 / 0.25 / 0.154）几乎全部来自 `llm / wiki / 是 / 的` 这种泛用 token，是典型的"v2 schema-configuration 卡反复出现"误中模式（worker prompt 已提示过）。
- 该 draft 与同 batch 的 `karpathy-llm-kb-three-layer-arch` 出自不同来源（marvin-hn vs DevelopersIO），可在后续 audit 形成 Karpathy 主题的多来源交叉引用。
