# fact_candidates

- source_id: `karpathy-x-launch-post`
- source_type: `webpage`
- source_url: `https://api.fxtwitter.com/karpathy/status/2040470801506541998`
- source_path: `data/raw/webpage/karpathy-x-launch-post`
- extraction_role: `source_mining_worker`
- draft_status: `candidate_set`

## 候选 1

- statement: FXTwitter API mirror 记录的这条 X 帖子 ID 为 `2040470801506541998`，作者字段为 Andrej Karpathy / `@karpathy`，发布时间字段为 `Sat Apr 04 16:45:23 +0000 2026`。
- fact_type: `known_fact`
- support: 由来源 JSON 的帖子元数据字段直接支持。
- scope: 仅限本地 API mirror 快照中 `$.tweet` 对象记录的信息。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.id`, `$.tweet.author.name`, `$.tweet.author.screen_name`, `$.tweet.created_at`。
- draft_status: `candidate`

## 候选 2

- statement: Karpathy 在这条帖子中把被引用的前一条推文描述为传播很广，并说明自己想以一个 `idea file` 分享一个可能略有改进的版本。
- fact_type: `known_fact`
- support: 由帖子正文的自述直接支持。
- scope: 仅限 Karpathy 对该发布帖和被引用前帖的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.text`；片段包含 `this tweet went very viral`、`improved version`、`idea file`。
- draft_status: `candidate`

## 候选 3

- statement: 这条帖子把 `idea file` 的理念表述为：在 LLM agents 时代，相比分享具体代码或应用，分享想法本身即可让他人的 agent 按其需求定制和构建。
- fact_type: `known_fact`
- support: 由帖子正文中对 `idea file` 的解释直接支持。
- scope: 仅限该发布帖对 `idea file` 概念的表述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.text`；片段包含 `less of a point/need of sharing the specific code/app`、`share the idea`、`agent customizes & builds`。
- draft_status: `candidate`

## 候选 4

- statement: 这条帖子将 `idea file` 指向一个 GitHub Gist，URL 为 `https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f`，来源中的 card 标题为 `llm-wiki`。
- fact_type: `known_fact`
- support: 由帖子正文 URL 和 card 元数据字段直接支持。
- scope: 仅限本地快照记录的链接和 card 展示信息。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.text`, `$.tweet.card.url`, `$.tweet.card.title`, `$.tweet.card.domain`；card 字段记录 domain 为 `gist.github.com`。
- draft_status: `candidate`

## 候选 5

- statement: Karpathy 在帖子中说，读者可以把该 gist 给自己的 agent，让 agent 构建个人的 LLM wiki 并指导如何使用。
- fact_type: `known_fact`
- support: 由帖子正文中对 gist 用途的说明直接支持。
- scope: 仅限该帖对 gist 预期用途的表述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.text`；片段包含 `give this to your agent`、`build you your own LLM wiki`、`guide you on how to use it`。
- draft_status: `candidate`

## 候选 6

- statement: Karpathy 说明该想法文件有意保持一定抽象和模糊，因为可发展方向很多，并提到人们可以调整该想法或在 Discussion 中贡献自己的版本。
- fact_type: `known_fact`
- support: 由帖子正文结尾对抽象程度和 Discussion 的说明直接支持。
- scope: 仅限该帖对 idea file 设计取向和参与方式的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.text`；片段包含 `abstract/vague`、`many directions`、`contribute their own in the Discussion`。
- draft_status: `candidate`

## 候选 7

- statement: 被引用的前一条推文 ID 为 `2039805659525644595`，标题式开头为 `LLM Knowledge Bases`，发布时间字段为 `Thu Apr 02 20:42:21 +0000 2026`。
- fact_type: `known_fact`
- support: 由来源 JSON 中嵌入的 quote 对象直接支持。
- scope: 仅限本地 API mirror 快照中 `$.tweet.quote` 对象记录的信息。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.id`, `$.tweet.quote.text`, `$.tweet.quote.created_at`。
- draft_status: `candidate`

## 候选 8

- statement: 被引用推文描述的 LLM wiki 流程包括：把来源文档放入 `raw/` 目录，再由 LLM 逐步编译成由 Markdown 文件组成的 wiki。
- fact_type: `known_fact`
- support: 由嵌入 quote 正文的 `Data ingest` 段落直接支持。
- scope: 仅限被引用推文对个人知识库数据摄取流程的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，段落标记 `Data ingest`；片段包含 `raw/ directory`、`incrementally "compile" a wiki`、`.md files`。
- draft_status: `candidate`

## 候选 9

- statement: 被引用推文称该 wiki 会包含 raw 数据摘要、backlinks，并将数据分类为 concepts、为其写文章且互相链接。
- fact_type: `known_fact`
- support: 由嵌入 quote 正文的 `Data ingest` 段落直接支持。
- scope: 仅限被引用推文对 wiki 内容结构的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，段落标记 `Data ingest`；片段包含 `summaries of all the data in raw/`、`backlinks`、`categorizes data into concepts`。
- draft_status: `candidate`

## 候选 10

- statement: 被引用推文称 Karpathy 使用 Obsidian 作为 IDE 式前端来查看 raw 数据、编译后的 wiki 和衍生可视化，并强调 wiki 数据由 LLM 写作和维护，自己很少直接编辑。
- fact_type: `known_fact`
- support: 由嵌入 quote 正文的 `IDE` 段落直接支持。
- scope: 仅限被引用推文中 Karpathy 对其个人工作流的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，段落标记 `IDE`；片段包含 `Obsidian as the IDE "frontend"`、`LLM writes and maintains`、`rarely touch it directly`。
- draft_status: `candidate`

## 候选 11

- statement: 被引用推文称，当 wiki 达到约 100 篇文章、约 400K words 的小规模时，Karpathy 可以让 LLM agent 针对该 wiki 回答复杂问题并继续研究。
- fact_type: `known_fact`
- support: 由嵌入 quote 正文的 `Q&A` 段落直接支持。
- scope: 仅限被引用推文对 Karpathy 某个近期研究 wiki 规模和问答用法的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，段落标记 `Q&A`；片段包含 `~100 articles`、`~400K words`、`complex questions against the wiki`。
- draft_status: `candidate`

## 候选 12

- statement: 被引用推文称 Karpathy 会让 LLM 对 wiki 做 `health checks`，例如发现不一致数据、补全缺失数据、寻找新文章候选的有趣连接，以逐步提升数据完整性。
- fact_type: `known_fact`
- support: 由嵌入 quote 正文的 `Linting` 段落直接支持。
- scope: 仅限被引用推文对 wiki 检查和清理方式的描述。
- source_evidence: `data/raw/webpage/karpathy-x-launch-post/raw.json`，JSON pointer `$.tweet.quote.text`，段落标记 `Linting`；片段包含 `health checks`、`find inconsistent data`、`impute missing data`、`new article candidates`。
- draft_status: `candidate`

