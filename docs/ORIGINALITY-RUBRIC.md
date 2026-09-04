# Originality Rubric｜原创资产分级

Originality Gate 的目标不是证明文章“从未有人写过”，而是确保文章提供普通新闻汇总之外的新增价值。

## A级原创资产｜强原创
可单独支撑 Standard/Deep 文章通过 Originality Gate：
- 作者亲测并保留过程/结果
- 自主计算且假设、公式、结果可复现
- 采访/小调查
- 一手职业经验或现场观察
- 自建数据集/原始数据整理
- 独立实验/复现

每项必须可说明“作者具体做了什么”，禁止伪造。

## B级原创资产｜中原创
至少 2 个可支撑 Standard/Deep：
- 独立产品/方案对比
- 跨多个高质量来源的数据整理
- 新的决策框架或分析框架
- 对公开材料进行重新编码、分类、测算或结构化
- 将跨领域材料形成有证据的新综合

B级不能只是换标题或换表达。

## C级原创资产｜弱原创
不能单独让 Standard/Deep 通过：
- 普通公开页面截图
- 单纯摘要
- 常规多源汇总
- 常识性解释
- 装饰性信息图

## 通过规则
- Flash：可 `conditional`，允许 0 个A/B，但必须明确资讯属性，不能包装成深度原创。
- Standard：至少 `1×A` 或 `2×B`。
- Deep：至少 `1×A + 1×B`；若以调查/亲测为核心，A资产必须是正文主证据之一。

## 记录格式

```yaml
research:
  originality_gate:
    status: pass | conditional | fail
    assets:
      - asset_id: O001
        level: A
        type: calculation
        description: "重新计算30年与40年房贷现金流与总利息"
        evidence_refs: [K001]
    score: 3
    commodity_content_risk: low
    missing_original_material: []
```

建议计分：A=3，B=2，C=0.5。分数只用于门槛判断，不代表爆款概率。
