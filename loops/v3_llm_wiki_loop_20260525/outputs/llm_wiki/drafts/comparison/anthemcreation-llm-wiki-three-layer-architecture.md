---
schema: comparison_provenance.v3
draft_card: ../cards/anthemcreation-llm-wiki-three-layer-architecture.md
draft_provenance: ../provenance/anthemcreation-llm-wiki-three-layer-architecture.md
similarity_result: ../similarity/anthemcreation-llm-wiki-three-layer-architecture.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.2857
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.25
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.125
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:30:00+08:00
edited_time: 2026-05-26T12:30:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-three-layer-architecture` 与本 draft **真共享主题**，不是 jaccard 误中：

- v2 卡片由 Karpathy 原始 gist 第 25–33 行直接抽取，statement 是"该来源把 LLM Wiki 架构分成三个层次：原始来源、wiki 和 schema"。
- 本 draft 由 Anthem Création 法语指南综述同一份 Karpathy gist，把三层翻译成 "Sources brutes immuables / Wiki gérée par LLM / Fichier d'instructions (agents.md)"，并显式给出"严格的写/读权限分离"。

这就是同一份 Karpathy 原始事实在两个不同来源中的并行表述。共享 token 只有 `llm / wiki / 三层 / 的`，但语义上对应的是同一架构划分。

top 2 `llm-wiki-schema-configuration-document` 是同 gist 的 schema 层细节，本 draft 也覆盖（用 agents.md 名字 + "agents.md 决定 fiabilité"）；同源同事实，邻接相关。

top 3 `llm-wiki-health-checks` 不在本 draft 范围；token 误中（仅 `llm / wiki`）。

## 2. draft 与候选在哪里不同

- **来源类型不同**：v2 卡片证据全部来自 Karpathy 原始 gist；本 draft 证据全部来自 Anthem Création 2026-04-12 法语博客（一个二手综述）。
- **覆盖维度不同（draft 更广）**：v2 卡片只断言"三层划分"这一条事实；本 draft 在三层之外增加 (a) "compilation 类比（raw=source code, wiki=executable）"、(b) "严格写/读权限分离"显式三句、(c) ingestion 时四类具体动作、(d) "agents.md 的质量决定 wiki 可靠性"、(e) 编辑器/文件格式建议（flat markdown）。
- **scope 不同**：v2 卡片 scope = "仅限该来源（Karpathy gist）对架构分层的描述"；draft scope = "Anthem Création 对 Karpathy 三层架构的法语二手综述与扩展"。
- 不是"v2 的扩展"也不是"完全相同"——draft 是**同主题、不同源、扩展维度**：一个独立来源对相同核心事实的并行确认 + 若干新维度补强。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 卡片 scope 被故意限定在 Karpathy gist 一手来源，把法语二手综述合并进去会破坏 v2 卡片的"single-source"边界。
- 不是 `new_card`：核心事实（三层架构）已经在 v2 被覆盖；写新卡会与 v2 形成内容重复，违反"同一事实只有一张 accepted card"的隐含约定。
- 不是 `duplicate_skip`：draft 带来的不只是确认，还有 (i) 二手来源对三层划分的独立背书、(ii) compilation 类比的明确引用、(iii) "权限严格分离"的紧凑三句话、(iv) "agents.md 决定可靠性"的法语原句——这些都是 v2 卡片当前 References 没有列出的新出处证据。
- 不是 `revise_before_gate`：draft 本身证据扎实、scope 清晰、风险与边界都标注了。

正确决定是 `provenance_delta`：把这条 draft 作为 v2 三层架构卡片的二手来源补强，写入反向链接到 v2 provenance；audit 阶段决定要不要在 v2 卡片的 References 段追加 Anthem Création 法语引文。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：在 fusion/audit 阶段，把 Anthem Création 法语综述作为 v2 `llm-wiki-three-layer-architecture` 卡片的二手出处补充进 provenance；如果 audit 认为"compilation 类比"与"严格权限分离"值得独立成卡，再拆出 child card，但默认本 draft 不直接写入 v2 卡 body。

## 5. 备注

- top 1/2 都是同一 Karpathy gist 的不同子事实卡——v2 在 gist 上做了细颗粒拆分（三层 / schema / wiki 层 / health checks），本 draft 在二手综述里把它们打包讲，导致 jaccard 不会特别高但语义高度对齐。
- draft 自己已经预测了 `new_card + possible related` 的判断，本评估改为 `provenance_delta`：因为 v2 卡片是"事实卡"而非"主题卡"，事实重叠 → 倾向把新证据反向链接而不是新建独立卡片。
