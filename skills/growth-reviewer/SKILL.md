---
name: growth-reviewer
description: 把真实公众号发布数据转成可复用增长经验，评估预登记实验，更新账号基线、作者声音假设和稳定规则。
version: "0.5"
reads: [topic, research, author, architecture, writing, visual, qa, publishing, publication, performance, experiment, workflow]
writes: [performance, learning, workflow]
resources: [../../ledger/content-ledger.csv, ../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml, ../../learning/proven-patterns.md, ../../learning/rejected-patterns.md]
---

# GrowthReviewer｜公众号增长复盘

遵循 v0.5 ArticleState、Schema 与 Skill Contract。

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
- 完读好转发低：表达价值、实用性、独特性、作者判断是否可复述
- 阅读/转发好关注低：账号长期定位与作者声音连接弱

## Step 5｜评论语义
分类共鸣、质疑、补充事实、求资源、反对、追问、转发对象暗示。

额外提取：
- 读者是否引用/复述作者的某个判断
- 哪个具体细节引发讨论
- 哪些评论把文章当“资讯摘要”，哪些体现“认这个作者的看法”

## Step 6｜Author Voice 复盘
记录本篇：
- narrative_choice
- entry_point 类型
- first_person_level
- qa.voice_review
- anti_template_pass 中实际删除/重排了什么

只观察这些选择与完读、分享、关注的关系，不把单篇相关性直接当因果。

重点问：
- 作者POV有没有被读者记住？
- 具体入口是否比摘要式开头更有效？
- 去掉标准建议清单后，完读/分享是否受影响？
- 哪种Voice Profile表达更容易形成关注而不只是阅读？

## Step 7｜评估预登记实验
只有 `experiment.preregistered=true` 时才做正式实验判断。

可验证作者声音相关假设，但必须在发布前登记，例如：
- detail-led opening vs summary opening
- strong POV vs neutral explainer
- numbered sections vs natural sections

输出 supports / inconclusive / contradicts，并记录干扰因素。

## Step 8｜模块归因
归因到 TopicHunter、ResearchPack、AuthorLens、ArticleArchitect、ViralWriter、VisualEditor、PublisherQA、PublishingPlan、Distribution。

每模块最多3条高置信判断，不把相关性直接写成因果。

## Step 9｜经验分级
- L0 observation：单篇
- L1 hypothesis：至少两篇类似信号
- L2 local_rule：同账号/题型3–5篇重复且无明显反例
- L3 stable_pattern：跨时间窗口仍成立

升级记录账号、题型、样本量、时间窗、证据、反例、置信度、复核日期。

Voice 规则同样遵守这个分级，不能因为一篇“更像人”的文章爆了就永久改变账号声音。

## Step 10｜基线与下一轮实验
使用真实、口径一致数据更新基线。下一轮实验最多3个；正式验证必须交给下一篇 PublishingPlan 预登记。

## 输出
Human Summary：表现结论、数据快照、漏斗、评论、作者声音复盘、实验结果、模块归因、经验等级、下一轮实验、Skill更新建议。

Persistence Patch：Ledger、baselines、hypotheses/proven/rejected。

State Patch：`performance.*`、`learning.*`、`workflow.stage: reviewed, gate: ready`。

## 禁止
- 虚构后台数据
- 单篇结果升级长期规则
- 把事后解释冒充实验
- 把“更像人”这种主观感觉直接包装成增长因果
- 把外部大号指标当本账号硬标准
- 声称已持久化但实际上没有
