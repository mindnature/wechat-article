---
name: article-architect
description: 把已验证研究素材组织成文章结构、故事线、情绪曲线和视觉节点，并建立 Claim/Calc 到正文的证据映射。
version: "0.4"
reads: [topic, research, account, production, workflow]
writes: [architecture, workflow]
---

# ArticleArchitect｜文章架构与证据映射

遵循 v0.4 ArticleState、Schema 与 Skill Contract。

## 前置门
- `workflow.stage: research`
- `workflow.gate: ready`
- Standard/Deep 必须通过对应 Originality Gate
- 核心 Claim 无 unsupported/false

Flash 可跳过本 Skill；若运行，只做 3–5 模块微架构。

## Step 1｜核心命题
一句话说明读者看完最该记住什么。要求具体、可证、不超过 Scope。

## Step 2｜读者任务
明确为什么现在看、已有问题、读完获得什么判断/行动。

## Step 3｜文章原型
热点解释、调查实验、产品体验、商业案例、决策算账、政策机会、人物故事、观点反转，可组合。

## Step 4｜证据绑定结构
每个模块必须记录：
```yaml
- section_id: A01
  purpose: hook | explain | evidence | contrast | decision | close
  key_message: ""
  claim_ids: [C001]
  calc_ids: [K001]
  case_ids: []
  statement_types: [fact, calculation]
  emotion: ""
  visual_node: ""
  transition: ""
```

事实性段落无 Claim/Calc/Case 时退回 ResearchPack；观点段必须标 opinion。

## Step 5｜原创资产落位
Standard/Deep 必须指出 A/B级原创资产出现在哪个 section。
Deep 的 A级资产必须进入核心论证，不能只放结尾。

## Step 6｜情绪曲线
好奇 → 意外 → 理解 → 反转 → 获得感 → 决策 → 余韵。情绪来自信息推进，不靠夸张词。

## Step 7｜开头
前250–300字快速完成事实/场景、冲突、读者关系、阅读承诺；硬事实必须绑定 Claim ID。

## Step 8｜视觉节点
标记 evidence/explain/story/rhythm。需要真实性的节点不得用AI伪造。

## Step 9｜模式控制
- Flash：3–5模块、减少背景层级
- Standard：4–7模块、完整证据与情绪线
- Deep：允许7+模块，但每一节必须有新增价值

## 输出
Human Summary：核心命题、读者任务、文章原型、证据绑定大纲、原创资产位置、开头、情绪线、视觉节点、结尾、风险。

State Patch：`architecture.*`，并设置 `workflow.stage: architecture, gate: ready`。

若发现证据断裂：`gate: rework`、`return_to: research`。

## 禁止
- 本阶段直接扩写全文
- 虚构人物/场景
- 用未验证事实制造钩子
- 情绪线脱离证据线
- A/B原创资产只“存在”却不进入正文结构
