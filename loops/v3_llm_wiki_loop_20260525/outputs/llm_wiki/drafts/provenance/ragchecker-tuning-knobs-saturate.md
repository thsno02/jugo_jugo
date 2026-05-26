---
schema: draft_card_provenance.v3
draft_card: ../cards/ragchecker-tuning-knobs-saturate.md
material_id: arxiv-ragchecker
digest_id: digest_arxiv-ragchecker
source_paths:
  - data/raw/arxiv/arxiv-ragchecker/agent_source_bundle.txt
created_time: 2026-05-26T11:52:00+08:00
edited_time: 2026-05-26T11:52:00+08:00
edited_entity: llm
---

## 源证据

- L819–820：*"Increasing the number ($k$) and size of chunks improves the recall of more useful information ($\text{claim recall}$ 61.5$\rightarrow$77.6 with $k$ 5$\rightarrow$20, 70.3$\rightarrow$77.6 with size 150$\rightarrow$300). Consequently, this provides more context for the generators to be more faithful to ($\text{faithfulness}$ 88.1$\rightarrow$92.2 with $k$ 5$\rightarrow$20, 91.2$\rightarrow$92.2 with size 150$\rightarrow$300), though at the same time they also become more sensitive to additional noise ($\text{noise sensitivity}$ 34.0$\rightarrow$35.4 with $k$ 5$\rightarrow$20, 34.5$\rightarrow$35.4 with size 150$\rightarrow$300). Improvements in the overall performance ($F1$ 51.7$\rightarrow$53.4 with $k$ 5$\rightarrow$20, 52.6$\rightarrow$53.4 with size 150$\rightarrow$300) indicates benefits from more context."*
- L363：*"Given a limited context length, a larger chunk size with a smaller k is preferred, especially for easier datasets (Finance, Writing). This is evident when comparing a chunk size of 150 with $k$=20 against a chunk size of 300 with $k$=10."*
- L408–410：*"the overlap ratio may not require extensive tuning in practice."*
- L822：*"prompts introduces explicit requirements for better faithfulness, context utilization, and lower noise sensitivity, generators show improvements in faithfulness (92.2$\rightarrow$93.6), but struggle with the subtle tension between context utilization (59.2$\rightarrow$63.7) and noise sensitivity (35.4$\rightarrow$38.1)."*
- L826–830：*"Improving the retriever is an effective way ... moderately increasing the number and size of chunks ... Note that the effect saturates ... When tuning the generator, the trilemma of context utilization, noise sensitivity, and faithfulness makes it difficult to improve all aspects simultaneously. RAG builders should prioritize certain aspects in the prompt based on their targets, user preferences and the generator's capability."*

## 卡片范围是否成立

本卡是 operational_rule，把论文 §"Diagnosis"  + §"Suggestions to RAG Builders" 提炼成四条可照抄的工程规则。所有数字（CR、CU、NS、faithfulness、F1）都直接引自论文 ablation 表与正文。最后"先选硬约束 → 再做帕累托"的三步总结是对论文 §830 句"RAG builders should prioritize certain aspects"的工程化展开，与作者原意一致，但句式是综合性提炼，因此在边界栏说明它属于"经验观察、非数学硬界"。

## 发表门控结果

本轮未运行。

## 备注

- 与既有卡 `ragchecker-generator-trilemma` 互补：那张说"为什么三角难同时优化"，本卡说"具体调哪个旋钮、调多少"。
- prompt-工程那一段与 trilemma 卡有重叠点（92.2→93.6 / 59.2→63.7 / 35.4→38.1），但本卡的关注点是"GPT-4 受益、Llama3-70B 不受益"这一模型差异，属于不同切面。
