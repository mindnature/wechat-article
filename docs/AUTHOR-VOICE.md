# Author Voice Architecture｜v0.7

v0.7 的核心判断：

> 文风AI不是靠更多形容词规则解决，但“去AI”也不能以牺牲结构清晰为代价。

最终目标是：

> **宏观结构清楚，微观表达自然；外面有框架，里面有人味。**

## 1. 主旨来自竞争，但不是“越深越好”
AuthorLens 必须生成3个POV，并主动指出每个为什么可能仍然平庸。

v0.7 同时评价：novelty / reader_value / specificity / frameworkability / evidence_strength。

最深但最难交付的角度不自动获胜。

## 2. 作者性来自真实取舍
Material Graveyard 让“哪些资料不写”可审计。作者围绕 selected POV 放弃大量非核心信息，而不是展示全部研究量。

## 3. 真犹豫必须有材料来源
允许作者不确定，但只能绑定 ResearchPack 的 Uxxx：冲突信源、partial evidence、missing data、计算假设、Scope边界、预测。

没有真实不确定性，就不要表演犹豫。

## 4. 结构清晰不是AI味
对于知识型、工具型、政策型、决策型公众号文章：

- 01/02/03/04 可以保留；
- 信息型小标题可以很明确；
- 核心结论可以第一屏直接给；
- 标题承诺“哪些”，正文就应该清楚分类。

这些是读者导航，不是AI模板。

真正需要打掉的是微观重复：
- 每节长度接近；
- 每节相同句法；
- 每节都“概括→解释→总结”；
- 每节都制造同一种反转；
- 每节最后都升华。

## 5. Voice Profile 只是边界
“自然、口语、有判断”不够可操作。

真正Voice来自用户确认的正/反例，详见 `VOICE-CALIBRATION.md` 与 `voice-samples/manifest.yaml`。

## 6. 分段生成优先于连续全文生成
连续生成容易形成统一节奏并一路延续。优先每个segment独立brief、独立调用，再做重排/删减。

无法隔离上下文时必须记录 fallback。

## 7. Clarity 先于 BlindReview
BlindReview 不能替代可读性工程。

在交给独立评审前，Writer 必须已经完成：
- Thesis Prominence
- Promise→Delivery
- numbered macro framework（适用时）
- Concrete Task Coverage
- Evidence Salience

盲审负责发现AI语感、通用模型句和Voice偏差，不负责替作者找标题答案。

## 8. 同上下文自评不算文风验证
Writer/QA共享同一上下文时共享盲点。

Standard/Deep 必须由 fresh session 或 different model 做 BlindReview，Reviewer 不得看到 pipeline 规则。

## 9. 最终评价

`Truth + Strong Thesis + Reader Promise + Clear Framework + Concrete Delivery + Selectivity + Real Uncertainty + Independent Voice Review`

“像人”不是唯一目标；真正好的公众号稿首先让读者愿意继续读、快速看懂、明确拿走东西，然后才谈作者声音。
