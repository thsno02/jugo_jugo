# 草稿知识卡 backlog

本文件记录还没有进入公开 KB 的 atomic draft card。它是恢复入口，不是事实来源。

## 状态枚举

- `drafted`: 已产出草稿卡和 provenance。
- `similarity_pending`: 尚未做相似门。
- `new_atomic_card`: 相似门认为可作为新卡进入发布审计。
- `merge_candidate`: 需要融合既有卡或既有草稿，先做融合审计。
- `provenance_delta`: 事实已存在，但来源可作为 provenance 增量，先做增量审计。
- `duplicate_skip`: 已被现有卡覆盖，暂不进入发布。
- `audit_pending`: 等待最终发布审计。
- `accepted`: 已进入 `llm_wiki/kb/`。

## 当前 backlog

| draft_id | source_id | candidate | draft_card | provenance | similarity_gate | audit_status | adoption_status | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `karpathy-x-launch-post-candidate-11` | `karpathy-x-launch-post` | `候选 11` | `llm_wiki/loop/iterations/iteration_20260525_0063_card_drafting_wiki_qa_scale/artifacts/draft_card.md` | `llm_wiki/loop/iterations/iteration_20260525_0063_card_drafting_wiki_qa_scale/artifacts/provenance.md` | `similarity_pending` | `deferred` | `not_started` | 已完成单卡 drafting；按新流程并入后置 audit/publication 批次。 |
