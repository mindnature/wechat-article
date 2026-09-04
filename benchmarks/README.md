# Benchmarks｜回归测试

`cases.yaml` 用于验证机制是否真的变好，而不是只让Prompt更长。

## 当前版本
v0.7 共35个固定案例。

## 重点模块
- TopicHunter：B001–B013、B026/B027、B032
- ResearchPack：Evidence / Calculation / Uncertainty / Depth Material
- AuthorLens：B021–B030、B035
- ArticleArchitect：B031–B035
- ViralWriter：B022/B023/B024/B028/B031–B034
- BlindReview：B029/B030
- PublisherQA：Truth + Clarity + Promise Delivery + BlindReview + Visual

## 不可退化项

### Truth / Depth
1. Scope不能扩大
2. Evidence断链必须失败
3. 计算保留假设/公式
4. Standard/Deep必须通过Tension Test
5. “多关注/多学习”不能算decision_change
6. 无独家材料路径且无强判断，不得包装成深度稿
7. AuthorLens必须3个POV竞争并淘汰2个
8. Material Graveyard必须形成真实取舍
9. 假犹豫必须绑定Uxxx
10. same-context BlindReview无效

### Clarity / Delivery｜v0.7
11. Reader Promise必须具体
12. `which/how/list`至少预览3个交付单元
13. POV选择必须评价frameworkability和specificity
14. 最深POV不能自动胜出
15. Reader Contract必须有core_answer
16. 标题问“哪些/怎么做”默认使用编号框架
17. Delivery Unit必须有concrete_examples
18. 默认核心结论进入前300字
19. First Screen不能被Benchmark/参数压满
20. Promise→Delivery必须pass
21. 1234本身不能触发Anti-Template失败
22. 大类词不能代替具体任务链

## 机器校验
CI 当前验证：
- 合法 v0.7 Standard → PASS
- Evidence断链 → FAIL
- 单个POV → FAIL
- generic decision_change → FAIL
- generic Reader Promise → FAIL
- selected POV frameworkability过低 → FAIL
- Delivery Unit无具体例子 → FAIL
- `which`文章不用编号框架 → FAIL
- 核心结论未进入第一屏 → FAIL
- 第一屏Evidence overload → FAIL
- same-context BlindReview → FAIL
- 假Uxxx → FAIL

## 语义回归
机器无法完全判断：
- core_answer是否真的强
- 01/02/03/04的分类是否是最佳分类
- first_screen_excerpt是否真正有点击后的阅读牵引力
- BlindReview指出的AI句是否真的被修好

这些仍需真实选题压力测试和独立BlindReview。
