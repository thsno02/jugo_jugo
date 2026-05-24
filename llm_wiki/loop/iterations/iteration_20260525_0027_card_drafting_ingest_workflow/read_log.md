# read_log

- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/task.md`: 读取任务目标、候选 11、允许输入、允许写入、知识卡要求、出处论证要求和成功门禁。
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`: 使用 `rg -n -C 4` 核对候选 11 的 statement、fact_type、support、scope 和 source_evidence。
- `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md:99-110`: 使用 `sed -n '99,110p'` 复核候选 11 完整字段；该读取范围包含候选 12 的标题和开头，未用于本次知识卡或出处论证。
- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38`: 读取指定来源证据行，用于支撑候选 11 的 ingest 示例流程事实。
- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/loop_status.md`: 写入后自检状态记录。
- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/loop_delivery.md`: 写入后自检交付状态和 `LOOP_DONE` 标记。
- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/artifacts/draft_card.md`: 写入后自检知识卡契约字段和 section 顺序。
- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/artifacts/provenance.md`: 写入后自检出处论证内容。
- `llm_wiki/loop/iterations/iteration_20260525_0027_card_drafting_ingest_workflow/read_log.md`: 写入后自检读写记录。
