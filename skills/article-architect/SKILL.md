---
name: article-architect
description: 把 selected POV 转成读者一眼能抓住的交付结构；冻结 Reader Contract、核心结论、1234宏观框架与 Promise→Delivery 映射。
version: "0.7"
reads: [topic, research, author, account, production, workflow]
writes: [architecture, workflow]
resources: [../../docs/AUTHOR-VOICE.md, ../../docs/VOICE-CALIBRATION.md, ../../docs/CLARITY-DELIVERY.md]
---

# ArticleArchitect｜文章架构与读者交付

## 前置门
### Standard / Deep
- `workflow.stage: author`
- `workflow.gate: ready`
- selected POV 有效
- Material Graveyard 达标
- 核心 Claim 无 unsupported/false

### Flash
可从 research 直接进入微架构，但仍要有 Reader Contract。

## 核心原则
1. selected POV 决定文章说什么，Reader Contract 决定读者怎么拿走。
2. 宏观结构必须清楚；Anti-Template 只打击微观机械表达，不打击01/02/03/04。
3. 标题承诺必须在正文里显式交付，不能让读者自己总结答案。
4. 结论优先于支持性证据；benchmark、参数、背景默认放在核心答案之后。
5. 一篇文章可以只说一个主判断，但必须把这个判断组织成可读、可扫、可记的框架。

## Step 1｜冻结 Reader Contract
读取 selected POV、topic.reader_value、标题方向与 decision_change，写：

```yaml
architecture:
  reader_contract:
    promise_type: which | how | why | compare | decide | explain | list | other
    promise: "读者点进来要得到什么"
    core_answer: "全文最重要的一句答案"
    answer_shape: numbered_framework | decision_tree | comparison | checklist | narrative | hybrid
    expected_units: 4
    delivery_units: []
```

### 标题→交付硬规则
- 标题问“哪些/哪几类” → 正文明确分类并逐类回答。
- 标题问“怎么/如何” → 正文明确步骤/动作。
- 标题问“该不该/值不值得” → 正文给判断标准、代价和结论。
- 标题承诺数字 → 正文必须同数量交付。

## Step 2｜Core Answer 必须能单独成立
`core_answer` 不是主题句，而是可以直接回答标题的结论。

差：`GPT-6让Agent更强。`

好：`高校老师接下来不该按“简单/复杂”分配任务，而应该把“能快速验收、做错可撤回、责任仍在人”的执行型工作整段交给Agent。`

如果 core_answer 太抽象、不能改变读者决定，退回 AuthorLens。

## Step 3｜选择宏观结构
### 默认优先 numbered_framework
以下类型默认使用 01/02/03/04：
- 知识解释
- 工具/教程
- 政策/科研机会
- 商业拆解
- 决策指南
- 标题含“哪些/几类/怎么/如何/清单/步骤”

叙事型、人物型、调查型可选 narrative/hybrid，但要记录为什么不用编号框架。

注意：编号只负责导航，不要求每节同长度或同写法。

## Step 4｜建立 Delivery Units
每个主要章节不是“一个解释模块”，而是一个读者交付单元：

```yaml
- unit_id: D01
  label: "文献研究：把搜、下、整、比交出去"
  answer: "一句清晰结论"
  concrete_examples:
    - "搜索→下载→去重→提取研究问题/数据/方法→建Literature Matrix"
  claim_ids: [C001]
  calc_ids: []
  uncertainty_ids: []
```

要求：
- Standard 通常 3–5 个主单元；
- 每个单元至少一个具体任务/案例/动作/数字；
- “文献研究”“教学工作”“科研管理”这种大类本身不算 concrete example，必须继续下钻到操作链。

## Step 5｜Thesis Prominence 设计
默认：前300个中文字符内必须出现 core_answer 的等价表达，并告诉读者正文将交付什么框架。

记录：

```yaml
architecture:
  thesis_prominence:
    required_in_first_screen: true
    max_chars: 300
    delayed_reason: ""
```

只有强叙事/调查稿可以延迟结论，且必须填写 delayed_reason。

## Step 6｜First-Screen Plan
第一屏默认至少完成：
1. 方向性答案/核心结论；
2. 本文明确交付什么（例如4类工作+3个边界）；
3. 可选：一个具体事实/场景建立可信度。

禁止把第一屏主要交给 Benchmark 缩写、模型参数或新闻背景。

## Step 7｜Evidence Salience
证据服务结论：
- 先给读者结论，再解释为什么；
- 技术指标出现后立即回答“它为什么改变本文判断”；
- 不连续堆多个 benchmark 名称；
- 不为了显示研究量把背景写在核心答案前面。

## Step 8｜结构设计
推荐结构：
- 开头：结论 + 交付预告
- 01/02/03/04：逐个 Delivery Unit
- 边界/反例：哪些不能交、为什么
- 结尾：回到核心判断标准

这不是固定篇章模板，而是知识/决策文章的默认可读骨架。若内容需要可变形。

每节后台仍记录证据：

```yaml
- section_id: A01
  delivery_unit_id: D01
  role: ""
  key_message: ""
  claim_ids: [C001]
  calc_ids: []
  case_ids: []
  uncertainty_ids: []
  statement_types: [fact, opinion]
  visual_node: ""
```

## Step 9｜Promise → Delivery 自检
进入 Writer 前必须检查：
- 标题承诺是否全部映射到 delivery_units；
- 每个 delivery unit 是否有明确答案；
- 是否存在“标题问A，正文主要讲B”；
- 是否把最强结论埋到后半段。

失败：`workflow.gate: rework, return_to: architecture/author`。

## 输出
Human Summary：Reader Contract、core answer、01/02/03/04框架、Delivery Units、第一屏计划、证据映射、明确不写的材料。

State Patch：`architecture.*`；通过后 `workflow.stage: architecture, gate: ready`。

## 禁止
- 为了反模板而牺牲导航
- 把“结构清晰”误判成AI味
- 标题问“哪些”却不给明确分类
- 用大类词代替具体任务
- 先堆Benchmark再给结论
- 重新引入已淘汰 POV
- 从墓地捞材料只为“完整”
