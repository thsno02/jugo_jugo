---
schema: draft_card_provenance.v3
draft_card: ../cards/wicer-blind-compilation-catastrophic-loss.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
created_time: 2026-05-26T11:05:00+08:00
edited_time: 2026-05-26T11:05:00+08:00
edited_entity: llm
---

## 源证据

- Table 3 `tab:wiki_results`（`main.tex` 第 736–746 行）逐档列出 light / moderate / aggressive 三种压缩目标的实际压缩率与质量：
  > "FC raw (80 docs) — 100% 3.46 17.3% — / Wiki-light 75% 35.4% 2.32 52.9% −1.14 / Wiki-moderate 50% 12.2% 2.25 57.1% −1.21 / Wiki-aggressive 25% 8.2% 2.14 60.3% −1.32 / RAG n/a n/a 3.63 17.7% +0.17"。
- Compression compliance failure 的因果归因（第 758–762 行）：
  > "The root cause is compression compliance failure: the compiler ignores target word counts, compressing 2×–3× beyond the requested level (light target 75% → actual 35%). ... The score-1 rate (53–60% for wikis vs. 17% for FC raw) confirms that answers fail because information is missing, not unfindable."。
- 延迟侧 sub-400 ms（第 748–750 行）：
  > "Compilation does yield a clear latency win: all wiki levels achieve sub-400 ms TTFT (2.8–5.6× faster than FC raw; full timing in Appendix wiki_timing)."。
- 编译过程描述（第 715–718 行）：
  > "For each of the 17 RepLiQA topics, we compile 80 raw documents into a structured wiki using Claude Sonnet as a knowledge engineer (blind to evaluation questions), targeting three compression levels—light (~75%), moderate (~50%), and aggressive (~25%)—yielding 51 compiled wikis."。

## 卡片范围是否成立

这张卡聚焦"盲编译的两个独立失效模式"——压缩比失控 + 关键事实丢失——并把它们与延迟收益放在同一张表里对照。所有结论都直接对应 Table 3 与该节 "Analysis" 段，没有把 WiCER 的修复机制混进来（修复机制由 `wicer-cegar-compile-evaluate-refine` 单独承载）。卡内"score-1 跳升到 53–60%"、"延迟 2.8–5.6× 加速但 sub-400 ms"等数字均来自源材料。

## 发表门控结果

本轮未运行。

## 备注

与 `wicer-cegar-compile-evaluate-refine` 互为前因后果（前者诊断问题、后者给出修复），适合作为相互 related 的成对卡。与 v2 现有 4 张 wiki workflow 卡无直接重叠，预计 `new_card`。
