---
id: olw-rejection-feedback-loop
title: olw 拒稿反馈闭环机制
status: accepted
card_type: mechanism
tags:
- feedback-loop
- human-in-the-loop
- quality-control
- llm-pipeline
created_time: 2026-06-12 18:00:00+08:00
edited_time: 2026-06-12 18:00:00+08:00
edited_entity: llm
source_ids:
- repo-kytmanov-obsidian-local
evidence_basis: code_implementation
justification: ../justification/olw-rejection-feedback-loop.md
canonical_concept: olw-rejection-feedback-loop
aliases:
- rejection feedback
- rejection feedback loop
- olw reject
- auto-block
summary: olw 的拒稿反馈闭环：reject draft 时附带原因存入 state DB，下次 compile 该 concept 时注入 prompt（PREVIOUS REJECTIONS），LLM 需针对性修正。 同一 concept 连续 5 次 rejection 无 approval 则自动阻断 auto-block， 排除后续编译直至 olw unblock。rejection
  feedback loop auto-block 五次拒稿阻断。
related:
- olw-three-stage-pipeline
---

olw 实现了一套拒稿反馈闭环机制，使人工审阅意见能被 LLM 在下次编译时吸收 [^src-1] [^card-1]：

**反馈注入**：当用户通过 `olw review` 或 `olw reject --feedback "..."` 拒绝一篇 draft 时，拒绝原因被存储到 state database 中。下一次编译该 concept 时，prompt 中会包含：

```
PREVIOUS REJECTIONS — address these issues:
- [用户的反馈内容]
```

LLM 据此针对性修正 draft 内容。

**自动阻断（auto-block）**：同一 concept 连续被 reject 5 次而没有任何一次 approval，该 concept 将被自动阻断，排除在未来所有 compile 之外 [^src-2]。需要人工通过 `olw unblock "Concept"` 明确重新启用。

此机制体现了 "self-improving wiki" 的设计理念——每次审阅都使 wiki 变得更精确，而 auto-block 则避免 LLM 在无法满足要求的 concept 上反复浪费算力。

[^src-1]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Rejection feedback loop" P416-435 -- "The feedback is stored in the state database. On the next compile of that concept, the prompt includes: PREVIOUS REJECTIONS"
[^src-2]: `data/raw/github_repo/repo-kytmanov-obsidian-local/repo/README.md` -- "Rejection feedback loop" P431 -- "After 5 rejections of the same concept without an approval, the concept is auto-blocked"
[^card-1]: 该机制是 olw 三阶段管线 (olw-three-stage-pipeline) 中 compile→review 之间的反馈回路
