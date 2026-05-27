---
schema: accepted_card_provenance.v3
card: ../cards/microsoft-agent-governance-eight-packages.md
material_id: microsoft-agent-governance-toolkit-docs
digest_id: digest_microsoft-agent-governance-toolkit-docs
source_paths:
  - data/raw/webpage/microsoft-agent-governance-toolkit-docs/text.txt
draft_card: ../../drafts/cards/microsoft-agent-governance-eight-packages.md
draft_provenance: ../../drafts/provenance/microsoft-agent-governance-eight-packages.md
similarity_result: ../../drafts/similarity/microsoft-agent-governance-eight-packages.json
comparison_provenance: ../../drafts/comparison/microsoft-agent-governance-eight-packages.md
gate:
  type: publication_gate
  result: passed
  decided_at: 2026-05-27T14:56:00+08:00
  gate_notes: 6/6 项通过；八个包的官方枚举有 verbatim 引用与行号。
created_time: 2026-05-26T11:40:00+08:00
edited_time: 2026-05-27T14:56:00+08:00
edited_entity: llm
---

## 源证据

- 八个包的并列定义（第 365 行 "Packages" 块）：
  > "⚙️ Agent OS Policy engine, agent lifecycle, governance gate 🔗 Agent Mesh Agent discovery, routing, and trust mesh 🛡️ Agent Runtime Execution sandboxing with four privilege rings 📊 Agent SRE Kill switch, SLO monitoring, chaos testing ✅ Agent Compliance OWASP verification, policy linting, integrity checks 🏪 Agent Marketplace Plugin governance and trust scoring ⚡ Agent Lightning RL training governance with violation penalties 🔒 Agent Hypervisor Execution audit, delta engine, commitment anchoring"。
- 框架无关声明（第 383 行）：
  > "Works with any agent framework: LangChain, CrewAI, AutoGen, Google ADK, OpenAI Agents, LlamaIndex, Haystack, Mastra, MCP, A2A, and more."。
- Policy & Authorization 用 OPA / Rego / Cedar（左侧导航第 134 行）：
  > "OPA / Rego / Cedar"。
- 关键 ADR 名字（第 268 行 等）：
  > "ADR-0002: Four Execution Rings ... ADR-0017: Merkle Audit Chain ADR-0018: Reconstructible Decision BOM ADR-0019: OTel Event Sink Pattern"。

## 卡片范围是否成立

文档首页本身是导航 + 高层描述（约 6 KB），把"八个包按职责并列"作为一张概念卡的范围合理：包名 + 一句话职责直接来自第 365 行的官方枚举，没有引申到论文外。卡内对"policy 是 first-class"、"运行时安全用环"、"Marketplace 用 trust score"的解读全部对应到文档侧边栏 / ADR 标题，没有捏造接口细节。"Framework Adapter Contract" 也直接出自侧边栏 (第 259 行)。

## 发表门控结果

- 类型：publication_gate
- 结果：passed
- 决定时间：2026-05-27T14:56:00+08:00
- 检查要点：
  - 表格 + 4 条要点 + 边界 + 整体观察，substantive。
  - 知识密度足；非标题复述。
  - 源支撑：八包枚举 verbatim + 框架无关声明 + ADR 名字。
  - References + Footnotes 双在；Footnotes 2 条 verbatim。
  - frontmatter 完整；related 含 6 张邻接卡。

## 备注

后续如果有人想拆出每个包的细节卡，应基于具体规范文档而非这张导航页；本卡作为"toolkit 全景"入口适合作为根。

## 相关 v3 draft 工件

- draft card: `../../drafts/cards/microsoft-agent-governance-eight-packages.md`
- draft provenance: `../../drafts/provenance/microsoft-agent-governance-eight-packages.md`
- similarity: `../../drafts/similarity/microsoft-agent-governance-eight-packages.json`
- comparison provenance: `../../drafts/comparison/microsoft-agent-governance-eight-packages.md`
