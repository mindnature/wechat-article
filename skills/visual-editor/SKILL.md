---
name: visual-editor
description: 为公众号文章规划封面、真实图、AI生成图和信息图，并管理图源、真实性、版权与视觉节奏。
version: "0.3"
reads: [architecture, writing, research, account]
writes: [visual, status]
---

# VisualEditor｜公众号视觉编辑

## 目标
把完成结构或正文的文章转成可执行视觉编辑单。图片不是装饰，而是文章的一部分。

遵循 `../../schemas/article-state.yaml` 与 `../../docs/SKILL-CONTRACT.md`。

## 核心原则
- 真实图优先负责“证明”。
- 生成图优先负责“解释、概念化、情绪表达”。
- 数据优先做图表/信息卡，不用氛围图代替数据。
- 图片数量由阅读节奏与信息功能决定。
- 标注图源不等于取得版权许可。
- 任何需要真实性的内容不得用AI伪造。

## Step 1｜读取视觉节点
优先读取 `architecture.visual_nodes`，再根据最终正文检查：
- 开头钩子区
- 关键事实区
- 数据/机制区
- 案例区
- 反转/高潮区
- 结论/行动区

只在“证据、解释、故事、情绪、节奏”至少承担一项功能时配图。

## Step 2｜分配功能
每张图主功能只能选一种：
`evidence | explain | story | emotion | rhythm`。

没有明确功能则删除。

## Step 3｜真实图 vs 生成图
判断顺序：
- 证明事件、政策、人物、产品、页面、原始数据 → 真实图
- 展示真实UI/论文/报告 → 真实截图
- 解释机制/流程/关系 → 生成图或自制信息图
- 表达不可直接拍摄的情绪/隐喻 → 生成图
- 已有真实图足够清晰 → 不为统一画风强行重生成

## Step 4｜封面
封面表达：`主题识别 + 最强冲突/数字/人物/对象`。

输出：
- 核心视觉
- 主元素
- 短文案（如需要，尽量4–10字）
- 真实/生成/混合方案
- 构图与留白
- 与标题是否重复

## Step 5｜真实图片资产单
每张真实图记录：

```yaml
- asset_id: V001
  function: evidence
  target: ""
  search_keywords: []
  preferred_source: ""
  source_url: ""
  source_label: ""
  rights_status: clear | likely_quotable | needs_confirmation | avoid
  privacy_risk: low | medium | high
  crop_note: ""
```

优先来源：官方/原始发布方 > 企业媒体包 > 权威媒体 > 明确许可图库/公共领域 > 其他可核验来源。

无来源搬运图、明显盗图、水印图不作为首选。

## Step 6｜生成图资产单
每张生成图记录：
- 内容主体
- 场景
- 信息功能
- 构图
- 风格
- 画幅
- 文字/标题留白
- 禁止项

禁止项至少检查：
- 错误文字
- 错误Logo
- 虚构数据
- 伪造政策页面
- 伪装真实新闻现场

## Step 7｜图源与权利
图注示例：
- `图源：国家自然科学基金委员会官网`
- `图源：Kickstarter 项目页面`
- `图源：新华社`
- `图源：XXX官网，作者整理`

许可状态不清时写入 `visual.rights_risks`，不能因为写了“图源”就当作无风险。

## Step 8｜执行边界
本 Skill 负责“视觉规划与资产规格”。

如果运行环境拥有图片搜索/生成/下载能力，可以按资产单执行；没有这些工具时必须明确标记 `planned_not_executed`，不能声称已经获得最终图片。

## 输出
### Human Summary
1. 视觉策略摘要
2. 封面方案
3. 文中插图表
4. 真实图搜索清单
5. AI生成图清单
6. 权利/隐私风险
7. 发布前视觉检查

### State Patch
- `visual.cover`
- `visual.inline_images`
- `visual.rights_risks`
- `status: visually_planned`

## 五号差异化
- 思然日新：政策、论文、项目指南、框架图优先
- 思然知己：产品页、模型能力、轻科技解释图优先
- 思然天工：界面截图、步骤图、前后对比、工作流图优先
- 思然经世：产品、价格、收入、众筹/商业数据与模式图优先
- 思然修远：真实社会事件 + 叙事情绪/生活场景图优先

## 禁止
- AI生成“像真实新闻现场”的伪证据图
- 为凑数量插无关图片
- 把图源标注当版权许可
- 生成图虚构可被误认成事实的数据/文件/言论
