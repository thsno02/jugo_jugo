---
schema: draft_card_provenance.v3
draft_card: ../cards/locomo-persona-event-graph-pipeline.md
material_id: arxiv-locomo
digest_id: digest_arxiv-locomo
source_paths:
  - data/raw/arxiv/arxiv-locomo/agent_source_bundle.txt
created_time: 2026-05-26T14:05:00+08:00
edited_time: 2026-05-26T14:05:00+08:00
edited_entity: llm
---

## 源证据

- 第 238-246 行（pipeline overview）：persona / temporal event graph / agent architecture / human filter 四节大纲。
- 第 248-251 行（persona 章节）："select an initial persona statement $p_c$ from the MSC dataset ... employ \texttt{gpt-3.5-turbo} as $\mathcal{M}$ to expand these into full persona statement $p$."
- 第 254-258 行（temporal event graph）：`\texttt{text-davinci-003}` 生成事件 + 因果连接，6-12 个月 / ≤25 事件 / 每批 $k=3$ 迭代生成。
- 第 263-272 行（reflect & respond）：定义 $w_k$、$o_{k_j}$、$\mathcal{H}_s$、$\mathcal{H}_l$，以及 response 条件。
- 第 275-284 行（image sharing & reaction）：caption→keyword→web search→BLIP-2 captioning。
- 第 290 行（人工编辑）：约 15% turn 编辑、19% 图片处理。

## 卡片范围是否成立

- 三模块（persona / event graph / reflect-respond）来自原文小节标题，没有合并或拆分。
- "事件图作为长期一致性 anchor"是对原文 reflect/respond 公式的归纳，原文确实显式把事件窗口加入 response 条件，因此是合理引申。
- "image 长期一致性丧失"在 limitations 章节有原话支撑（第 515 行 "the images in our dataset can be replaced with their captions without much loss of information"），不属于过度推断。

## 发表门控结果

本轮未运行。

## 备注

- 与 mem0 卡片可能存在概念重叠（observation / summary 两层记忆），建议在 comparison_provenance 时统一术语：observation 在 LoCoMo 指"assertion about speaker"，在 mem0 中可能含义不同。
