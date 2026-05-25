# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0037_card_audit_llm_wiki_pattern_file/task.md`
  - reason: 当前任务包。
  - use: 确认允许输入、允许写入、审计问题、结论格式和阻塞条件。
- path: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/artifacts/draft_card.md`
  - reason: 任务指定草稿知识卡。
  - use: 审计 statement、fact_type、support、scope、status、References 和 Footnotes。
- path: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/artifacts/provenance.md`
  - reason: 任务指定出处论证。
  - use: 核对出处论证是否足以 justify 草稿卡暂时成立。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:1-5`
  - reason: 任务指定来源证据和允许行号。
  - use: 核对标题、模式定位和 idea file 用途是否支撑卡片 statement。
- path: `llm_wiki/loop/iterations/iteration_20260525_0001_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  - reason: 任务指定 fact_candidate_path，且只允许 candidate 1。
  - use: 读取失败，未取得 candidate 1 内容，未用于补充事实或改变审计结论。
