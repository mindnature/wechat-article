---
name: article-architect
description: 基于 selected POV、真实证据与材料墓地，选择最自然的叙事路径并建立证据映射；结构服务判断，不追求完整覆盖。
version: "0.6"
reads: [topic, research, author, account, production, workflow]
writes: [architecture, workflow]
resources: [../../docs/AUTHOR-VOICE.md, ../../docs/VOICE-CALIBRATION.md]
---

# ArticleArchitect｜文章架构与叙事选择

## 前置门
### Standard / Deep
- `workflow.stage: author`
- `workflow.gate: ready`
- selected_pov_id 有效
- Material Graveyard 达标
- 核心 Claim 无 unsupported/false

### Flash
可从 research 直接进入微架构。

## 核心原则
1. 只服务 selected POV，不重新打开已经被 AuthorLens 淘汰的角度。
2. 材料墓地里的内容默认禁止进入正文，除非出现新证据并退回 AuthorLens 重新选择。
3. 后台证据链严格，前台结构自由。
4. 一篇文章只要把一个问题说透，不负责“完整”。

## Step 1｜锁定主线
读取 selected POV、entry_point、decision_change、narrative_choice、material_graveyard。

如果大纲开始重新吸收被淘汰的“第二显然”角度，立即停止。

## Step 2｜必要模块
建议3–7个，但不是硬要求。每个模块必须说明为什么它对 selected POV 必不可少。

```yaml
- section_id: A01
  role: ""
  key_message: ""
  claim_ids: [C001]
  calc_ids: []
  case_ids: []
  uncertainty_ids: [U001]
  statement_types: [fact, opinion]
  author_function: observation | judgment | evidence | tension | example | implication | close
  visual_node: ""
```

## Step 3｜真实不确定性落位
只有 ResearchPack 的 Uxxx 节点可以进入 uncertainty_ids。

如果某个“开放问题”没有 Uxxx 支撑，就只能写成作者问题，不能伪装成证据不确定性。

## Step 4｜开头
从 entry_point 进入。不要自动补新闻背景；背景只在读者无法理解当前段落时补最少量。

## Step 5｜结构允许不均匀
可以一大段+数个短段，可以少标题，可以没有标准结论段。内容轻重决定节奏。

## Step 6｜结尾
优先回到 selected POV 对读者决定的影响。可以停在判断、代价、限制或真实未解问题，不强制建议清单。

## 输出
Human Summary：selected POV、主线、明确不写的材料、必要模块、证据/不确定性映射、开头/结尾路径、模板风险。

State Patch：`architecture.*`；通过后 `workflow.stage: architecture, gate: ready`。

## 禁止
- 重新引入已淘汰 POV
- 从墓地捞材料只为“完整”
- 强制五段式/六段式
- 假不确定性
- 每篇都反转/清单/升华
