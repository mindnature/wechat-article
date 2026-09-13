const stages = [
  {
    step: "01",
    name: "研究",
    skill: "TopicHunter + ResearchPack",
    description: "确认选题价值，收集来源、事实、数据、争议与风险。",
  },
  {
    step: "02",
    name: "观点",
    skill: "AuthorLens",
    description: "生成多个真正不同的 POV，并按读者价值与证据强度筛选。",
  },
  {
    step: "03",
    name: "结构",
    skill: "ArticleArchitect",
    description: "冻结 Reader Contract、核心答案和正文交付结构。",
  },
  {
    step: "04",
    name: "写作",
    skill: "ViralWriter",
    description: "分段生成正文，执行 Clarity Pass 与 Paragraph Rhythm。",
  },
  {
    step: "05",
    name: "审稿",
    skill: "BlindReview + PublisherQA",
    description: "独立审稿，检查事实、观点兑现、AI 感与可发布性。",
  },
];

export default function HomePage() {
  return (
    <main className="shell">
      <header className="topbar">
        <div>
          <p className="eyebrow">WECHAT ARTICLE · V0.8</p>
          <h1>公众号 AI 编辑部</h1>
        </div>
        <button className="secondaryButton">文章库</button>
      </header>

      <section className="hero">
        <div className="heroCopy">
          <p className="eyebrow">从选题到可发布成稿</p>
          <h2>把一篇公众号文章，交给一支 AI 编辑部。</h2>
          <p className="lead">
            系统不会直接“吐一篇文章”，而是依次完成研究、观点竞争、文章架构、正文写作和独立审稿。
          </p>
        </div>

        <div className="composer">
          <label htmlFor="topic">今天想写什么？</label>
          <textarea
            id="topic"
            placeholder="例如：57万高校教师参加教创赛之后，教学比赛是在促教，还是又变成了一项考核？"
            rows={5}
          />
          <div className="composerFooter">
            <div className="inputModes">
              <span>选题</span>
              <span>粘贴素材</span>
              <span>上传文件</span>
            </div>
            <button className="primaryButton">开始研究</button>
          </div>
        </div>
      </section>

      <section className="workflowSection">
        <div className="sectionHeading">
          <div>
            <p className="eyebrow">EDITORIAL WORKFLOW</p>
            <h3>文章生产主链</h3>
          </div>
          <p>每一步都对应仓库中已经存在的 Skill，而不是重新造一套写作逻辑。</p>
        </div>

        <div className="stageGrid">
          {stages.map((stage) => (
            <article className="stageCard" key={stage.step}>
              <span className="stageNumber">{stage.step}</span>
              <h4>{stage.name}</h4>
              <p className="skillName">{stage.skill}</p>
              <p>{stage.description}</p>
            </article>
          ))}
        </div>
      </section>

      <section className="principles">
        <div>
          <p className="eyebrow">CORE PRINCIPLES</p>
          <h3>第一版先守住三件事</h3>
        </div>
        <div className="principleList">
          <div>
            <strong>来源可追溯</strong>
            <span>重要事实必须回到 Source。</span>
          </div>
          <div>
            <strong>Human Gate</strong>
            <span>研究、观点、结构三个关键节点允许用户确认。</span>
          </div>
          <div>
            <strong>独立审稿</strong>
            <span>BlindReview 与正文生成保持上下文隔离。</span>
          </div>
        </div>
      </section>
    </main>
  );
}
