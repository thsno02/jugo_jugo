---
schema: accepted_card_provenance.v3
card: ../cards/mem0-locomo-benchmark-evaluation.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
draft_card: ../../drafts/cards/mem0-locomo-benchmark-evaluation.md
draft_provenance: ../../drafts/provenance/mem0-locomo-benchmark-evaluation.md
similarity_result: ../../drafts/similarity/mem0-locomo-benchmark-evaluation.json
comparison_provenance: ../../drafts/comparison/mem0-locomo-benchmark-evaluation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T11:57:00+08:00
  gate_notes: 6/6 项通过；主表四类 J 数字 + RAG/full-context 对比 + 91% p95 降幅 + 论文未声称的边界齐备。
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-27T11:57:00+08:00
edited_entity: llm
---

## 源证据

- 第 1010–1011 行（`experiment_setup.tex`）：
  > "The LOCOMO dataset is designed to evaluate long-term conversational memory in dialogue systems. It comprises 10 extended conversations, each containing approximately 600 dialogues and 26000 tokens on average, distributed across multiple sessions ... originally included an adversarial question category, which was designed to test systems' ability to recognize unanswerable questions. However, this category was excluded from our evaluation."
- 第 1047–1085 行（`result.tex` 主表 verbatim）：F1/B1/J 数据，所有方法。
- 第 1218–1264 行（latency_comparison 表）：search/total 延迟与 token，含 RAG 各 chunk size 配置、full-context、A-Mem、LangMem、Zep、OpenAI、Mem0、Mem0g。
- 第 689–691 行（abstract）：26% over OpenAI、91% p95 lower、>90% token cost 节省。
- 第 1313–1318 行：Zep ~600k vs Mem0 ~7k vs Mem0g ~14k 的 token 占用对比 + Zep 异步图构建的运营观察。

## 卡片范围是否成立

- 卡片以 source_claim 类型记录论文报告的评估结果，不引申算法、不替论文做判断。
- 直接来自源：四类问题 J 数据、延迟数据、token 占用、26%/91% 抽象声明、Zep 600k 等数字。
- 引申点："论文未声称的事"那一节是对论文边界的诚实标注（评估排除 adversarial、未做多模态、未公布 NOOP 比率），这些都是从文中明显可见的缺席，非新增主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T11:57:00+08:00
- 检查要点：
  - source_claim 卡给出主表 + 时延 + token 三轴数字，非标题复述。
  - 知识密度合格。
  - source_ids 含 `arxiv-mem0`，正文锚到 result.tex 第 1047-1264 / 1297 / 1313-1318 行 + abs.tex 第 681-698 行。
  - 含 `## References` 与 `## Footnotes`。
  - frontmatter 字段完整。
  - related 已挂上 6 张相关卡。

## 备注

- 与 batch 内其它三张 Mem0 卡构成完整覆盖（管线、操作、图变体、评估）。
- 注意：abstract 中 "26% over OpenAI" 是加权综合，未在 §4 主表中以单一行直接显示。卡片正文已用"加权后"的措辞描述。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/mem0-locomo-benchmark-evaluation.md`
- draft provenance: `../../drafts/provenance/mem0-locomo-benchmark-evaluation.md`
- similarity: `../../drafts/similarity/mem0-locomo-benchmark-evaluation.json`
- comparison provenance: `../../drafts/comparison/mem0-locomo-benchmark-evaluation.md`
