---
schema: accepted_card_provenance.v3
card: ../cards/ragas-faithfulness-metric.md
material_id: arxiv-ragas
digest_id: digest_arxiv-ragas
source_paths:
  - data/raw/arxiv/arxiv-ragas/agent_source_bundle.txt
draft_card: ../../drafts/cards/ragas-faithfulness-metric.md
draft_provenance: ../../drafts/provenance/ragas-faithfulness-metric.md
similarity_result: ../../drafts/similarity/ragas-faithfulness-metric.json
comparison_provenance: ../../drafts/comparison/ragas-faithfulness-metric.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；两步算法、F = |V|/|S| 公式、prompt verbatim、WikiEval 0.95 与"context 错则失效"边界齐备。
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开两步算法、为何先拆再验证、实证、边界，多段 substantive。
  - 知识密度：机制 + 设计动机 + 数字 + 边界 + 误用条件全覆盖。
  - 源支撑：source_ids 含 arxiv-ragas；L133 / L141 / L147 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：7 张同源 / 跨论文姊妹卡。

## 备注

- 该卡是 mechanism 类，适合作为"如何用 LLM 做事实核查"主题的入口。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/ragas-faithfulness-metric.md`
- draft provenance: `../../drafts/provenance/ragas-faithfulness-metric.md`
- similarity: `../../drafts/similarity/ragas-faithfulness-metric.json`
- comparison provenance: `../../drafts/comparison/ragas-faithfulness-metric.md`
