# Benchmarks｜回归测试

`cases.yaml` 用于验证机制是否真的变好，而不是只让Prompt更长。

## 当前版本
v0.6 共30个固定案例。

## 重点模块
- TopicHunter：B001–B013、B026、B027
- ResearchPack：Evidence/Calculation/Uncertainty/Depth Material
- AuthorLens：B021–B030
- ViralWriter：B022/B023/B024/B028/B029
- BlindReview：B029/B030
- PublisherQA：事实门 + Blind Review结果

## v0.6新增不可退化项
1. Standard/Deep 必须通过 Tension Test
2. “多关注/多学习”不能算 decision_change
3. 无独家材料路径且无强判断，不得包装成Standard深度稿
4. AuthorLens 必须生成3个POV并淘汰2个
5. 每个POV必须写 banality_self_critique
6. Material Graveyard 必须形成真实取舍压力
7. 假犹豫必须有真实 Uxxx
8. Writer 必须 segment + reorder/delete
9. same-context BlindReview 无效
10. 未经用户确认的历史稿不能自动成为Voice Gold Sample

## 机器校验
CI 会验证：
- 合法 v0.6 Standard PASS
- Evidence断链 FAIL
- 单个POV直接进入写作 FAIL
- generic decision_change FAIL
- same-context BlindReview FAIL
- 引用不存在的Uxxx FAIL

## 语义回归
JSON Schema/validator 不能独立判断“第三层/第四层观点是否真的更好”。B026–B030 仍需要真实选题压力测试和外部BlindReview。
