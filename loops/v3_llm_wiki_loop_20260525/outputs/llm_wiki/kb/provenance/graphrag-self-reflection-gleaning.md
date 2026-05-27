---
schema: accepted_card_provenance.v3
card: ../cards/graphrag-self-reflection-gleaning.md
material_id: arxiv-graphrag
digest_id: digest_arxiv-graphrag
source_paths:
  - data/raw/arxiv/arxiv-graphrag/agent_source_bundle.txt
draft_card: ../../drafts/cards/graphrag-self-reflection-gleaning.md
draft_provenance: ../../drafts/provenance/graphrag-self-reflection-gleaning.md
similarity_result: ../../drafts/similarity/graphrag-self-reflection-gleaning.json
comparison_provenance: ../../drafts/comparison/graphrag-self-reflection-gleaning.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:08:00+08:00
  gate_notes: 6/6 项通过：3×4 chunk×reflection 表 + logit bias=100 实现细节 + 边界，证据锚定到 §App E.2 与 fig:chunkentities。
created_time: 2026-05-26T15:00:00+08:00
edited_time: 2026-05-27T10:08:00+08:00
edited_entity: llm
---

## 源证据

- 行 60–77（`appendix.tex` §Self-Reflection）：
  - "*Self-reflection* is a prompt engineering technique where the LLM generates an answer, and is then prompted to evaluate its output for correctness, clarity, or completeness, then finally generate an improved response based on that evaluation."（行 64）
  - "Using larger chunk size is less costly in terms of calls to the LLM. However, the LLM tends to extract few entities from chunks of larger size."（行 67–68）
  - "GPT-4 extracted almost twice as many entity references when the chunk size was 600 tokens than when it was 2400."（行 69）
  - "we first ask the LLM to assess whether all entities were extracted, using a logit bias of 100 to force a yes/no decision."（行 72）
  - "If the LLM responds that entities were missed, then a continuation indicating that 'MANY entities were missed in the last extraction' encourages the LLM to detect these missing entities."（行 73）
  - "This approach allows us to use larger chunk sizes without a drop in quality (\autoref{fig:chunkentities}) or the forced introduction of noise."（行 74）

- 行 1441–1487（`self_reflection_figure.tex` 中的 `pgfplots` 曲线点）：实体引用数随 chunk size × reflection 迭代变化的原始数据。
  - 600 token：(0, 9348) → (1, 15976) → (2, 19491) → (3, 27240)
  - 1200 token：(0, 7119) → (1, 12877) → (2, 17794) → (3, 22399)
  - 2400 token：(0, 5761) → (1, 10606) → (2, 14897) → (3, 19433)

- 行 769–774（§3.1.1 Source Documents → Text Chunks）：chunk size 的权衡声明——"longer text chunks require fewer LLM calls for such extraction (which reduces cost) but suffer from degraded recall of information that appears early in the chunk"。

## 卡片范围是否成立

- 卡片主张的核心是"chunk size + gleaning 的双轴调参法则 + 具体数字 + logit bias=100 的实现细节"。这些都直接来自源文本，没有引申。
- 表格里的实体引用数是从 `fig:chunkentities` 的 pgfplots 坐标点逐字转录。
- 唯一带"操作含义"色彩的引申是"先把 chunk 设大再用 gleaning 补 recall"——这是 GraphRAG 论文叙事本身的策略（行 74 的"allows us to use larger chunk sizes without a drop in quality"直接支撑）。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:08:00+08:00
- 检查要点：
  - 非标题复述：以"问题数据 + 实现细节 + 为何 logit bias=100 + 操作含义 + 边界"五段实质展开。
  - 知识密度：3×4 chunk-reflection 表 + 实现步骤 + 边界三条。
  - 源支撑：appendix §Self-Reflection 与 fig:chunkentities 原始 pgfplots。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 6 个 v3 draft id。

## 备注

- 与现有 `graphrag-global-sensemaking-pipeline` 卡片不重复：那张卡片把 chunk → entity 抽取列为流水线第一步，但未展开 gleaning 细节与具体数字。
- v2 卡片层暂未发现相关条目（按 worker 规约未读 v2）。
- Adoption 阶段观察：comparison 三个 v2 候选 jaccard ≤ 0.07 只共享「的」，无 fusion 必要。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/graphrag-self-reflection-gleaning.md`
- draft provenance: `../../drafts/provenance/graphrag-self-reflection-gleaning.md`
- similarity: `../../drafts/similarity/graphrag-self-reflection-gleaning.json`
- comparison provenance: `../../drafts/comparison/graphrag-self-reflection-gleaning.md`
