# RAG 式文档问答不积累综合知识

statement: 该来源将常见的 LLM 文档问答体验描述为 RAG：用户上传一组文件，LLM 在查询时检索相关片段并生成答案；同时指出这种方式在不同问题之间不会积累已经综合出的知识。

fact_type: known_fact

support: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:7-10` 先描述了上传文件、查询时检索相关片段并生成答案的 RAG 式体验，随后说明 LLM 会在每个问题上从头重新发现知识，没有积累；遇到需要综合多个文档的细微问题时，它每次都要重新寻找并拼接相关片段。

scope: 仅限该来源对 RAG 式文档问答体验的对比性描述；不扩展为对所有 RAG 系统或所有文档问答产品的通用评价。

status: draft

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:7-10`

## Footnotes

- 这里的“RAG 式文档问答体验”是对来源描述的中文整理，用来指代来源中“上传文件、查询时检索片段、生成答案”的体验形态。
