---
id: runtime-agent-boundary
title: 运行时与代理的职责边界
status: accepted
card_type: distinction
tags: [llm-wiki, architecture, runtime, agent, responsibility-division]
created_time: 2026-06-05T10:00:00+08:00
edited_time: 2026-06-05T10:00:00+08:00
edited_entity: llm
source_ids: [clawhub-llm-wiki-karpathy]
justification: ../justification/runtime-agent-boundary.md
canonical_concept: runtime-agent-boundary
aliases: [运行时-代理边界, runtime-agent contract, 确定性运行时与智能代理分工]
summary: >-
  runtime-agent-boundary（运行时-代理边界 / runtime-agent contract）llm-wiki-karpathy 的架构核心：确定性运行时拥有路径/ID/验证/写入/清单追踪/导航生成，代理拥有摘要/OCR/综合/笔记分类/持续改进
related: [human-llm-role-division, representation-first-ingest, three-layer-architecture]
---

llm-wiki-karpathy 运行时在「Runtime Philosophy」中明确划定了确定性运行时与 LLM 代理之间的职责边界[^src-1]。

**运行时拥有（确定性、可审计）**[^src-2]：
- 规范路径（canonical paths）
- 规范 ID（canonical IDs）
- 验证（validation）
- 确定性写入（deterministic writes）
- 清单驱动的表示追踪（manifest-backed representation tracking）
- 生成的 wiki 导航（generated wiki navigation）

**代理拥有（需要智能、不确定性）**[^src-3]：
- 摘要（summarization）
- OCR、视觉处理或档案化工作（在运行时外部执行）
- 综合（synthesis）
- 决定产出归属为 output、concept、entity 还是 synthesis
- 持续改进 wiki 而非让价值困在对话中

这一划分不同于人机角色分工（human-llm-role-division）——后者描述的是人类与 LLM 在工作流层面的分工（人类策展/提问，LLM 执行维护），而本卡描述的是在 LLM 操作内部，确定性代码与智能代理之间的进一步分层。运行时将所有可确定性化的操作收归自身，保证可审计性和可重现性；将所有需要语义理解的操作留给代理[^src-4]。

## Footnotes

[^src-1]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "The runtime owns: ... The agent owns: ..."
[^src-2]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "The runtime owns: canonical paths, canonical IDs, validation, deterministic writes, manifest-backed representation tracking, generated wiki navigation"
[^src-3]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "The agent owns: summarization, OCR, vision, or profiling work performed outside the runtime, synthesis, deciding whether a result belongs in output, concept, entity, or synthesis, improving the wiki over time instead of leaving value trapped in chat"
[^src-4]: `data/raw/webpage/clawhub-llm-wiki-karpathy/text.txt` -- "Runtime Philosophy" -- "kb_prepare_source_bundle is the bridge between those layers for non-text assets"
