---
schema: draft_card_provenance.v3
draft_card: ../cards/kunal-local-setup-walls.md
material_id: kunal-local-knowledge-base
digest_id: digest_kunal-local-knowledge-base
source_paths:
  - data/raw/webpage/kunal-local-knowledge-base/text.txt
created_time: 2026-05-26T12:15:00+08:00
edited_time: 2026-05-26T12:15:00+08:00
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

本轮未运行。

## 备注

- 与 kunal-llm-c-rag-misinterpretation 互补：前者讲 Kunal 解读偏差，本卡讲 Kunal 实操经验里的真实价值。
- 与 robin-cartier-scale-ceiling 互补：两张卡共同构成"本地 wiki 模式的实际限制"全景图。
