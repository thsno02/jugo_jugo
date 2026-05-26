---
schema: draft_card_provenance.v3
draft_card: ../cards/lightmem-sleep-time-offline-parallel-update.md
material_id: arxiv-lightmem
digest_id: digest_arxiv-lightmem
source_paths:
  - data/raw/arxiv/arxiv-lightmem/agent_source_bundle.txt
created_time: 2026-05-26T11:07:00+08:00
edited_time: 2026-05-26T11:07:00+08:00
edited_entity: llm
---

## 源证据

- §3.3 Soft Updating at Test Time（行 855–866）：
  > "At test time, when memory entries arrive, LightMem directly inserts them into LTM with soft updates, thereby decoupling the update process from online inference. Due to real-time updates being converted to direct insertions, interaction latency is significantly reduced."
  > "$\mathcal{Q}(e_i) = \operatorname{Top}_{k}\{(e_j, \mathrm{sim}(v_i, v_j)) \mid t_j \geq t_i, j \neq i\}_{:n}$"
- §3.3 Offline Parallel Update（行 868–872）：
  > "The online update mechanism in existing memory frameworks enforces sequential updates, leading to a total latency that accumulates with each update."
  > "Since the update targets are independent across queues, updates can be executed in parallel, thereby greatly reducing the total latency."
- Case study（行 660–683）：直接给出 Hard update vs LightMem Soft update 的对比示例，含 Tokyo / Kyoto 的具体行内容。
- 论文显式指出 LLM 把"相关不冲突"误判成冲突的失败模式（行 656–658）。
- Online-only token cost 缩减比例：行 597–598。
- Update 是 baseline 流程中的最后一步（在线执行）的说明：Table `tab:detail_process` 行 213–263。

## 卡片范围是否成立

机制段落和数字全部对应论文 §3.3 与 case study；时间戳约束、并行性、case study 的"Tokyo + Kyoto"原文直接复用。"sleep-time 触发条件未严格定义"这一边界是从论文反向观察得到的：论文显示触发是"all entries inserted" 或 "update trigger" 两种描述，未给定具体策略——卡片里如实指出。

## 发表门控结果

本轮未运行。

## 备注

- 与 v2 中关于 memory consolidation / sleep replay 的卡片可能重叠（如果存在）。
- 与 `lightmem-three-stage-atkinson-shiffrin` 主卡互补：那张卡概括三模块，这张展开 Light3。
