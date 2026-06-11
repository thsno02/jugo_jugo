---
id: llm-wiki-deterministic-lint
title: LLM Wiki 确定性 Lint 健康检查
status: accepted
card_type: mechanism
tags: [llm-wiki, lint, wiki-health, validation, quality-assurance]
created_time: 2026-06-11T10:00:00+08:00
edited_time: 2026-06-11T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/llm-wiki-deterministic-lint.md
canonical_concept: llm-wiki-deterministic-lint
aliases: [kb_lint, wiki lint, 确定性健康检查, schema lint, wiki health check]
summary: >-
  llm-wiki-deterministic-lint（kb_lint / 确定性健康检查）llm-wiki-karpathy 运行时提供确定性 lint 操作，检测八类 wiki 健康问题：缺失表示链、过时表示、不一致 asset_paths、孤立页面、过时源覆盖、无支撑声明、矛盾候选项、缺失高价值页面
related: [gap-mapping-promotion, runtime-agent-boundary, representation-first-ingest]
---

llm-wiki-karpathy 运行时通过 `kb_lint` 命令提供确定性的 wiki 健康检查[^src-1]。该操作完全由运行时执行（不依赖 LLM 推理），覆盖八类结构性健康问题：

1. **缺失表示链（missing representation trails）**——多模态源笔记是否有可信的审查路径
2. **过时表示（stale representations）**——已存储的中间表示是否与原始资产不再同步
3. **不一致 asset_paths**——声明的资产路径是否与实际已审查的资产匹配
4. **孤立页面（isolated pages）**——wiki 中没有被任何其他页面链接的页面
5. **过时源覆盖（stale source coverage）**——源笔记是否仍然反映原始资料的最新状态
6. **无支撑声明（unsupported claims）**——wiki 页面中缺少来源支撑的断言
7. **矛盾候选项（contradiction candidates）**——wiki 内部可能存在互相矛盾的内容
8. **缺失高价值页面（missing high-value pages）**——应当存在但尚未创建的页面[^src-2]

`kb_lint` 与 `kb_map_gaps` 互补但职责不同：lint 面向已有内容的结构性缺陷（验证性），gap mapping 面向尚未存在的知识空白（扩展性）[^src-3]。lint 在 v0.4.4 中扩展了多模态相关检查——如果多模态源笔记在被 wiki 依赖之前没有可信的审查路径，lint 会发出警告[^src-4]。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "CLI Commands" -- "llm-wiki-karpathy kb_lint --vault-root /vault"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "deterministic lint for schema and wiki health, including warnings for missing representation trails, stale representations, inconsistent asset_paths, isolated pages, stale source coverage, unsupported claims, contradiction candidates, and missing high-value pages"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "What 0.4.4 Implements" -- "deterministic gap mapping and promotion through kb_map_gaps and kb_promote_gap"
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/clawhub-llm-wiki-karpathy/markdown.md` -- "Runtime Philosophy" -- "kb_lint stays deterministic, but now also checks whether multimodal source notes have a believable review trail before the wiki starts depending on them."
