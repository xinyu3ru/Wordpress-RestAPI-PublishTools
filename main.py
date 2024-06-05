"""
markdown预处理，如果没有slug，那么就创建一个slug

列表 need_post文件夹下的所有文件夹，然后一一发表。
发表完成一个，更新一个链接，然后把文件夹复制到posted文件夹，然后删除本文件夹

"""

def href_info(link):
    return "<br/><br/><br/>\n\n\n\n## 本文永久更新地址: \n[" + link + "](" + link + ")"

# 在README.md中插入信息文章索引信息，更容易获取google的收录
def insert_index_info_in_readme():
    # 获取_posts下所有markdown文件
    md_list = get_md_list(os.path.join(os.getcwd(), "_posts"))
    # 生成插入列表
    insert_info = ""
    md_list.sort(reverse=True)
    # 读取md_list中的文件标题
    for md in md_list:
        (content, metadata) = read_md(md)
        title = metadata.get("title", "")
        insert_info = insert_info + "[" + title +"](" + "https://"+domain_name + "/p/" + os.path.basename(md).split(".")[0] +"/" + ")\n\n"
    # 替换 ---start--- 到 ---end--- 之间的内容

    insert_info = "---start---\n## 目录(" + time.strftime('%Y年%m月%d日') + "更新)" +"\n" + insert_info + "---end---"

    # 获取README.md内容
    with open (os.path.join(os.getcwd(), "README.md"), 'r', encoding='utf-8') as f:
        readme_md_content = f.read()

    print(insert_info)

    new_readme_md_content = re.sub(r'---start---(.|\n)*---end---', insert_info, readme_md_content)

    with open (os.path.join(os.getcwd(), "README.md"), 'w', encoding='utf-8') as f:
        f.write(new_readme_md_content)

    print("==new_readme_md_content==>>", new_readme_md_content)

    return True

def main():
    # 1. 获取网站数据库中已有的文章列表
    post_link_id_list = get_posts()
    print(post_link_id_list)
    link_id_dic = post_link_id_list_2_link_id_dic(post_link_id_list)
    print(link_id_dic)
    # 2. 获取md_sha1_dic
    # 查看目录下是否存在md_sha1.txt,如果存在则读取内容；
    # 如果不存在则创建md_sha1.txt,内容初始化为{}，并读取其中的内容；
    # 将读取的字典内容变量名，设置为 md_sha1_dic
    md_sha1_dic = get_md_sha1_dic(os.path.join(os.getcwd(), ".md_sha1"))

    # 3. 开始同步
    # 读取_posts目录中的md文件列表
    md_list = get_md_list(os.path.join(os.getcwd(), "_posts"))

    for md in md_list:
        # 计算md文件的sha1值，并与md_sha1_dic做对比
        sha1_key = os.path.basename(md).split(".")[0]
        sha1_value = get_sha1(md)
        # 如果sha1与md_sha1_dic中记录的相同，则打印：XX文件无需同步;
        if((sha1_key in md_sha1_dic.keys()) and ("hash_value" in md_sha1_dic[sha1_key]) and (sha1_value == md_sha1_dic[sha1_key]["hash_value"])):
            print(md+"无需同步")
        # 如果sha1与md_sha1_dic中记录的不同，则开始同步
        else:
            # 读取md文件信息
            (content, metadata) = read_md(md)
            # 获取title
            title = metadata.get("title", "")
            terms_names_post_tag = metadata.get("tags",  domain_name)
            terms_names_category = metadata.get("categories", domain_name)
            post_status = "publish"
            link = urllib.parse.quote(sha1_key , safe='').lower() 
            content = markdown.markdown(content + href_info("https://"+domain_name+"/p/"+link+"/"), extensions=['tables', 'fenced_code'])
            # 如果文章无id,则直接新建
            if(("https://"+domain_name+"/p/"+link+"/" in link_id_dic.keys()) == False):
                new_post(title, content, link, post_status, terms_names_post_tag, terms_names_category)
                print("new_post==>>", {
                    "title": title, 
                    "content": content, 
                    "link": link, 
                    "post_status": post_status,
                    "terms_names_post_tag": terms_names_post_tag,
                    "terms_names_category": terms_names_category
                });
            # 如果文章有id, 则更新文章
            else:
                # 获取id
                id = link_id_dic["https://"+domain_name+"/p/"+link+"/"]
                edit_post(id, title, content, link, post_status, terms_names_post_tag, terms_names_category)

                print("edit_post==>>", {
                    "id": id, 
                    "title": title, 
                    "content": content,
                    "link": link,
                    "post_status": post_status, 
                    "terms_names_post_tag": terms_names_post_tag,
                    "terms_names_category": terms_names_category
                });

    # 4. 重建md_sha1_dic
    rebuild_md_sha1_dic(os.path.join(os.getcwd(), ".md_sha1"), os.path.join(os.getcwd(), "_posts"))
    # 5. 将链接信息写入insert_index_info_in_readme
    insert_index_info_in_readme()

main()
