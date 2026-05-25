# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0036_card_drafting_llm_wiki_pattern_file/task.md`
  reason: 确认当前窄任务、允许输入、允许写入和成功门禁。
  use: 作为本轮唯一任务边界。
- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  reason: 核对 `候选 1` 的字段。
  use: 只读取并使用 `候选 1` 的 statement、fact_type、support、scope 和 source_evidence。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  reason: 读取任务指定的来源证据行。
  use: 只使用第 1-5 行支撑草稿卡与出处论证。
