# Rublog 博客 Github 仓库

这个项目脱胎于[WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools)，这为我提供了思路。
鉴于我不喜欢 xmlrpc ，所以使用 wordpress 的 restAPI 更新。
更新库来自于[wordpress-markdown-blog-loader](https://github.com/binxio/wordpress-markdown-blog-loader)，部分修改。

[点这里，跳过博客目录看仓库说明](#用github-actions写markdown文章自动更新到wordpress)

---start---

## 目录(2024年06月05日更新)

---end---

## 用Github Actions写Markdown文章，自动更新到WordPress

- 写博客最舒服的格式是Markdown；

- 管理博客站最省心的方式是WordPress；

- 推广博客站最好的平台是Github；

这个项目可以让你用 Markdown 写博客，push 更新到 Github 后，Github Actions 自动将文章更新到 WordPress，并将 WordPress 站的文章索引更新到 Github 仓库的README.md，供搜索引擎收录。

![image-20210119181051609](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033557RhdS4nmK.png)

### 使用Github Actions 有什么好处？

Github Actions 可以让我们无需安装开发环境，即可完成代码的运行。

![image-20210119180656968](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033850KpH03KNE.png)

对于本项目而言，我可以用手机版Git App，或者Github网页完成新建文章, 然后push到仓库，Github Actions会自动帮我完成相关代码运行，代码可以帮我更新文章到WordPress网站，并生成新的文章目录索引，并自动给你更新到README.md, 供搜索引擎收录。

![image-20210119180529083](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033950bTXn7Skr.png)

### 如何保护自己的WordPress账户密码？

Github 有一个 secrets 功能，可以将用户名密码等关键信息保护起来，只有Github Actions可以读取到关键信息。

本项目需要设置三个secret

- WordPress登录用户名, 变量名为 USERNAME
- WordPress登录密码，变量名为 PASSWORD
- WordPress的域名，变量名为 HOST

![image-20210119173133800](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230341284PaHwCDm.png)

### 如何新建文章？

在`need_post` 目录下复制 example 目录改名之后继续编辑文件夹下的 `index.md` markdown文件即可

![image-20210119181544158](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230342738acPGWSM.png)

### 文章管理：如何为文章分类/加关键词标签？

在 `.md` 文件顶部填写以下初始化信息，即可完成标题（title），标签（tags），分类（categories）的设置，**其中title为必填项目**（这些关键词不是我定义的，我借用了著名静态博客构建工具 [hexo](https://github.com/hexojs/hexo) 的标准）

``` tag and category
---
title: 我是标题
tags: 
- 我是0号标签关键词
- 我是1号标签关键词
- 我是2号标签关键词
categories:
- 我是1号分类
- 我是2号分类
---

```

## 标签(tags)和分类(categories)有什么区别？

标签(tags)是针对单篇文章的关键词，比如香蕉的标签有 **黄色**，**味甜** （标签是香蕉的属性）
分类(categories)是本篇文章的归属，比如香蕉的分类为 **水果**，**植物**

![image-20210119182027684](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123034368EXM02d37.png)

## 如何使用？

完成以上配置后

每次在`_posts` 文件夹新增或更新文章后，运行

``` git
git pull && git add _posts && git commit -m "update" && git push
```

![image-20210119182503520](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123034888HbKthGTh.png)

即可！

![image-20210119182653436](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036038n18wBCfT.png)

### Github README.md显示效果,（新增的文章排在首位）

![image-20210119184015781](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230361713668ZtFR.png)

### WordPress网站也同步发布了文章

![image-20210119182849720](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036272XED7hTE0.png)

## 如何用手机完成博客更新操作？

![微信图片_20210119192838](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036503KhBJRrpj.jpeg)

用锤子便签，可以优雅舒适地写Markdown，手机App很好用，还有网页版可以用，有5GB的免费空间，能写到锤子倒闭。
python3 -m wordpress_markdown_blog_loader posts upload example --host test.yourdomain.cn
