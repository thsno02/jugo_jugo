# Data Scope / 数据范围

本 run 不生成 topic content node，只重置计划。

下一轮 topic node 的 primary evidence scope 应从以下文件开始：

- `data/raw/gist_raw/karpathy-gist-llm-wiki/text.txt`
- `data/raw/webpage/karpathy-x-launch-post/raw.txt`
- `data/raw/hacker_news/hacker-news-original-thread/text.txt`
- `data/manifests/sources.jsonl`
- `data/manifests/claims.jsonl`
- `data/manifests/claim_source_links.jsonl`
- `reports/source_gap_review.md`
- `reports/coverage_framework.md`
