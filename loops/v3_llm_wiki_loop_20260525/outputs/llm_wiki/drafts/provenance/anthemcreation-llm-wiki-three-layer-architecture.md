---
schema: draft_card_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-three-layer-architecture.md
material_id: anthemcreation-fr-guide
digest_id: digest_anthemcreation-fr-guide
source_paths:
  - data/raw/webpage/anthemcreation-fr-guide/text.txt
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-26T11:50:00+08:00
edited_entity: llm
---

## 源证据

- 三层结构原文（第 78–86 行）：
  > "Le système repose sur trois couches distinctes : Sources brutes immuables ... Wiki gérée par LLM ... Fichier d'instructions : un fichier comme agents.md qui définit les règles de structure, de liaison et de comportement du LLM dans la wiki."。
- 写/读权限严格分离（第 104 行）：
  > "Les sources brutes restent immuables. Le LLM écrit dans la wiki, l'utilisateur lit la wiki. La séparation des rôles est stricte."。
- 编译类比（第 76 行）：
  > "les sources brutes sont comme du code source, et la wiki LLM est l'exécutable compilé. Vous ne re-compilez pas à chaque fois que vous lancez un programme."。
- LLM 在 ingestion 阶段做的四类动作（第 94–102 行）：
  > "Créer une nouvelle page d'entité ... Mettre à jour une page existante ... Signaler et synthétiser les contradictions ... Créer des backlinks automatiques entre pages liées"。
- agents.md 的权重（第 162 行）：
  > "La qualité de votre agents.md détermine directement la fiabilité de la base."。
- 编辑器要求（第 126 行）：
  > "L'essentiel reste que vos fichiers soient en markdown plat, compatible avec n'importe quel éditeur."。

## 卡片范围是否成立

这张卡承担"Karpathy LLM wiki 的三层结构 + 编译类比 + 写/读权限边界"。所有结论都直接来自原文具体段落，没有把原始 Gist 内容（卡片范围外）补进来。Ingestion 阶段四类动作和"agents.md 决定可靠性"也是法语原文的直接复述。卡内"为什么三层是必要的"由原文的 strict separation 语句支撑，没有引申。

## 发表门控结果

本轮未运行。

## 备注

v2 已存在两张相邻卡 `idea-file-as-agent-era-artifact` 与 `llm-knowledge-base-five-stage-workflow`，主题接近但视角不同（agent-era artifact / 五阶段 workflow）；本卡侧重"三层 + 权限分离 + 编译类比"这一具体分解，估计在 comparison_provenance 阶段会被打上 high similarity 但 distinction 充足。预计 `new_card` + possible related。
