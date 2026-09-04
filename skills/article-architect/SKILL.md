---
name: article-architect
description: 把已验证研究素材组织成微信公众号文章结构、故事线、情绪曲线和视觉节点，并显式绑定证据主张。
version: "0.3"
reads: [topic, research, account]
writes: [architecture, status]
---

# ArticleArchitect｜文章架构与情绪设计

## 目标
在写正文之前，把“素材”变成“可读的叙事”。解决资料堆砌、逻辑平铺、情绪平直、结论松散，同时确保每个关键段落知道自己依赖哪条证据。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

## 前置门
只有以下条件满足才进入：
- `status` 已到 `researched`
- 核心 Evidence Ledger 无 unsupported/false 主张
- Originality Gate 为 pass 或有明确 conditional 理由

否则退回 ResearchPack。

## Step 1｜一句核心命题
回答：读者看完全文后最应该记住什么？

要求：
- 具体
- 可证
- 不超过现有证据范围
- 不写口号

## Step 2｜读者任务
明确：
- 为什么现在要看
- 已有误解/焦虑/问题是什么
- 看完获得什么判断、知识或行动

## Step 3｜文章原型
可选或组合：
- 热点解释型
- 调查实验型
- 产品体验型
- 商业案例拆解型
- 决策算账型
- 政策机会型
- 人物/故事型
- 观点反转型

## Step 4｜证据绑定结构
构建 4–7 个模块，每个模块记录：

```yaml
- section_id: A01
  purpose: hook | explain | evidence | contrast | decision | close
  key_message: ""
  claim_ids: [C001, C002]
  calc_ids: [K001]
  case_ids: []
  emotion: ""
  visual_node: ""
  transition: ""
```

没有 Claim/Calc/Case 支撑的事实性段落必须回 ResearchPack 补证据；纯观点段落标明 opinion。

## Step 5｜情绪曲线
为各模块标注主要情绪，例如：
`好奇 → 意外 → 理解 → 反转 → 获得感 → 决策 → 余韵`

情绪必须来自信息推进，不靠夸张措辞硬造。

## Step 6｜开头设计
前 250–300 字尽快完成：
- 具体事实/场景
- 反差或利益点
- 为什么与目标读者有关
- 阅读承诺

任何用于开头的硬事实都必须有 Claim ID。

## Step 7｜视觉节点
在大纲阶段标注：
- evidence：官方、产品、现场、政策、数据截图
- explain：流程、机制、关系、对比卡
- story：人物、产品、场景
- rhythm：长文视觉呼吸

说明为什么这里需要图，且不得用AI图替代需要真实性的证据图。

## Step 8｜结尾设计
优先：
- 决策框架
- 回扣开头
- 2–4 个行动建议
- 有价值的开放问题

禁止空泛“未来可期/拭目以待”。

## 输出
### Human Summary
1. 一句话核心命题
2. 目标读者与阅读承诺
3. 文章原型
4. 证据绑定大纲
5. 开头方案 2–3 个
6. 情绪曲线
7. 视觉节点
8. 结尾方案
9. 写作风险

### State Patch
仅写：
- `architecture.*`
- `status: architected`

## 禁止
- 在本阶段直接扩写完整正文
- 为戏剧性虚构人物/场景
- 用未经验证主张制造开头反差
- 让情绪曲线脱离证据线
- 用宏大判断替代机制与数据
