---
schema: claude_code_theme.v1
theme: source_to_card_workflow
publish_status: sanitized
---

# Source To Card Workflow

Claude Code 交互反复确认了一条生产线：知识不是从主题目录里凭空写出来，而是从 source material 中被挖掘、拆分、证明和入库。

## Pipeline

```text
source material
-> routed read surface
-> questioning loop
-> draft card
-> justification journal
-> fusion decision
-> active KB card
```

## Key Decisions

- topic plan 只是建议，不是可执行事实来源；
- source mining 是核心动作；
- draft-first 比直接写入 KB 更可审计；
- provenance 是把 draft 做实为 fact-like card 的过程；
- card 应保持可读的 zet card 形态，不应退化成机器中间态。

## Full-Read Bias

Claude session 中一个重要纠偏是：大上下文模型下，防御性截断 source 会遗漏 paper 后半段的 evaluation、ablation、limitation 和 appendix。对于可承载的材料，默认策略应是完整读取，再做结构化提问。

## Evidence Basis

v5 引入 `evidence_basis`，把不同 source 类型区分开：

- experimental paper；
- theoretical paper；
- practitioner report；
- community discussion；
- documentation；
- code implementation。

这让 audit 可以按证据类型分层，而不是对所有卡使用同一标准。
