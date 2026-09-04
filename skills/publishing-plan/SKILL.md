---
name: publishing-plan
description: 在QA通过后生成微信公众号发布计划，确定最终标题、封面、摘要、发布时间、分发、承接与数据回收，并可预登记增长实验。
version: "0.4"
reads: [topic, writing, visual, qa, account, production, workflow, experiment]
writes: [publishing, experiment, workflow]
resources: [../../learning/account-baselines.yaml, ../../learning/hypotheses.yaml]
---

# PublishingPlan｜公众号发布策略

遵循 v0.4 ArticleState、Schema 与 Skill Contract。

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

任何改动若引入新事实或扩大 Scope，退回 PublisherQA。

## Step 2｜发布紧迫度
按 production.mode、topic.timing、signal.freshness 判断：
- immediate：小时级热点
- same_day：当天
- scheduled：有明确时段
- evergreen：时段敏感度低

不凭经验编造“黄金时间”；优先使用账号历史基线。样本不足时标记 confidence low。

## Step 3｜发布窗口
输出具体建议窗口及理由：
- 热点剩余寿命
- 目标读者活跃场景
- 同账号历史表现
- 是否需要抢在竞争内容前

## Step 4｜分发计划
只选择与文章目标一致的渠道，例如：
- 公众号主推
- 朋友圈
- 视频号承接
- 小红书/其他平台改编

禁止诱导、强迫、欺骗式互动。

## Step 5｜内容承接
判断是否需要：
- 后续深挖
- 工具教程
- 数据更新
- 评论区问题二次文章

输出 `followups`，避免爆文成为孤立流量。

## Step 6｜实验预登记
如 learning/hypotheses 中有待测试假设，可在发布前写：
```yaml
experiment:
  experiment_id: EXP-001
  hypothesis: "具体金额标题提高阅读转化"
  variable: title_type
  variant: concrete_money
  comparator: abstract_benefit
  primary_metric: read_rate
  preregistered: true
```

一次只改少量变量。没有实验则留空。

## Step 7｜数据回收计划
默认记录：1h / 24h / 72h。
需要保存：曝光、阅读、分享、完读、关注、推荐来源等平台可得指标。

## 输出
### Human Summary
最终标题、封面、摘要、发布窗口、紧迫度、分发、承接、实验、数据回收计划。

### State Patch
- `publishing.*`
- `experiment.*`（如有）
- `workflow.stage: publishing, gate: ready`

真正完成微信公众号发布后，才由发布动作写：
- `publication.published_at`
- `publication.url`
- `workflow.stage: published`

## 禁止
- QA未A就进入发布
- 视觉资产未ready就声称可发布
- 包装阶段重新加入未经QA的新事实
- 凭空断言固定黄金发布时间
- 事后才伪造实验假设
