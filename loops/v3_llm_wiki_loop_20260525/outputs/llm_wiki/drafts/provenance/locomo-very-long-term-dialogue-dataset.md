---
schema: draft_card_provenance.v3
draft_card: ../cards/locomo-very-long-term-dialogue-dataset.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
created_time: 2026-05-26T14:00:00+08:00
edited_time: 2026-05-26T14:00:00+08:00
edited_entity: llm
---

## 源证据

- 第 72-77 行（title.tex）：`Evaluating Very Long-Term Conversational Memory of LLM Agents`，作者 Maharana / Lee / Tulyakov / Bansal / Barbieri / Fang。
- 第 113-114 行（abstract）："a dataset of \textit{very} long-term conversations, each encompassing 300 turns and 9K tokens on avg., over up to 35 sessions."
- 第 149 行（compare table 行）：`\textbf{\dataset{} (ours)} & 304.9 & 19.3 & 9,209.2 & few months & \ding{51} & LLM-gen. + crowdsourc.`
- 第 290 行（人工编辑量）："annotators edited nearly 15\% of the dialog turns and removed or substituted approx. 19\% images".
- bibtex 条目 `maharana-etal-2024-evaluating`（第 1825-1844 行）给出 ACL 版数字 600 turns / 16K tokens / 32 sessions——版本差异说明。

## 卡片范围是否成立

- "9K token / 19 session / 50 段"全部直接来自 abstract 和对比表，无引申。
- "前作 ≤5 session ≤1.2K token"来自同一对比表中其它数据集行（MSC、Conversation Chronicles），属于源材料内的事实。
- "ACL 版与 arXiv 版数字不同"是直接观察到的差异，已在 footnote 标注；卡片选择 arXiv 版数字以匹配本材料路径。

## 发表门控结果

本轮未运行。

## 备注

- v2 已有卡片集中（auto-index-replaces-rag-at-small-scale 等）没有覆盖 LoCoMo 的具体量级，未观察到直接冲突。
- comparison_provenance 阶段可考察是否要新增一张"long-term dialogue benchmarks 量级演进"对照表的卡。
