# WeChat Article｜公众号内容生产系统

模块化 AI Skills 工作流。目标不是“让AI写得像人”，而是同时守住四件事：

> **事实可信、观点有力、结构清楚、标题兑现。**

## 当前版本：v0.7 Clarity & Delivery

v0.7 修复 v0.6 压测暴露出的新问题：为了降低AI模板感，系统把“宏观结构清晰”一起拆掉，导致文章有观点但不好读，核心结论埋得太深，标题问“哪些”正文却不直接给分类。

### v0.7 核心修正

- 新增 `Reader Promise Test`：选题阶段先明确读者点进来到底拿什么
- POV竞争从“越深越好”改为五维：`新鲜度 × 读者收益 × 具体度 × 可框架化 × 证据强度`
- ArticleArchitect 新增 `Reader Contract`
- 新增 `Thesis Prominence`：默认前300字出现核心答案
- 新增 `Delivery Units`：正文每个主要章节必须交付一个具体单元
- 知识/工具/决策文章默认允许并鼓励 `01/02/03/04`
- 新增 `Concrete Task Rule`：不能只写“文献研究/科研管理”，必须下钻到任务链
- 新增 `Clarity Pass`
- 新增 `Promise → Delivery Gate`
- Anti-Template 改为只打击微观机械表达，不再打击宏观清晰结构
- Benchmark 从30个扩展到35个

v0.6 的 Tension Test、3 POV竞争、Material Graveyard、Uncertainty Ledger、Segmented Generation、Independent BlindReview 全部保留。

## 一句话原则

> **外面有框架，里面有人味；先给答案，再给证据。**

## Standard 主链

```text
TopicHunter
  ↓
Tension Test + Reader Promise Test
  ↓
ResearchPack
Evidence / Calculation / Uncertainty / Originality
  ↓
AuthorLens
3 POV竞争 → 五维筛选 → selected POV
  ↓
ArticleArchitect
Reader Contract / Core Answer / 01-04 Delivery Units / First-Screen Plan
  ↓
ViralWriter
First Screen → 分段生成 → Clarity Pass → Reorder/Delete → Anti-Template
  ↓
BlindReview
fresh session / different model
  ↓
VisualEditor
  ↓
PublisherQA
Truth + Thesis Prominence + Promise Delivery + Concrete Delivery + BlindReview
  ↓
PublishingPlan
  ↓
发布 → GrowthReviewer
```

## 1. TopicHunter：不只问“值不值得写”

Standard / Deep 必须同时通过：

### Tension Test
- 有具体矛盾/未解问题
- 能改变读者某个具体决定
- 有独家材料路径或证据约束的强判断

### Reader Promise Test
- 标题向读者承诺什么？
- 现在能不能先给一个方向性答案？
- 能不能拆成3–5个清晰交付单元？

“了解趋势”“提高认知”不是有效 Reader Promise。

## 2. AuthorLens：深度不再自动胜出

必须生成3个真正不同的 POV，并分别评价：

- novelty
- reader_value
- specificity
- frameworkability
- evidence_strength

最哲学、最深的观点不一定获胜。

如果一个观点无法变成清晰的 01/02/03/04，读者也不知道怎么用，它不适合作为知识型公众号主线。

## 3. Reader Contract

Architect 必须冻结：

```yaml
promise_type: which
promise: "高校老师能拿到哪些Agent委派建议"
core_answer: "把易验收、可撤回、责任仍在人手里的执行链整段交给Agent"
answer_shape: numbered_framework
expected_units: 4
```

标题问什么，正文就必须交付什么。

- “哪些” → 明确分类
- “怎么做” → 明确步骤
- “值不值得” → 判断标准 + 代价 + 结论
- 标题承诺4个 → 正文真的给4个

## 4. Thesis Prominence

Standard / Deep 默认要求：

> **核心结论在前300个中文字符内出现。**

第一屏至少包含：
1. 方向性答案/核心结论；
2. 文章会交付什么框架；
3. 可选：一个具体事实或场景建立可信度。

Benchmark、参数、政策背景默认放在核心答案之后。

## 5. 01/02/03/04 不是AI味

对知识型、工具型、决策型、政策解读型文章，清晰编号是正向导航。

允许甚至鼓励：

```text
01｜文献研究：先把“搜、下、整、比”交出去
02｜数据分析：把“跑、错、改、重跑”交出去
03｜科研管理：把跨Word、Excel、网页的材料活交出去
04｜教学准备：把生产型工作交出去
```

AI味来自的是微观重复：
- 每节同长度
- 每节同句式
- 每节都“总结→解释→总结”
- 每节都反转
- 每节都升华

所以 v0.7 的 Anti-Template 只处理微观模板，不拆宏观框架。

## 6. Concrete Task Rule

“文献研究”不是具体交付。

要继续拆到：

`搜索 → 下载 → 去重 → 提取研究问题/数据/方法 → 建Literature Matrix → 标Gap`

“数据分析”也不够，要拆到：

`导入 → 清洗 → 跑代码 → 看报错 → 重跑 → 出图 → 导出`

读者必须能想象：这件事明天怎么发生在自己的电脑上。

## 7. Clarity Pass

Writer 在 BlindReview 前必须检查：

- thesis_in_first_screen
- promise_delivery_status
- numbered_framework_used
- missing_delivery_units
- evidence_overload_first_screen
- concrete_task_coverage

Clarity不过，不能靠“文风自然”补救。

## 8. BlindReview 仍然独立

v0.6 规则保留：

有效：
- fresh_session
- different_model

无效：
- same_context

BlindReview主要审AI感、语感、Voice；它不能替代 Reader Contract 和 Promise→Delivery。

## 9. Evidence / Originality / Uncertainty 继续保留

事实层仍然严格：

`Source → Claim/Calc → Architecture → Writing → QA`

Originality：
- Flash：可conditional
- Standard：≥1A 或 ≥2B
- Deep：≥1A + ≥1B

真实犹豫只能绑定 Uxxx，不允许为了“人味”表演不确定。

## 10. 机器校验

```bash
pip install -r requirements-dev.txt
python scripts/validate_state.py path/to/article-state.yaml
```

v0.7 Validator 会拦：

- Reader Promise 空泛
- “哪些/怎么做”却没有至少3个交付预览
- selected POV 可框架化/具体度太低
- Reader Contract缺Core Answer
- Delivery Unit没有具体例子
- 标题问“哪些”却不用明确编号框架
- 核心结论没有进入第一屏
- 第一屏被Benchmark/支持性证据压满
- Promise未兑现
- Concrete Task Coverage失败
- 同上下文BlindReview
- 假U节点/证据断链

## 11. Benchmark

当前35个案例。

v0.7 新增：
- B031：核心观点埋后半篇
- B032：标题问“哪些”正文不分类
- B033：不能把1234误判成AI味
- B034：只有抽象大类、没有具体任务链
- B035：深但不可交付的POV不能自动胜出

## 最终质量标准

一篇稿子必须同时满足：

`Truth + Strong Thesis + Reader Promise + Clear Framework + Concrete Delivery + Natural Voice`

其中最重要的顺序是：

> **读者先看懂你要说什么，再决定要不要相信你的证据；先兑现标题，再谈文风。**
