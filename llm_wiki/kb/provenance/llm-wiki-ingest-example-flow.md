# 出处论证：Ingest 示例流程

knowledge_card: `llm_wiki/kb/cards/llm-wiki-ingest-example-flow.md`

## 事实来源

这张卡来自 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38`。该位置是来源文本的 Operations / Ingest 小节，直接描述 ingest 时对新来源和 LLM 的处理方式，并给出一个 example flow。

## 为什么来源能支撑它

证据行先说明新来源会被放入 raw collection，并让 LLM process it。随后来源以示例流程列出多个连续动作：LLM 读取来源、与用户讨论 key takeaways、写 wiki summary page、更新 index、更新相关 entity 和 concept pages，并向 log 追加 entry。候选事实和草稿卡只整理这组被明说的动作序列，因此支撑关系直接。

## 来源明说的部分

- 新来源被放入 raw collection。
- 用户让 LLM 处理该来源。
- 示例流程包括读取来源、讨论要点、写摘要页、更新 index、更新相关实体和概念页、追加日志记录。

## 整理后的表述

草稿卡把来源中的英文流程压缩为中文原子事实，并把 "An example flow" 表述为“示例操作流程”。“从放入新来源到更新 wiki 与日志”是对同一证据行中动作顺序的概括，不添加额外步骤。

## 成立范围

该事实只在这份来源对 ingest 操作的示例描述范围内成立。它不声称这是所有 LLM wiki 的必要规范，也不使用来源后半段关于一次来源可能触及 10-15 页、单个摄取或批量摄取偏好的内容来扩展事实边界。

## 采纳状态

审计报告给出 `audit_result: pass`，因此本出处论证随知识卡采纳到 `llm_wiki/kb/`。
