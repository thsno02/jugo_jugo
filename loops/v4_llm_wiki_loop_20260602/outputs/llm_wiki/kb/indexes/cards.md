---
type: index
scope: active_cards_only
loop_id: v4_llm_wiki_loop_20260602
generated: 2026-06-05T00:10:00+08:00
total_cards: 19
source: karpathy-gist-llm-wiki
---

# KB Card Index（Active Only）

> 19 张 active 卡片，全部来源于 `karpathy-gist-llm-wiki`。

## 核心模式

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [LLM Wiki 模式](../cards/llm-wiki-pattern.md) | `llm-wiki-pattern` | 用 LLM 增量构建持久化 wiki 的知识库模式，区别于 RAG |
| [Wiki 作为复利型知识制品](../cards/wiki-compounding-artifact.md) | `wiki-compounding-artifact` | wiki 中持续积累的五类结构：交叉引用、矛盾、综合、页面、归档答案 |
| [维护成本归零论点](../cards/maintenance-cost-zero.md) | `maintenance-cost-zero` | 人类放弃 wiki 因维护负担增长快于价值；LLM 使维护成本趋近于零 |

## 架构

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [三层架构](../cards/three-layer-architecture.md) | `three-layer-architecture` | 不可变原始资料层、LLM 拥有的 wiki 层、人机共同演化的 schema 层 |
| [Schema 文件的配置角色](../cards/schema-as-configuration.md) | `schema-as-configuration` | schema 使 LLM 从通用聊天机器人变为有纪律的 wiki 维护者 |
| [Wiki 即 Git 仓库](../cards/wiki-as-git-repo.md) | `wiki-as-git-repo` | markdown 文件 = git 仓库，免费获得版本历史、分支和协作 |

## 操作

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [摄入操作](../cards/ingest-operation.md) | `ingest-operation` | LLM 读取新资料并整合到 wiki，单次可触及 10-15 个页面 |
| [查询操作与答案归档](../cards/query-and-answer-filing.md) | `query-and-answer-filing` | LLM 搜索 wiki 综合答案；好答案归档为新页面产生复利效应 |
| [巡检操作](../cards/lint-operation.md) | `lint-operation` | 定期健康检查：矛盾、过时主张、孤立页面、缺失引用、数据缺口 |

## 导航与基础设施

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [索引文件导航机制](../cards/index-based-navigation.md) | `index-based-navigation` | index.md 在中等规模（~100 资料）下运作良好，超出后可用 qmd |
| [活动日志文件](../cards/log-file.md) | `log-file` | log.md append-only 时间线，记录摄入/查询/巡检，可 grep 解析 |
| [跨会话连续性机制](../cards/cross-session-continuity.md) | `cross-session-continuity` | schema + log + wiki 文件实现跨会话持久化 |

## 角色与参与

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [人机角色分工](../cards/human-llm-role-division.md) | `human-llm-role-division` | 人类策展/引导/提问/思考；LLM 负责一切苦差事 |
| [人类参与程度谱系](../cards/review-involvement-spectrum.md) | `review-involvement-spectrum` | 从逐条深度审查到批量低监督处理的可调谱系 |

## 应用与工具

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [应用领域](../cards/use-case-domains.md) | `use-case-domains` | 个人/研究/书籍/团队/其他五类应用，模式统一适用 |
| [Obsidian 工具生态](../cards/obsidian-tooling.md) | `obsidian-tooling` | Web Clipper、graph view、Marp、Dataview、本地图片 |

## 风险与限制

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [源忠实性风险与不可变锚点](../cards/source-faithfulness-risk.md) | `source-faithfulness-risk` | 多轮变换后知识漂移风险；raw sources 锚点但无系统性验证 |

## 历史与设计哲学

| 卡片 | canonical | 摘要 |
|------|-----------|------|
| [Memex 精神联系](../cards/memex-connection.md) | `memex-connection` | 与 Bush 1945 年 Memex 的精神联系：私人策展、关联路径 |
| [刻意抽象与模块化](../cards/intentional-abstraction.md) | `intentional-abstraction` | 描述模式而非实现，所有组件可选且模块化 |
