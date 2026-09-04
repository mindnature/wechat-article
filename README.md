# WeChat Article｜公众号爆款生产系统

面向微信公众号内容生产的模块化 AI Skills 工作流。

目标不是用一个“大而全 Prompt”包办所有环节，而是建立一条可核验、可复盘、可逐步学习的内容生产链：选题、研究、架构、写作、视觉、质检、发布后学习。

## 当前版本：v0.3 Foundation

v0.3 的重点不是继续增加 Skill，而是修复 v0.2 的工程底座：

- 所有 Skill 读写统一 `ArticleState`
- 关键事实进入 Evidence Ledger
- 自行算账进入 Calculation Ledger
- 政策/规则/案例强制 Scope 标签
- 选题评分拆成 Market / Account Fit / Evidence / Competition / Timing，取消伪精确总分
- 加入 Originality Gate，防止退化成 AI 二手整理号
- 加入 Content Ledger，支持历史去重
- 加入 learning/ 持久化增长经验
- 加入 benchmarks/ 回归测试
- 统一 7 个 Skill 的 front matter 与输入/输出契约

## 目录

```text
wechat-article/
├── README.md
├── docs/
│   └── SKILL-CONTRACT.md
├── schemas/
│   └── article-state.yaml
├── ledger/
│   └── content-ledger.csv
├── learning/
│   ├── README.md
│   ├── account-baselines.yaml
│   ├── hypotheses.yaml
│   ├── proven-patterns.md
│   └── rejected-patterns.md
├── benchmarks/
│   ├── README.md
│   └── cases.yaml
└── skills/
    ├── topic-hunter/SKILL.md
    ├── research-pack/SKILL.md
    ├── article-architect/SKILL.md
    ├── viral-writer/SKILL.md
    ├── visual-editor/SKILL.md
    ├── publisher-qa/SKILL.md
    ├── growth-reviewer/SKILL.md
    └── shared/account-profiles.md
```

## 核心：ArticleState

所有子 Skill 使用 `schemas/article-state.yaml` 作为共享状态，不再依靠自由文本接力。

推荐状态流：

```text
signal
  ↓
topic_selected
  ↓
researched
  ↓
architected
  ↓
drafted
  ↓
visually_planned
  ↓
qa_passed
  ↓
published
  ↓
reviewed
```

任何环节发现关键证据问题，都可以退回上一阶段。

每个 Skill 输出两层：

1. `Human Summary`：给作者阅读；
2. `State Patch`：仅更新自己负责的 ArticleState 字段。

详见 `docs/SKILL-CONTRACT.md`。

## 生产链

```text
原始信号 / 热点 / 政策 / 产品 / 案例
        ↓
TopicHunter
去重 + Scope + 真实竞争扫描 + 独特角度 + 账号路由
        ↓
ResearchPack
Source Registry + Evidence Ledger + Calculation Ledger + Originality Gate
        ↓
ArticleArchitect
核心命题 + 证据绑定结构 + 故事线 + 情绪线 + 视觉节点
        ↓
ViralWriter
完整正文 + title_safe 标题 + 事实/计算/推断边界
        ↓
VisualEditor
封面 + 真实图资产单 + AI图资产单 + 图源/权利风险
        ↓
PublisherQA
标题/首屏/Scope/证据/计算/图片/版权/排版硬质检
        ↓
发布
        ↓
GrowthReviewer
1h / 24h / 72h 漏斗复盘 + Content Ledger + learning/
        ↓
下一轮 TopicHunter
```

## 五个公众号

共享账号画像：`skills/shared/account-profiles.md`

- 思然日新：高校青年教师 / 教学科研 / 项目申报 / AI工作流
- 思然知己：AI热点 / AI学习方向
- 思然天工：AI工具 / Skill / Agent / 教程与工作流
- 思然经世：AI赚钱 / 商业机会 / 副业与案例拆解
- 思然修远：30+成长 / 工作家庭 / 关系选择 / 社会热点

同一事件可以跨账号使用，但必须改变核心问题、目标读者、证据结构和读者收益。

## v0.3 的三个硬闸门

### 1. Scope Gate

所有政策、规则、统计、趋势必须明确范围：

`global | national | province | city | institution | company | single_case | unknown`

例如：上海部分银行的贷款口径不能直接写成全国统一政策。

### 2. Evidence Gate

标题、导语、核心结论里的关键事实必须进入 `research.claims`，绑定来源与验证状态。

准备写进标题的事实还必须：

```text
title_safe: true
```

### 3. Originality Gate

标准/深度文章至少增加一种普通新闻没有的内容：

- 自主计算
- 作者亲测
- 一手职业经验
- 独立对比
- 数据整理
- 原始截图
- 采访/调查
- 新框架/跨源综合

如果完全没有，标记：

```text
commodity_content_risk: high
```

避免系统长期退化成“AI重新写公开资料”。

## 评分方式

v0.2 的单一100分制已取消。

TopicHunter 分开输出：

### Market Score
- demand 0–5
- urgency 0–5
- conflict 0–5
- information_gap 0–5

### Account Fit
- identity_match 0–5
- historical_fit 0–5 / N/A
- actionability 0–5

另外独立判断：

- Evidence Confidence
- Competition Level
- Timing

在没有足够历史数据前，不把“97分”包装成统计意义上的爆款概率。

## Content Ledger

`ledger/content-ledger.csv` 记录每篇文章：

- 日期
- 账号
- 事件
- 核心角度
- 标题
- 发布状态
- 阅读/分享/完读/关注等表现

TopicHunter 在新题进入时先做去重：

`clear | related | duplicate | unchecked`

## Learning Layer

GrowthReviewer 的经验不再停留在聊天里。

`learning/` 按四级沉淀：

- Level 0 Observation
- Level 1 Hypothesis
- Level 2 Local Rule
- Level 3 Stable Pattern

只有 Level 2/3 才可作为长期稳定规则；外部头部账号经验只能作为初始假设。

## Benchmarks

`benchmarks/cases.yaml` 当前包含 14 个固定回归案例，包括：

- 40年房贷与地方/全国 Scope
- AI商业个案
- 国自然政策指南
- 网友县城工资讨论
- 单高校AI政策
- AI工具亲测
- 高收入个案
- 班群热点
- 科研Benchmark
- 弱热点
- 假新闻
- 过时热点
- 重复选题
- 计算敏感题

修改 Skill 后必须检查关键能力没有退化，尤其是：Scope、假新闻、重复、计算、个案泛化、伪造亲测。

## 当前设计边界

v0.3 仍然不是全自动智能体：

- 尚未加入 `signal-radar`
- 尚未加入 `wechat-viral-engine` 总控 Orchestrator
- VisualEditor 在没有图片搜索/生成工具时只负责规划，不得声称已经执行
- learning/ 的持久化取决于运行环境是否有仓库写权限
- benchmarks 当前是固定测试协议，尚无自动 runner

这些是刻意保留的边界。先把底层协议稳定，再做自动化总控。

## 下一阶段建议

先用 3–5 个真实选题跑 v0.3 回归：

1. 40年房贷
2. GENiEX AI对讲机
3. 人工智能经济学项目指南
4. 一个弱热点
5. 一个只有二手来源的可疑事件

确认 ArticleState、Evidence Ledger、Originality Gate 和 Content Ledger 运行稳定后，再进入 v0.4：

- SignalRadar
- Visual Asset Executor
- WeChatViralEngine Orchestrator
- Benchmark runner

## 核心原则

- 热点不是选题，角度才是。
- 一手来源优先于二手转述。
- 范围比措辞更重要。
- 计算必须可复现。
- 信息线与情绪线同时设计。
- 真实图负责证明，生成图负责解释/表达。
- 标注图源不等于自动取得版权许可。
- 不机械追求短文，长度由信息价值决定。
- 单篇爆文只产生观察，不直接改写长期规则。
- 爆款是概率工程，不以标题党替代事实、独特性和读者价值。
