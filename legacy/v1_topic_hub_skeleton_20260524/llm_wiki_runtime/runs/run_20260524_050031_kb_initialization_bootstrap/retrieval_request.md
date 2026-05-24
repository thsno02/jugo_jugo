# Retrieval Request / 检索请求

run_id:: bootstrap_node_batch
target_node:: dynamic_retrieval_as_controlled_fallback
created_by:: audit
status:: completed_with_partial_failure

## 为什么现有 data 不足

本地 source gap review 记录了 blocked Reddit captures 和 intercepted enterprise article。这些是 community reception 与 enterprise suitability 的硬性 evidence gap。

## 缺失 evidence

- 可用的 community discussion evidence。
- 可替代 intercepted AICritique 页面的 enterprise evidence。

## Desired source types

- discussion_thread
- issue_thread
- blog_post
- enterprise_guide

## Acceptance criteria

- Raw source 必须保存。
- Source manifest 必须更新。
- Provenance 必须记录 retrieval。
- Retrieved evidence 必须被引用或明确拒绝。

## 公司网络说明

当前运行环境可能拦截网页。只做有限正常尝试；被拦截来源记录后，后续在个人设备重新 retrieve。
