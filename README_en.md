# Rublog Blog Github Repository

This project was born out of [WordPressXMLRPCTools](https://github.com/zhaoolee/WordPressXMLRPCTools), which provided me with ideas.
Whereas

[Click here to skip the blog directory and read the warehouse description] (#Use github-actions to write markdown articles and automatically update them to wordpress)

---start---

## Table of contents (updated on June 5, 2024)

---end---

## Use Github Actions to write Markdown articles and automatically update to WordPress

- The most comfortable format for blogging is Markdown;

- The most worry-free way to manage a blog site is WordPress;

- The best platform to promote your blog site is Github;
  
This project allows you to write a blog using Markdown. After pushing the update to Github, Github Actions will automatically update the article to WordPress, and update the article index of the WordPress site to README.md in the Github warehouse for search engines to include.

![image-20210119181051609](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033557RhdS4nmK.png)

### What are the benefits of using Github Actions?

Github Actions allows us to run the code without installing a development environment.

![image-20210119180656968](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033850KpH03KNE.png)

For this project, I can use the mobile version of Git App or the Github web page to create a new article, and then push it to the warehouse. Github Actions will automatically help me run the relevant code. The code can help me update the article to the WordPress website and generate a new article. The article directory is indexed and automatically updated to README.md for search engines to include.

![image-20210119180529083](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123033950bTXn7Skr.png)

### How to protect your WordPress account password?

Github has a secrets function that can protect key information such as username and password. Only Github Actions can read key information.

This project requires setting up three secrets

- WordPress login username, variable name is USERNAME
- WordPress login password, variable name is PASSWORD
- WordPress domain name, variable name is HOST

![image-20210119173133800](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230341284PaHwCDm.png)

### How to create a new article?

Copy the example directory in the `need_post` directory, rename it, and continue editing the `index.md` markdown file in the folder.

![image-20210119181544158](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230342738acPGWSM.png)

### Article management: How to classify/add keyword tags to articles?

Fill in the following initialization information at the top of the `.md` file to complete the settings of title, tags, and categories, **title is a required item** (these keywords are not defined by me , I borrowed the standard of the famous static blog building tool [hexo](https://github.com/hexojs/hexo))

```tag and category
---
title: I am the title
tags:
- I am No. 0 tag keyword
- I am the No. 1 tag keyword
- I am the No. 2 tag keyword
categories:
- I am Category No. 1
- I am classified as No. 2
---

```
## What is the difference between tags and categories?

Tags are keywords for a single article. For example, the tags for banana are **yellow**, **sweet** (tags are attributes of banana)
Categories are where this article belongs. For example, bananas are classified as **Fruit**, **Plant**

![image-20210119182027684](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123034368EXM02d37.png)

## how to use?

After completing the above configuration

Every time after adding or updating an article in the `_posts` folder, run

``` git
git pull && git add _posts && git commit -m "update" && git push
```

![image-20210119182503520](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123034888HbKthGTh.png)

That’s it!

![image-20210119182653436](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036038n18wBCfT.png)

### Github README.md display effect, (new articles are ranked first)

![image-20210119184015781](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/16111230361713668ZtFR.png)

### The WordPress website also published articles simultaneously

![image-20210119182849720](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036272XED7hTE0.png)

## How to complete blog update operation using mobile phone?

![WeChat picture_20210119192838](https://raw.githubusercontent.com/zhaoolee/WordPressXMLRPCTools/master/README/1611123036503KhBJRrpj.jpeg)

With Hammer Notes, you can write Markdown elegantly and comfortably. The mobile app is very easy to use, and there is also a web version available. It has 5GB of free space and can write until Hammer collapses.
