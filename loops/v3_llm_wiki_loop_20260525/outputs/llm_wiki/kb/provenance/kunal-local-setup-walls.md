---
schema: accepted_card_provenance.v3
card: ../cards/kunal-local-setup-walls.md
material_id: kunal-local-knowledge-base
digest_id: digest_kunal-local-knowledge-base
source_paths:
  - data/raw/webpage/kunal-local-knowledge-base/text.txt
draft_card: ../../drafts/cards/kunal-local-setup-walls.md
draft_provenance: ../../drafts/provenance/kunal-local-setup-walls.md
similarity_result: ../../drafts/similarity/kunal-local-setup-walls.json
comparison_provenance: ../../drafts/comparison/kunal-local-setup-walls.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T10:26:00+08:00
  gate_notes: 6/6 项通过：三堵墙完整 verbatim + 修复路径 + 总体定性 + 边界；"90% 想试的人"是解读层措辞，已在 comparison 中标注属可接受范围。
created_time: 2026-05-26T12:15:00+08:00
edited_time: 2026-05-27T10:26:00+08:00
edited_entity: llm
---

## 源证据

- 行 95："Here's where things get real. The README makes it look straightforward: clone the repo, compile, tokenize your data, run. In practice, I hit three walls that cost me an entire Saturday."
- 行 97（Wall 1 完整段）：macOS Clang 无 OpenMP；brew install gcc；HN 最常见抱怨；error message 不指向真相。
- 行 99（Wall 2 完整段）：单文件输入；400 markdown 文件；需自写预处理脚本。
- 行 101（Wall 3 完整段）：M2 CPU 30+ 秒；CUDA 数秒；硬件门槛。
- 行 119–129：作者总结"概念正确、当前实现太早"以及四点改进路径（更好的小模型、更聪明的 chunking/检索、真正 UI、增量索引）。

## 卡片范围是否成立

本卡聚焦"三堵墙"这一可操作守则，是对 Kunal 文章工程价值最高的一段的提炼。每堵墙的描述与修复路径直接来自原文。"类别稳定"是合理引申。"它解释为什么 Karpathy markdown + agent 路线更可推广"是把两个来源（Kunal vs Karpathy gist）做横向对照，明确标注为本卡的解读，不是 Kunal 文章主张。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T10:26:00+08:00
- 检查要点：
  - 非标题复述：以 Wall 1/2/3 + 为什么做成守则 + 操作含义 + 边界四段实质展开。
  - 知识密度：3 堵墙具体修复路径 + 4 点改进路径外推 + 类别稳定性论证。
  - 源支撑：kunal-local-knowledge-base 行 95-129 verbatim。
  - References / Footnotes 存在。
  - frontmatter 完整。
  - related 字段 3 个 v3 draft id。
  - "90% 想试的人"属 draft 解读层措辞（comparison 阶段已点名），原文未给百分比；门控接受，因为整体证据完整且解读边界已标注。

## 备注

- 与 kunal-llm-c-rag-misinterpretation 互补：前者讲 Kunal 解读偏差，本卡讲 Kunal 实操经验里的真实价值。
- 与 robin-cartier-scale-ceiling 互补：两张卡共同构成"本地 wiki 模式的实际限制"全景图。
- Adoption 阶段观察：v2 候选 #2 撞 `rag/文档` 但论点是 wiki vs RAG 性质对比，与本卡部署工程清单论点轴正交，不可 fusion。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/kunal-local-setup-walls.md`
- draft provenance: `../../drafts/provenance/kunal-local-setup-walls.md`
- similarity: `../../drafts/similarity/kunal-local-setup-walls.json`
- comparison provenance: `../../drafts/comparison/kunal-local-setup-walls.md`
