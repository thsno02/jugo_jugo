---
schema: draft_card_provenance.v3
draft_card: ../cards/langgraph-tool-runtime-store-access.md
material_id: langchain-long-term-memory-docs
digest_id: digest_langchain-long-term-memory-docs
source_paths:
  - data/raw/webpage/langchain-long-term-memory-docs/text.txt
created_time: 2026-05-26T12:20:00+08:00
edited_time: 2026-05-26T12:20:00+08:00
edited_entity: llm
---

## 源证据

- 第 165 行：
  > "Tools can then read from and write to the store using the runtime.store parameter."
- 第 186–208 行（Read 块）：完整 `get_user_info` 示例 + 多模型选项卡 + `agent.invoke(..., context=Context(user_id='user_123'))`。
- 第 212–234 行（Write 块）：完整 `save_user_info` 示例 + `runtime.store.put(('users',), runtime.context.user_id, dict(user_info))`。

## 卡片范围是否成立

- 卡片以 operational_rule 类型记录"工具如何通过 ToolRuntime 读写 store"，与官方文档"Read/Write long-term memory in tools"两节正面对应。
- 直接来自源：ToolRuntime[Context] 签名、`runtime.store` 与 `runtime.context` 双轨、多模型选项卡示意 model-agnostic。
- 引申点：
  - "store 不自动写"是对页面整体设计的复述（页面所有示例都需显式 `.put`），未引入新主张；
  - "高频写场景需注意 token / 延迟成本"是行业常识，标为"局限"而非源主张。

## 发表门控结果

本轮未运行。

## 备注

- 与 `langgraph-store-namespace-key-json-model` 形成模型+访问的两卡序列；comparison 阶段可建立 cross-link。
- v2 卡片中无对应运行时模型卡，无重叠。
