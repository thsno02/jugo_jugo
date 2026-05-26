---
id: karpathy-wiki-aliases-and-dedup
title: 强制别名 + 两层语义重复检测：跨语言去重的工程承诺
status: draft
card_type: mechanism
tags: [#obsidian, #karpathy-wiki, #deduplication, #cross-lingual]
created_time: 2026-05-26T12:35:00+08:00
edited_time: 2026-05-26T12:35:00+08:00
edited_entity: llm
source_ids: [obsidian-community-plugin]
provenance_card: ../provenance/karpathy-wiki-aliases-and-dedup.md
aliases: [page aliases, semantic-tier duplicate detection, alias-aware search]
related: [karpathy-llm-wiki-obsidian-plugin-overview]
---

## 问题：跨语言写作的 wiki 容易长出"语义重复页"

在多语种使用场景里，同一概念会以不同语言、缩写、拼写出现：CoT vs 思维链；DSA vs DeepSeek-Sparse-Attention。早期版本（< v1.7.10）的 Karpathy LLM Wiki 插件缺少别名感知，会在两种写法各生成一页，造成"假双胞胎"——大幅降低 wiki 的连接质量。

## 解决方案的两层结构

### 1. 强制别名（Mandatory Page Aliases）

每个生成页**必须**至少含 1 个别名，常见类型：

- 翻译（如 `"监督学习"` 之于 Supervised Learning）；
- 缩写（如 `"DSA"` 之于 DeepSeek-Sparse-Attention）；
- 别称（如 product code name vs 公开名）。

别名写在 frontmatter 的 `aliases: []`，是后续重复检测和 alias-aware 搜索的基础。**没有别名 = 重复检测失灵**——这是页面在 FAQ 中明确指出的：早于 v1.7.11 生成的页缺少别名是"无害但限制功能"的状态，需 `Complete Aliases` 命令补齐。

### 2. 两层语义重复检测（v1.7.10+）

Lint 时分两轮判定候选：

- **Tier 1（始终 LLM 验证）**：直接名称匹配——跨语言对照、缩写匹配、高相似标题。Tier 1 候选**全部送 LLM 复核**，因为这是高置信信号。
- **Tier 2（填充剩余 token 预算）**：间接信号——共享链接、中等相似度。Tier 2 仅在 LLM 预算还有余时纳入，避免拖慢 lint。

发现重复后用户可以 `Merge Duplicates`：插件让 LLM 融合两页内容，**同时保留双方的别名**（防止融合后再次被判为新候选）。

## 与同 batch 其它 dedup 思想的对比

- 与 **mem0** 的 `Contradicts → DELETE` 路径相比，Karpathy 插件的策略是"先**人工触发** Lint，再 **LLM 验证** 候选，再用户**审视后 Merge**"——三步都有人参与，写入安全等级高，但延迟与人力成本也高。
- 与 **memory-as-metabolism** 的 minority retention 立场不同：插件做的是"语义重复"的合并，而不是"少数派假说"的保留——目标是减少冗余，不是保留方差。两者不冲突，但说明 dedup 与 minority retention 是两个独立坐标轴。

## 关键设计选择

- 别名是**写入时强制**的，不是事后修复——LLM 生成页时就要给 alias，避免技术债积压；
- LLM 验证作为 Tier 1 的**默认**而非 fallback——快但便宜的相似度匹配只用来生成候选，不直接判定；
- Merge 不破坏元数据：reviewed/sources/aliases 在 fusion 后保留。

## 升级路径中的注意点

页面 FAQ 提示：从 < v1.7.11 升级时，**先 Regenerate index → Lint → Complete Aliases → Merge Duplicates** 才能享受 alias-aware 搜索；老版生成的页没补别名前，搜索 "DSA" 找不到 "DeepSeek-Sparse-Attention"。这意味着别名机制是**前置**的——索引和检索都依赖它工作。

## References

- 来源页面：`data/raw/webpage/obsidian-community-plugin/text.txt`。
- 第 261–267 行：Mandatory Page Aliases、Duplicate Detection & Merge、Smart Knowledge Fusion 的特性段。
- 第 215–229 行：从 < v1.7.11 升级的步骤。
- 第 276–280 行：Semantic-Tier Duplicate Detection 的 Tier 1/Tier 2 细节。
- 第 410–414 行：FAQ "Why does Lint show missing aliases"、"Why do I see duplicate pages like 'CoT' and '思维链'"、"How does duplicate detection work"。

## Footnotes

[^1]: Mandatory aliases verbatim（第 262 行）："Every generated page includes at least 1 alias (translation, acronym, alternate name), enabling cross-language duplicate detection."

[^2]: Tier 1/Tier 2 verbatim（第 277 行）："Tier 1 (direct name matches: cross-language, abbreviations, high-similarity titles) always verified; Tier 2 (indirect signals: shared links, moderate similarity) fills token budget."

[^3]: 跨语言重复实例 verbatim（第 412 行）："Why do I see duplicate pages like 'CoT' and '思维链'? Pre-v1.7.10 versions lacked alias-aware duplicate detection. Run Lint Wiki → Merge Duplicates to fuse them."
