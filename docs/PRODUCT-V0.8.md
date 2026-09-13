# WeChat Article v0.8｜Product Foundation

v0.8 的目标不是继续增加写作规则，而是把现有 AI Skills 工作流升级为一个可以被真实用户操作的公众号文章生产 Web App。

## 产品定位

> 一支可操作、可回退、可审稿的 AI 编辑部。

用户输入一个选题或一组素材，系统依次完成研究、观点竞争、文章架构、正文写作和独立审稿，最终形成可发布的公众号文章。

第一版不追求“一键全自动”。关键决策保留 Human Gate。

## V0.8 MVP 范围

只打通五个阶段：

1. Research
   - TopicHunter
   - ResearchPack
2. Angle
   - AuthorLens
3. Architecture
   - ArticleArchitect
4. Writing
   - ViralWriter
5. Review
   - BlindReview
   - PublisherQA

VisualEditor、PublishingPlan、GrowthReviewer 继续保留在仓库中，但不作为第一版主链的上线阻塞项。

## Human Gate

以下节点默认要求用户确认：

- Research 完成后：确认素材是否足够、是否继续。
- AuthorLens 完成后：从多个 POV 中选择主线。
- ArticleArchitect 完成后：确认 Reader Contract、核心答案和文章结构。

Writing 与 Review 可以自动连续执行，但用户始终可以回退到任一 Gate 修改后重新生成。

## 产品页面

### 1. 首页 / 文章库

- 新建文章
- 最近文章
- 当前状态
- 更新时间

### 2. New Article

支持三类输入：

- 一个选题
- 粘贴素材
- 上传文件

第一版可以只实现选题文本输入，另外两类保留接口。

### 3. Research

展示：

- 核心事实
- 来源
- 数据
- 争议
- 不确定性
- 原创材料路径
- Reader Promise 判断

重要事实必须能回到 Source。

### 4. Angle

至少展示三个真正不同的 POV，并展示：

- novelty
- reader_value
- specificity
- frameworkability
- evidence_strength

用户选择 selected POV 后进入 Architecture。

### 5. Architecture

展示并允许编辑：

- promise_type
- promise
- core_answer
- answer_shape
- expected_units
- first_screen_plan
- 01/02/03/04 delivery units

### 6. Editor

正文编辑器至少支持：

- 查看当前正文
- 手动修改
- 重新生成当前 section
- 查看历史版本
- 执行 Clarity / Paragraph Rhythm 校验

### 7. Review

BlindReview 必须与 Writer 保持上下文隔离。

展示：

- 事实风险
- 标题兑现
- Thesis Prominence
- Reader Promise Delivery
- Paragraph Rhythm
- AI / template 感
- 修改建议

用户可选择“按审稿意见重写”。

## 状态模型

现有 `schemas/article-state.*` 是 v0.8 的状态基础，不另起一套完全不同的数据模型。

Web App 中建议逐步映射为：

```text
ArticleProject
├── metadata
├── topic
├── sources
├── claims
├── calculations
├── uncertainty
├── research
├── pov_candidates
├── selected_pov
├── reader_contract
├── outline
├── drafts
├── reviews
├── visual_assets
└── publishing_plan
```

## 架构原则

### Skills 是内容引擎，Web 是操作层

不得把现有 Skills 的方法论硬编码进页面组件。页面通过 Workflow Runtime 调用 Skill，并把结果写回 Article State。

### Source → Claim → Architecture → Writing → QA

事实链不得被 UI 简化掉。产品化之后仍需保留来源、Claim、Calculation、Uncertainty 等状态。

### BlindReview 隔离

BlindReview 不允许直接继承 Writer 的完整上下文。Workflow Runtime 必须支持为 review stage 创建 fresh context，并允许配置 different model。

### 可回退，不覆盖

正文和关键状态均需版本化。重新生成不得静默覆盖上一版本。

## 暂不进入 V0.8 MVP

- 微信公众号自动发布
- 多人协作
- Skill 市场
- 视频生成
- 完整图片生成工作台
- MCP 市场
- 桌面 Agent
- 多模型自由切换 UI
- 复杂计费体系

## 当前代码结构

```text
wechat-article/
├── apps/
│   └── web/
├── packages/
│   └── workflow/
├── skills/
├── schemas/
├── benchmarks/
├── scripts/
└── docs/
```

## v0.8 Definition of Done

满足以下条件才算 Product Foundation 完成：

1. 用户可以创建 Article Project。
2. Project 状态可以持久化。
3. 可以从 Web UI 启动 Research stage。
4. 可以在 Human Gate 选择 POV 并确认 Architecture。
5. Writer 可以基于冻结后的 Architecture 生成正文。
6. BlindReview 使用隔离上下文运行。
7. 正文存在版本历史。
8. 现有 article-state validator 和 readability validator 仍可运行。
9. benchmarks 不因产品化被删除或绕过。
