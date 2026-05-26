---
schema: comparison_provenance.v3
draft_card: ../cards/karpathy-gist-three-layers.md
draft_provenance: ../provenance/karpathy-gist-three-layers.md
similarity_result: ../similarity/karpathy-gist-three-layers.json
existing_cards:
  - card_id: llm-wiki-three-layer-architecture
    card_path: llm_wiki/kb/cards/llm-wiki-three-layer-architecture.md
    score: 0.25
  - card_id: llm-wiki-schema-configuration-document
    card_path: llm_wiki/kb/cards/llm-wiki-schema-configuration-document.md
    score: 0.2222
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1111
decision: provenance_delta
audit_required: true
created_time: 2026-05-26T12:34:00+08:00
edited_time: 2026-05-26T12:34:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

top 1 `llm-wiki-three-layer-architecture` 与 draft **同一来源 + 同一段落**：

- v2 卡片 References 指向 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33`（Architecture 段）。
- 本 draft Footnotes 指向 `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt:27-33`（同一 Architecture 段）+ 第 15 行（"You never (or rarely) write the wiki yourself"）+ 第 75 行（intentionally abstract）。

两者从字面到证据都是同一份 gist 同一段落的两次抽取。

top 2 `llm-wiki-schema-configuration-document` 同 gist 第 33 行（schema 段），draft 在 schema 那一段直接复用相同原文行号。

top 3 `llm-wiki-health-checks` token 误中（仅 `llm / wiki`），与 draft 范围无关。

## 2. draft 与候选在哪里不同

- **scope 不同**：v2 把同一份 Architecture 段拆成三张独立卡（三层架构定义 / schema 配置文档 / wiki 层生成与维护）；本 draft 把它们打包成一张"三层 + 所有权分离"的合并视图。
- **新出处证据**：v2 三张卡片未引用第 15 行"You never (or rarely) write the wiki yourself"——这是本 draft 给出的新行号证据，强化"所有权分离"这一论点。
- **新论点角度**：v2 卡片表述为"事实的客观描述"（"该来源把架构分成三层"）；draft 把它表述为"所有权分离是关键工程含义" + "wiki 是可重建的派生工件" + "schema 是人 + LLM 共同演进"。这些是从同一原文做的合理推论，但 v2 卡片刻意没有这样推论。
- **不是"同源同卡"**：虽然 v2 三张卡的并集与 draft 范围重叠，但 v2 选择了拆分粒度，draft 选择了整合视角；audit 应判断哪一种粒度更适合 v3。
- 不是"v2 的扩展或不同视角不同源"——是同源、同事实集、但**抽取粒度与论点框架不同**。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：v2 故意把 Architecture 段拆成 3 张窄卡，把 draft 直接合进其中任一张都会破坏 v2 的颗粒度策略；audit 必须先决定 v3 是否要保留 v2 的拆分粒度。
- 不是 `new_card`：draft 的所有原文行号几乎都已被 v2 三张卡片覆盖（除了第 15 行）；新建一张合并视角的卡会与 v2 三张并列形成事实重复。
- 不是 `duplicate_skip`：draft 给出了第 15 行 + 第 75 行的新证据 + "所有权分离 / wiki 可重建 / schema 共同演进"三条论点框架——这些是 v2 卡片当前 References 与 statement 都没有的，足以作为 provenance 增量。
- 不是 `revise_before_gate`：draft 证据完整、scope 清晰（distinction 类型卡）、边界（gist 自陈 intentionally abstract、三层不强制、人偶尔编辑 wiki 的余地）都标注。

正确决定是 `provenance_delta`：把本 draft 作为 v2 三张 Karpathy gist 衍生卡（特别是 `llm-wiki-three-layer-architecture`）的论点框架补强 + 第 15 行新行号证据补强。audit 阶段决定要不要在 v2 卡 References 段追加第 15 行 + 第 75 行；并决定要不要采纳"所有权分离"作为 v2 三层架构卡的次级论点。

## 4. 决策

- decision: provenance_delta
- audit_required: true
- 后续动作建议：fusion_audit 把 draft 第 15 行（"You never (or rarely) write the wiki yourself"）反向链接进 v2 `llm-wiki-three-layer-architecture` 与 `llm-wiki-wiki-layer-generated-markdown-directory`（不在本 batch top-3 但 audit 应该交叉检查）的 provenance；判断是否把 draft 的"所有权分离"框架升格为 v2 三层卡的 Note 段。draft 本身不再独立 publish 为 accepted 卡。

## 5. 备注

- 这是 batch 中**唯一**"同源同段，与多张 v2 卡同时高重合"的案例。jaccard 分数（0.25 / 0.2222 / 0.1111）反而比 lightmem 等无关卡片低，因为 token 集合相对窄；提醒下次校准时分数与"是否同源同事实"并不正相关。
- v2 的细颗粒拆分（每段事实一张卡）vs draft 的整合视角（一个 distinction 卡），是 v2 → v3 重要的设计选择；建议 audit 阶段把这条决策记录到 reflections。
