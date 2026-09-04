# WeChat Article｜公众号爆款生产 Skills

面向微信公众号内容生产的模块化 AI Skills 工作流。

目标不是用一个“大而全 Prompt”包办所有环节，而是把选题、研究、结构、写作、视觉、质检和复盘等关键能力拆成可单独测试、迭代和组合的中粒度 Skill。

## 当前版本：v0.2 Production Loop

已部署 7 个核心 Skill：

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
├── visual-editor/
│   └── SKILL.md
├── publisher-qa/
│   └── SKILL.md
├── growth-reviewer/
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
        ↓
VisualEditor
封面 + 真实图搜索单 + AI生成图 + 图源规则 + 视觉节奏
        ↓
PublisherQA
标题/首屏/事实/图片/版权/排版/读者收益终检
        ↓
发布
        ↓
GrowthReviewer
1h / 24h / 72h 数据复盘 + 漏斗诊断 + Skill更新建议
        ↓
反哺下一轮选题与生产规则
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

### 5. 正文已完成，需要封面和文中插图
运行 `VisualEditor`。

其输出会区分：

- 真实图：负责证明事件、产品、人物、政策、数据等真实对象；
- 生成图：负责解释机制、抽象概念、情绪和视觉节奏；
- 图源：所有网上真实图都要求记录可追溯来源，并单独提示授权/版权状态。

### 6. 准备发布
运行 `PublisherQA`。

最终给出：

- A：可发布
- B：修改后发布
- C：暂缓发布

### 7. 已发布，有后台数据
运行 `GrowthReviewer`。

不要只看阅读量。优先建立五个账号自己的：

- 点击/阅读转化
- 完读
- 转阅比
- 赞阅比
- 关注转化
- 推荐流量
- 题型基线

单篇表现只形成观察或假设；多篇重复验证后，才升级为长期规则。

## 设计原则

- 热点不是选题，角度才是。
- 一手来源优先于二手转述。
- 信息线与情绪线同时设计。
- 真实图负责“证明”，生成图负责“解释/表达”。
- 标注图源不等于自动获得版权许可；优先官方、明确授权、CC/公共领域等可核验素材。
- 不机械追求短文，长度由信息价值决定。
- 爆款是概率工程，不以标题党替代事实和读者价值。
- 复盘必须形成实验，但不能把单篇偶然表现永久写进 Skill。

## 当前模块职责

| Skill | 核心问题 |
|---|---|
| TopicHunter | 这个热点到底该从什么角度写？ |
| ResearchPack | 有哪些可信、独特、足够支撑文章的素材？ |
| ArticleArchitect | 这篇文章应该按什么故事线和情绪线展开？ |
| ViralWriter | 如何把结构写成可发布的公众号正文？ |
| VisualEditor | 哪些地方需要真实图、生成图、封面和信息图？ |
| PublisherQA | 发之前有哪些事实、标题、图片、排版风险？ |
| GrowthReviewer | 发布后到底为什么爆/没爆，下一轮改什么？ |

## 下一阶段

计划继续加入：

- `signal-radar`：全网信号发现、去重聚类、时效与热度判断
- `wechat-viral-engine`：总控 Orchestrator，按用户输入自动选择并调用子 Skill
- `benchmarks/`：用真实文章建立回归测试样例
- `learning/`：沉淀经 GrowthReviewer 验证后的稳定规则

建议先用真实选题压力测试 v0.2，例如：

- 40年房贷与35岁门槛
- AI对讲机 / GENiEX
- 人工智能经济学项目指南

用完整链路跑通后，再开发总控 `WeChatViralEngine`。
