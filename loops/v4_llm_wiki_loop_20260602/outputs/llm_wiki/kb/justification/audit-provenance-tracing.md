---
schema: justification_journal.v1
card: ../cards/audit-provenance-tracing.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/llm-wiki-net/text.txt`
源证据：
- L56-58 — "Answer the broader trust question. Reuse the librarian pass, trace outputs across raw/, wiki/, and output/, detect drift, inspect provenance, and do fresh research when local evidence is not enough."
- L326-327 — "Audit walks that full artifact graph. It can trace an output back through the wiki state and raw sources it depended on, then escalate into fresh research when the stored evidence is stale or incomplete."
范围论证：审计溯源是一个独立的验证机制，具有明确的输入（制品图）、操作（追踪+漂移检测+升级研究）和产出（信任评估）。它回应了 source-faithfulness-risk 卡中识别的风险，但作为一个机制而非风险描述，构成独立卡片。
