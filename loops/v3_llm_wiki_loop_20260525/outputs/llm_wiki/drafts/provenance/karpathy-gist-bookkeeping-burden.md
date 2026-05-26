---
schema: draft_card_provenance.v3
draft_card: ../cards/karpathy-gist-bookkeeping-burden.md
material_id: karpathy-gist-llm-wiki
digest_id: digest_karpathy-gist-llm-wiki
source_paths:
  - data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-26T11:50:00+08:00
edited_entity: llm
---

## 源证据

- 行 66（"Why this works" 完整段）："The tedious part of maintaining a knowledge base is not the reading or the thinking — it's the bookkeeping. ... Humans abandon wikis because the maintenance burden grows faster than the value. LLMs don't get bored, don't forget to update a cross-reference, and can touch 15 files in one pass. The wiki stays maintained because the cost of maintenance is near zero."
- 行 68："The human's job is to curate sources, direct the analysis, ask good questions, and think about what it all means. The LLM's job is everything else."
- 行 37："A single source might touch 10-15 wiki pages."
- 行 41：lint 段定义 LLM 周期性健康检查的具体维度——contradictions、stale claims、orphans、missing cross-references、data gaps。

## 卡片范围是否成立

本卡聚焦"维护成本是真瓶颈、LLM 把它降到零"这一论证。Karpathy 在 gist 中有完整逐字表述。"人侧分工"也来自原文。"维护负担超线性增长、新内容价值 sub-linear"是把原文"grows faster than the value"做简单数学化的解释，属于合理改写。"大规模下 LLM 也可能漏更新"是 Robin Cartier 等实践者已经在另一个材料里写过的边界（本卡用作 boundary note），未直接引用其他材料的具体来源。

## 发表门控结果

本轮未运行。

## 备注

- 与 v3 已有 idea-file-as-agent-era-artifact 主题相邻但视角不同：那张卡是"idea file as artifact"，本卡是"为什么这种模式能持续运转"。
- 在 Robin Cartier 来源中提到的"~200 页天花板"将另起一卡，本卡不展开。
