---
schema: justification_journal.v1
card: ../cards/comparison-storage-vs-retrieval-compression.md
created_time: 2026-06-05T18:00:00+08:00
---

## creation | 2026-06-05T18:00:00+08:00

生成方式：governance cross-link judgment（token-economics-cross-domain cluster）
来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt` + `data/raw/arxiv/arxiv-zep/agent_source_bundle.txt`
源证据：
- Mem0 论文 sections/result.tex — "Zep's memory graph consumes in excess of 600k tokens... extensive redundancy across the graph"
- Zep 论文 Section 4.3 / Table 2 — "Full-context 115k tokens... Zep 1.6k tokens... accuracy improvement up to 18.5%"
范围论证：memory-compression-token-ratio 卡（Mem0 视角）和 longmemeval-context-compression 卡（Zep 视角）对同一系统的 token 效率给出了表面矛盾的评价。这一矛盾本身揭示了一个可独立成卡的原子洞察：记忆系统的 token 效率存在存储与检索两个独立维度，优化一个不保证另一个，甚至可以反向相关。该区分对系统设计评估有直接实践意义。
