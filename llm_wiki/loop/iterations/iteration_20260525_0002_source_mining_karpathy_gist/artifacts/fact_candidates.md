# fact_candidates

- source_id: karpathy-gist-llm-wiki
- source_title: Andrej Karpathy LLM Wiki / LLM Knowledge Bases idea file
- source_type: gist_raw
- source_path: data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt
- draft_status: candidate_set

## 候选 1

- statement: 该来源把 “LLM Wiki” 描述为一种使用 LLM 构建个人知识库的模式，并说明该文件用于向 LLM agent 传达高层想法，而具体实现应由 agent 与用户协作展开。
- fact_type: known_fact
- support: 来源开头直接给出标题、模式定位和文件用途。
- scope: 仅限该来源对自身文档目的和 LLM Wiki 概念的描述。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:1-5`；证据要点：标题和开头段落说明这是面向 LLM 的个人知识库模式说明文件，具体细节由用户与 agent 协作展开。
- draft_status: candidate

## 候选 2

- statement: 该来源将常见 RAG 体验描述为在查询时从上传文件中检索相关片段并生成答案，并指出这种方式不会在问题之间积累已经综合出的知识。
- fact_type: known_fact
- support: 来源在核心想法部分先描述 RAG 工作方式，再说明其“每次重新发现”的局限。
- scope: 仅限该来源对 RAG 式文档问答体验的对比性描述。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:7-10`；证据要点：核心想法小节先描述 RAG 式文档问答，再指出其每次查询都重新查找和拼接、缺少积累。
- draft_status: candidate

## 候选 3

- statement: 该来源提出的替代模式是让 LLM 递增式构建并维护一个持久 wiki，使其位于用户与原始来源之间，并在新增来源时把关键信息整合进既有 wiki。
- fact_type: known_fact
- support: 来源在核心想法部分明确把持久 wiki 与只在查询时检索原文区分开。
- scope: 仅限该来源提出的 LLM Wiki 模式。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:11-13`；证据要点：来源提出让 LLM 维护一个位于用户与原始材料之间的持久 wiki，并在新增来源时把信息纳入既有结构。
- draft_status: candidate

## 候选 4

- statement: 在该来源中，wiki 被定位为会随新增来源和提问持续变丰富的持久复合产物，其中交叉引用、矛盾标记和综合内容会被保留下来。
- fact_type: known_fact
- support: 来源明确强调 wiki 是持久且会复合增长的产物，并列出其保留的内容类型。
- scope: 仅限该来源对 LLM Wiki 产物性质的描述。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:13`；证据要点：来源强调 wiki 会保存已有链接、矛盾标记和综合结果，并随新增来源与问题继续变丰富。
- draft_status: candidate

## 候选 5

- statement: 该来源把人的角色描述为负责来源、探索和提出问题，而把 LLM 的角色描述为负责总结、交叉引用、归档和维护知识库。
- fact_type: known_fact
- support: 来源说明用户通常不直接写 wiki，并用 Obsidian 与 LLM agent 的协作比喻说明分工。
- scope: 仅限该来源对人机分工的描述。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:15-16` 和 `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:68-69`；证据要点：来源分别说明用户很少直接写 wiki、负责选源和提问，而 LLM 负责摘要、链接、归档和维护。
- draft_status: candidate

## 候选 6

- statement: 该来源列举 LLM Wiki 可用于个人记录、长期研究、读书陪伴 wiki、业务团队内部 wiki，以及竞争分析、尽调、旅行规划、课程笔记和兴趣深挖等场景。
- fact_type: known_fact
- support: 来源在适用场景列表中逐项给出这些用例。
- scope: 仅限该来源列举的可能应用场景。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:17-23`；证据要点：来源列出个人记录、研究、读书、团队内部知识库，以及其它长期积累知识的场景。
- draft_status: candidate

## 候选 7

- statement: 该来源把 LLM Wiki 架构分成三个层次：原始来源、wiki 和 schema。
- fact_type: known_fact
- support: 来源在 Architecture 小节直接列出三层结构。
- scope: 仅限该来源提出的架构分层。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:25-33`；证据要点：Architecture 小节明确写出三层结构，随后分别解释原始来源、wiki 和 schema。
- draft_status: candidate

## 候选 8

- statement: 在该来源的架构中，原始来源是由用户策展的来源文档集合，被视为不可变且由 LLM 读取但不修改的事实来源。
- fact_type: known_fact
- support: 来源对 Raw sources 层作出定义，并说明其不可变与 source of truth 地位。
- scope: 仅限该来源对 Raw sources 层的规定。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:27-30`；证据要点：原始来源层被描述为用户策展的文档集合，LLM 只读不改，并被设定为事实依据。
- draft_status: candidate

## 候选 9

- statement: 在该来源的架构中，wiki 层是由 LLM 生成的 markdown 文件目录，包含摘要、实体页、概念页、比较、概览和综合等内容，并由 LLM 创建、更新、维护交叉引用和一致性。
- fact_type: known_fact
- support: 来源对 The wiki 层的定义列出了内容类型和 LLM 负责的维护行为。
- scope: 仅限该来源对 wiki 层的规定。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:31-32`；证据要点：wiki 层被描述为 LLM 生成和维护的 markdown 文件目录，包含多类页面并保持链接与一致性。
- draft_status: candidate

## 候选 10

- statement: 在该来源的架构中，schema 是指导 LLM 如何组织 wiki、遵循约定以及执行摄取、问答和维护工作流的配置文档。
- fact_type: known_fact
- support: 来源对 The schema 层的定义说明了它的文件形式和作用。
- scope: 仅限该来源对 schema 层的规定。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:33`；证据要点：schema 层被描述为配置文档，用来规定结构、约定，以及摄取、问答和维护流程。
- draft_status: candidate

## 候选 11

- statement: 该来源描述的摄取流程包括把新来源放入原始集合、让 LLM 读取来源、与用户讨论要点、写摘要页、更新索引、更新相关实体和概念页，并向日志追加记录。
- fact_type: known_fact
- support: 来源在 Operations 的 Ingest 小节给出示例流程。
- scope: 仅限该来源示例化的 ingest 操作流程。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:35-38`；证据要点：Ingest 小节给出从放入新来源到阅读、讨论、写摘要、更新页面与日志的示例流程。
- draft_status: candidate

## 候选 12

- statement: 该来源描述的查询流程是让 LLM 针对 wiki 搜索相关页面、阅读页面并带引用综合答案；来源还主张有价值的问答结果可以作为新页面写回 wiki。
- fact_type: known_fact
- support: 来源在 Operations 的 Query 小节说明查询步骤和把答案归档回 wiki 的做法。
- scope: 仅限该来源对 query 操作流程的描述。
- source_evidence: `data/raw/gist_raw/karpathy-gist-llm-wiki/raw.txt:39-40`；证据要点：Query 小节说明 LLM 先查找并阅读相关 wiki 页面，再生成带引用答案，且有价值答案可回写为新页面。
- draft_status: candidate
