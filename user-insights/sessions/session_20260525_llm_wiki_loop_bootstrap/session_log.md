---
schema: user_insights_session_summary.v1
session_id: session_20260525_llm_wiki_loop_bootstrap
project: jugo_jugo_llm_wiki
main_language: zh
coverage: partial
sensitivity: sanitized
publish_status: publishable_summary
redaction_note: 原始用户输入（Raw Input）已摘要化；不保留本机路径、设备环境细节或完整聊天片段。
---

# LLM Wiki Loop 0-1 设计会话摘要

本文件是公开版过程记录（process record）。它保留设计决策、纠偏路径和机制演化，不保留逐字聊天 transcript。

## Coverage

- 来源类型（source class）：当前会话可见上下文（visible context）与 compact handoff。
- 覆盖级别（coverage）：partial，不能声明覆盖完整 transcript。
- 发布策略（publish policy）：只发布摘要化洞察；原始聊天记录保留本地，不进入 git。

## Timeline

| ID | 主题 | 过程信号 | 可发布洞察 |
| --- | --- | --- | --- |
| E001 | KB 初始化入口 | instruction | 用户目标不是生成一次性计划，而是启动可持续执行的 LLM Wiki KB 生成流程。 |
| E002 | 自治与环境边界 | boundary | 长时间任务需要自治、反思、可恢复状态；外部获取失败应记录为环境限制，而不是阻塞主循环。 |
| E003 | 中文主语言与目标漂移 | correction | 文档主语言应保持中文；任务核心是生成 LLM Wiki topic KB，而不是讨论如何设计 KB。 |
| E004 | legacy/demo 管理 | correction | 早期偏移产物可存档为 demo，但正式循环必须回到 source material。 |
| E005 | topic plan 的地位 | design evolution | topic plan 只是建议，知识应从 papers、webpages、repos 等 source mining 中 bottom-up 生长。 |
| E006 | skills 与 KB 双交付 | decision | skills 不是最终交付物的替代品；它们必须被用于生产 KB，并在 loop 中共同演化。 |
| E007 | main-agent 控制面 | architecture boundary | main-agent 应保持上下文清洁，负责决策、调度、干预和验收；具体生产应由 skill/sub-agent 承担。 |
| E008 | Markdown 结构与卡片密度 | quality feedback | Footnotes 应置于文末以保证渲染；大量 source 不能只产出少量粗卡。 |
| E009 | bottom-up 原则 | correction | 当前阶段应从 atomic card 到 hub 聚合，避免过早 top-down 规划。 |
| E010 | atomic card 可靠性 | design rule | atomic card 承载 known fact / accepted fact，需要强 provenance 支撑；hub 和 cluster 不是当前重点。 |
| E011 | schema 简化 | preference | card schema 应保持人类可读，避免把 zet card 退化成机器中间态。 |
| E012 | provenance 范式 | decision | provenance 是把 draft card 做实为 fact card 的可读过程文档，不只是流水日志。 |
| E013 | 文件管理与独立审计 | instruction | loop 需要可审计文件结构、legacy 管理、context isolation 审计和 focus drift 审计。 |
| E014 | sub-agent/runtime 探索 | open question | sub-agent 行为和 scope 需要预定义；运行时可通过脚本、tool 或 hook 触发更稳定的隔离机制。 |
| E015 | goal mode 目标 | instruction | 无人值守目标包括完成 loop 前置条件，并记录积压的用户洞察（user insights）。 |
| E016 | user-insights sidecar | instruction | user-insights 记录应写入 canonical workspace，主语言中文，coverage 不足时明确标注 partial/limited。 |

## Design Decisions

- 知识生产采用自底向上（bottom-up）模型：source material -> atomic draft -> provenance -> fact card -> later hub。
- main-agent 是控制面（control plane），不是主要执行者（executor）。
- provenance 是事实做实机制（fact-justification mechanism），不只是审计日志。
- card 应保持可读的 zet card 形态；metadata 服务检索和治理，但不能压倒正文。
- context isolation 是 loop 运行时设计的核心变量，需要独立审计。

## Publish Notes

- 本公开摘要删除了原始用户输入、私有路径、设备环境细节和完整工具路径。
- 可公开复用的是机制与设计判断；不可公开的是完整聊天 transcript 和本地 session 文件。

## Open Questions

- 是否将 session 级记录聚合成 project-level topics，需要单独触发 dream mode / organize_workspace。
- card citation、footnote、related metadata 的最终统一模型仍需后续 loop 验证。
