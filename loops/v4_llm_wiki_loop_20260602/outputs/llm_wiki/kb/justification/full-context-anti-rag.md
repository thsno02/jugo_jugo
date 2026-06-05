---
schema: justification_journal.v1
card: ../cards/full-context-anti-rag.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/obsidian-community-plugin/text.txt`
源证据：
- L343-344 — "This plugin follows Karpathy's philosophy: feed the LLM full Wiki context, not chunked RAG retrieval. Long-context models are strongly recommended"
- L347 — "Why not RAG? Karpathy's original critique argues that RAG fragments knowledge and breaks the LLM's ability to reason across the full knowledge graph."
- L114 — "ChatGPT knows the internet. LLM-Wiki knows you... Every response is a trailhead, not a dead end."
- L370 — "For local models (Ollama): context windows are typically smaller (8K-128K). Consider using a cloud provider for ingestion + local model for query."
范围论证：现有 KB 有 rag-wiki-synthesis-distinction（写入循环区分）和 llm-wiki-rag-depth-distinction（推理深度区分），但都未聚焦于全上下文 vs 分块检索这一具体的架构实现选择及其对模型选型的直接后果；该卡填补这一视角
