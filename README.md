# WeChat Article｜公众号内容生产系统

模块化 AI Skills 工作流。目标不是“让AI写得像人”，而是同时守住五件事：

> **事实可信、观点有力、结构清楚、标题兑现、正文好读。**

## 当前版本：v0.7.1 Paragraph Rhythm

v0.7.1 是 v0.7 Clarity & Delivery 的可读性补丁。它不改 TopicHunter、3 POV竞争、Reader Contract、BlindReview 等主链，专门修复一个实际压测问题：

> 文章虽然有 01/02/03/04 框架，但正文为了“节奏感”被拆成大量几个字、一句话一段，导致手机端滑屏距离变长、信息密度下降、AI味反而更重。

### v0.7.1 核心修正

- 新增 `Paragraph Rhythm` 正文段落规则
- 正常正文默认以 2–4 句自然段完成一个小意思
- 单句段落只用于核心结论、转折、必要停顿，不能成为默认排版
- 禁止连续 3 个及以上一句一段
- 20字以内极短正文段默认整篇不超过2个，且不能连续
- 禁止“算力。数据。场景。融资。”式名词逐行拆分
- 保留 01/02/03/04 宏观导航，不把编号结构误判成AI味
- 新增 `scripts/validate_readability.py`，直接扫描正文换行和段落长度
- 新增统一校验入口 `scripts/validate_article.py`
- 新增 B036–B039 四个可读性回归案例

v0.7 的 Reader Promise、五维POV筛选、Reader Contract、Thesis Prominence、Delivery Units、Concrete Task Rule、Clarity Pass 全部保留；v0.6 的 Tension Test、Material Graveyard、Uncertainty Ledger、Segmented Generation、Independent BlindReview 也继续保留。

## 一句话原则

> **外面有框架，里面用完整自然段；先给答案，再给证据。**

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
First Screen → 分段生成 → Clarity Pass → Paragraph Rhythm → Reorder/Delete → Anti-Template
  ↓
BlindReview
fresh session / different model
  ↓
VisualEditor
  ↓
PublisherQA
Truth + Thesis Prominence + Promise Delivery + Concrete Delivery + Paragraph Rhythm + BlindReview
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

最哲学、最深的观点不一定获胜。如果一个观点无法变成清晰的读者交付结构，它不适合作为知识型公众号主线。

## 3. Reader Contract

Architect 必须冻结：

```yaml
promise_type: which
promise: "高校老师能拿到哪些Agent委派建议"
core_answer: "把易验收、可撤回、责任仍在人手里的执行链整段交给Agent"
answer_shape: numbered_framework
expected_units: 4
```

标题问什么，正文就必须交付什么：
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

## 5. 01/02/03/04 是导航，不是正文节奏

对知识型、工具型、决策型、政策解读型文章，清晰编号是正向导航。

推荐：

```text
01｜文献研究：先把“搜、下、整、比”交出去

老师不需要自己在数据库、文件夹和表格之间反复切换。Agent 可以先完成检索、下载、去重、提取研究问题和方法，再把结果整理成 Literature Matrix；老师最后检查关键文献和研究缺口是否可靠。
```

不推荐：

```text
01｜文献研究

搜索。
下载。
去重。
提取。
建矩阵。
```

宏观结构可以规整，微观正文必须重新合并成自然叙述。

## 6. Paragraph Rhythm｜正文段落节奏

v0.7.1 新增规则：
- 正文默认2–4句一个自然段；
- 一个段落完成一个小意思，不要求每段一样长；
- 可以在段内使用短句，但不要把每个短句单独拆段；
- 单句段只能少量用于核心结论、转折、必要停顿；
- 禁止连续3个及以上单句正文段；
- 20字以内极短正文段默认整篇不超过2个，且不能连续；
- 小标题、列表项、图注不计入正文短段统计。

详细规则见 `docs/PARAGRAPH-RHYTHM.md`。

## 7. Concrete Task Rule

“文献研究”不是具体交付，要继续拆到：

`搜索 → 下载 → 去重 → 提取研究问题/数据/方法 → 建Literature Matrix → 标Gap`

“数据分析”也不够，要拆到：

`导入 → 清洗 → 跑代码 → 看报错 → 重跑 → 出图 → 导出`

读者必须能想象：这件事明天怎么发生在自己的电脑上。

## 8. Clarity Pass

Writer 在 BlindReview 前必须检查：
- thesis_in_first_screen
- promise_delivery_status
- numbered_framework_used
- missing_delivery_units
- evidence_overload_first_screen
- concrete_task_coverage
- paragraph_rhythm

Clarity/Paragraph Rhythm 不过，不能靠“文风自然”补救。

## 9. BlindReview 仍然独立

有效：
- fresh_session
- different_model

无效：
- same_context

BlindReview主要审AI感、语感、Voice；它不能替代 Reader Contract、Promise→Delivery 和 Paragraph Rhythm。

## 10. Evidence / Originality / Uncertainty 继续保留

事实层仍然严格：

`Source → Claim/Calc → Architecture → Writing → QA`

Originality：
- Flash：可conditional
- Standard：≥1A 或 ≥2B
- Deep：≥1A + ≥1B

真实犹豫只能绑定 Uxxx，不允许为了“人味”表演不确定。

## 11. 机器校验

统一推荐：

```bash
pip install -r requirements-dev.txt
python scripts/validate_article.py path/to/article-state.yaml
```

只查状态/证据链：

```bash
python scripts/validate_state.py path/to/article-state.yaml
```

只查正文碎片化：

```bash
python scripts/validate_readability.py path/to/article-state.yaml
```

Readability validator 会扫描：
- 单句正文段占比
- 连续单句段数量
- 20字以内极短段数量
- 极短段是否连续堆叠

它不处罚 01/02/03/04 小标题和正常列表项。

## 12. Benchmark

当前共39个案例：35个核心工作流案例 + 4个 Paragraph Rhythm 案例。

v0.7 核心新增：
- B031：核心观点埋后半篇
- B032：标题问“哪些”正文不分类
- B033：不能把1234误判成AI味
- B034：只有抽象大类、没有具体任务链
- B035：深但不可交付的POV不能自动胜出

v0.7.1 新增：
- B036：名词逐行拆分必须失败
- B037：连续一句一段必须失败
- B038：少量关键单句强调允许通过
- B039：01/02/03/04 + 自然正文段必须通过

## 最终质量标准

一篇稿子必须同时满足：

`Truth + Strong Thesis + Reader Promise + Clear Framework + Concrete Delivery + Natural Paragraphs + Natural Voice`

最终顺序是：

> **先让读者一眼看懂结构，再让他顺畅读完段落；小标题负责导航，正文负责把话说完整。**
