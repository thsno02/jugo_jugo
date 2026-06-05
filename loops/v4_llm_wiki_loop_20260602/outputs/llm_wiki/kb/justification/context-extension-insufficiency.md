---
schema: justification_journal.v1
card: ../cards/context-extension-insufficiency.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/arxiv/arxiv-mem0/agent_source_bundle.txt`
源证据：
- sections/intro.tex — "these improvements merely delay rather than solve the fundamental limitation"
- sections/intro.tex — "simply presenting longer contexts does not ensure effective retrieval or utilization of past information, as attention mechanisms degrade over distant tokens"
- sections/result.tex — Table 2 full-context row: 26031 tokens, p95=17.117s, Judge=72.90%
范围论证：该卡片记录 Mem0 论文对上下文窗口扩展的批判性论证，与 KB 中已有的 context-window-degradation 互补但不重叠——本卡聚焦于"为什么扩展窗口不能替代持久记忆"的论证逻辑和实证证据，而非窗口退化的一般现象。
