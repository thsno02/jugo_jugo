---
schema: accepted_card_provenance.v3
card: ../cards/alce-prompting-strategies.md
material_id: arxiv-alce
digest_id: digest_arxiv-alce
source_paths:
  - data/raw/arxiv/arxiv-alce/agent_source_bundle.txt
draft_card: ../../drafts/cards/alce-prompting-strategies.md
draft_provenance: ../../drafts/provenance/alce-prompting-strategies.md
similarity_result: ../../drafts/similarity/alce-prompting-strategies.json
comparison_provenance: ../../drafts/comparison/alce-prompting-strategies.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:08:00+08:00
  gate_notes: 6/6 通过；七种策略 + 取舍结论原文 verbatim、行号定位齐全；边界涵盖数据集 / 模型缩放 / 成本。
created_time: 2026-05-26T11:25:00+08:00
edited_time: 2026-05-27T14:08:00+08:00
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

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:08:00+08:00
- 检查要点：
  - 不是标题复述：七种策略逐条解释 + 四条规则化结论 + 三条边界。
  - 知识密度足够：策略对比 + 操作规则 + 反例（Interact 不提升）+ 缩放边界（ChatGPT vs GPT-4）。
  - 源支撑齐全：所有策略与结论锁到 `agent_source_bundle.txt` 具体行段。
  - References 与 Footnotes 双章节存在。
  - frontmatter 完整合法，distinction 类型与正文一致。
  - related 已链 ALCE 系列与 ragchecker。

## 备注

- 与 v2 卡片可能存在"prompting 策略对比"通用主题；区分点：本卡聚焦 long-form citation 任务下的取舍，不涉及代码 / agent / multi-hop。
- comparison 显示与 v2 的 0.09 相似度来自 `的` 撞分，决策合理。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/alce-prompting-strategies.md`
- draft provenance: `../../drafts/provenance/alce-prompting-strategies.md`
- similarity: `../../drafts/similarity/alce-prompting-strategies.json`
- comparison provenance: `../../drafts/comparison/alce-prompting-strategies.md`
