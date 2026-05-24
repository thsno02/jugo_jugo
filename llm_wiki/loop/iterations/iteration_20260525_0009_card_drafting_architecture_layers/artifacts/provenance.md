# 出处论证：LLM Wiki 的三层架构

## 事实来源

本卡只依据 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33`。候选字段用 `llm_wiki/loop/iterations/iteration_20260525_0002_source_mining_karpathy_gist/artifacts/fact_candidates.md` 中的候选 7 核对。

## 支撑关系

来源在 `Architecture` 小节中先明说 `There are three layers`，随后分别以三个条目说明 `Raw sources`、`The wiki` 和 `The schema`。因此，“该来源把 LLM Wiki 架构分成三个层次”是来源直接支持的事实。

## 明说内容

来源明说的内容包括：架构有三层；三层分别是 `Raw sources`、`The wiki` 和 `The schema`；每一层有不同职责。原始来源是策展后的来源文档集合，wiki 是 LLM 生成和维护的 markdown 文件目录，schema 是告诉 LLM wiki 结构、约定和工作流的文档。

## 整理表述

卡片中的“原始来源、wiki 和 schema”是对来源中 `Raw sources`、`The wiki` 和 `The schema` 的中文整理。卡片没有加入来源之外的架构背景，也没有把三层关系扩写为通用方法论。

## 成立范围

该事实只在这个来源提出的 LLM Wiki 架构分层范围内成立。它不声称所有 LLM Wiki 项目都必须采用这三层，也不声称这是唯一可行的架构。

## 草稿状态原因

当前只使用了指定来源的一段证据，足以支撑这张候选卡作为草稿存在；但尚未经过更高层的采纳流程，也没有使用额外来源交叉验证。因此状态保持为 `draft`。
