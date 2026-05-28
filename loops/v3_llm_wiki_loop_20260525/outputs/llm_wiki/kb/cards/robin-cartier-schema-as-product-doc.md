---
id: robin-cartier-schema-as-product-doc
title: 真正的创新不是 wiki 而是 schema 文件——"给 AI 同事的活产品需求文档"
status: accepted
card_type: source_claim
tags: [#schema, #CLAUDE-md, #AGENTS-md, #robin-cartier, #PRD]
created_time: 2026-05-26T12:05:00+08:00
edited_time: 2026-05-28T10:35:00+08:00
edited_entity: llm
source_ids: [robin-cartier-llm-knowledge-bases]
provenance_card: ../provenance/robin-cartier-schema-as-product-doc.md
aliases: [schema is the real innovation, living PRD for AI colleague]
related: [karpathy-gist-three-layers, robin-cartier-scale-ceiling, llm-wiki-schema-is-most-important, aillm-wiki-schema-as-bottleneck, agents-md-as-schema-layer, llm-wiki-mcp-design-boundary-mechanics-not-content]
---

Robin Cartier 在 verdict 里下了一个比 Karpathy 原 gist[^v3-1] 更激进的判断：**真正可推广的创新不是 wiki 本身，而是 schema 文件**[^v2-1]——而且 schema 不应该被看作"配置"，应该看作"给 AI 同事的活产品需求文档"。

**原话**："The schema file is the real innovation, not the wiki itself. Treating CLAUDE.md as 'a living product requirements document for an AI colleague' scales far beyond knowledge management to any workflow that needs operational knowledge encoded for the LLM to follow autonomously."[^src1]

这句话拆开来有三个含义：
1. **schema 的可推广性 > wiki 的可推广性**：wiki 模式天花板在 200 页[^v3-2]，但用 schema 来"以文档形式编码工作流"这一模式不受此限制——可用在任何需要 LLM 自主执行的协作流程上。
2. **schema 是 PRD 不是 README**：PRD（product requirements document）的语义意味着它"指定要做什么、怎么验收"。Schema 也应该写得让 LLM 在没有人监督的情况下能照执行——这等价于把"运营 know-how"编码进文档；
3. **"活"——schema 需要持续演化**。Karpathy gist 里也说"You and the LLM co-evolve this"；Robin 把这一点强调为可推广性的关键属性。

**为什么这是一个有用的视角调整**：
- 把 schema 看作 PRD 后，工程团队就有了已知的产品工程语言来评估它：清晰度、可验收准则、版本治理、变更日志；
- 它把 LLM-as-colleague 从隐喻提升为一种实际的"协作合同"——LLM 看 schema 就像新员工看入职手册；
- 它解释了为什么 Karpathy 模式可以扩展到 wiki 之外：任何"重复发生的、依赖 LLM 自主执行的工作流"（CI 运维、Pull Request 评审、定期报告生成等）都可用 schema-as-PRD 编码。

**对应到本仓库的"loop capsule"实践**：本仓库的 loop README + 任务模板（如 batch_worker_prompt.md）本质上就是一份 schema-as-PRD——它告诉每个 worker 角色、边界、产物格式、失败处理。这一模式的成立性来自 Robin 的观察。

边界与误用：
- "schema 是真创新"是 Robin 自己的判断（带价值排序），不是 Karpathy 的原话——把它当事实主张时要标明出处；
- "无监督执行"是理想态，实际中 schema 仍需多次迭代和必要的人工审查门控；
- 把任何配置文件都包装成"PRD"是一种话术性扩张；不是所有 schema 都需要 PRD 那么高的形式化度，简单脚本的 README 仍然有效。

## References

Robin Cartier, "Karpathy's LLM Knowledge Base: A Practitioner's Verdict" (2026-04-08)，Key points 段落的最后一条。

- 源路径：`data/raw/webpage/robin-cartier-llm-knowledge-bases/text.txt`（行 29 schema 是真创新这一论断；行 19 schema 文件的角色定义；行 33 Jack Roberts 把同模式放进 AI memory OS 的语境）。

## Footnotes

- 核心论断原文（行 29）："The schema file is the real innovation, not the wiki itself. Treating CLAUDE.md as 'a living product requirements document for an AI colleague' scales far beyond knowledge management to any workflow that needs operational knowledge encoded for the LLM to follow autonomously [src-002]."
- Schema 角色定义（行 19）："Schema file (e.g. CLAUDE.md) — governs folder structure, citation rules, ingest workflow, and linting conventions."
- 更广 AI memory OS 框架（行 33）："Jack Roberts places the same pattern inside a broader AI memory operating system: Obsidian/markdown is the readable long-term memory option, while Pinecone/vector memory is the scalable semantic-search option [src-059]."
