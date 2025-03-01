# Rublog 部落格 Github 儲存庫

這個項目借鑒於 [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools) ，這為我提供了思路。

鑒於我不喜歡 xmlrpc ，所以使用 wordpress 的 RestAPI 更新。

WordPress API 庫來自於 [wordpress-markdown-blog-loader](https://github.com/binxio/wordpress-markdown-blog-loader)，輕微修改。

[點這裡，跳過部落格目錄看倉庫說明](#用Github Actions寫Markdown文章，自動更新到WordPress)

[點這裡，倉庫使用說明](#使用教學)

[中文简体](../README.md) --- [English](README_EN.md) --- [Deutsch](README_DE.md) --- [Français](README_FR.md) --- [Español](README_ES.md) --- [Русский](README_RU.md) --- [繁體中文](README_ZH-CHT.md) --- [日本語](README_JP.md)

## 目錄(2024年07月27日更新)

[如何使用github actions發佈markdown文章到WordPress網站](https://www.rxx0.com/?p=4150)&emsp; &emsp; 發佈時間： 2024-07-27-05:24

[使用 act 調試 github actions 技巧](https://www.rxx0.com/software/diao-shi-github-actions-de-4-chong-gong-ju.html) &emsp;&emsp; 發佈時間： 2024-07-27-04:55 

[兩種方法解決SourceTree通過SSH連接GitHub Permission denied (publickey)問題](https://www.rxx0.com/software/liang-chong-fang-fa-jie-jue-sourcetree-tong-guo-ssh-lian-jie-github-permission-denied-publickey-wen-ti.html)  
&emsp;&emsp;發佈時間： 2024-07-26-10:58 

[測試 python & markdown 自動發佈文章](https://www.rxx0.com/software/test-python-and-markdown-to-automatically-publish-articles.html)&emsp; &emsp; 發佈時間： 2024-07-24-16:10

---完---  （在繁体中文语境中也是这样表述“完”字 ，所以“---完---” 这种形式本身在繁体中文里也是适用的  ）  

## 用Github Actions寫Markdown文章，自動更新到WordPress

- 寫部落格最舒服的格式是Markdown；

- 管理部落格站最省心的方式是WordPress；

- 推廣部落格站最好的平台是Github；

這個項目可以讓你用 Markdown 寫部落格，push 更新到 Github 後，Github Actions 自動將文章更新到 WordPress，並將文章網址更新到 README.md。

![repo 說明](../posted/readme/images/rxx0_2024-07-25_21-55-47.png)

### 使用Github Actions有甚麼好處？

Github Actions 可以讓我們無需安裝開發環境，即可完成程式碼的運行。

![github actions 運行](../posted/readme/images/rxx0_2024-07-25_22-06-46.png)

只需要新建Markdown文章，然後更新到倉庫，Github Actions會自動更新文章到WordPress，並把文章鏈接更新到README.md。  

![更新文章連接到readme（此句英文原文“链接”用“link”更合适，完整正确英文表述是“Update the article link to the readme”  ，这里是按照要求翻译中文部分 ）  ](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## 使用教學

### WordPress 需要安裝的外掛程式（Plugins）

- [Rankmath](https://rankmath.com/wordpress/plugin/seo-suite) SEO 外掛程式

### 取得需要的WordPress配置

特殊處理的只有 WordPress 登入密碼，這個登入密碼不是網頁登入的後台密碼，需要單獨生成 RestAPI 應用程式密碼。

_應用程式密碼允許透過非互動式系統（例如 XML-RPC 或 REST API）進行身份驗證，而無需提供您的實際密碼。應用密碼可隨時撤銷。它們不能用於透過傳統方式登入您的網站。_

生成方式如下：→ 生成方式如下：

这段内容本身就是简体中文和繁体中文写法一致，无需转换。如果你还有其他内容需要转换，欢迎继续向我提问。  

![生成 RestAPI 應用程式密碼](../posted/readme/images/rxx0_2025-03-01_09-03-37.png)

![生成 RestAPI 應用程式密碼](../posted/readme/images/rxx0_2025-03-01_10-36-02.png)

### 如何保護自己的WordPress帳戶密碼？

Github有一個secrets功能，可以將使用者名稱密碼等關鍵資訊保護起來，只有Github Actions可以讀取到關鍵資訊。

本項目需要設置三個祕密

- 填寫 WordPress 登入使用者名稱，變量名為 USERNAME
- 填寫 WordPress RestAPI 應用程式密碼，變數名為 PASSWORD
- 填寫 WordPress 的域名，變量名為 HOST

![倉庫需要的祕密](../posted/readme/images/rxx0_2024-07-27_11-07-35.png)

### 允許 Github Actions 回寫倉庫

Github的安全保護功能越來越健全，需要單獨開啟這個權限。開放方法如下：

![倉庫需要的回寫權限](../posted/readme/images/rxx0_2024-07-27_11-45-46.png)

### 如何新建文章？ 可翻译为：如何新建文章？（繁體中文本身與簡體相同）如果是要轉換字體，即為：如何新建文章？（轉換為繁體字體）

如果是想以更加符合台灣等地表述習慣的翻譯：如何新增文章？  轉換為繁體字體是：如何新增文章？  

將`posted`目錄下的 example 資料夾改名，複製到`need_post`資料夾，繼續編輯資料夾下的 `index.md` markdown 檔案。

The "images" folder stores the referenced pictures, or directly references online pictures, CDN pictures, or pictures from image hosting platforms. 

![如何新建文章 （这本身就是繁体中文，和简体一样 ）

若是逐字对应更标准的繁体写法：如何新建文章 → 如何新建文章 

非要转换为繁體中文表述，也可寫成：如何新撰文章  （把“建”換成“撰”更具文言文/传统意味  ）  ](../posted/readme/images/rxx0_2024-07-25_22-15-07.png)

### 文章管理：如何為文章分類/加關鍵詞標籤？

在 `.md` 檔案頂部填寫以下初始化資訊，即可完成標題（title），標籤（tags），分類（categories）的設定，**以下內容均為必填項目**。

```tag and category
author: xinyu2ru
categories:
- software
date: 2024-07-24 08:21:00
excerpt: 這裡寫文章的摘要內容，這段文字應該出現在文章摘要。
image: images/banner.jpg
status: publish
title: 這裡寫文章的標題
focus-keywords: markdown upload wordpress
```

- **author 必須存在**
- The classification directory of "categories" must exist
- **banner圖片必須存在**

## 標籤(tags)和分類(categories)有什麼區別？

標籤(tags)是針對單篇文章的關鍵詞，比如香蕉的標籤有 **黃色**，**味甜** （標籤是香蕉的屬性）
分類（categories）是本篇文章的歸屬，比如香蕉的分類為 **水果**，**植物** 可翻譯為：
分類（categories）是本篇文章的歸屬，比如香蕉的分類為 **水果**，**植物**
分類（categories）是本篇文章的歸屬，例如香蕉的分類為**水果**、**植物** 。

分類（categories）is the attribution of this article. For example, the classification of bananas is **fruit**, **plant** 。  

## 如何使用？  的 Traditional Chinese 是：如何使用？（繁简同形）不过更常见的表述会是：如何使用？→ 如何使用？（“怎”也常写为“怎” ）  

如果是问“怎样使用”的 Traditional Chinese 则是：怎樣使用？  

完成以上配置後

每次在「need_post」資料夾新增或更新文章後，運行git指令即可！

```git
git pull && git add _posts && git commit -m "update" && git push
```

也可以使用各種 git 管理軟體將更新提交到 GitHub。

### Github README.md顯示效果，（新增的文章排在首位）

![更新文章鏈接到readme）  ](../posted/readme/images/rxx0_2024-07-25_22-09-41.png)

## 如何用手機完成部落格更新操作？

錘子便簽，可以優雅舒適地寫Markdown 。

Obsidian，也是我現在主要用的編輯軟件，電腦和手機均可用。

## 更新

- SEO 外掛由 Yoast 改為 Rank Math (2025年2月11日 11:51)
- 更新本 README 檔案 (2025年3月1日 09:32)
