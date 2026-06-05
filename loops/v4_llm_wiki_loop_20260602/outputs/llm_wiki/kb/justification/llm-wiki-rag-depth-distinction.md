---
schema: justification_journal.v1
card: ../cards/llm-wiki-rag-depth-distinction.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/anthemcreation-fr-guide/text.txt`
源证据：
- L156 — "La difference fondamentale n'est pas la vitesse, c'est la profondeur du raisonnement."
- L156 — "Une LLM wiki repond depuis une connaissance deja synthetisee, avec des liens entre concepts, des contradictions resolues, et des syntheses pre-construites. Le raisonnement multi-hop (relier trois concepts distincts pour repondre a une question complexe) devient naturel."
- L158 — "Pour des wikis de 100 articles, le markdown structure suffit largement. La vector database devient utile seulement au-dela d'une certaine echelle"
范围论证：该材料明确提出 LLM Wiki 与 RAG 的根本区别在于推理深度而非速度，并具体阐述了多跳推理优势。这一 distinction 是原子性的（仅关于差异维度的定义），与现有 wiki-compounding-artifact 卡（关于复利积累的机制）互补但不重叠。
