---
schema: accepted_card_provenance.v3
card: ../cards/anthemcreation-llm-wiki-three-layer-architecture.md
material_id: anthemcreation-fr-guide
digest_id: digest_anthemcreation-fr-guide
source_paths:
  - data/raw/webpage/anthemcreation-fr-guide/text.txt
draft_card: ../../drafts/cards/anthemcreation-llm-wiki-three-layer-architecture.md
draft_provenance: ../../drafts/provenance/anthemcreation-llm-wiki-three-layer-architecture.md
similarity_result: ../../drafts/similarity/anthemcreation-llm-wiki-three-layer-architecture.json
comparison_provenance: ../../drafts/comparison/anthemcreation-llm-wiki-three-layer-architecture.md
gate:
  type: fusion_audit
  result: passed
  decided_at: 2026-05-27T14:32:00+08:00
  gate_notes: 四项判据全部通过；draft 作为 Anthem Création 法语二手综述，在 v2 三层架构卡 scope 外补充了 compilation 类比、严格写读权限分离、ingestion 四类动作、agents.md 决定可靠性。
v2_anchor:
  card_id: llm-wiki-three-layer-architecture
  card_path: loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
  comparison_decision: provenance_delta
created_time: 2026-05-26T11:50:00+08:00
edited_time: 2026-05-27T14:32:00+08:00
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

- 类型：fusion_audit
- 结果：passed
- 决定时间：2026-05-27T14:32:00+08:00
- 检查要点：
  - 三问被实质回答：comparison 明确说明 v2 卡来源 Karpathy gist 第 25–33 行，本 draft 来源 Anthem Création 2026-04-12 法语博客对同 gist 的综述。
  - v2 anchor body 已读：v2 卡 statement「该来源把 LLM Wiki 架构分成三个层次：原始来源、wiki 和 schema」已与 draft 三层翻译对照。
  - draft 不破坏 v2 scope：核心事实（三层划分）与 v2 一致，draft 新加的 compilation 类比、严格权限分离三句话、ingestion 四类动作、agents.md 可靠性、flat markdown 建议均在 v2 紧致 scope 之外。
  - provenance 链可追溯：本文件显式记录 v2_anchor + comparison_provenance 路径。

## 备注

v2 已存在两张相邻卡 `idea-file-as-agent-era-artifact` 与 `llm-knowledge-base-five-stage-workflow`，主题接近但视角不同（agent-era artifact / 五阶段 workflow）；本卡侧重"三层 + 权限分离 + 编译类比"这一具体分解，估计在 comparison_provenance 阶段会被打上 high similarity 但 distinction 充足。预计 `new_card` + possible related。

- adoption 阶段观察：v2 卡片由 Karpathy gist 一手抽取，本 draft 来自法语二手综述；并存使得三层架构有原文 + 第三方独立背书两种证据形态。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/anthemcreation-llm-wiki-three-layer-architecture.md`
- draft provenance: `../../drafts/provenance/anthemcreation-llm-wiki-three-layer-architecture.md`
- similarity: `../../drafts/similarity/anthemcreation-llm-wiki-three-layer-architecture.json`
- comparison provenance: `../../drafts/comparison/anthemcreation-llm-wiki-three-layer-architecture.md`
