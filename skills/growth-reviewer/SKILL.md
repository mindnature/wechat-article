---
name: growth-reviewer
description: 把公众号发布数据转成可复用增长经验，更新账号基线、假设和稳定规则，并反向修正生产链。
version: "0.3"
reads: [topic, research, architecture, writing, visual, qa, publication, performance]
writes: [performance, learning, status]
resources: [../../ledger/content-ledger.csv, ../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml, ../../learning/proven-patterns.md, ../../learning/rejected-patterns.md]
---

# GrowthReviewer｜公众号增长复盘

## 目标
把单篇文章的发布数据转成可复用经验，并反向更新选题、研究、结构、写作、视觉与发布时间规则。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

本 Skill 不以阅读量作为唯一结论，而是区分：曝光、点击、完读、分享、推荐放大、关注转化和账号长期价值。

## 数据输入
最低：
- 标题
- 账号
- 发布时间
- 1h/24h/72h阅读量（有多少给多少）

推荐：曝光、推荐占比、订阅读者阅读、分享、点赞、在看、收藏、完读率、新增关注、取关、评论、阅读来源、封面版本、同期账号基线。

没有的平台数据写 N/A，禁止补猜。

## Step 1｜写入 Content Ledger
将文章基础信息与真实表现补充到 `../../ledger/content-ledger.csv`。

如果当前环境不能直接写文件，输出标准 Ledger Row Patch，不得声称已经持久化。

## Step 2｜加载账号基线
读取 `../../learning/account-baselines.yaml`。

优先与：
1. 同账号历史基线
2. 同账号同题型基线
3. 相近发布时间/热点类型
比较。

没有足够样本时明确 `baseline_confidence: low`。

## Step 3｜关键指标
数据可用时计算：
- 曝光→阅读转化率
- 推荐曝光→阅读转化率
- 完读率/平均阅读时长
- 转阅比 = 分享÷阅读
- 赞阅比 = 点赞÷阅读
- 在看率
- 收藏率
- 关注转化率 = 新增关注÷阅读
- 净增关注

不同平台口径不一致时不强行横比。

## Step 4｜漏斗诊断
### 曝光低
选题势能、时机、冷启动、人群匹配。

### 曝光有但点击低
优先标题、封面、身份匹配、冲突强度。

### 点击好但完读低
标题承诺、开头、信息增量位置、结构、长度价值密度、视觉节奏。

### 完读好但转发低
身份表达、实用性、独特观点、可复述判断不足。

### 阅读/转发好但关注低
文章与账号长期定位连接弱，或属于偶发跨圈题。

### 推荐快速放大
复盘首批行为、标题清晰度、目标人群、转发/完读与推荐人群差异。

## Step 5｜评论区语义复盘
分类：共鸣、质疑、补充事实、求教程/资源、反对、追问、转发对象暗示。

提取：
- 哪一句真正打中读者
- 哪一部分没讲清
- 下一篇自然延伸题
- 读者真实语言

## Step 6｜模块归因
归因到：
- SignalRadar
- TopicHunter
- ResearchPack
- ArticleArchitect
- ViralWriter
- VisualEditor
- PublisherQA
- Distribution

每个模块最多0–3条高置信度判断，禁止把相关性直接写成因果。

## Step 7｜经验分级与持久化
读取 `../../learning/hypotheses.yaml`、`proven-patterns.md`、`rejected-patterns.md`。

等级：
- Level 0 observation：单篇
- Level 1 hypothesis：至少两篇类似信号
- Level 2 local_rule：同账号/题型3–5篇重复且无明显反例
- Level 3 stable_pattern：跨时间窗口仍成立

升级规则必须记录：账号、题型、样本量、时间窗口、支持证据、反例、置信度、复核日期。

如果运行环境不能直接更新 learning 文件，只输出明确的 `Learning Patch`；不得声称“已经学习完成”。

## Step 8｜更新账号基线
当后台数据真实且口径一致时，更新 `account-baselines.yaml`。

推荐使用滚动统计而不是简单覆盖：
- sample_size
- median/mean（视指标分布）
- 近30天与全历史分开

样本不足时不建立硬阈值。

## Step 9｜下一轮实验
每次最多3个实验，一次只改少量变量，例如：
- 金额型标题 vs 抽象利益标题
- 固定发布时间窗口连续测试
- 核心冲突提前到前100字
- 第一张证据图位置前后对照

## 输出
### Human Summary
1. 表现结论：爆发/高于基线/正常/低于基线/失败但有亮点
2. 数据快照
3. 漏斗诊断
4. 成功/失败原因≤5
5. 评论区信号
6. 模块归因
7. 经验等级
8. 下一轮实验≤3
9. Skill更新建议

### Persistence Patch
- Content Ledger row
- account-baselines update（如满足）
- hypotheses/proven/rejected patch

### State Patch
- `performance.*`
- `learning.*`
- `status: reviewed`

## 禁止
- 单篇阅读量决定全部结论
- 一次巧合升级长期规则
- 虚构后台数据
- 把外部大号指标当本账号硬标准
- 把高点击自动等于好内容
- 声称已持久化但实际只生成了建议
- 建议诱导、强迫、欺骗式互动
