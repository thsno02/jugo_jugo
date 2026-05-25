# Raw sources 是只读事实来源

statement: 在该来源的架构中，`Raw sources` 是由用户策展的来源文档集合；它们被视为不可变，LLM 可以读取但不修改，并被设为事实来源。

fact_type: known_fact

support: 来源在介绍“三层”架构时定义 `Raw sources` 层：它由用户策展的来源文档组成，包括文章、论文、图片和数据文件；来源同时说明这些材料不可变，LLM 只读取而不修改，并称其为 `source of truth`。

scope: 仅限该来源对 `Raw sources` 层的规定。

status: accepted

provenance: `llm_wiki/kb/provenance/raw-sources-readonly-source-of-truth.md`

## 简短说明

这张卡只记录 `Raw sources` 层的角色：它不是 LLM 生成或改写的内容层，而是用户维护、供 LLM 读取的事实依据层。

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:27-30`

## Footnotes

- “事实来源”是对原文 `source of truth` 的中文整理；“架构中”来自原文在定义 `Raw sources` 前说明共有三层。
