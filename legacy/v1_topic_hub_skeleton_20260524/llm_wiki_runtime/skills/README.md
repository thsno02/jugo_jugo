# 旧版 Skill 快照

这个目录保存 v1 主题/枢纽骨架循环当时使用过的技能。它们不是当前活跃技能集。

主要问题：

- 主语言多为英文，不符合当前文档规范。
- 生产对象是节点、主题、枢纽页或版本束，不是原子事实知识卡。
- 部分技能会把出处论证、引用、采纳、视图构建接到主题/节点层，容易复现旧版焦点漂移。

当前应使用：

- `llm_wiki/skills/llmwiki-loop-controller/`
- `llm_wiki/skills/llmwiki-source-mining/`
- `llm_wiki/skills/llmwiki-card-drafting/`
- `llm_wiki/skills/llmwiki-card-audit/`
- `llm_wiki/skills/llmwiki-card-adoption/`
- `llm_wiki/skills/llmwiki-skill-evolution/`

除非是在审计旧版 v1 为什么跑偏，否则不要复用本目录下的旧 skill。
