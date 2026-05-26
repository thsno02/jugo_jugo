---
schema: draft_card_provenance.v3
draft_card: ../cards/alce-prompting-strategies.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-26T11:25:00+08:00
edited_entity: llm
---

## 源证据

- `sections/intro.tex` L1138-1143：实验结论汇总（Summ/Snippet、Interact、Rerank、ClosedBook+PostCite、passage 数 scaling）。
- `sections/appendix.tex` L327-331：Interact 的"check 后必须立即 output、最多 3 文档"硬限制。
- `sections/appendix.tex` `app_sec:propmt` L511-644：各策略的 instruction 模板（Vanilla / Summ / Snippet / Interact / InlineSearch / ClosedBook）。
- `header.tex` L206-225：策略代号缩写（`\vani`, `\summ`, `\snippet`, `\interact`, `\search`, `\rerank`, `\close`, `\posthoc`）。
- `sections/intro.tex` L1138：closed-book+PostCite 的判定语句。

## 卡片范围是否成立

卡片范围是"五种 prompting 策略 + 各自的取舍结论"，不涉及具体表格数字。把策略与结论合并是合理的，因为论文 introduction 自己也用同样方式做汇总（项目化罗列）。

- 每个策略的描述都能在 `app_sec:propmt` 的 instruction 表中找到原文模板。
- 结论行直接引用 `intro.tex` 项目化罗列的 (3)-(5) 条与 closed-book 的描述。
- "rerank 用 metric 当选择器"是源材料 `\rerank{}` 的同义复述。

未做的引申：

- 没把具体 baseline 得分写进卡（如 ChatGPT vs GPT-4 的 citation 分），那些应保留在 reference 表里。
- 没把 ALCE 三数据集的不同行为写成姊妹结论——这部分留给 `alce-three-evaluation-datasets`。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 卡片可能存在"prompting 策略对比"通用主题；区分点：本卡聚焦 long-form citation 任务下的取舍，不涉及代码 / agent / multi-hop。
