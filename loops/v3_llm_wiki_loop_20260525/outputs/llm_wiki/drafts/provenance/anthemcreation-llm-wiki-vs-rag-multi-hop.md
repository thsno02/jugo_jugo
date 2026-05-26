---
schema: draft_card_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-vs-rag-multi-hop.md
material_id: anthemcreation-fr-guide
digest_id: digest_anthemcreation-fr-guide
source_paths:
  - data/raw/webpage/anthemcreation-fr-guide/text.txt
created_time: 2026-05-26T11:55:00+08:00
edited_time: 2026-05-26T11:55:00+08:00
edited_entity: llm
---

## 源证据

- 核心差异："不是速度，是推理深度"（第 156 行）：
  > "La différence fondamentale n'est pas la vitesse, c'est la profondeur du raisonnement. ... Le raisonnement multi-hop (relier trois concepts distincts pour répondre à une question complexe) devient naturel."。
- 适用规模 10–几百篇（第 154 行 + 第 210 行）：
  > "La LLM wiki, elle, excelle dans un registre différent : la connaissance personnelle à échelle individuelle, de 10 à quelques centaines de documents." / "Le système excelle à échelle personnelle, typiquement de 10 à quelques centaines de documents. Au-delà, la gestion des interliens peut devenir coûteuse en tokens et une vector search devient plus adaptée."。
- LLM 弱会传染错误（第 162 行 + 第 210 行）：
  > "Un modèle trop faible peut propager des erreurs sans les signaler." / "La qualité dépend directement du LLM utilisé pour les ingestions : un modèle faible peut propager des erreurs."。
- 演化方向之一：RAG-vector 混合（第 174 行）：
  > "L'hybridation RAG-vector pour les déploiements en équipe ou à l'échelle entreprise"。
- 编译类比（第 76 行 + 第 202 行 FAQ）：
  > "le RAG re-compile à chaque fois, la LLM wiki lance directement l'exécutable."。

## 卡片范围是否成立

这张卡只承担 "LLM wiki vs RAG 的差异" 与"它的边界"。对比表的五个维度（时机 / 单位 / 矛盾处理 / 推理深度 / 适用规模）均能在原文找到对应句子，没有引入论文外的对比维度。边界条件（规模 / 模型质量 / 无官方实现）逐条来自 FAQ 与 vs RAG 节，没有越界。最后一段"不是替代 RAG 而是让出位置"是把原文 framing 与"个人量级"陈述合并的中文总结，仍然在原文允许范围内。

## 发表门控结果

本轮未运行。

## 备注

与 v2 已有 `auto-index-replaces-rag-at-small-scale` 在主题上邻近但角度不同——v2 卡讨论"小规模 auto-index 替代 RAG"的判断，本卡讨论"LLM wiki vs RAG"的差异和适用区间。预计 `new_card`，需要在 comparison_provenance 阶段交叉评估是否补充 related。
