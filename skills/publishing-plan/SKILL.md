---
name: publishing-plan
description: 在QA通过后生成微信公众号发布计划，确定最终标题、封面、摘要、发布时间、分发、承接与数据回收，并可预登记增长实验。
version: "0.5"
reads: [topic, author, writing, visual, qa, account, production, workflow, experiment]
writes: [publishing, experiment, workflow]
resources: [../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml]
---

# PublishingPlan｜公众号发布策略

遵循 v0.5 ArticleState、Schema 与 Skill Contract。

## 前置门
必须：
- `workflow.stage: qa`
- `workflow.gate: ready`
- `qa.status: A`
- `visual.assets_ready: true`

否则不得生成“ready to publish”。

## Step 1｜最终包装冻结
确定：
- final_title：从已通过QA的标题中选
- final_cover_asset_id：必须指向 ready 封面
- summary：公众号摘要/分享摘要

最终包装必须继续保持 AuthorLens 的主问题和 Voice Profile，不得为了“更像爆款”把标题/摘要改回通用AI资讯腔。

任何改动若引入新事实、扩大 Scope 或改变作者主判断，退回 PublisherQA。

## Step 2｜发布紧迫度
按 production.mode、topic.timing、signal.freshness 判断：
- immediate：小时级热点
- same_day：当天
- scheduled：有明确时段
- evergreen：时段敏感度低

不凭经验编造“黄金时间”；优先使用账号历史基线。样本不足时标记 confidence low。

## Step 3｜发布窗口
输出具体建议窗口及理由：热点剩余寿命、目标读者活跃场景、同账号历史表现、竞争内容时间差。

## Step 4｜分发计划
只选择与文章目标一致的渠道，例如公众号主推、朋友圈、视频号承接、小红书/其他平台改编。

跨平台改编可以重写，不要求把公众号文章压缩成统一摘要模板。

## Step 5｜内容承接
判断是否需要后续深挖、工具教程、数据更新、评论区问题二次文章。

后续文章应延续读者真实问题，不为了“做系列”机械拆分。

## Step 6｜实验预登记
如 learning/hypotheses 中有待测试假设，可在发布前登记 experiment.*。一次只改少量变量。

可新增与作者声音有关的实验，例如：
- 具体细节开头 vs 摘要式开头
- 强作者判断标题 vs 中性资讯标题
- 有/无数字编号小标题

没有预登记的事后解释不能包装成正式实验。

## Step 7｜数据回收计划
默认记录 1h / 24h / 72h，并保存平台可得曝光、阅读、分享、完读、关注、推荐来源等指标。

## 输出
Human Summary：最终标题、封面、摘要、发布窗口、紧迫度、分发、承接、实验、数据回收计划。

State Patch：
- `publishing.*`
- `experiment.*`（如有）
- `workflow.stage: publishing, gate: ready`

真正发布后才写 `publication.*` 与 `workflow.stage: published`。

## 禁止
- QA未A就进入发布
- 视觉资产未ready就声称可发布
- 包装阶段重新加入未经QA的新事实
- 为点击把作者主线重新包装成通用“XX来了，普通人怎么办”
- 凭空断言固定黄金发布时间
- 事后才伪造实验假设
