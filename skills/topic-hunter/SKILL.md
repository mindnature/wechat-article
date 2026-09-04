---
name: topic-hunter
description: 将原始信号加工成高潜公众号选题，完成去重、Scope、真实竞争扫描、账号路由、模式选择和锚定评分。
version: "0.4"
reads: [signal, account, production]
writes: [signal, topic, production, workflow]
resources: [../../ledger/content-ledger.csv, ../shared/account-profiles.md, ../../learning/account-baselines.yaml, ../../docs/PRODUCTION-MODES.md]
---

# TopicHunter｜爆款选题与角度

遵循 `../../schemas/article-state.yaml`、`article-state.schema.json` 与 `../../docs/SKILL-CONTRACT.md`。

## 目标
把“值得关注的事件”加工成“值得特定读者点击、读完和转发的选题”。本 Skill 不写正文。

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

无法完整扫描：`competition.status: partial/unverified`。

## Step 3｜角度扩展
至少覆盖：身份、利益、冲突、数据、决策、机制、人性、商业、一手增量。

优先“情理之中、预料之外”，但不能为了反差扩大 Scope 或制造事实。

## Step 4｜模式选择
读取 `PRODUCTION-MODES.md`，选择：
- flash：窗口极短、事实较简单
- standard：默认主力
- deep：需要亲测/调查/数据/商业深挖

记录 `production.mode` 和 `mode_reason`。

## Step 5｜账号路由
读取五号画像。同一事件跨号必须改变核心问题、读者、证据结构和收益。

## Step 6｜锚定评分
### Market Score
#### demand
0 无明显讨论
1 小圈层信号
2 单平台有讨论
3 多来源有讨论
4 多平台明显升温/核心人群强关注
5 全国级或目标人群极强热点

#### urgency
0 无时效
1 月级窗口
2 周级窗口
3 数日窗口
4 24–48小时窗口
5 正在突发/窗口按小时计算

#### conflict
0 无明显冲突
1 轻微差异
2 有选择/争议
3 明确利益或预期差
4 强身份/利益反差
5 高强度且可证的冲突

#### information_gap
0 公开信息已充分解释
1 轻微信息差
2 可补若干事实
3 有明显机制/数据缺口
4 有独特解释或一手增量空间
5 普遍讨论与关键事实/机制存在显著断层

### Account Fit
#### identity_match
0 几乎无关 → 5 核心读者强代入

#### historical_fit
有足够历史数据才评分；否则 N/A。

#### actionability
0 看完无判断变化 → 5 能直接影响选择/行动。

另行输出 Evidence、Competition、Timing，不合并总分。

## Step 7｜进入研究门
通过条件：
- 目标读者明确
- Scope 已明确或可研究澄清
- competition 至少 partial（工具不可用时允许 unverified 但必须披露）
- 存在信息增量/原创资产可能
- timing 未明显过期

通过：`workflow.stage: topic, gate: ready`。
失败：`gate: blocked/rework` 并写 return_to。

## 输出
### Human Summary
事实核、Scope、去重、竞争样本表、TOP5角度、账号、生产模式、锚定评分、最终1–3个题目。

### State Patch
仅修改 `signal.*`、`topic.*`、`production.*`、`workflow.*`。

### Persistence Patch
Ledger/基线不可访问时标记 `not_persisted`。

## 禁止
- 热点即写正文
- 把地方/单一个案写成全国/行业趋势
- 把模型记忆伪装成竞争扫描
- 用无法核验数字做标题
- 用分数制造伪统计概率
