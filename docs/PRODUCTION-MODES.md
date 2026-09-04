# Production Modes｜三档生产模式 v0.6

事实、Scope、版权、隐私门槛在所有模式中相同。v0.6 额外区分“资讯速度”和“主旨深度/盲审强度”。

## Flash｜抢热点
适用：当天突发、窗口短、主要价值是快速解释。

最小链路：
`TopicHunter → ResearchPack Lite → ViralWriter → VisualEditor → PublisherQA → PublishingPlan`

Flash 可跳过完整 AuthorLens / ArticleArchitect / BlindReview，但必须明确一个具体入口和一个判断；不得降低事实门。

## Standard｜标准文章
适用：日常主力。

链路：
`TopicHunter → ResearchPack → AuthorLens → ArticleArchitect → ViralWriter → BlindReview → VisualEditor → PublisherQA → PublishingPlan`

要求：
- Tension Test=pass；
- exclusive material path 或 strong judgment candidate 至少一个成立；
- 完整 Evidence / Uncertainty Ledger；
- Originality ≥1A 或 ≥2B；
- AuthorLens 生成3个POV并淘汰2个；
- 材料墓地 discarded_units ≥ retained_units；
- Writer 分段生成并做独立 reorder/delete pass；
- BlindReview 必须 fresh_session 或 different_model；
- BlindReview 未通过不得进入 VisualEditor。

## Deep｜深度旗舰
适用：亲测、调查、商业拆解、长期品牌内容。

链路同 Standard。

额外要求：
- Originality ≥1A+1B；
- 更强的一手/独家材料；
- selected POV 必须被A级材料改变或约束；
- 盲审建议优先 different_model；
- 不追求日更。

## 模式选择
优先根据：
1. 热点剩余窗口
2. 是否有真正张力
3. 是否能得到独家材料或形成强判断
4. 证据复杂度
5. 账号价值
6. 文章寿命

如果只有“热点+公开资料+第二显然观点”，应降为 Flash/backup，而不是包装成 Standard 深度稿。
