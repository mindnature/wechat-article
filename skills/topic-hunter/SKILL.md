---
name: topic-hunter
description: 将热点、政策、产品、案例或原始信号加工成适合微信公众号的高潜选题与独特角度，并完成账号路由、竞争扫描与去重判断。
version: "0.3"
reads: [signal, account, ledger, learning]
writes: [signal.duplicate_check, topic, status]
---

# TopicHunter｜爆款选题与角度

## 目标
把“值得关注的事件”加工成“值得点击、值得转发、适合特定读者的公众号选题”。本 Skill 不写正文。

所有结构化字段遵循 `../../schemas/article-state.yaml` 和 `../../docs/SKILL-CONTRACT.md`。

## 核心原则
1. 热点只是原材料，角度决定竞争力。
2. 第一反应通常也是多数创作者的第一反应，必须先做真实竞争扫描。
3. 优先寻找“情理之中、预料之外”的切口，但不得为了反差牺牲事实。
4. 每个选题必须回答：给谁看、为什么现在看、为什么点开、为什么转发。
5. 不把单一个案、地方执行口径或企业规则自动提升为全国/行业趋势。
6. 不使用伪精确的单一“97分”。把市场势能、账号适配、证据可信度、竞争强度与时机分开判断。

## 输入
至少包含一种：事件、链接、新闻、政策、产品、案例、关键词、候选题。
可选：目标公众号、目标读者、时效窗口、已有素材。

## Step 0｜Content Ledger 去重
优先检查 `../../ledger/content-ledger.csv`：
- 同事件 + 同核心角度：`duplicate`
- 同事件 + 不同角度：`related`
- 未写过：`clear`

如果无法访问 Ledger，标记 `unchecked`，不得声称“没有写过”。

重复选题只有在出现“新增事实、新数据、新政策、新案例或完全不同读者任务”时才能继续。

## Step 1｜事实核与 Scope
先压缩成一句中性事实，并给事件范围打标签：
`global | national | province | city | institution | company | single_case | unknown`。

范围不清时必须保留 `unknown`。

## Step 2｜真实竞争角度扫描
如有网页/搜索能力，必须搜索真实市场内容，而不是凭模型记忆猜“大家都怎么写”。

至少检查 3 类来源，优先：
- 微信公众号公开内容/新榜等公众号数据源
- 知乎/微博/小红书等讨论场
- 新闻媒体/行业媒体/搜索结果

记录：
- `scanned_sources`
- 已拥挤标题/角度
- 内容空位
- 竞争强度 low/medium/high

如果工具不可用或证据不足，写 `competition.status: unverified/partial`。

## Step 3｜角度扩展
至少从以下维度生成候选：
- 身份：谁会觉得“说的就是我”
- 利益：钱、收入、成本、机会、风险、时间
- 冲突：规则门槛、赢家输家、预期反转
- 数据：关键数字、数量级、同比、成本收益
- 决策：读者是否需要做选择
- 机制：为什么现在发生
- 人性：焦虑、体面、身份、关系、控制、选择
- 商业：谁赚钱、怎么赚钱、价值链如何重组
- 一手增量：作者能否亲测、计算、调查、复现

## Step 4｜反差过滤
逐个问：
- 是否只是任何媒体都能写的第一反应？
- 是否只是换标题，没有信息增量？
- 是否存在更具体人群、更直接利益、更意外但可证的冲突？
- 是否需要把范围缩小，才能避免过度概括？

淘汰泛泛角度。

## Step 5｜账号路由
读取 `../shared/account-profiles.md`。

若多个账号可写，必须分别说明：
- 核心问题
- 目标读者
- 所需证据
- 读者收益

禁止一稿多号简单改写。

## Step 6｜分离式评分
### Market Score（每项0–5）
- demand：外部关注度
- urgency：时效紧迫度
- conflict：冲突/反差强度
- information_gap：信息差

### Account Fit Score（每项0–5）
- identity_match：目标读者身份匹配
- historical_fit：历史数据匹配；样本不足填 N/A
- actionability：读者能否据此行动/判断

另行输出：
- `evidence_confidence`: high/medium/low/unknown
- `competition.level`: low/medium/high/unknown
- `timing`: now/soon/evergreen/late/unknown

不要把这些维度强行压成一个总分。

## Step 7｜进入研究前的门
优先推荐满足以下条件的题：
- Scope 明确或可在 ResearchPack 中澄清
- 竞争扫描至少 partial
- 有明确目标读者
- 存在信息增量或可构造一手增量
- 时间窗口仍成立

否则进入备选或拒绝。

## 输出
### Human Summary
1. 事实核 + Scope
2. Content Ledger 去重结果
3. 真实竞争扫描
4. 候选角度 TOP 5
5. 推荐账号与理由
6. Market Score / Account Fit / Evidence / Competition / Timing
7. 最终推荐 1–3 个题目雏形

### State Patch
仅输出：
- `signal.scope`
- `signal.duplicate_check`
- `topic.*`
- `status: topic_selected`（仅当通过）

## 禁止
- 看到热点即直接写文章
- 用“震惊/突然/炸了”等制造假冲突
- 把网友个案泛化成全国趋势
- 把地方银行/学校/企业规则写成全国统一政策
- 把模型记忆伪装成真实竞争扫描
- 用无法核验的数据作为标题核心
