import type { Metadata } from "next";
import "./globals.css";

export const metadata: Metadata = {
  title: "公众号 AI 编辑部",
  description: "从选题、研究、观点、结构、写作到审稿的公众号文章生产系统",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="zh-CN">
      <body>{children}</body>
    </html>
  );
}
