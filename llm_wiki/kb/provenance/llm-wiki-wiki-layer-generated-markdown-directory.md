# 出处论证：Wiki 层由 LLM 生成和维护

- knowledge_card: `llm_wiki/kb/cards/llm-wiki-wiki-layer-generated-markdown-directory.md`

## 事实来源

这张知识卡来自 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:31-32`。其中第 31 行是实际证据，第 32 行为空行。

## 支撑关系

来源明确把 "The wiki" 定义为一个由 LLM 生成的 markdown 文件目录，并列出它包含 summaries、entity pages、concept pages、comparisons、an overview、a synthesis。来源还明确说 LLM 完全拥有这一层，负责创建页面、在新来源到来时更新页面、维护交叉引用，并保持整体一致。

因此，知识卡中的事实可以成立：wiki 层的文件形式、主要内容类型，以及 LLM 对该层的写入和维护职责，均由指定证据直接支撑。

## 明说与整理

来源明说的部分包括：wiki 层是 LLM 生成的 markdown 文件目录；包含摘要、实体页、概念页、比较、概览和综合；LLM 完全负责该层；LLM 创建页面、更新页面、维护交叉引用并保持一致；读者读取该层，LLM 写入该层。

整理后的部分包括：将 "The wiki" 统一表述为“wiki 层”；将英文内容类型译为中文；将来源中的多个动作合并为“由 LLM 生成和维护”。这些整理没有加入新的背景判断，只是把来源句子压缩成一条原子事实。

## 成立范围

该事实只在该来源描述的架构中成立，范围限定为该来源对 wiki 层的规定。它不能外推为所有 wiki、所有 LLM 知识库，或该架构在实践中的效果判断。

## 采纳状态

该卡已通过审计并采纳，状态为 `accepted`；事实范围仍保持当前限定。
