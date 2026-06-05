---
schema: justification_journal.v1
card: ../cards/my-llm-wiki-implementation.md
created_time: 2026-06-05T10:00:00+08:00
---

## creation | 2026-06-05T10:00:00+08:00

生成方式：Mode A questioning loop
来源：`data/raw/pypi/pypi-my-llm-wiki/text.txt`
源证据：
- L100 — "Andrej Karpathy shared a concept he called LLM Wiki — a personal knowledge system with three layers"
- L102 — "my-llm-wiki implements all three layers."
- L103-104 — "pip install my-llm-wiki cd your-project && llm-wiki ."
- L104 — "The output wiki-out/vault/ is a drop-in Obsidian vault"
- L108-114 — 四类文件支持的完整描述
范围论证：该卡记录 LLM Wiki 概念的一个具体开源实现（PyPI 包），与已有的 obsidian-karpathy-wiki-plugin（Obsidian 插件实现）和 kb-compile-implementation（Claude Code 命令实现）并列，共同构成 LLM Wiki 模式的实现生态图景。作为 example_pattern 卡，其范围是描述该工具的技术选型和能力边界，而非重复三层架构或复利制品等已有概念卡的内容。
