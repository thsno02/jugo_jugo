---
schema: draft_card_provenance.v3
draft_card: ../cards/poisonedrag-survives-advanced-rag-and-agents.md
material_id: arxiv-poisonedrag
digest_id: digest_arxiv-poisonedrag
source_paths:
  - data/raw/arxiv/arxiv-poisonedrag/agent_source_bundle.txt
created_time: 2026-05-26T11:48:00+08:00
edited_time: 2026-05-26T11:48:00+08:00
edited_entity: llm
---

## 源证据

- L1619–1624：*"We conduct experiments to evaluate the effectiveness of PoisonedRAG for these advanced RAG schemes. Table~\ref{tab:advanced-rag} shows PoisonedRAG can achieve high ASRs, demonstrating that those advanced RAG schemes are also vulnerable to our PoisonedRAG. The reason is that the crafted malicious texts are relevant to the target questions, making the LLM generate incorrect answers based on malicious texts."*
- L1587–1599：Self-RAG / CRAG 在 NQ / HotpotQA / MS-MARCO 上的 ASR（0.77/0.87/0.73/...）与 F1（0.89–1.0）。
- L1632–1637：*"We used the English Wikipedia dump from Dec. 20, 2018 to create a knowledge database ... The total number of texts in the knowledge database is 21,015,324 ... Results in Table~\ref{tab:real-world case study} show PoisonedRAG is effective in this real-world scenario."*；表中 NQ 0.95/0.97、HotpotQA 1.0/0.94、MS-MARCO 0.94/0.91。
- L1662–1663：*"Our black-box attack achieves 0.72, 0.58, and 0.52 ASR, respectively"* on NQ / HotpotQA / MS-MARCO with ReAct Agent。
- L2063–2066：*"We conduct experiments on the FEVER dataset ... PoisonedRAG can achieve a 0.98 and 0.99 F1-Score in black-box and white-box settings ... a 0.97 and 0.88 ASR ..."*

## 卡片范围是否成立

卡片把"PoisonedRAG 在四个被认为更难攻击的设置上仍有效"作为一个 source claim 整合在一起。每个数字与每个数据集出处均来自上述段落。"高级 RAG 不天然防投毒"的解读是对论文 L1623 原句的提炼，与作者意图一致。CRAG / Self-RAG 的"为什么不行"解释直接来自 L1623。"规模不是防御"是对 21M vs 5 恶意文本的明显比例关系的合理结论。

## 发表门控结果

本轮未运行。

## 备注

- 与既有卡 `poisonedrag-existing-defenses-insufficient` 是不同切面：那张说"事后过滤防御"无效，本卡说"上游高级 RAG / 大规模语料 / agent 框架"也无效。两张可在 v2 阶段合并为"端到端硬化均失效"元卡。
- 数字与图表的位置都给到了具体行号，便于后续验证。
