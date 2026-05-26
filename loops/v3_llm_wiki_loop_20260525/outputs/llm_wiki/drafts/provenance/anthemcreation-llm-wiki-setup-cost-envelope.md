---
schema: draft_card_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-setup-cost-envelope.md
material_id: anthemcreation-fr-guide
digest_id: digest_anthemcreation-fr-guide
source_paths:
  - data/raw/webpage/anthemcreation-fr-guide/text.txt
created_time: 2026-05-26T12:00:00+08:00
edited_time: 2026-05-26T12:00:00+08:00
edited_entity: llm
---

## 源证据

- 5 步搭建流程（第 116–124 行）：
  > "Copiez le Gist original d'Andrej Karpathy depuis GitHub et collez-le dans votre agent LLM (Claude, OpenAI Codex ou Grok fonctionnent tous). Créez un répertoire vide sur votre machine. ... Ouvrez ce dossier dans Obsidian comme nouveau vault. ... Ajoutez vos premières sources brutes dans un sous-dossier séparé (ex. /sources/). ... Instruisez le LLM d'ingérer la première source en créant les pages initiales ..."。
- Obsidian 可替换（第 126 行）：
  > "Obsidian n'est pas obligatoire, mais il est recommandé par Karpathy pour son affichage graphique des liens. Des alternatives viables existent : VS Code avec une extension Markdown Preview Enhanced, ou Logseq qui gère aussi les backlinks bidirectionnels. L'essentiel reste que vos fichiers soient en markdown plat, compatible avec n'importe quel éditeur."。
- 成本表（第 130–136 行）：
  > "Obsidian + LLM open source (Llama 3) Gratuit 0 €/mois / Obsidian + Claude API Gratuit ~0,01 à 0,10 € par doc ingéré / Wiki de 100 documents (Claude) Moins de 10 € Faible (ingestions incrémentales)"。
- 规模限制（第 210 行）：
  > "Le système excelle à échelle personnelle, typiquement de 10 à quelques centaines de documents. Au-delà, la gestion des interliens peut devenir coûteuse en tokens et une vector search devient plus adaptée."。
- 弱 LLM 风险 + 无官方实现（第 210 行 + 第 162 行）：
  > "La qualité dépend directement du LLM utilisé pour les ingestions : un modèle faible peut propager des erreurs. Enfin, aucune implémentation officielle en code n'a été publiée par Karpathy au lancement, ce qui nécessite une configuration manuelle initiale basée sur le Gist." / "Un modèle trop faible peut propager des erreurs sans les signaler. Prévoyez une revue humaine périodique des pages clés"。

## 卡片范围是否成立

这张卡只承担"个人版搭建路径 + 成本上限 + 风险"。所有步骤、成本数字与限制条款均出自源原文，没有引入估算。"三条操作信号"是把成本表三行直接读为工程结论（先用 Claude 后迁移 / 成本线性 / 完全零费用版本可达），属于直接读出而非引申。

## 发表门控结果

本轮未运行。

## 备注

与 `anthemcreation-llm-wiki-three-layer-architecture` 互为搭档（前者讲 what，本卡讲 how + cost）。与 v2 的 `llm-knowledge-base-five-stage-workflow` 在"步骤化落地"方面可能有重叠，但本卡聚焦"5 分钟最小可行 + 成本封顶"，颗粒度不同。预计 `new_card`。
