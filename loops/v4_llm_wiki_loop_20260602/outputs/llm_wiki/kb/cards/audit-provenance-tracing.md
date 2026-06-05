---
id: audit-provenance-tracing
title: 审计与溯源追踪
status: accepted
card_type: mechanism
tags: [llm-wiki, audit, provenance, trust, drift-detection]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [llm-wiki-net]
justification: ../justification/audit-provenance-tracing.md
canonical_concept: audit-provenance-tracing
aliases: [审计溯源, audit provenance, 可信度审计, provenance tracing]
summary: >-
  audit-provenance-tracing（审计溯源 / audit provenance / 可信度审计 / provenance tracing）
  是 LLM Wiki 的信任验证机制：沿 output->wiki->raw 完整制品图追踪，检测漂移，
  复用 librarian 评分通道，当本地证据不足时升级为新鲜研究
related: [inventory-evidence-separation, non-lossy-episodic-store, source-faithfulness-risk, three-layer-architecture]
---

LLM Wiki 的审计（audit）机制回答的是**更广泛的信任问题**——wiki 和产出是否仍然可信[^src-1]。

审计沿**完整的制品图（artifact graph）**工作，具体路径为 `output/` -> `wiki/` -> `raw/`[^src-2]：
1. **复用 librarian 通道**——对文章进行陈旧度和质量评分，采用两级扫描：先快速元数据检查，再对标记文章做深度内容阅读[^src-3]
2. **跨层追踪**——从产出追溯到它依赖的 wiki 状态和原始来源[^src-4]
3. **漂移检测**——检查产出是否已偏离其上游来源的当前状态[^src-5]
4. **升级研究**——当本地语料库的证据不足以回答信任问题时，审计会发起新鲜的网络研究[^src-6]

审计支持不同粒度：可针对整个 wiki（`/wiki:audit --wiki nutrition`）、单个制品（`/wiki:audit --artifact output/report.md`）、或项目（`/wiki:audit --project nutrition-playbook`）[^src-7]。

这一机制与源忠实性风险形成互补——后者识别了 wiki 内容偏离原始来源的风险，审计则提供了结构性的验证手段[^card-1]。审计的遍历路径正是三层架构所定义的制品层次：从产出经 wiki 回溯到不可变的 raw sources[^card-2]。值得注意的是，审计仅沿证据链（raw + wiki + output）工作，inventory 作为操作状态被刻意排除在证据体系之外[^card-3]。

与 Graphiti 的无损 episode 存储相比，LLM Wiki 的审计采取事后遍历策略——在需要验证时沿制品图回溯，而非在数据写入时即建立双向索引[^card-4]。

## Footnotes

[^src-1]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L56-58 -- "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/, wiki/, and output/, detect drift, inspect provenance"
[^src-2]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L326-327 -- "Audit walks that full artifact graph. It can trace an output back through the wiki state and raw sources it depended on"
[^src-3]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Librarian" L52-54 -- "Score every article for staleness and quality. Two-tier scan: fast metadata check, then deep content read for flagged articles."
[^src-4]: `data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L326 -- "trace an output back through the wiki state and raw sources it depended on"
[^src-5]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L58 -- "detect drift, inspect provenance"
[^src-6]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L58 -- "do fresh research when local evidence is not enough"
[^src-7]: `data/raw/webpage/llm-wiki-net/text.txt` -- "Quick Start: Audit" L256-258 -- "/wiki:audit --wiki nutrition /wiki:audit --artifact output/report-gut-brain.md"
[^card-1]: [源忠实性风险与不可变锚点](source-faithfulness-risk.md) -- 本卡提供结构性的漂移检测与溯源验证机制，该卡识别 wiki 内容偏离原始来源的风险及 lint 对忠实度检查的缺位
[^card-2]: [三层架构](three-layer-architecture.md) -- 本卡的审计遍历路径（output->wiki->raw）正是三层架构所定义的制品层次
[^card-3]: [清单与证据的刻意分离](inventory-evidence-separation.md) -- 本卡沿证据链溯源，该卡解释 inventory 为何被刻意排除在证据体系之外
[^card-4]: [无损 Episode 数据存储与双向溯源](non-lossy-episodic-store.md) -- 本卡采取事后遍历制品图的溯源策略，该卡描述 Graphiti 在写入时即建立双向索引的内建溯源
