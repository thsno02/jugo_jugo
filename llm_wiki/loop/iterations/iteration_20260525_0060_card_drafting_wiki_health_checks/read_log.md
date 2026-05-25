# read_log

- `llm_wiki/loop/iterations/iteration_20260525_0051_source_mining_karpathy_x_launch/artifacts/fact_candidates.md`
  - 用途：仅核对 `候选 12` 的候选字段。
  - 读取方式：按 `## 候选 12` 块边界抽取，遇到下一个 `## 候选 N` 即停止。
  - 边界情况：输出未暴露相邻候选内容。
- `data/raw/webpage/karpathy-x-launch-post/raw.json`
  - 用途：读取唯一允许的来源证据。
  - 读取方式：只输出 JSON pointer `.tweet.quote.text`。
