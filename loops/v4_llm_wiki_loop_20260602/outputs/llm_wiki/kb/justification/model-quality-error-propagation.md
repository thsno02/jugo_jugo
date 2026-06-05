---
schema: justification_journal.v1
card: ../cards/model-quality-error-propagation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/webpage/anthemcreation-fr-guide/text.txt`
源证据：
- L162 — "La LLM wiki repose entierement sur la qualite du modele pour gerer les contradictions entre sources. Un modele trop faible peut propager des erreurs sans les signaler."
- L162 — "Prevoyez une revue humaine periodique des pages cles, surtout dans les premieres semaines."
- L162 — "La qualite de votre agents.md determine directement la fiabilite de la base."
- L110 — "Ce fichier d'instructions est le levier principal pour garder une wiki coherente sur la duree."
范围论证：该材料从模型能力维度阐述了源忠实性风险，与现有 source-faithfulness-risk 卡（聚焦多轮变换的知识漂移）形成互补视角。同时提出了 agents.md 质量和人工审查两项具体缓解措施，使其作为 operational_rule 独立成卡。复用 canonical_concept: source-faithfulness-risk。

## governance | 2026-06-05T15:00:00+08:00

操作：canonical 归一化
旧 canonical: source-faithfulness-risk → 新 canonical: model-error-propagation
理由：与 source-faithfulness-risk.md 共享 canonical 但主题不同——
本卡聚焦模型能力不足导致的错误传播，而非 wiki 内容偏离源文本的漂移风险。
