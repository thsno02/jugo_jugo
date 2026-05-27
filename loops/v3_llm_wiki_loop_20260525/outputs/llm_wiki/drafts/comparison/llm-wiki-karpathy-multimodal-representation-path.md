---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-karpathy-multimodal-representation-path.md
draft_provenance: ../provenance/llm-wiki-karpathy-multimodal-representation-path.md
similarity_result: ../similarity/llm-wiki-karpathy-multimodal-representation-path.json
existing_cards:
  - card_id: llm-wiki-ingest-example-flow
    card_path: llm_wiki/kb/cards/llm-wiki-ingest-example-flow.md
    score: 0.1
  - card_id: idea-file-abstract-vague
    card_path: llm_wiki/kb/cards/idea-file-abstract-vague.md
    score: 0
  - card_id: idea-file-share-the-idea
    card_path: llm_wiki/kb/cards/idea-file-share-the-idea.md
    score: 0
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

- 候选 #1 `llm-wiki-ingest-example-flow`：共享 token `ingest`——这是本批 LOW 中**主题最接近的低分撞**。两边都讨论 ingest，但论点轴层级不同（见下）。
- 候选 #2、#3：score=0，无共享 token，无关。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-ingest-example-flow`：仅记录 Karpathy gist L35–38 描述的"新源进 raw collection → LLM 读源 → 与用户讨论 → 写 wiki 摘要页 → 更新 index → 更新相关实体/概念页 → 追加 log 条目"这一**示例性概念流程**。属于高层 mental model，没有具体软件实现。
- draft 来源是 `clawhub-llm-wiki-karpathy/text.txt` L46–95，描述 `@harrylabs/llm-wiki-karpathy` v0.4.4 **具体软件包**的两条 ingest 路径：
  - 文本类（.md / .txt / .csv / .json / .html）走 `kb_prepare_source` + `kb_read_raw` 直接编译；
  - 非文本类（PDF / .png / .jpg / .webp / .svg）走 representation-first 路径：`kb_get_raw_asset` → `kb_prepare_source_bundle` → agent 外部执行 OCR/vision → `kb_prepare_representation` + `kb_upsert_representation` 存入 `.llm-kb/representations/` → `kb_read_representations` 校验 → `compile_readiness=ready` 后 `kb_upsert_source_note`。
- 两者抽象层级不同：候选 #1 是概念示例，draft 是 v0.4.4 软件包的实现细则；且 draft 的 representation-first 论点（runtime 不做 OCR / vision，把多模态理解隔离在 agent 一侧）是候选 #1 完全没有的设计立场。

## 3. 下一步的核心依据

- 不是 `merge_candidate`：抽象层级不同，候选 #1 的概念性流程描述无法承载 draft 的 manifest v2 schema / lint 检查项 / compile_readiness 三态等具体内容。
- 不是 `provenance_delta`：尽管 draft 是候选 #1 的"具体落地之一"，但两者的核心论点不同（概念流程 vs 软件包实现细则）；把 draft 作为候选 #1 的 provenance 补丁会丢失 representation-first 的设计立场。
- 不是 `duplicate_skip`：无内容覆盖。
- 不是 `revise_before_gate`：draft 已有两路径定义、5 步流程、manifest v2 字段、lint 检查项、3 个边界标注（runtime 不 auto OCR / stale representations / 不支持视频音频）；门控可继续。
- 综合判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；门控阶段建议核 `kb_*` 命令名拼写是否逐字对齐 clawhub-llm-wiki-karpathy README。

## 5. 备注

- 这是 LOW batch 中**少见的"top 1 与 draft 主题真有交集"**案例（共享 `ingest`），但抽象层级差异让 `new_card` 而不是 `provenance_delta` 更合适。
- top 2/3 score=0，是 v2 仅 15 张候选 + jieba 分母效应导致的极端情况。

## 6. 2026-05-27 v2_anchor 再核对

**触发**：first-pass loop report 中把本卡片列为"3 张 similarity miss"之一。

**再核对结论**：top-1 `llm-wiki-ingest-example-flow` @ 0.100 是真实 v2 邻居（共享 ingest 主题），worker 已在 §1–§3 正确识别并讨论。所谓"miss"判断不成立——真实邻居就在 top-1。

**最终决策**：维持 worker 原判 **`new_card`**。原因：
- 抽象层级差异：v2 是 Karpathy gist 描述的概念示例流程（read source → discuss → summarize → update index → log）；draft 是 `@harrylabs/llm-wiki-karpathy` v0.4.4 软件包的具体 ingest 实现（manifest v2 schema / kb_* 工具集 / representation-first 路径 / compile_readiness 三态 / lint 检查项）。两者主题相邻但论点对象完全不同。
- 设计立场差异：draft 的核心主张"runtime 不做 OCR/vision，把多模态理解隔离在 agent 一侧"是 v2 完全没有的工程立场。

**是否加 v2_anchor 到 kb provenance**：不加。本卡是新主题（多模态 ingest）+ 新软件包（v0.4.4）的具体实现细则，不是 v2 ingest-example-flow 的 delta；从抽象层看 v2 卡是"概念示例"，draft 是"软件包实现"，把两者绑成 anchor 关系会误导后续读者。

**audit trail**：recheck performed 2026-05-27；recheck conclusion = `new_card_confirmed`；topical neighbor v2 `llm-wiki-ingest-example-flow` 已在 §1 explicit 标注。
