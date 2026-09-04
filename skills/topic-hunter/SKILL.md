---
name: topic-hunter
description: 将原始信号加工成高潜公众号选题，完成去重、Scope、竞争扫描、张力测试、读者承诺测试、账号路由和模式选择。
version: "0.7"
reads: [signal, account, production]
writes: [signal, topic, production, workflow]
resources: [../../ledger/content-ledger.csv, ../shared/account-profiles.md, ../../learning/account-baselines.yaml, ../../docs/PRODUCTION-MODES.md, ../../docs/CLARITY-DELIVERY.md]
---

# TopicHunter｜选题、张力与读者承诺

## 目标
不只判断“有没有深度”，还要判断“读者为什么点、点进来能拿走什么、能否被组织成清晰答案”。

## Step 0｜去重
Content Ledger：同事件+同角度=duplicate；同事件+不同角度=related；无法访问=unchecked。

duplicate 只有新事实/新数据/新政策/新案例/新读者任务才继续。

## Step 1｜事实核与 Scope
用一句中性事实描述事件，并标记 Scope。

## Step 2｜真实竞争扫描
有工具时至少扫描3类来源：公众号/新榜、社交讨论场、新闻/行业媒体。

只对本次样本下结论，禁止“全网没人写”。

## Step 3｜角度扩展
至少覆盖：身份、利益、冲突、数据、决策、机制、人性、商业、一手增量。

第三层/第四层不是目的；目的是找到“既有判断，又能被读者清楚拿走”的角度。

## Step 4｜Tension Test
记录：contradiction / unresolved_question / decision_change / exclusive_material_path / strong_judgment_candidate。

Standard/Deep：
- contradiction或unresolved_question至少一个具体；
- decision_change不能只是“多关注/多学习/提高认知”；
- exclusive_material_path或strong_judgment_candidate至少一个成立。

## Step 5｜Reader Promise Test｜v0.7新增
每个最终候选题必须回答：

```yaml
topic:
  reader_promise:
    promise_type: which | how | why | compare | decide | explain | list | other
    promise: "读者点进来具体要拿到什么"
    provisional_answer: "现在能不能先给一个方向性答案"
    delivery_shape: numbered_framework | decision_tree | comparison | checklist | narrative | hybrid
    delivery_preview:
      - "01 ..."
      - "02 ..."
      - "03 ..."
    status: pass | weak | fail
```

通过要求：
- promise具体，不是“了解趋势”；
- provisional_answer能直接回应标题；
- 对知识/工具/决策型题，至少能预览3个清晰交付单元；
- 若标题是“哪些/怎么/如何/几类”，默认可形成编号框架。

失败例：
- 标题问“哪些工作可以交给Agent”，但正文只能泛谈“AI更强了”；
- 标题问“怎么做”，但只能解释背景；
- 角度听起来很深，却无法拆成读者能拿走的结构。

Reader Promise weak/fail：降级、换角度或不写，不允许指望Writer后面硬救。

## Step 6｜模式选择
- Flash：窗口短/资讯价值为主
- Standard：有张力、有明确Reader Promise、可交付
- Deep：在Standard基础上有更强一手材料/实验/调查

## Step 7｜账号路由
同一事件跨号必须改变：核心问题、Reader Promise、证据结构和读者收益。

## Step 8｜评分
Market Score与Account Fit保留，但不合并成伪精确总分。

重点增加一个人工判断：`delivery_potential = high | medium | low`。

如果“深度高、delivery_potential低”，不优先。

## Step 9｜进入研究门
Standard/Deep必须：
- 目标读者明确
- Scope可控
- competition至少partial
- timing未过期
- Tension Test=pass
- Reader Promise Test=pass

失败：blocked/rework，并写 return_to。

## 输出
Human Summary：事实核、Scope、竞争样本、候选角度、Tension Test、Reader Promise、delivery preview、账号、模式、评分、最终1–3个标题方向。

State Patch：signal.* / topic.* / production.* / workflow.*。

## 禁止
- 热点即写正文
- 把“更深”当唯一选角标准
- 标题承诺与正文潜在交付不一致
- “了解趋势/提升认知”式空Reader Promise
- 无明确交付结构却硬做Standard/Deep
