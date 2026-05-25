# 小规模研究 wiki 可用于复杂问答

statement: 被引用推文描述，当某个近期研究 wiki 达到约 100 篇文章、约 400K words 的小规模时，就可以让 LLM agent 针对该 wiki 回答各种复杂问题，并继续研究答案。

fact_type: known_fact

support: 该 quote text 的 `Q&A` 段落直接写到：这个近期研究 wiki 的规模示例是约 100 篇文章、约 400K words；达到这种足够大的程度后，可以向 LLM agent 提出围绕该 wiki 的复杂问题，agent 会继续研究答案。该段还说明，在这种小规模下，LLM 对自动维护索引文件、简短摘要和读取重要相关资料已经表现得相当可用。

scope: 仅限该 quote text 对一个近期研究 wiki 的规模示例与 Q&A/research 用法的描述；不推广到所有 wiki、所有模型、所有规模，也不补充作者身份、发布时间或外部背景。

status: draft

## References

- `data/raw/webpage/karpathy-x-launch-post/raw.json`, JSON pointer `$.tweet.quote.text`。

## Footnotes

- 这里的“约 100 篇文章”“约 400K words”“小规模”和“复杂问题”均来自该 quote text 的 `Q&A` 段落；中文表述为整理后的转述。

