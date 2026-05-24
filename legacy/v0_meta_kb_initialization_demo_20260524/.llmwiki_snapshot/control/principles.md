# KB 初始化原则

1. 先保存 raw source，再进行 synthesis。
2. `nodes/` 是可维护知识对象数据库。
3. `kb/` 是 adopted version 的消费视图。
4. 每个 node version 都必须包含 `node.yaml`、`card.md`、`provenance.md`、`change.md`。
5. 具体 claim 用 footnote 支撑，背景/定义/过程语境用 reference 支撑。
6. Provenance 是知识对象本身的一部分，不是附录。
7. Major change 只创建 impact review tasks，不自动重写下游。
8. 动态检索必须先写 gap/request，再保存 raw source，再进入 provenance。
9. 每次 0-1 node run 都是 skill evaluation sample。
10. 公司电脑网络受限时，只做有限普通检索；被拦截就记录并延期到个人设备重试。
