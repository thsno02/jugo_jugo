---
schema: draft_card_provenance.v3
draft_card: ../cards/graphrag-leiden-community-hierarchy.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
created_time: 2026-05-26T11:01:00+08:00
edited_time: 2026-05-26T11:01:00+08:00
edited_entity: llm
---

## 源证据

- §3.1.4 给出 Leiden + 分层细分：
  > "we use Leiden community detection (Traag2019Leiden) in a hierarchical manner, recursively detecting sub-communities within each detected community until reaching leaf communities that can no longer be partitioned." (行 823–824)
  > "Each level of this hierarchy provides a community partition that covers the nodes of the graph in a mutually exclusive, collectively exhaustive way, enabling divide-and-conquer global summarization." (行 826)
- §3.1.5 给出递归摘要构造规则（行 838–843）：
  > "Leaf-level communities. The element summaries of a leaf-level community are prioritized and then iteratively added to the LLM context window until the token limit is reached. The prioritization is as follows: for each community edge in decreasing order of combined source and target node degree (i.e., overall prominence) ..."
  > "Higher-level communities. ... iteratively substitute sub-community summaries (shorter) for their associated element summaries (longer) until they fit within the context window."
- C0–C3 单元/token 表 `tab:community summaries`（行 438–446）：根级 C0 仅 34/55 个社群，token 数 26k/40k；叶级 C3 1310/2142 个社群，746k/1140k tokens；占 TS 全文 token 上限的 2.3–2.6% 与 66.8–73.5%。
- §2.2 给出"用社群划分代替 subgraph 引用"的设计动机：
  > "GraphRAG contrasts with these approaches by focusing on a previously unexplored quality of graphs in this context: their inherent modularity (newman2006modularity) and the ability to partition graphs into nested modular communities of closely related nodes" (行 735)
- 模板实现细节：
  > "We implemented Leiden community detection using the graspologic library (chung2019graspy)." (行 959)

## 卡片范围是否成立

卡片描述的全部机制都源于论文 §3.1.4 + §3.1.5，并未把"社群层级越深越好"或"换 Louvain 会更好"等论文未做的判断加进来。"加新文档时只需要增量更新被影响的社群子树"这一句是从论文显式提到的 MECE 划分 + Leiden 增量化能力的合理引申，但严格来说论文没有专门评测"增量更新"，所以放在"实践含义"段而非"机制"段。如果 comparison provenance 阶段觉得这一句越界，可改为"由于划分 MECE，理论上支持增量更新"。

## 发表门控结果

本轮未运行。

## 备注

- 与 `graphrag-global-sensemaking-pipeline` 卡片配套，本卡专门聚焦在"社群层"这一中间产物；流水线卡片只一笔带过。
- 与 `graphrag-root-community-token-efficiency` 卡片在 C0 token 数据上重叠，但本卡聚焦"层次结构本身"，那张卡聚焦"成本权衡"，由后续合并阶段裁定是否合并。
