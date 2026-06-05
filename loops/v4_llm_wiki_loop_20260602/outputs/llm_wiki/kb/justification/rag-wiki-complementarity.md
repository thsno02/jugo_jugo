---
schema: justification_journal.v1
card: ../cards/rag-wiki-complementarity.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/developersio-jp-pattern/text.txt`
源证据：
- L82-83 — "個人的には、「RAG か wiki か」は二択ではないと思っています"
- L83 — "アドホックな質問には RAG 的な検索が便利で、全体像の把握やプロジェクト横断の理解には wiki が便利"
- L99 — "自分の場合は Memory MCP（Mem0 + pgvector）という検索レイヤーが間に入っていて、RAG 的な検索と wiki の両方を使い分けています"
范围论证：既有 KB 从 Karpathy gist 角度将 RAG 定位为 wiki 的对照物（暗含替代关系），本文作者基于实际同时运用两者的经验，明确提出互补而非替代的关系。这是一个独立的 distinction，补充了现有 llm-wiki-pattern 卡中对 RAG 关系的单一视角。
