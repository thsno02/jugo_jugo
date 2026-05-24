- path: llm_wiki/loop/iterations/iteration_20260525_0007_card_audit_raw_sources_truth_r1/task.md
  reason: 读取当前任务包，确认允许输入、允许写入、审计问题和交付格式。
  usage: 作为本轮审计边界和输出门禁。
- path: llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/draft_card.md
  reason: 读取任务指定草稿知识卡。
  usage: 审计 statement、fact_type、support、scope、status、正文结构和 section 顺序。
- path: llm_wiki/loop/iterations/iteration_20260525_0006_card_drafting_raw_sources_truth_r1/artifacts/provenance.md
  reason: 读取任务指定出处论证。
  usage: 判断论证是否能支撑草稿卡暂时成立。
- path: data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt
  lines: 27-30
  reason: 读取任务指定来源证据行。
  usage: 核对草稿卡和出处论证中的事实表述是否有来源支撑。
