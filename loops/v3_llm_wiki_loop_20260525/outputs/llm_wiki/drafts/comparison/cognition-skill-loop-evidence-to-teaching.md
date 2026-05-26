---
schema: comparison_provenance.v3
draft_card: ../cards/cognition-skill-loop-evidence-to-teaching.md
draft_provenance: ../provenance/cognition-skill-loop-evidence-to-teaching.md
similarity_result: ../similarity/cognition-skill-loop-evidence-to-teaching.json
existing_cards:
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0.0769
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.0714
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.0625
decision: new_card
audit_required: false
created_time: 2026-05-26T16:00:00+08:00
edited_time: 2026-05-26T16:00:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三个候选 jaccard 都低于 0.08，shared_tokens 仅为「的」。draft 标题的实质 token 是 Cognition / 四步 / 巩固 / 衰减 / 教学 / 证据 / 闭环，与 v2 候选（全部是 Karpathy LLM-wiki 元描述卡）无任何术语级重合。属于 jaccard 噪声。

## 2. draft 与候选在哪里不同

draft 是 mechanism 卡，来源 `cognitionus-llm-wiki-guide`，描述 Cognition 产品把团队编码 agent 知识闭环拆成「Ask first / Capture work / Save skills / Retrieve later」四步，并对位「Evidence / Consolidation / Decay / Teaching」四机制；附带 confirm-first capture、person-specific retrieval、group-code setup 三条治理承诺。属于「agent 团队记忆产品设计」论点轴。

三张 v2 候选都是 Karpathy LLM-wiki 元描述：idea file 抽象性、wiki 三层架构、schema 配置文档。论点轴（团队 coding agent 技能产品 vs 个人 LLM wiki 模式）、来源类型（产品文案 vs Karpathy gist）、机制（人审 SKILL + 衰减 + 检索 vs LLM 写 markdown wiki）都不同。两者抽象上都属于「LLM 维护知识库」，但具体 layer 完全不交集。

## 3. 下一步的核心依据

shared_tokens 全是「的」，无语义关联。draft 引文具体到 L49-107 / L112-146 / L60-107，scope 自洽（产品宣传材料、未公开实现细节，已明示边界）。无任何 v2 卡可 merge 或 provenance_delta。综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：进入 publication_gate。

## 5. 备注

- Cognition skill loop 与 v2 KB 在抽象的「LLM 维护知识库」概念上同源，但本批次 v2 卡 scope 都严格限于 Karpathy 来源，不能 cross-link。未来若 KB 引入「跨来源概念聚合卡」类型可重新考虑。
