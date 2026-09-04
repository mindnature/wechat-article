---
name: growth-reviewer
description: 把真实公众号发布数据转成可复用增长经验，评估预登记实验，更新账号基线、作者声音、清晰度与读者交付假设。
version: "0.7"
reads: [topic, research, author, architecture, writing, blind_review, visual, qa, publishing, publication, performance, experiment, workflow]
writes: [performance, learning, workflow]
resources: [../../ledger/content-ledger.csv, ../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml, ../../learning/proven-patterns.md, ../../learning/rejected-patterns.md]
---

# GrowthReviewer｜公众号增长复盘

遵循 v0.7 ArticleState、Schema 与 Skill Contract。

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
- 曝光有点击低：标题/封面/Reader Promise不够具体
- 点击好完读低：第一屏、Thesis Prominence、宏观框架、价值密度、视觉
- 完读好转发低：交付价值、可复述观点、实用性、身份代入
- 阅读/转发好关注低：账号定位与作者声音连接弱

## Step 5｜Clarity & Delivery 复盘｜v0.7
记录本篇：
- promise_type
- reader_contract.core_answer
- answer_shape
- expected_units / delivery_units
- thesis_in_first_screen
- numbered_framework_used
- concrete_task_coverage
- evidence_overload_first_screen

结合真实数据只做有边界的判断：
- 标题点击不差但完读低：检查 Reader Promise 是否在第一屏快速兑现；
- 完读高：观察清晰编号、具体任务链是否可能有帮助，但不单篇归因；
- 评论/转发中反复引用某个编号或框架：记录为可复述性信号；
- 评论出现“所以到底怎么做/哪些”类追问：检查 Promise→Delivery 是否仍有缺口。

## Step 6｜评论语义
分类共鸣、质疑、补充事实、求资源、反对、追问、转发对象暗示。

额外提取：
- 读者能否复述 core_answer；
- 哪个编号/Delivery Unit 被引用最多；
- 哪个具体任务链引发“我也要试”；
- 哪些评论说明正文没有兑现标题承诺；
- 哪些评论把文章只当资讯摘要，哪些体现“认这个作者的看法”。

## Step 7｜Author Voice 复盘
记录 narrative_choice、entry_point、first_person_level、BlindReview findings、Anti-Template实际删改。

重点问：
- 作者POV有没有被记住？
- 具体入口是否有效？
- 微观表达自然度有没有和宏观清晰度同时保住？

不要把“结构清晰”与“AI味低”设成对立实验变量。

## Step 8｜评估预登记实验
只有 `experiment.preregistered=true` 时才做正式实验判断。

可验证：
- core answer first-screen vs delayed answer
- concrete numbered framework vs abstract sections
- strong POV vs neutral explainer
- detail-led opening vs summary opening

一次尽量只改一个主要变量。输出 supports / inconclusive / contradicts，并记录干扰因素。

## Step 9｜模块归因
归因到 TopicHunter、ResearchPack、AuthorLens、ArticleArchitect、ViralWriter、BlindReview、VisualEditor、PublisherQA、PublishingPlan、Distribution。

每模块最多3条高置信判断，不把相关性直接写成因果。

## Step 10｜经验分级
- L0 observation：单篇
- L1 hypothesis：至少两篇类似信号
- L2 local_rule：同账号/题型3–5篇重复且无明显反例
- L3 stable_pattern：跨时间窗口仍成立

Clarity、Voice、标题和框架规则全部遵守同一分级。

## Step 11｜基线与下一轮实验
使用真实、口径一致数据更新基线。下一轮实验最多3个；正式验证必须交给下一篇 PublishingPlan 预登记。

## 输出
Human Summary：表现结论、数据快照、漏斗、Clarity/Delivery复盘、评论、Voice复盘、实验结果、模块归因、经验等级、下一轮实验、Skill更新建议。

Persistence Patch：Ledger、baselines、hypotheses/proven/rejected。

State Patch：`performance.*`、`learning.*`、`workflow.stage: reviewed, gate: ready`。

## 禁止
- 虚构后台数据
- 单篇结果升级长期规则
- 把事后解释冒充实验
- 把“1234结构”或“像人”直接包装成增长因果
- 把外部大号指标当本账号硬标准
- 声称已持久化但实际上没有
