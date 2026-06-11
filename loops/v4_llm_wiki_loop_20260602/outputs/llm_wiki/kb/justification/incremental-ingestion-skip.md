---
card_id: incremental-ingestion-skip
decision: accepted
confidence: high
---

## 提取理由

源材料描述了两层增量机制：(1) Smart Batch Skip 在文件夹摄入时跳过已处理文件，(2) 单文件重复摄入时执行页面级增量合并。这是一个独立的工程模式——通过分层跳过/合并策略实现批量操作的幂等性和成本效率。源材料将其明确列为 API 成本控制手段之一。

## 与已有卡的区分

- `extraction-granularity-control`: 该卡控制每次提取的深度（产出多少），本卡控制哪些文件需要处理（跳过已处理的）
- `obsidian-karpathy-wiki-plugin`: 该卡概览性提及命令功能，未展开增量处理机制
- `query-to-wiki-feedback`: 该卡的哈希去重与本卡的文件级跳过是同一设计理念（写入前去重）在不同场景的体现

## 原子性判断

该卡聚焦单一洞察：批量摄入通过文件级跳过 + 页面级合并实现增量处理，核心是幂等性保障和成本优化。
