---
name: article-architect
description: 基于已验证证据与 AuthorLens 的作者视角，选择最自然的叙事路径并建立证据映射；结构服务观点，不输出统一模板。
version: "0.5"
reads: [topic, research, author, account, production, workflow]
writes: [architecture, workflow]
resources: [../../docs/AUTHOR-VOICE.md]
---

# ArticleArchitect｜文章架构与叙事选择

遵循 v0.5 ArticleState、Schema 与 Skill Contract。

## 前置门
### Standard / Deep
- `workflow.stage: author`
- `workflow.gate: ready`
- AuthorLens Humanity Test 不得为高模板风险
- 核心 Claim 无 unsupported/false

### Flash
可从 research 直接进入微架构，也可运行简化 AuthorLens。

## 核心原则
1. 结构服务作者 POV，不反过来。
2. 后台可以高度结构化，前台不能让读者看见“流程模板”。
3. 不追求完整覆盖 ResearchPack；必须尊重 `author.material_to_ignore`。
4. 不强制反转、方法论、行动清单或情绪曲线。
5. 一篇文章可以只回答一个问题，只要证据边界完整。

## Step 1｜锁定主线
读取：
- `author.pov`
- `author.entry_point`
- `author.narrative_choice`
- `author.material_to_ignore`

把全文压成一个主问题或主判断。

如果出现两个同等重要主线，优先删一个，或拆成两篇。

## Step 2｜选择叙事而非套模板
沿 AuthorLens 已选的主结构组织：
- single-thread
- scene-led
- evidence-led
- argument-led
- case-led
- diary-led
- compare-led

禁止自动切换成：
`新闻背景 → 深层原因 → 影响 → 普通人建议`。

## Step 3｜结构只保留必要模块
建议 3–7 个模块，但不是硬要求。

每个模块记录：
```yaml
- section_id: A01
  role: ""
  key_message: ""
  claim_ids: [C001]
  calc_ids: []
  case_ids: []
  statement_types: [fact, opinion]
  author_function: observation | judgment | evidence | tension | example | implication | close
  visual_node: ""
```

不要求每节长度相近，不要求每节都有结论句。

## Step 4｜证据绑定但不让ID进入成稿
事实、数字继续绑定 Claim/Calc/Case。

但这些ID只服务审计，不能让 Writer 按“每条证据一段”的方式机械展开。

允许一个段落同时吸收多条证据，也允许某些背景证据完全不写。

## Step 5｜开头服从 Entry Point
优先从 `author.entry_point` 开始。

开头只需要做到：让目标读者愿意继续读。

不再强制同时完成“事实+冲突+读者关系+阅读收益”。

可以：
- 直接落一个细节
- 直接放一个数字
- 直接提出作者困惑
- 直接进入一个场景
- 直接给判断

前提是事实可追溯，且不故作悬念。

## Step 6｜允许不均匀节奏
可以有：
- 一个很长的核心段 + 两个短段
- 少量小标题甚至无数字编号
- 中间停顿
- 未完全封口的判断

不为了“像人”故意杂乱；不均匀必须来自内容轻重不同。

## Step 7｜情绪只做可选注释
`architecture.optional_emotion_notes` 只在故事/人物/实验类文章有帮助时填写。

禁止再使用固定：
`好奇 → 意外 → 理解 → 反转 → 获得感 → 决策 → 余韵`。

## Step 8｜结尾不承担强制任务
根据主线自然选择：
- 回到开头细节
- 停在一个判断
- 留一个问题
- 给1–2个行动建议
- 给一个现实限制

不要求升华，不要求清单，不要求“未来展望”。

## 输出
### Human Summary
- 主问题/主判断
- Narrative Choice
- 哪些材料明确不写
- 3–7个必要模块（可少于/多于）
- 证据映射
- 开头路径
- 结尾路径
- 模板风险

### State Patch
写入 `architecture.*`：
- core_thesis
- article_type
- reader_task
- narrative_choice
- structure
- optional_emotion_notes
- visual_nodes

通过后：`workflow.stage: architecture, gate: ready`。

## 禁止
- 把ResearchPack完整搬进正文结构
- 强制五段式/六段式完整结构
- 每篇都制造反转
- 每篇都以“普通人怎么办”结束
- 为了结构漂亮牺牲作者真实判断
