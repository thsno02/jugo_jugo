# Justification: karpathy-llm-wiki-pattern-automation

## 提取理由
材料标题即点明"automates the Karpathy LLM Wiki pattern"，Source types 节详述三种源的 fetch 策略和 detail level 机制。这是工具的核心价值主张和技术实现路径，与架构卡互补但独立。

## 证据强度
- evidence_basis: code_implementation — 描述的 fetch 策略、工具链（gh/yt-dlp/crawler）、detail level 均为实际实现
- Karpathy pattern 引用有 gist 链接佐证

## 原子性检验
- 单一主题：Karpathy 模式如何被产品化（ingest pipeline + 源类型策略）
- 不涉及架构层次定义（卡1）或 agent 行为协议（卡3）

## 来源段落
- Title/intro (L1-5)
- "Source types" (L103-113)
