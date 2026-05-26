---
schema: draft_card_provenance.v3
draft_card: ../cards/ragas-faithfulness-metric.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-26T11:00:00+08:00
edited_entity: llm
---

## 源证据

1. `agent_source_bundle.txt:131-147` —— Faithfulness 段完整算法描述。
2. `agent_source_bundle.txt:135-139` —— Statement decomposition prompt。
3. `agent_source_bundle.txt:141-146` —— Verification prompt。
4. `agent_source_bundle.txt:147` —— 分数公式 F = |V| / |S|。
5. `agent_source_bundle.txt:238-242` —— Table 1，Ragas Faithfulness accuracy = 0.95。
6. `agent_source_bundle.txt:271` —— "the Ragas prediction are in general highly accurate"。

## 卡片范围是否成立

- 卡片范围严格限定在 Faithfulness 的算法 + 公式 + 实证结果 + 边界，与 framework 卡 / 其它指标卡职责清晰分离。
- "context 本身错则 Faithfulness 不识别" 是基于指标定义（grounded in context）的合理边界声明，论文未直接讨论但定义里就这么限定。
- "prompt 含 demo 影响拆解粒度" 来自 footnote 2（"we include a demonstration as part of the prompt"）。

## 发表门控结果

本轮未运行。

## 备注

- 该卡是 mechanism 类，适合作为"如何用 LLM 做事实核查"主题的入口。
