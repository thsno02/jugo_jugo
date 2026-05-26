---
schema: comparison_provenance.v3
draft_card: ../cards/llm-wiki-ingest-vs-query-workflow.md
draft_provenance: ../provenance/llm-wiki-ingest-vs-query-workflow.md
similarity_result: ../similarity/llm-wiki-ingest-vs-query-workflow.json
existing_cards:
  - card_id: llm-wiki-health-checks
    card_path: llm_wiki/kb/cards/llm-wiki-health-checks.md
    score: 0.1429
  - card_id: llm-wiki-listed-use-cases
    card_path: llm_wiki/kb/cards/llm-wiki-listed-use-cases.md
    score: 0.1429
  - card_id: llm-wiki-pattern-file
    card_path: llm_wiki/kb/cards/llm-wiki-pattern-file.md
    score: 0.1429
decision: new_card
audit_required: false
created_time: 2026-05-26T16:05:00+08:00
edited_time: 2026-05-26T16:05:00+08:00
edited_entity: llm
---

## 1. draft 与候选为什么看起来相关

三张候选的 jaccard 分数完全一样（0.1429），共享 token 仅为 `llm`、`wiki`。这是因为 draft 标题"LLM wiki 工作流分 ingest（写入侧）与 query（读取侧）两步"以"LLM wiki"开头，自然撞上 v2 任何以"LLM Wiki ..."命名的卡。`ingest` / `query` / `工作流` 等关键 token 都没有在候选标题里出现。

## 2. draft 与候选在哪里不同

- 候选 #1 `llm-wiki-health-checks`：仅记录推文 Linting 段中 LLM 对 wiki 做 health checks 这一事实点。和 ingest/query 两阶段流程无关。
- 候选 #2 `llm-wiki-listed-use-cases`：是个 use case 清单（personal / research / business 等），与 workflow 拆分无重叠。
- 候选 #3 `llm-wiki-pattern-file`：是 "LLM Wiki" 模式 idea file 元描述，未涉及 workflow 机制。
- draft 来源是 `anthemcreation-en-guide/text.txt` L92–L176，描述完整 ingest 阶段（建 entity 页 / 更新 / 合成矛盾 / 自动 backlink）与 query 阶段（多跳推理）的角色分离与 setup 步骤，并指出 agents.md 是写阶段契约。这是机制（mechanism）卡，论点轴是"workflow 拆分及为何分阶段有意义"，v2 top 3 候选都不在这一轴上。

## 3. 下一步的核心依据

由 (1) (2)：top 3 与 draft 没有任何机制/工作流层面的重叠，只是机械主题词撞分。

- 不是 `merge_candidate`：top 3 内无可合并对象。
- 不是 `provenance_delta`：top 3 中没有卡能从本 draft 直接获得新证据/新边界。
- 不是 `duplicate_skip`：内容无覆盖。
- 不是 `revise_before_gate`：draft 已有清楚的两阶段定义、边界、quotes（第 100–108 行 / 第 176 行）与 Obsidian 可替代等反例；门控时再核对术语统一即可。
- 因此判 `new_card`。

## 4. 决策

- decision: new_card
- audit_required: false
- 后续动作建议：publication_gate；后续若同主题三卡（karpathy-... / my-llm-wiki-... / 本卡）一起进入 wiki，应统一 ingest/query 术语并互相 cross-link。

## 5. 备注

- v2 KB 内其实有 `llm-wiki-query-answer-writeback` 与 `llm-wiki-ingest-example-flow` 两张卡（Karpathy gist 视角的 ingest/query 流程描述），但它们没有进入本 draft 的 top 3。如果 publication_gate 评审需要更完整的 v2 对比，可手动追加这两张卡的对照（属审计阶段，不在本卡读取边界）。
- top 3 三张卡分数完全相同，是 v2 仅 15 张候选 + 高频 token "llm/wiki" 在小池子中机械撞分的典型表现。
