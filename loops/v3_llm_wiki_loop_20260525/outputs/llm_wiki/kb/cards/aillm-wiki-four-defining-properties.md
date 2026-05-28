---
id: aillm-wiki-four-defining-properties
title: aillm.wiki 给 LLM Wiki 模式总结的四个定义性属性
status: accepted
card_type: distinction
tags: [#llm-wiki, #knowledge-base, #karpathy, #marketing]
created_time: 2026-05-26T11:45:00+08:00
edited_time: 2026-05-28T10:40:00+08:00
edited_entity: llm
source_ids: [aillm-wiki-directory]
provenance_card: ../provenance/aillm-wiki-four-defining-properties.md
aliases: ["LLM Wiki four properties", "aillm.wiki definition"]
related: [llm-knowledge-base-five-stage-workflow, aillm-wiki-schema-as-bottleneck, enterprise-llm-wiki-four-properties, karpathy-gist-three-layers, karpathy-llm-kb-three-layer-arch, karpathy-llm-wiki-vs-rag]
---

aillm.wiki 是 Karpathy LLM Wiki 模式公开传播后第一波出现的"非官方目录站"之一。它把这个模式压缩为四条**对外可营销的定义性属性**——既是它向"非技术用户"解释 LLM Wiki 时的话术，也是社区暂时形成的最低共识：

1. **Persistent Knowledge（持久 / 复利）**——和 RAG 每次重新检索不同，新源会"波及"已有页面、自动标记矛盾、保持互链[^src1]。原文举例："Add a paper about transformer scaling and the pages for attention, optimization, and GPU economics all get updated — not just retrieved from a chunk cache."
2. **Markdown-First（纯文本优先）**——一组 markdown 文件 + 文件夹，不需要 vector DB / embedding / 基础设施；可被 `grep`、`git diff`、离线打开。原话："The knowledge base outlives any tool you use to build it."[^src2]
3. **LLM-Maintained（LLM 维护）**——人定 schema，LLM 编译、更新、互引；输出可预测、可审计；人留在循环里但不打字[^src3]。
4. **Token-Efficient（token 经济）**——把"编译后的知识"装进上下文比把"原始 chunk"灌进上下文便宜很多；声称在小到中等规模的知识库（如 400K 词）上比 RAG 在 latency 与 accuracy 上都更优[^src4]。

为什么这四条值得记住：

- 它们是**当下社区对 LLM Wiki 与 RAG 差别**的最简洁划分，可以作为做项目宣传或工程取舍时的"四个 lens"。
- 缺哪一条都不该叫 LLM Wiki：如果用了 vector DB 就破坏了 Markdown-First；如果靠人手写页面就破坏了 LLM-Maintained；如果每次回答都现切 chunk 就退化为 RAG[^v3-1]，破坏了 Persistent Knowledge。
- 这是**站方话术，不是技术规范**。Karpathy 的 gist 本人写得更模糊（"intentionally vague"）[^v3-2]，aillm.wiki 是社区把模糊定义实例化的尝试之一。

边界与误读：

- "Token-Efficient" 声称的 latency / accuracy 优势仅在 small-to-mid 规模下成立，原文也明确这一点（"For most personal knowledge bases ..."）。把它推到数千文档级会失效，这与 Karpathy 在原帖中 "~small scale" 的限定一致[^v3-3]。
- "Markdown-First" 不是"禁止任何工具"——下面 aillm.wiki 的"Open-Source Directory"等栏目本身就在评测各种 Obsidian 插件、Claude Code 工作流；意思是**底层数据是 markdown**，工具可换。
- 这四条属性是平台自陈，未经第三方验证；引用时应注明来源。

## References

- 四属性章节："Persistent Knowledge / Markdown-First / LLM-Maintained / Token-Efficient"（`data/raw/webpage/aillm-wiki-directory/text.txt`，第 25–39 行）。
- 与 RAG 的对比段（同文件 L25–27）以及 small-to-mid 规模限定（L37–39）。

## Footnotes

- L26–27：*"Unlike RAG, your knowledge compounds. New sources ripple through existing pages, contradictions get flagged, and everything stays interlinked."*
- L30–31：*"Plain markdown files in a folder. No vector DB, no embeddings, no infrastructure to maintain ... The knowledge base outlives any tool you use to build it."*
- L33–35：*"Let Claude, Gemini, or any capable LLM compile, update, and cross-reference your raw sources into a structured wiki — automatically."*
- L37–39：*"A 400K-word wiki beats RAG on small-to-mid knowledge bases for both latency and accuracy."*
