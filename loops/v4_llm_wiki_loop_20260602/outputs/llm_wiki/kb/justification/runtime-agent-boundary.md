---
schema: justification_journal.v1
card: ../cards/runtime-agent-boundary.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt`
源证据：
- "Runtime Philosophy" — "The runtime owns: canonical paths, canonical IDs, validation, deterministic writes, manifest-backed representation tracking, generated wiki navigation"
- "Runtime Philosophy" — "The agent owns: summarization, OCR, vision, or profiling work performed outside the runtime, synthesis, deciding whether a result belongs in output, concept, entity, or synthesis, improving the wiki over time instead of leaving value trapped in chat"
- "Runtime Philosophy" — "kb_prepare_source_bundle is the bridge between those layers for non-text assets"
范围论证：本卡描述运行时（代码）与代理（LLM）之间的职责划分，这是一个独立于 human-llm-role-division 的分层。后者处于工作流层面（人类 vs LLM），本卡处于系统实现层面（确定性代码 vs 智能代理）。两者正交：即使在 LLM 全权操作的范围内，仍需进一步区分什么由确定性程序处理、什么由具备理解力的代理处理。
