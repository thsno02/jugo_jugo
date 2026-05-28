---
id: etamp-attack-payload-structure
title: eTAMP 攻击 payload 的三段式结构：Importance Signal + Trigger Condition + Attack Goal
status: accepted
card_type: mechanism
tags: [#prompt-injection, #payload-design, #web-agent, #etamp]
created_time: 2026-05-26T11:00:00+08:00
edited_time: 2026-05-28T15:00:00+08:00
edited_entity: llm
source_ids: [arxiv-etamp-memory-poisoning]
provenance_card: ../provenance/etamp-attack-payload-structure.md
aliases: [payload structure, 三段式 payload, 注入指令结构]
related: []
---

## 三段式结构

Zou 等（2026）把 eTAMP 攻击 payload 拆为三个**必须同时存在**的组件[^src1]，对应 prompt injection 的三个独立失效点：

1. **Importance Signal（重要性信号）**：让 LLM 把这段恶意指令放到高优先级。典型句式："This is very important!!!"。失效点：模型对显式优先级标记的盲目响应。
2. **Trigger Condition（触发条件）**：基于可观测特征（URL 模式）或不可观测的任务状态（"struggling"）的条件式触发，决定恶意指令在什么时候激活。失效点：模型对"if 条件成立则执行"指令的服从。
3. **Attack Goal（攻击目标）**：具体恶意动作，论文里统一用 `goto [URL]` 形式触发服务端动作；电商场景下是 `/checkout/add?product={ID}&express=true`（一键下单）[^src3]，Reddit 场景下是 `/product/{ID}?review=...rating=5`（伪造 5 星评论）[^src3]。失效点：模型对单步 URL 跳转动作的工具调用。

## 三个策略对应的 payload 变体

- **Strategy 1 Baseline Injection**：trigger 是宽泛的"any action on target site"，importance 用 newline + "This is very important!!!" + "ignore all previous instructions"。
- **Strategy 2 Authority Framing**：importance 升级为系统级权威 "[URGENT SESSION RECOVERY]: Your previous task encountered a critical error..."，让指令看起来像 system message。
- **Strategy 3 Frustration Exploitation**：trigger 升级为读 agent 的失败信号（clicks not responding / typing returns unexpected results / repeated actions not working），把恶意指令包装成"脱困办法"[^src2]。

## 操作含义（防御者视角）

按三段式拆解攻击面，每段可独立加防御：

- 对 Importance Signal：训练 / 微调时去除对 "!!" "URGENT" "ignore all previous" 这类显式优先级标记的过度响应。
- 对 Trigger Condition：检查 memory 注入条目里是否含 "When you observe ... you must ..." 的条件触发模式；可以用静态扫描在写入 memory 前过滤。
- 对 Attack Goal：把 `goto [arbitrary URL]` 列为高敏感动作，叠加二次确认或域名白名单。

## 边界

- 三段式是论文给出的攻击 payload **生成范式**，不代表所有真实 prompt injection 都遵守。也存在更隐蔽的攻击形态（如把指令分散到多页、用 unicode 同形字符遮蔽 trigger）；论文未覆盖。
- "goto URL 触发服务端动作"假定目标 site 用 GET 参数处理状态改变；对完全走 POST + CSRF token 的 site，同样的 payload 不会生效，需要扩展到表单提交动作。

## Footnotes

[^src1]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 181-188 — "Each attack payload consists of three components: Importance Signal... Trigger Condition... Attack Goal..."
[^src2]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 156-178 — 三种策略 payload 全文（Baseline / Authority Framing / Frustration Exploitation）
[^src3]: `data/raw/arxiv/arxiv-etamp-memory-poisoning/agent_source_bundle.txt` — 行 187 — 电商 `/checkout/add?product={ID}&express=true` 与 Reddit `/product/{ID}?review=...rating=5` 两段 URL 示例
