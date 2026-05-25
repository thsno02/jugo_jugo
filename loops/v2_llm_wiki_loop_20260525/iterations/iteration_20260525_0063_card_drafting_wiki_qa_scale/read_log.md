
# read_log

- path: `llm_wiki/loop/iterations/iteration_20260525_0063_card_drafting_wiki_qa_scale/artifacts`
  - reason: 启动时确认允许写入目录是否存在。
  - use: 只确认目录存在；未读取任务证据内容。
- path: `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
  - reason: 核对任务指定的 `候选 11` 字段。
  - use: 使用精确 awk 边界读取 `## 候选 11` 到下一个候选标题之前的内容；输出未暴露相邻候选字段。
- path: `data/raw/webpage/karpathy-x-launch-post/raw.json`
  - reason: 读取任务指定来源证据。
  - use: 仅用 `jq -r '.tweet.quote.text'` 读取 JSON pointer `$.tweet.quote.text`。

未读取 `legacy/`、旧审计报告、已采纳 KB 卡片、其它候选块或来源 JSON 的其它字段。

