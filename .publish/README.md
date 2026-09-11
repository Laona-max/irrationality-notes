# 閱讀筆記發布流程

正式網站：https://irrationality-notes.vercel.app

原稿：Laona-max/irrationality-notes 的 index.md。
發布：Laona-max/irrationality-quartz 的 content/index.md，由 Vercel 監看 main 自動建置。

在同一個資料夾將兩個資料庫分別 clone 成 notes 和 quartz，於 quartz 執行 npm ci。修改 notes 原稿後，在 notes 執行 `sh .publish/publish.sh '更新閱讀筆記'`。流程會同步文章、執行 Quartz 建置、提交並推送兩個資料庫；Vercel 會自動發布。

同步時只在發布副本補上頁面標題資料，保留原稿全文。請勿直接編輯 quartz/content；它會由 notes 重新產生。
