export type WorkflowStageId =
  | "research"
  | "angle"
  | "architecture"
  | "writing"
  | "review"
  | "visual"
  | "publishing";

export type WorkflowStage = {
  id: WorkflowStageId;
  label: string;
  skills: string[];
  humanGate: boolean;
  description: string;
};

export const ARTICLE_WORKFLOW: WorkflowStage[] = [
  {
    id: "research",
    label: "研究",
    skills: ["topic-hunter", "research-pack"],
    humanGate: true,
    description: "验证选题、建立证据链、记录来源与不确定性。",
  },
  {
    id: "angle",
    label: "观点",
    skills: ["author-lens"],
    humanGate: true,
    description: "生成并比较多个 POV，选择最适合读者与证据的主线。",
  },
  {
    id: "architecture",
    label: "结构",
    skills: ["article-architect"],
    humanGate: true,
    description: "冻结 Reader Contract、核心答案和正文交付结构。",
  },
  {
    id: "writing",
    label: "写作",
    skills: ["viral-writer"],
    humanGate: false,
    description: "按结构分段生成，执行清晰度与段落节奏检查。",
  },
  {
    id: "review",
    label: "审稿",
    skills: ["blind-review", "publisher-qa"],
    humanGate: false,
    description: "使用独立上下文完成盲审与发布前质量检查。",
  },
  {
    id: "visual",
    label: "配图",
    skills: ["visual-editor"],
    humanGate: false,
    description: "生成封面与插图方案，并写入视觉资产状态。",
  },
  {
    id: "publishing",
    label: "发布",
    skills: ["publishing-plan", "growth-reviewer"],
    humanGate: false,
    description: "输出发布计划并为发布后的复盘保留数据入口。",
  },
];

export const MVP_STAGE_IDS: WorkflowStageId[] = [
  "research",
  "angle",
  "architecture",
  "writing",
  "review",
];

export function getNextStage(current: WorkflowStageId): WorkflowStage | null {
  const currentIndex = ARTICLE_WORKFLOW.findIndex((stage) => stage.id === current);
  if (currentIndex < 0 || currentIndex === ARTICLE_WORKFLOW.length - 1) return null;
  return ARTICLE_WORKFLOW[currentIndex + 1];
}
