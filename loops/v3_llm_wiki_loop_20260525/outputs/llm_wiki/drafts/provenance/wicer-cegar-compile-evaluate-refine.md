---
schema: draft_card_provenance.v3
draft_card: ../cards/wicer-cegar-compile-evaluate-refine.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

- 算法伪代码（`main.tex` 第 781–802 行 `algorithm` 环境）：
  > "Probe selection: Select one QA pair per source document → Q_probe ... For each q ∈ Q_probe, generate answer from W_t, score with LLM judge ... Failures_t ← {q : score(q) ≤ 1} ... For each failed q, extract critical facts from source doc d_q ... W_{t+1} ← Compile(D, r, preserve=F_cumulative)"。
- CEGAR 类比段落（第 806–820 行）：
  > "In CEGAR, a concrete system M = (S, S_0, R, L) is approximated by an abstract model M̂ via a surjective mapping h : S → Ŝ; when model-checking M̂ produces a counterexample, it is analyzed—if spurious, the abstraction is refined to eliminate it, and the loop repeats. In WiCER, the concrete system is the full document collection D, the abstraction is the compiled wiki W_t ..."。
- 与静态编译流水线对比（第 460–464 行）：
  > "WiCER differs in two respects: (1) it targets a flat wiki artifact optimized for KV cache serving rather than a retrieval index, and (2) it closes the loop by evaluating the compiled artifact against diagnostic probes and iteratively refining it—a feedback mechanism absent from static compilation pipelines."。
- 每轮代价（第 886 行 "Analysis and Limitations" 段）：
  > "Each iteration requires ~130K API input tokens and ~17K output tokens (one compilation call, ~80 judge calls, ~15 diagnosis calls); the 80 local inference probes run at zero API cost. At current Sonnet pricing this totals ~$1–2 per iteration, completing in ~50 minutes"。
- 第 2 轮峰值与"random knowledge displacement"（第 884 行）：
  > "Ten of seventeen topics peak at iteration 2; the remaining seven peak at iteration 1 or show no gain, as the random knowledge displacement effect—fixing targeted facts displaces others—limits further improvement."。

## 卡片范围是否成立

WiCER 是这份 NeurIPS 2026 投稿的核心算法贡献，把它作为一张独立的 "mechanism" 卡是合理的：算法步骤、CEGAR 类比、收敛性论证和每轮代价都在同一节内可以闭环引用，读者读完不需要回到论文就能复述出"是什么 / 怎么转 / 为什么会收敛 / 什么时候不收敛"。
卡内"典型停在第 2 轮"、"代价 \$1–2 / 轮"、"local_education 不收敛"等具体数字直接来自论文，未做引申；CEGAR 抽象/具体的对应是把论文 Table 5（`tab:cegar_map`）的内容用中文复述，没有添加超出论文范围的解释。

## 发表门控结果

本轮未运行。

## 备注

可能与 v2 中关于 "LLM Wiki 编译" 或 "评估闭环" 的概念卡有概念重叠（待 comparison_provenance 阶段核对）；但 v2 现有 4 张卡的 slug（`auto-index-replaces-rag-at-small-scale`、`file-outputs-back-as-compounding-loop`、`idea-file-as-agent-era-artifact`、`llm-knowledge-base-five-stage-workflow`）题面与本卡均不在同一个抽象层级，预计为 `new_card`。
