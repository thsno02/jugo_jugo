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
related: []
---

LLM Wiki 的审计（audit）机制回答的是**更广泛的信任问题**——wiki 和产出是否仍然可信[^src-1]。

审计沿**完整的制品图（artifact graph）**工作，具体路径为 `output/` -> `wiki/` -> `raw/`[^src-2]：
1. **复用 librarian 通道**——对文章进行陈旧度和质量评分，采用两级扫描：先快速元数据检查，再对标记文章做深度内容阅读[^src-3]
2. **跨层追踪**——从产出追溯到它依赖的 wiki 状态和原始来源[^src-4]
3. **漂移检测**——检查产出是否已偏离其上游来源的当前状态[^src-5]
4. **升级研究**——当本地语料库的证据不足以回答信任问题时，审计会发起新鲜的网络研究[^src-6]

审计支持不同粒度：可针对整个 wiki（`/wiki:audit --wiki nutrition`）、单个制品（`/wiki:audit --artifact output/report.md`）、或项目（`/wiki:audit --project nutrition-playbook`）[^src-7]。

这一机制与已有的源忠实性风险卡形成对照——前者识别了 wiki 内容偏离原始来源的风险，审计则提供了结构性的验证手段。

## Footnotes

[^src-1]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L56-58 -- "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/, wiki/, and output/, detect drift, inspect provenance"
[^src-2]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L326-327 -- "Audit walks that full artifact graph. It can trace an output back through the wiki state and raw sources it depended on"
[^src-3]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Librarian" L52-54 -- "Score every article for staleness and quality. Two-tier scan: fast metadata check, then deep content read for flagged articles."
[^src-4]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "How the wiki works" L326 -- "trace an output back through the wiki state and raw sources it depended on"
[^src-5]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L58 -- "detect drift, inspect provenance"
[^src-6]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Audit" L58 -- "do fresh research when local evidence is not enough"
[^src-7]: `/Users/lw/Desktop/GitHub/llm_wiki/jugo_jugo/data/raw/webpage/llm-wiki-net/text.txt` -- "Quick Start: Audit" L256-258 -- "/wiki:audit --wiki nutrition /wiki:audit --artifact output/report-gut-brain.md"
