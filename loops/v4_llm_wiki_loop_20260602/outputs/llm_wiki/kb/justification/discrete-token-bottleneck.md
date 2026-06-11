---
schema: justification_journal.v1
card: ../cards/discrete-token-bottleneck.md
created_time: 2026-06-11T10:00:00+08:00
---

## creation | 2026-06-11T10:00:00+08:00

生成方式：Mode A extraction from structured source
来源：`data/raw/webpage/complete-tech-live-frontier/markdown.md`
源证据：
- 第4行 — "large language models are internally continuous (dense vectors at every layer), but they're forced to interface with the world through a discrete token bottleneck."
- 第5行 — "Discards distributional uncertainty — a full probability distribution collapses to one sampled token."
- 第6行 — "Prevents superposition of hypotheses — one token, one path; you can't hold two reasoning branches in the same vector slot."
- 第7行 — "Wastes compute on fluency — tokens that exist for grammar carry no reasoning content but cost just as much."
范围论证：现有卡片均聚焦 LLM Wiki 方法论层面（摄入、架构、工作流等），未涉及该文来源所追踪的研究领域核心问题——即离散 token 接口的结构性代价。该源明确列出三重代价作为结构化列表，构成一个独立的原子概念，值得单独记录。与 latent-reasoning-continuous-thought 和 communication-depth-spectrum 形成因果链：本卡定义问题，那两张卡描述两条解法路线。
