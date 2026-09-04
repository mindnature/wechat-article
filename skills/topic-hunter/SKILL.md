---
name: topic-hunter
description: 将原始信号加工成高潜公众号选题，完成去重、Scope、真实竞争扫描、张力测试、账号路由、模式选择和锚定评分。
version: "0.6"
reads: [signal, account, production]
writes: [signal, topic, production, workflow]
resources: [../../ledger/content-ledger.csv, ../shared/account-profiles.md, ../../learning/account-baselines.yaml, ../../docs/PRODUCTION-MODES.md]
---

# TopicHunter｜爆款选题与角度

遵循 v0.6 ArticleState、Schema 与 Skill Contract。

## 目标
不只判断“值不值得写”，还要判断“有没有足够张力写出不平庸的主旨”。本 Skill 不写正文。

## Step 0｜去重
检查 Content Ledger：
- 同事件+同核心角度：duplicate
- 同事件+不同角度：related
- 未出现：clear
- 无法访问：unchecked

duplicate 只有出现新事实、新数据、新政策、新案例或完全不同读者任务才继续。

## Step 1｜事实核与 Scope
用一句中性事实描述事件，并标记：
`global | national | province | city | institution | company | single_case | unknown`。

## Step 2｜真实竞争扫描
有搜索能力时至少扫描 3 类来源：公众号/新榜、社交讨论场、新闻/行业媒体。

记录 `sampled_competitors`：标题、来源、时间、角度、目标人群、热度线索。

只能说“本次已扫描样本中……”，禁止声称“全网没人写”。

## Step 3｜角度扩展
至少覆盖：身份、利益、冲突、数据、决策、机制、人性、商业、一手增量。

优先寻找第三层/第四层问题，而不是停在“这个新闻说明什么”。

## Step 4｜Tension Test｜张力测试
每个候选角度必须回答：

1. `contradiction`：具体矛盾/反常识点是什么？
2. `unresolved_question`：哪一个问题还没有被公开材料直接回答？
3. `decision_change`：如果这个判断成立，读者会具体改变哪个决定？
4. `exclusive_material_path`：有没有可能补到别人没有的一手材料，如真实JD、真实对话、亲测、数据、采访、作者职业经验？
5. `strong_judgment_candidate`：如果没有独家材料，是否存在一个可证据约束、但明确不顺着主流说法走的强判断？

写入：
```yaml
topic:
  tension_test:
    status: pass | weak | fail
    contradiction: ""
    unresolved_question: ""
    decision_change: ""
    exclusive_material_path: ""
    strong_judgment_candidate: ""
    note: ""
```

### 通过门
Standard / Deep 至少满足：
- contradiction 或 unresolved_question 不是空泛句；
- decision_change 必须是具体选择变化，不能只是“多关注/多学习/提高认知”；
- `exclusive_material_path` 与 `strong_judgment_candidate` 至少一个成立。

两者都没有：
- 可以降为 Flash 资讯稿；或
- 标记 backup / reject；
- 不允许靠 AuthorLens 后面硬造深度。

## Step 5｜模式选择
- flash：窗口极短，或只有资讯价值
- standard：有可展开张力和材料
- deep：需要亲测/调查/数据/商业深挖

## Step 6｜账号路由
读取五号画像。同一事件跨号必须改变核心问题、读者、证据结构和收益。

## Step 7｜锚定评分
保留 Market Score 与 Account Fit，但评分不替代 Tension Test。

### Market Score
- demand 0–5
- urgency 0–5
- conflict 0–5
- information_gap 0–5

### Account Fit
- identity_match 0–5
- historical_fit：有数据才评分，否则 N/A
- actionability 0–5

另行输出 Evidence、Competition、Timing，不合并总分。

## Step 8｜进入研究门
通过条件：
- 目标读者明确
- Scope 已明确或可研究澄清
- competition 至少 partial（工具不可用时允许 unverified 但必须披露）
- timing 未明显过期
- Standard / Deep 的 Tension Test=pass

通过：`workflow.stage: topic, gate: ready`。
失败：`gate: blocked/rework` 并写 return_to。

## 输出
Human Summary：事实核、Scope、去重、竞争样本、候选角度、Tension Test、账号、生产模式、锚定评分、最终1–3个题目。

State Patch：`signal.*`、`topic.*`、`production.*`、`workflow.*`。

## 禁止
- 热点即写正文
- 把地方/单一个案写成全国/行业趋势
- 把模型记忆伪装成竞争扫描
- 用无法核验数字做标题
- 把“AI正在改变一切”之类空话当 tension
- 没有独家材料路径也没有强判断，却把普通新闻包装成深度稿
