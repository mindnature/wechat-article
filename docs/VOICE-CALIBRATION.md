# Voice Calibration｜用真实样例校准作者声音

## 结论
形容词型 Voice Profile 只能做边界提醒，不能当作真正的风格校准。

模型对“自然、口语化、有判断力”的理解与作者本人并不一致。真正有效的 Voice Calibration 必须来自用户明确确认的正例/反例。

## 样例要求
每个账号达到 `calibrated` 至少需要：
- 3 个 positive samples
- 2 个 negative samples

样例优先是段落级，不要整篇不加标注地扔进去。

每个样例记录：
- exact excerpt
- function：opening / transition / judgment / explanation / closing / rhythm
- why：具体哪里像/不像

## 正例不是“让模型模仿句子”
只抽取可迁移特征：
- 开头从事实还是判断进入
- 句长如何变化
- 转折是否直接
- 一段承担几个动作
- 作者判断多锋利
- 是否经常省略解释
- 结尾是封口还是留白

禁止复刻原句、固定口头禅或人为制造同一种句式。

## 反例同样重要
negative sample 应优先来自：
- 事实正确但AI味重的旧稿
- 作者明确说“不像我”的段落
- 过于完整、平均、解释型的文字

反例必须指出原句，不只写“AI味重”。

## 样例来源规则
- 只有用户明确确认过“这段像/这段不像”才能进入 manifest。
- 历史文章、Library 文件、旧成稿如果没有明确标签，只能作为候选，不能自动升级为 Voice Gold Sample。
- 不允许模型从“看起来不错”自行判断用户一定认可。

## 运行优先级
写作时：
`user-confirmed exemplars > 本篇 AuthorLens 约束 > account voice profile adjectives`

盲审时：
可把正/反例匿名混排，但 Reviewer 不得知道哪段是新稿、哪段是历史样例。
