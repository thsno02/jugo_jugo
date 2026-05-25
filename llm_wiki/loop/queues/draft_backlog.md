# 草稿知识卡 backlog

本文件记录还没有进入公开 KB 的 scoped draft knowledge card。它是恢复入口，不是事实来源。

## 状态枚举

- `drafted`: 已产出草稿卡和 provenance。
- `similarity_pending`: 尚未做 title similarity top3。
- `similarity_top3_ready`: 已列出 top3 accepted A 卡。
- `comparison_provenance_ready`: 已回答三问并写入 comparison provenance。
- `new_card`: similarity + comparison 认为可作为新卡进入发布审计。
- `merge_candidate`: 需要融合既有卡或既有草稿，先做融合审计，再把 comparison provenance 链接回 A 卡 provenance。
- `provenance_delta`: 知识已存在，但来源可作为 provenance 增量，先做增量审计，再把 comparison provenance 链接回 A 卡 provenance。
- `duplicate_skip`: 已被现有卡覆盖，暂不进入发布。
- `audit_pending`: 等待最终发布审计。
- `accepted`: 已进入 `llm_wiki/kb/`。

## 当前 backlog

| draft_id | source_id | candidate | draft_card | provenance | similarity_top3 | comparison_provenance | audit_status | adoption_status | note |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| `karpathy-x-launch-post-candidate-11` | `karpathy-x-launch-post` | `候选 11` | `llm_wiki/loop/iterations/iteration_20260525_0063_card_drafting_wiki_qa_scale/artifacts/draft_card.md` | `llm_wiki/loop/iterations/iteration_20260525_0063_card_drafting_wiki_qa_scale/artifacts/provenance.md` | `similarity_pending` | `not_started` | `deferred` | `not_started` | 已完成单卡 drafting；需要按 V2 补 metadata / similarity top3 / comparison provenance 后再进入 audit/publication。 |
