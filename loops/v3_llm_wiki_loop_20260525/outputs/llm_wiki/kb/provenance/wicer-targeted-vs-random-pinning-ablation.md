---
schema: accepted_card_provenance.v3
card: ../cards/wicer-targeted-vs-random-pinning-ablation.md
material_id: arxiv-wicer
digest_id: digest_arxiv-wicer
source_paths:
  - data/raw/arxiv/arxiv-wicer/agent_source_bundle.txt
draft_card: ../../drafts/cards/wicer-targeted-vs-random-pinning-ablation.md
draft_provenance: ../../drafts/provenance/wicer-targeted-vs-random-pinning-ablation.md
similarity_result: ../../drafts/similarity/wicer-targeted-vs-random-pinning-ablation.json
comparison_provenance: ../../drafts/comparison/wicer-targeted-vs-random-pinning-ablation.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:30:00+08:00
  gate_notes: 6/6 通过；Table 5 +0.16 vs +0.95、5.9× 差距、16/17 主题胜、local_education 反例均回到 §6.4（L888–937）。
created_time: 2026-05-26T11:15:00+08:00
edited_time: 2026-05-27T14:30:00+08:00
edited_entity: llm
---

## 源证据

- 控制实验设定（第 894–896 行）：
  > "for each score-1 failure, a random 50–100 word passage from a random source document is pinned instead of the diagnosed critical facts. All other parameters are identical to WiCER. Each topic uses an independent blind compilation; blind baselines differ slightly from Table tab:wicer due to LLM compiler non-determinism."。
- Table 5 数据（第 905–928 行）逐主题列出 Blind / Random Pin / WiCER 三列质量，并给出 Mean 行：
  > "Mean 2.23 / 2.39 / 3.18"。
- 结果总结（第 930–937 行）：
  > "random pinning improves only +0.16 over blind compilation, while WiCER achieves +0.95—a 5.9× larger gain, winning sixteen of seventeen topics. The sole exception (local_education) is the same topic where WiCER itself shows 0% recovery, suggesting compilation-resistant structure. These results confirm that WiCER's gains stem from targeted diagnosis, not the pinning mechanism itself."。
- 主表里 local_education 的 0% 行（第 862 行）：
  > "local_education 2.41 / 38.8% 2.41 / 38.8% 3.37 0% ---"。

## 卡片范围是否成立

这张卡只承担一件事：**报告并解读 WiCER 论文的 ablation 实验**。所有数字、唯一反例主题、控制实验的 50–100 词设定都直接来自论文 §6.4 与 Table 5；"诊断信号比加密度重要"是对 +0.16 vs +0.95 这一对照的直接解读，没有引入论文外的因素。Card 末尾"任何 failure-driven 强化都该带 random control"是工程通则，但表述方式留在了"WiCER 是这种 control 的范例"层面，不算超范围。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:30:00+08:00
- 检查要点：
  - 非标题复述：正文展开 ablation 设定、数字、三条解读与工程教训。
  - 知识密度：实验设定 + 反事实数字 + CEGAR spurious 解释。
  - 源支撑：source_ids 含 arxiv-wicer；§6.4 完整 verbatim。
  - References / Footnotes 齐备。
  - frontmatter 完整且合法。
  - related 已填充：5 张 WiCER / RAGChecker / ARES 相邻卡。

## 备注

主卡 `wicer-cegar-compile-evaluate-refine` 解释机制为什么应该收敛；本卡用 ablation 提供"该机制的功劳归于诊断而非 pinning"的反事实证据，两卡互为支撑。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/wicer-targeted-vs-random-pinning-ablation.md`
- draft provenance: `../../drafts/provenance/wicer-targeted-vs-random-pinning-ablation.md`
- similarity: `../../drafts/similarity/wicer-targeted-vs-random-pinning-ablation.json`
- comparison provenance: `../../drafts/comparison/wicer-targeted-vs-random-pinning-ablation.md`
