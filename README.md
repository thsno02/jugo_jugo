# LLM Wiki 原始知识库工作区

这个仓库是 LLM Wiki 方向的原始资料与知识生产工作区。资料来源包括 Andrej Karpathy 的 LLM Knowledge Bases 原始想法、社区实现、博客、论文、包页面和讨论串。

当前活跃 KB 方向已经切换到 `llm_wiki/`：用出处论证做实、接近 zet 风格知识卡的原子事实生产。旧的节点/主题实验已经移入 `legacy/`，避免依赖隐藏目录，也方便人类审计。

## 目录

- `data/manifests/seed_sources.json`：人工整理过的来源队列。
- `data/manifests/sources.jsonl`：每个来源的最新获取结果。
- `data/logs/source_access_log.jsonl`：追加式来源访问日志。
- `data/raw/`：已保存的 HTML、文本、arXiv source bundle、JSON、浅层 GitHub clone 等原始资料。
- `llm_wiki/`：当前活跃的原子事实 KB 工作区。
- `legacy/`：已经归档的 demo 与主题/枢纽骨架，并说明它们为什么不再是活跃 KB 形态。
- `scripts/fetch_sources.py`：当前阶段使用的轻依赖来源获取脚本。
- `docs/RESEARCH_PROTOCOL.md`：资料获取协议和操作规则。

## 运行

```bash
python3 scripts/fetch_sources.py --manifest data/manifests/seed_sources.json
```

可以用 `--skip-repos` 只快速获取网页，也可以用 `--only ID` 重新获取单个来源。

对于 arXiv 条目，脚本优先获取 `https://arxiv.org/e-print/<id>` source bundle，并把 TeX / BibTeX 风格文件整理成 agent 可读的 `agent_source_bundle.txt`。只有在 arXiv 不提供 TeX source 时，才保留 PDF 作为主要来源。
