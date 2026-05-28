---
id: llm-wiki-karpathy-lint-grounding-trail
title: kb_lint 强制 wiki 内容必须有 grounding trail
status: accepted
card_type: operational_rule
tags: [#llm-wiki, #lint, #grounding, #karpathy, #wiki-health]
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-28T11:38:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
provenance_card: ../provenance/llm-wiki-karpathy-lint-grounding-trail.md
aliases: ["kb_lint", "wiki health checks"]
related: [llm-wiki-karpathy-runtime-vs-agent-split, llm-wiki-karpathy-multimodal-representation-path, karpathy-llm-kb-three-operations, llm-wiki-contradictions-are-assets, enterprise-llm-wiki-drift-detection-loop, nvk-llm-wiki-audit-and-librarian]
---

`@harrylabs/llm-wiki-karpathy` 把 wiki health 直接做成 runtime 的一等品[^v3-1]：`kb_lint` 是 deterministic 的，每次运行同一份 vault 必出同样的告警集合。lint 检查项不是纯结构性的，而是同时对"内容是否有 grounding"做检测，这让 wiki 内部的可信度可以被工具复核。

README 列出的 lint 检查项[^src1]（一一对应 wiki 失败模式）：

- **missing representation trails**：source note 引用了非文本资产，但 `.llm-kb/representations/` 下没有相应 OCR / vision / metadata representation[^v3-2]。表示这条 note 是"agent 看了图说话"，没有可复核的中间产物。
- **stale representations**：representation 比对应资产更老，意味着资产已更新但 representation 没重生成；wiki 仍引用旧理解。
- **inconsistent asset_paths**：source note 的 `asset_paths` 与 manifest 里 reviewed asset refs 不对齐——意味着 agent 写笔记时引用了未真正审查过的资产。
- **isolated pages**：没有任何反向链接的孤岛页面，提示这页知识没有被整合进 wiki 网络。
- **stale source coverage**：某些 source 已经被 wiki 反复展开，但底层 raw 已更新而 source note 未跟进。
- **unsupported claims**：wiki 里的主张找不到 source 支撑。这是 Karpathy 个人 vault 健康检查的核心动作的 runtime 等价物。
- **contradiction candidates**：多份 source 对同一事实给出冲突说法的候选清单——agent 决定如何裁决，但 lint 先把候选暴露出来。
- **missing high-value pages**：通过 `kb_map_gaps` 识别出"应该有但不存在"的笔记，对应 Karpathy 工作流里"agent 发现知识缺口"的步骤。

操作含义：

- **lint 是写完后的强制门槛，而不是可选检查**——runtime 把 lint 暴露成顶层命令，意味着任何 wiki 发布前都应该跑一次。
- **lint 不修复，agent 修复**：lint 列出告警；修复（重生成 representation、补 backlink、消解矛盾、补缺笔记）需要 agent 决策。这条规则与 runtime/agent 责任分割一致。
- **多模态 wiki 必须有 "believable review trail"**[^src2]：仅靠 source note 文本无法证明 agent 真的读了 PDF / 图片；representation trail 是这份证据。无 trail 的多模态 note 会被 lint 拦下。

边界：

- lint 是 deterministic 的结构 / grounding 检查，**不**做语义正确性判断。例如 representation 里的 OCR 文本本身错了、agent 把"红色"看成"蓝色"，lint 无法发现——这类错误依赖 agent / 人工 review。
- lint 项依赖 manifest schema v2 的字段，旧 vault 升级时需要先跑 `kb_repair_source_ids` 等修复命令。
- `contradiction candidates` 不会主动消解；这条信号只是输入，最终需要 agent / 用户做语义裁决[^v3-3]。

## Footnotes

[^src1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` L73 — "deterministic lint for schema and wiki health, including warnings for missing representation trails, stale representations, inconsistent asset_paths, isolated pages, stale source coverage, unsupported claims, contradiction candidates, and missing high-value pages"
[^src2]: 同文件 L174-175 — "kb_lint stays deterministic, but now also checks whether multimodal source notes have a believable review trail before the wiki starts depending on them."
[^src3]: 同文件 L67-68 — "deterministic gap mapping and promotion through kb_map_gaps and kb_promote_gap"
[^v3-1]: [llm-wiki-karpathy-runtime-vs-agent-split](llm-wiki-karpathy-runtime-vs-agent-split.md) — runtime / agent 责任分割的本卡。
[^v3-2]: [llm-wiki-karpathy-multimodal-representation-path](llm-wiki-karpathy-multimodal-representation-path.md) — representation-first ingest 路径与 `.llm-kb/representations/` 的本卡。
[^v3-3]: [llm-wiki-contradictions-are-assets](llm-wiki-contradictions-are-assets.md) — 矛盾作为资产、人做最终裁决的本卡。
