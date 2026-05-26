---
schema: draft_card_provenance.v3
draft_card: ../cards/wicer-fc-rag-document-count-crossover.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
created_time: 2026-05-26T11:10:00+08:00
edited_time: 2026-05-26T11:10:00+08:00
edited_entity: llm
---

## 源证据

- Policygenius 上 FC 优势（第 4 节，Table 1/2，第 568–614 行）：
  > "Mean score 4.38 / 4.08 ... TTFT median 0.857 s / 6.277 s ... Full-context warm queries achieve sub-second TTFT (median 0.86 s, 7.3× faster than RAG's 6.28 s)"。
- RepLiQA 上的翻转（第 656–671 行）：
  > "mean FC Q8 score is 3.47 (σ=0.11; ≥4: 64.0%) compared to 4.35 (≥4: 90.0%) on Policygenius. More importantly, RAG consistently outperforms full-context: RAG mean is 3.64 (σ=0.16), and RAG wins on 13 of 15 topics with the remaining 2 tied (|Δ| < 0.05). Full-context does not win a single topic. The mean quality gap is −0.18 points (FC − RAG), a complete reversal of the Policygenius +0.27 gap."。
- Lost-in-the-middle 的具体计数（第 672–683 行）：
  > "full-context produces 17.0% score-1 answers (vs. 1.2% on Policygenius), and cross-referencing per-question scores reveals 557 cases across all 15 FC topics (530 across the 14 Q8 topics) where FC scored 1 but RAG scored ≥4. ... RAG's score-1 rate is comparable at 17.7%, driven by retrieval misses (87.9% accuracy), but its failures are on different questions"。
- Crossover 与 LLM Wiki thesis（第 687–690 行）：
  > "These results establish a clear crossover ... That full-context excels on compiled knowledge but degrades on raw collections reinforces the LLM Wiki thesis: the quality of compilation, not just context length, determines viability."。
- Q4 在大语料下的质量退化（第 634–638 行）：
  > "Q4 reduces TTFT by 4.8% on average but, unlike on Policygenius, degrades quality at 80 documents: Q8 outscores Q4 in 13 of 14 topics (mean Δ = +0.14), indicating that reduced KV precision exacerbates attention dilution at scale."。
- TTFT 比例 7.3× → 4.6×（第 641–644 行）：
  > "Median RAG TTFT is 4.83 s (σ=0.22 s), yielding a full-context TTFT advantage of ~4.6× on average—consistent with the 7.3× advantage on Policygenius (the smaller ratio reflects larger RepLiQA corpora increasing FC TTFT proportionally more than RAG)."。

## 卡片范围是否成立

这张卡聚焦的是"两个真实语料上 FC vs RAG 的对照实验所暴露的质量翻转及其机制"。所有关键数字（4.38/4.08、3.47/3.64、7.3×/4.6×、557 个 lost-in-the-middle 案例）都来自论文 §4 / §5 / Appendix G 的对照表，没有引入论文外的解释。"窗口占比不是唯一变量"这一推断是把 70% vs 57–99% 窗占比与质量结果直接对照得出，而不是引申。三条"操作启示"是对论文 Discussion 段中 deployment 建议的中文复述。

## 发表门控结果

本轮未运行。

## 备注

与 `wicer-cegar-compile-evaluate-refine`、`wicer-blind-compilation-catastrophic-loss` 在主题上互补——前者讲算法、本卡讲它出现的"经验前提"。可与 v2 中 `auto-index-replaces-rag-at-small-scale` 比较：v2 卡讨论的是"小规模 auto-index 取代 RAG"，本卡讨论的是"全上下文 KV cache 与 RAG 随文档数量的翻转"，抽象层级不同，预计 `new_card`，但可在 comparison_provenance 阶段交叉评估是否需要标注 related。
