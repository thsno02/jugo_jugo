# Schema 是配置文档

statement: 在该来源的架构中，schema 是指导 LLM 如何组织 wiki、遵循约定以及执行摄取、问答和维护工作流的配置文档。

fact_type: known_fact

support: 来源第 33 行把 `The schema` 描述为一个文档，用来告诉 LLM wiki 的结构、约定，以及在摄取来源、回答问题或维护 wiki 时应遵循的工作流；同一行还称它是关键配置文件。

scope: 仅限该来源对 schema 层的规定。

status: draft

## Note

在这个架构里，schema 的主要作用是约束 LLM 的 wiki 维护行为：它规定结构、约定和工作流，使 LLM 按该 wiki 的规则工作。这里的表述只对应来源中的 schema 层定义，不扩展到其它 wiki 或 agent 架构。

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:33`

## Footnotes

- 无。
