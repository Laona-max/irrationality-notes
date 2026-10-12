# 閱讀筆記發布流程

正式網站：https://irrationality-notes.vercel.app

原稿：Laona-max/irrationality-notes。`index.md` 是「閱讀筆記」首頁，每篇讀書筆記使用獨立 Markdown 檔案。
發布：Laona-max/irrationality-quartz 的 content/，由 Vercel 監看 main 自動建置。

目前文章：
- `非理性的魅惑_序論與第一章筆記.md`
- `知識分子為何犯錯_第二章讀書心得.md`

新增文章時，在原稿儲存庫建立獨立檔案，並在 `index.md` 加上入口；不要用單篇文章取代首頁。站名與導覽由 Quartz 儲存庫的 `quartz.config.ts` 和 `quartz.layout.ts` 管理。

在同一個資料夾將兩個資料庫分別 clone 成 notes 和 quartz，於 quartz 執行 npm ci。修改 notes 原稿後，在 notes 執行 `sh .publish/publish.sh '更新閱讀筆記'`。流程會同步文章、執行 Quartz 建置、提交並推送兩個資料庫；Vercel 會自動發布。

同步時只在發布副本補上頁面標題資料，保留原稿全文。請勿直接編輯 quartz/content；它會由 notes 重新產生。
