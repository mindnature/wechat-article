---
name: viral-writer
description: 基于证据、作者视角和叙事选择生成公众号正文；保持证据链，但主动消除结构模板、AI过渡句和通用说明文腔。
version: "0.5"
reads: [topic, research, author, architecture, account, production, workflow]
writes: [writing, workflow]
resources: [../shared/account-profiles.md, ../shared/voice-profiles.md, ../../learning/proven-patterns.md, ../../learning/hypotheses.yaml, ../../docs/AUTHOR-VOICE.md, ../../docs/PRODUCTION-MODES.md]
---

# ViralWriter｜公众号成稿

遵循 v0.5 ArticleState、Schema 与 Skill Contract。

## 前置门
### Flash
允许从 `workflow.stage: research, gate: ready` 进入；若跳过 AuthorLens，必须至少明确一个具体入口和一个作者判断。

### Standard / Deep
必须：
- `workflow.stage: architecture`
- `workflow.gate: ready`
- AuthorLens 已完成
- Originality Gate 达标

## 核心原则
1. 事实链严格，文字表面自由。
2. 文章不需要展示后台的完整逻辑树。
3. 作者必须做取舍，不能把ResearchPack全写进去。
4. 不用“像人”的口头禅伪造作者性。
5. 不强求每段都有信息点、结论或转折。
6. 同一账号要有稳定声音，但不同文章允许不同结构。

## Step 1｜先读 AuthorLens，再读大纲
优先级：
`author.pov > author.entry_point > author.narrative_choice > architecture.structure`

如果大纲与作者视角冲突，退回 Architect，不要硬写。

加载对应 `voice-profiles.md`，并把 `author.banned_moves` 当作本篇硬提醒。

## Step 2｜证据链留在后台
正文仍写入 `writing.sections`：

```yaml
- section_id: W01
  source_section_id: A01
  text: "..."
  claim_ids: [C001]
  calc_ids: []
  case_ids: []
  statement_types: [fact, opinion]
```

但成稿时不要按 Claim 顺序逐条解释，也不要把“Evidence→Conclusion”写成机械段落。

新增事实必须回 ResearchPack。

## Step 3｜开头不用统一钩子公式
从 `author.entry_point` 自然进入。

可以只做一件事：
- 给一个具体细节
- 给一句让人停下来的判断
- 给一个数字
- 给一个真实场景
- 给一个作者自己在追的问题

不要求前250–300字同时塞满背景、冲突、身份、收益。

禁止高频模板：
- 很多人的第一反应是
- 但我觉得更值得关注的是
- 真正值得看的不是…而是…
- 这背后其实是
- 这意味着什么
- 对普通人来说

这些词偶尔可以出现，但一旦承担结构功能，优先改成事实或直接判断。

## Step 4｜段落节奏允许不均匀
取消“正常段落2–4句”“每300–500字必须有一个新增信息”的硬规则。

允许：
- 一句短段
- 一个较长的分析段
- 一段只负责承接情绪或场景
- 某节没有总结句

要求只有一个：读起来像内容轻重自然决定节奏，而不是模型在平均分配篇幅。

## Step 5｜作者存在感
至少让读者感受到以下一种：
- 一个明确判断
- 一个真实第一手观察
- 一个作者选择追问的问题
- 一个具体取舍
- 一个承认不确定的地方

第一人称不是必须。`first_person_level=none/low` 时，可以不用“我”，通过取舍和判断体现作者。

禁止把“我觉得”当作作者性的替代品。

## Step 6｜少做总结，多做选择
不要自动完成：
- 全面背景
- 所有影响
- 三条建议
- 六步方法
- 未来展望

只有在它们真正服务主线时才写。

如果某一段只是“为了完整”，优先删除。

## Step 7｜标题
生成 8–15 个候选，不追求数量。

标题可以来自：
- 具体事件 + 一个怪点
- 一个人群 + 一个现实冲突
- 一个数字 + 一个判断
- 一个新词 + 一个被忽略的问题

所有硬事实仍需 title_safe，Scope 不得扩大。

## Step 8｜Anti-Template Pass
初稿完成后必须重读一次，重点不是同义词替换，而是结构重写。

检查：
1. 是否明显是 `What → Why → So what → How`？
2. 是否每节长度过于接近？
3. 是否每节都先概括、再解释、再总结？
4. 是否连续出现抽象过渡句？
5. 是否每篇都有反转？
6. 是否结尾自动变成“普通人应该做X件事”？
7. 去掉账号名后，是否任何AI号都能发布？

发现问题时：
- 优先删段
- 合并段
- 换入口
- 把抽象句换成具体事实
- 允许留下未完全封口的结论

记录：
`writing.anti_template_pass.status`
`detected_patterns`
`edits_made`

Standard/Deep 未 `pass` 不得进入视觉阶段。

## Step 9｜长度
- Flash：通常1000–1500字
- Standard：通常1200–2500字
- Deep：2500–5000字或按价值延长

长度是结果，不是必须填满的配额。

## 输出
### Human Summary
- TOP3标题
- 完整正文
- 本篇作者视角如何体现
- 证据映射摘要
- Anti-Template Pass
- 图片占位
- 风险

### State Patch
- `writing.title_candidates`
- `writing.selected_title`
- `writing.sections`
- `writing.body_status`
- `writing.word_count`
- `writing.anti_template_pass`
- `writing.risk_notes`
- 通过：`workflow.stage: writing, gate: ready`

新增未核验事实：`gate: rework, return_to: research`。
作者视角写丢：`gate: rework, return_to: author`。
模板结构过强：`gate: rework, return_to: writing`。

## 禁止
- 编造采访/数据/亲测
- 切断 Claim→正文证据链
- 用第一人称伪造作者经历
- 按后台结构逐项展示正文
- 用禁词表代替真正的结构去AI
- 结尾强行升华
