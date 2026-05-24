# 资料获取协议

## 目标

为 LLM Wiki 研究项目建立本地原始知识库。资料范围包括：

- Karpathy 的原始帖子 / gist 以及相关 launch discussion。
- 社区实现、插件、模板和框架。
- 解释、实践或批评这个模式的博客与指南。
- 论文、包页面、目录页和讨论串。

## 当前阶段

当前阶段只获取和保存原始材料。不要过早总结、排序、激进去重，或编译最终 wiki。

## 来源规则

- 尽可能保存不可变的原始文件。
- 可以额外保存可读文本作为便利产物，但必须保留原始 HTML / PDF / JSON。
- 在 manifest 中记录 source URL、final URL、content type、status、hash、fetch time 和 local paths。这些字段名作为数据 schema 保留英文。
- GitHub repo 要 shallow clone，并在可用时保存 GitHub API metadata。
- arXiv 论文优先使用 `https://arxiv.org/e-print/<id>` source bundle，而不是 PDF。将 `.tex`、`.bib`、`.bbl`、`.sty`、`.cls`、`.md`、`.txt` 和 metadata 文件整理成 agent 可读 bundle。
- 讨论平台要尽量同时保存 HTML 页面和可访问的公开 JSON endpoint。
- 不绕过 auth、paywall、robots 限制或 private content。

## 工具策略

第一轮只使用已经安装的工具：`git`、`gh`、`curl` / `wget`、Python 和 `requests`。

`beautifulsoup4`、`trafilatura`、`readability-lxml` 这类可选抽取包需要用户批准后再安装。它们有助于提升正文抽取质量，但不是原始资料保存的必要条件。arXiv 有 TeX/source 时，避免依赖 PDF parsing 作为主要读取路径。
