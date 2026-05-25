
# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0049_card_audit_llm_wiki_use_cases/task.md`
  - reason: 读取当前任务包，确认允许输入、允许写入、审计问题和成功门禁。
  - usage: 作为本轮唯一任务来源。
- path: `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/draft_card.md`
  - reason: 读取待审计知识卡。
  - usage: 核对 `statement`、`fact_type`、`support`、`scope`、`status`、正文、`References` 和 `Footnotes`。
- path: `llm_wiki/loop/iterations/iteration_20260525_0044_card_drafting_llm_wiki_use_cases/artifacts/provenance.md`
  - reason: 读取出处论证。
  - usage: 核对来源如何支撑草稿卡及其成立范围。
- path: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt`
  - allowed_range: `17-23`
  - reason: 读取任务允许的来源证据行。
  - usage: 核对草稿卡声明是否由来源明说内容支撑。
- path: `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md`
  - allowed_range: `candidate 6 only`
  - reason: 读取任务允许的候选事实。
  - usage: 核对草稿卡是否对应 candidate 6。
