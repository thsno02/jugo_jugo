# Raw sources 是只读事实来源

statement: 在该来源的架构中，`Raw sources` 是用户策展的来源文档集合；这一层被设定为不可变，由 LLM 读取但不修改，并作为事实来源。

fact_type: known_fact

support: 来源在三层架构说明中把 `Raw sources` 定义为用户策展的来源文档集合，列举文章、论文、图像和数据文件等材料，并明确说这些材料不可变，LLM 只读取而不修改，且这是 `source of truth`。

scope: 仅限该来源对 `Raw sources` 层的规定。

status: draft

## 说明

这张卡只记录 `Raw sources` 层的一个原子事实：它在该架构里承担只读的事实依据角色。这里的“原始来源”是对 `Raw sources` 的中文整理，“事实来源”对应来源中的 `source of truth`。

## References

- `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:27-30`

## Footnotes

[^1]: 本卡没有扩展到其它层，也没有推断该架构之外的通用知识库设计原则。
