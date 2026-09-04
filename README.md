# WeChat Article｜公众号爆款生产 Skills

面向微信公众号内容生产的模块化 AI Skills 工作流。

目标不是用一个“大而全 Prompt”包办所有环节，而是把选题、研究、结构、写作等关键能力拆成可单独测试、迭代和组合的中粒度 Skill。

## 当前版本：v0.1 Core

已部署第一批 4 个核心 Skill：

```text
skills/
├── topic-hunter/
│   └── SKILL.md
├── research-pack/
│   └── SKILL.md
├── article-architect/
│   └── SKILL.md
├── viral-writer/
│   └── SKILL.md
└── shared/
    └── account-profiles.md
```

## 推荐工作流

```text
原始热点 / 政策 / 产品 / 案例 / 想法
        ↓
TopicHunter
爆款选题 + 独特角度 + 账号路由 + 100分评分
        ↓
ResearchPack
一手/二手来源 + 数据 + 时间线 + 案例 + 反方证据 + 可视化素材
        ↓
ArticleArchitect
核心命题 + 文章原型 + 故事线 + 情绪曲线 + 插图节点
        ↓
ViralWriter
标题候选 + 完整正文 + 图片占位 + 标签 + 风险检查
```

## 五个公众号

共享账号画像位于 `skills/shared/account-profiles.md`：

- 思然日新：高校青年教师 / 教学科研 / 项目申报 / AI工作流
- 思然知己：AI热点 / AI学习方向
- 思然天工：AI工具 / Skill / Agent / 教程与工作流
- 思然经世：AI赚钱 / 商业机会 / 副业与案例拆解
- 思然修远：30+成长 / 工作家庭 / 关系选择 / 社会热点

同一事件可以跨账号使用，但必须改变核心问题、目标读者、证据结构和读者收益，禁止一稿多号简单改写。

## 典型用法

### 1. 只有一个热点
先运行 `TopicHunter`，不要直接写文章。

### 2. 已经确定题目，需要找素材
从 `ResearchPack` 开始。

### 3. 已有完整素材，但文章容易写散
运行 `ArticleArchitect` 后再进入写作。

### 4. 结构已经成熟，需要完整成稿
运行 `ViralWriter`。

## 设计原则

- 热点不是选题，角度才是。
- 一手来源优先于二手转述。
- 信息线与情绪线同时设计。
- 真实图负责“证明”，生成图负责“解释/表达”。
- 不机械追求短文，长度由信息价值决定。
- 爆款是概率工程，不以标题党替代事实和读者价值。

## 下一阶段

计划继续加入：

- `visual-editor`：封面 + 文中真实图 + AI生成图 + 图源规则
- `publisher-qa`：标题、事实、图片、排版、发布前质检
- `growth-reviewer`：1h / 24h / 72h 数据复盘与规则更新
- `signal-radar`：全网信号发现与去重聚类
- `wechat-viral-engine`：总控 Orchestrator，按用户输入自动调用子 Skill

建议先用真实选题压力测试 v0.1，再根据数据迭代评分、结构和写作规则。
