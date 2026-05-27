---
schema: accepted_card_provenance.v3
card: ../cards/idea-file-as-agent-era-artifact.md
material_id: karpathy-x-launch-post
digest_id: digest_karpathy-x-launch-post
source_paths:
  - data/raw/webpage/karpathy-x-launch-post/text.txt
draft_card: ../../drafts/cards/idea-file-as-agent-era-artifact.md
draft_provenance: ../../drafts/provenance/idea-file-as-agent-era-artifact.md
similarity_result: ../../drafts/similarity/idea-file-as-agent-era-artifact.json
comparison_provenance: ../../drafts/comparison/idea-file-as-agent-era-artifact.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:36:00+08:00
  gate_notes: 四项判据全部通过；draft 把 v2 两张同源 known_fact（idea-file-abstract-vague + idea-file-share-the-idea）综合到 concept 层，并补三个成立条件与 idea file ≠ README ≠ 设计文档的下游边界。
v2_anchor:
  card_id: idea-file-abstract-vague
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/idea-file-abstract-vague.md
  comparison_decision: provenance_delta
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-27T14:36:00+08:00
edited_entity: llm
---

## 源证据

- 主要片段：`data/raw/webpage/karpathy-x-launch-post/text.txt`，JSON 指针 `$.tweet.text`。
  - "I wanted share a possibly slightly improved version of the tweet in an \"idea file\". The idea of the idea file is that in this era of LLM agents, there is less of a point/need of sharing the specific code/app, you just share the idea, then the other person's agent customizes & builds it for your specific needs."
  - "You can give this to your agent and it can build you your own LLM wiki and guide you on how to use it etc. It's intentionally kept a little bit abstract/vague because there are so many directions to take this in."
- 相关产物：gist 链接 `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`（idea file 本身；本轮未读取）。

## 卡片范围是否成立

卡片的范围正是该推文中提出的概念主张：在智能体时代，分发单元从"应用 / 代码"转移为"刻意抽象的想法，由接收者的智能体去落地"。推文文本直接支持卡片正文中三个子主张：

1. 接收者智能体承担实际构建——由 "your agent and it can build you your own LLM wiki and guide you on how to use it" 支撑。
2. 想法的杠杆率高于代码——由 "less of a point/need of sharing the specific code/app" 支撑。
3. 刻意欠规格化是优点——由 "intentionally kept a little bit abstract/vague because there are so many directions to take this in" 支撑。

卡片中关于 "idea file ≠ README ≠ 设计文档" 的边界澄清来自对原文的引申，原文并未直接表述；它被作为澄清放在正文里，目的是防止显而易见的误用，而不是当作引用。

## 发表门控结果

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:36:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确 v2 top1（idea-file-abstract-vague）与 v2 top2（idea-file-share-the-idea）和 draft 取自同一 `$.tweet.text`，draft 把两条 known_fact 综合到 concept 层。
  - v2 anchor body 已读：v2 idea-file-abstract-vague statement「idea file 被有意保持抽象 / 模糊」已与 draft "刻意欠规格化反而是优点" 对照。
  - draft 不破坏 v2 scope：draft 在 v2 两张紧致 known_fact 之上加 (a) "agent 时代分发载体"概念框架、(b) 三个成立条件、(c) idea file ≠ README ≠ 设计文档 ≠ spec 的下游边界——均超出 v2 单句 scope。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径；comparison 备注同时建议 audit 阶段反向链接到 v2 top2 idea-file-share-the-idea。

## 备注

- 本卡片只来源于外层推文文本，不来源于被引用的 "LLM Knowledge Bases" 推文；因此与从那条 quote 中抽取的工作流卡片的范围不重叠。
- adoption 阶段观察：v2 同源还有 `idea-file-share-the-idea`（comparison top2，score 0.182），作为下游使用边界亦应反向链接；本 kb provenance 主 v2_anchor 仅记录用户指定的 `idea-file-abstract-vague`，audit 阶段可加二级链接。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/idea-file-as-agent-era-artifact.md`
- draft provenance: `../../drafts/provenance/idea-file-as-agent-era-artifact.md`
- similarity: `../../drafts/similarity/idea-file-as-agent-era-artifact.json`
- comparison provenance: `../../drafts/comparison/idea-file-as-agent-era-artifact.md`
