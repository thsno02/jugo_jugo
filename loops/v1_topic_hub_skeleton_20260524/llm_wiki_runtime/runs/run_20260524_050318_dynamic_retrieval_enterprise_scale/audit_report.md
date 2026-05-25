# Audit Report / 审计报告

audit_result:: passed

## 检查项

- 使用 source 前已有 retrieval request。
- AICritique 失败响应被保存并拒绝作为 evidence。
- Atlan 来源保存到 `data/raw/`。
- `data/manifests/sources.jsonl` 记录了两个动态检索尝试。
- Node version bundle 完整。
- Card 有 Footnotes 和 References。
- Provenance 区分 source evidence、失败尝试、synthesis 和 vendor bias。
