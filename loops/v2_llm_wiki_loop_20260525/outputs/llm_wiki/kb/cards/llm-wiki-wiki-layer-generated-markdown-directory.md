# Wiki 层由 LLM 生成和维护

- statement: 在该来源的架构中，wiki 层是一个由 LLM 生成的 markdown 文件目录，包含摘要、实体页、概念页、比较、概览和综合等内容；LLM 负责创建页面、在新来源到来时更新页面、维护交叉引用并保持整体一致。
- fact_type: known_fact
- support: 来源在定义 "The wiki" 层时，直接说明它是 LLM 生成的 markdown 文件目录，并列出内容类型与 LLM 对该层的创建、更新、交叉引用和一致性维护职责。
- scope: 仅限该来源对 wiki 层的规定。
- status: accepted
- provenance: `llm_wiki/kb/provenance/llm-wiki-wiki-layer-generated-markdown-directory.md`

该事实只描述这套架构中 wiki 层的角色边界：人读取 wiki 层，LLM 写入并维护 wiki 层。它不说明其它系统中的 wiki 组织方式，也不说明该做法的效果或适用条件。

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:31-32`

## Footnotes

[^1]: 来源第 31 行把 "The wiki" 定义为 LLM 生成的 markdown 文件目录，并说明 LLM 完全负责该层的创建、更新、交叉引用和一致性维护；第 32 行为空行。
