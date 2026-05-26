---
schema: draft_card_provenance.v3
draft_card: ../cards/idea-file-as-agent-era-artifact.md
material_id: karpathy-x-launch-post
digest_id: digest_karpathy-x-launch-post
source_paths:
  - data/raw/webpage/karpathy-x-launch-post/text.txt
created_time: 2026-05-25T22:05:00+08:00
edited_time: 2026-05-26T09:30:00+08:00
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

本轮未运行。第一次正式生产 pass 只产出 draft + similarity；发表门控按 `LOOP_START_PROMPT.md` 推后到下一阶段。

## 备注

- 本卡片只来源于外层推文文本，不来源于被引用的 "LLM Knowledge Bases" 推文；因此与从那条 quote 中抽取的工作流卡片的范围不重叠。
