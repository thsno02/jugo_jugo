# read_log

- 读取：`llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/draft_card.md`；用途：定位上一版草稿卡中需按审计要求收窄的 statement。
- 读取：`llm_wiki/loop/iterations/iteration_20260525_0052_card_drafting_idea_file_agent_builds/artifacts/provenance.md`；用途：检查是否存在同类未由 `$.tweet.text` 直接证明的归属语。
- 读取：`llm_wiki/loop/iterations/iteration_20260525_0053_card_audit_idea_file_agent_builds/artifacts/audit_report.md`；用途：确认 `required_changes` 和残余风险。
- 读取：`data/raw/webpage/karpathy-x-launch-post/raw.json` 的 `$.tweet.text`；用途：核对 statement 的直接来源支撑；未使用该 JSON 的其它字段。
- 读取：`llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md` 中 `候选 3` 块；用途：核对候选字段。第一次按英文 candidate 标题边界尝试无输出，未作为证据；随后按中文 `候选 3` 边界读取，未显示相邻候选内容。
