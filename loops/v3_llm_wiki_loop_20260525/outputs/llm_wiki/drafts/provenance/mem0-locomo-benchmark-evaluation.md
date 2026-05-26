---
schema: draft_card_provenance.v3
draft_card: ../cards/mem0-locomo-benchmark-evaluation.md
material_id: arxiv-mem0
digest_id: digest_arxiv-mem0
source_paths:
  - data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-26T11:45:00+08:00
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

本轮未运行。

## 备注

- 与 batch 内其它三张 Mem0 卡构成完整覆盖（管线、操作、图变体、评估）。
- v2 卡片中无对应基准评估卡片，无重叠。
- 注意：abstract 中 "26% over OpenAI" 是加权综合，未在 §4 主表中以单一行直接显示。卡片正文已用"加权后"的措辞描述，避免与表格数据冲突。
