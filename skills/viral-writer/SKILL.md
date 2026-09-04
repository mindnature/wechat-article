---
name: viral-writer
description: 基于 Reader Contract、selected POV 与证据生成正文；先兑现标题承诺和核心结论，再用分段生成、重排与微观去模板保持自然表达。
version: "0.7"
reads: [topic, research, author, architecture, account, production, workflow]
writes: [writing, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../shared/voice-samples/manifest.yaml, ../../learning/proven-patterns.md, ../../learning/hypotheses.yaml, ../../docs/AUTHOR-VOICE.md, ../../docs/PRODUCTION-MODES.md, ../../docs/CLARITY-DELIVERY.md]
---

# ViralWriter｜公众号成稿

遵循 v0.7 ArticleState、Reader Contract 与证据链。

## 前置门
### Flash
research ready；至少有一个具体入口、一个明确判断和一个 Reader Contract。

### Standard / Deep
必须：architecture ready、AuthorLens完成、Originality达标、selected POV可追溯、Reader Contract完整。

## 核心原则
1. 先让读者抓住结论，再展示研究量。
2. 标题承诺必须显式兑现。
3. 知识/工具/决策文章允许并鼓励01/02/03/04宏观框架。
4. 去AI针对微观写法，不针对宏观清晰度。
5. 每个主要章节必须有具体任务、动作、案例、数字或决策，不写空壳大类。
6. Evidence在后台严格，正文里只保留改变判断所需的那部分。

## Step 1｜先写 First Screen，不先写背景
读取：
- `architecture.reader_contract.core_answer`
- `architecture.reader_contract.delivery_units`
- `architecture.thesis_prominence`

默认前300个中文字符必须：
- 出现核心结论/方向性答案；
- 告诉读者这篇明确会交付什么；
- 可再放一个具体事实或场景建立可信度。

如果标题是“哪些工作可以交给Agent”，第一屏就应说：
- 判断标准是什么；
- 接下来会给哪几类工作。

禁止第一屏主要由Benchmark名、模型参数、背景复述组成。

## Step 2｜按 Delivery Units 建 Segment Briefs
每个主要段的 brief 至少含：
- `delivery_unit_id`
- 本节一句答案
- 具体任务/案例/动作
- 必要 Claim/Calc/Case
- 可用 uncertainty node
- 本节禁止写的背景噪音

对于 `numbered_framework`，标题直接使用信息型小标题：

`01｜文献研究：先把“搜、下、整、比”交出去`

而不是：

`01｜文献研究`

## Step 3｜Concrete Task Rule
当标题承诺“哪些工作/哪些场景/怎么做”时，正文必须下钻到可想象的操作链。

例如：
- 文献研究 → 搜索/下载/去重/提取/矩阵/Gap
- 数据分析 → 导入/清洗/跑代码/看报错/重跑/出图
- 项目申报 → 读通知/提条件/建清单/核附件/汇总Excel/找缺项

如果一节只剩“教学、科研、管理”等大类，没有动作链，视为未交付。

## Step 4｜分段生成
仍保留 v0.6 的隔离机制：
- 优先 isolated_segments；
- 不支持时标 single_context_fallback；
- 不得一次连续顺写全文后假装分段。

记录 generation_trace。

## Step 5｜组装时先检查“读者能不能扫懂”
在 Anti-Template 前先做 Clarity Pass：

```yaml
writing:
  clarity_pass:
    status: pass | rework | not_run
    thesis_in_first_screen: true
    promise_delivery_status: pass | rework | not_run
    numbered_framework_used: true
    missing_delivery_units: []
    evidence_overload_first_screen: false
    concrete_task_coverage: pass | rework | not_run
    edits_made: []
```

必须检查：
- 前300字是否出现核心结论；
- 标题承诺是否已映射到正文；
- 读者扫小标题能否复述文章结构；
- 每个Delivery Unit是否有具体任务/案例；
- 是否先堆证据后给答案。

Standard/Deep `clarity_pass.status != pass` 不得进入 BlindReview。

## Step 6｜Reorder / Delete Pass
继续保留结构级删减，但目标改为：
- 让最强结论前移；
- 删除不服务 Promise 的段；
- 合并重复说明；
- 把支持性证据移动到对应结论之后。

至少执行一种真实结构动作；记录 `generation_trace.reorder_pass=true`。

## Step 7｜Anti-Template Pass：只审微观模板
允许：
- 01/02/03/04
- 清晰总框架
- 第一屏结论先行
- 小标题高度信息化

重点打击：
- 每节长度接近
- 每节都“总结→解释→总结”
- 每节都做一次“不是…而是…”
- 连续抽象过渡
- 每节结尾都升华
- 固定三建议/六步法

不要因为存在编号结构就判AI味。

## Step 8｜真实不确定性
任何“还不能确定/我会保留判断”必须绑定真实 Uxxx。证据明确时直接说清楚，不表演犹豫。

## Step 9｜标题
标题与Reader Contract绑定。标题问什么，正文就交付什么。

生成8–15个候选即可，硬事实需 title_safe。

## Step 10｜Blind Review Handoff
只有 Clarity Pass + Anti-Template Pass 都通过后，才生成 body-only blind packet。

BlindReview 主要审AI感、语感和Voice；不能替代 Promise→Delivery 与 Thesis Prominence。

## 输出
Human Summary：TOP3标题、第一屏、完整正文、Reader Contract交付情况、Clarity Pass、generation trace、Anti-Template edits、BlindReview packet。

State Patch：`writing.*`；完成后 `workflow.stage: writing, gate: ready`。

## 禁止
- 把“反模板”理解成“不要1234”
- 标题问A正文讲B
- 核心结论埋到后半篇
- 用Benchmark开场压住读者利益
- 用“文献研究/教学/科研管理”等大类代替具体工作链
- 一次连续顺写全文后假装分段
- 伪第一人称/伪犹豫
