# LLM Wiki Loop Workspace

这个仓库是 LLM Wiki 方向的原始资料、loop 实验和候选知识产物工作区。资料来源包括 Andrej Karpathy 的 LLM Knowledge Bases 原始想法、社区实现、博客、论文、包页面和讨论串。

当前没有仓库根目录级别的 promoted stable `llm_wiki/` 产品。`llm_wiki` 仍然是 loop 输出候选，而不是稳定产品目录。

所有 loop 实验都放在 `loops/`。一个 loop 是否 active、archived、abandoned 或 promoted，由 `loops/registry.json` 和对应 capsule 的 `status.json` 表达，不再通过移动到 `legacy/` 表达。

## 目录

- `data/manifests/seed_sources.json`：人工整理过的来源队列。
- `data/manifests/sources.jsonl`：每个来源的最新获取结果。
- `data/logs/source_access_log.jsonl`：追加式来源访问日志。
- `data/raw/`：已保存的 HTML、文本、arXiv source bundle、JSON、浅层 GitHub clone 等原始资料。
- `loops/`：所有 loop capsule，包括历史实验、候选产物和当前 loop 指针。
- `loops/registry.json`：loop 状态索引和 stable product promotion 状态。
- `loops/current_loop.json`：当前 active loop 指针；没有 active loop 时为 `null`。
- `loops/v2_llm_wiki_loop_20260525/outputs/llm_wiki/`：上一轮 loop 产出的候选 LLM Wiki KB，不是稳定根目录产品。
- `scripts/fetch_sources.py`：当前阶段使用的轻依赖来源获取脚本。
- `docs/RESEARCH_PROTOCOL.md`：资料获取协议和操作规则。

## 运行

```bash
python3 scripts/fetch_sources.py --manifest data/manifests/seed_sources.json
```

可以用 `--skip-repos` 只快速获取网页，也可以用 `--only ID` 重新获取单个来源。

对于 arXiv 条目，脚本优先获取 `https://arxiv.org/e-print/<id>` source bundle，并把 TeX / BibTeX 风格文件整理成 agent 可读的 `agent_source_bundle.txt`。只有在 arXiv 不提供 TeX source 时，才保留 PDF 作为主要来源。
