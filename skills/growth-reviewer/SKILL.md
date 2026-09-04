---
name: growth-reviewer
description: 把真实公众号发布数据转成可复用增长经验，评估预登记实验，更新账号基线、假设和稳定规则。
version: "0.4"
reads: [topic, research, architecture, writing, visual, qa, publishing, publication, performance, experiment, workflow]
writes: [performance, learning, workflow]
resources: [../../ledger/content-ledger.csv, ../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml, ../../learning/proven-patterns.md, ../../learning/rejected-patterns.md]
---

# GrowthReviewer｜公众号增长复盘

遵循 v0.4 ArticleState、Schema 与 Skill Contract。

## 前置门
必须已真实发布：`workflow.stage: published`。没有后台数据时只记录待复盘，不虚构结果。

## Step 1｜Content Ledger
写入文章基础信息和真实表现；无法持久化则输出 Ledger Patch 并标记 not_persisted。

## Step 2｜账号基线
优先同账号、同题型、相近时段/热点类型。样本不足：`baseline_confidence: low`。

## Step 3｜关键指标
可用时计算：曝光→阅读、推荐曝光→阅读、完读/时长、转阅比、赞阅比、在看率、收藏率、关注转化率、净增关注。

口径不同不横比。

## Step 4｜漏斗诊断
- 曝光低：选题/时机/冷启动/人群
- 曝光有点击低：标题/封面/身份匹配
- 点击好完读低：承诺、开头、结构、价值密度、视觉
- 完读好转发低：表达价值、实用性、独特性
- 阅读/转发好关注低：账号长期定位连接弱

## Step 5｜评论语义
分类共鸣、质疑、补充事实、求资源、反对、追问、转发对象暗示；提取真实语言和自然延伸题。

## Step 6｜评估预登记实验
只有 `experiment.preregistered=true` 时才做正式实验判断：
- 检查 variable 是否真的只改变少量变量
- 用 primary_metric 评价
- 输出 supports / inconclusive / contradicts
- 记录干扰因素

没有预登记的事后解释只能降级为 observation，不能包装成实验结果。

## Step 7｜模块归因
归因到 TopicHunter、ResearchPack、ArticleArchitect、ViralWriter、VisualEditor、PublisherQA、PublishingPlan、Distribution。每模块最多3条高置信判断，不把相关性直接写成因果。

## Step 8｜经验分级
- L0 observation：单篇
- L1 hypothesis：至少两篇类似信号
- L2 local_rule：同账号/题型3–5篇重复且无明显反例
- L3 stable_pattern：跨时间窗口仍成立

升级记录账号、题型、样本量、时间窗、证据、反例、置信度、复核日期。

## Step 9｜基线更新
使用真实、口径一致数据。优先滚动统计：sample_size、median/mean、近30天、全历史。样本不足不建硬阈值。

## Step 10｜下一轮实验
最多3个；若要正式验证，必须交给下一篇 PublishingPlan 预登记。

## 输出
Human Summary：表现结论、数据快照、漏斗、评论、实验结果、模块归因、经验等级、下一轮实验、Skill更新建议。

Persistence Patch：Ledger、baselines、hypotheses/proven/rejected。

State Patch：`performance.*`、`learning.*`、`workflow.stage: reviewed, gate: ready`。

## 禁止
- 虚构后台数据
- 单篇结果升级长期规则
- 把事后解释冒充实验
- 把外部大号指标当本账号硬标准
- 声称已持久化但实际上没有
