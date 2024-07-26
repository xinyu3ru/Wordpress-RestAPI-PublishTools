import logging
import os
import re
import time


def href_info(title, link):
    return "[" + title + "](" + link + ")&emsp; &emsp; " + time.strftime("发布时间： %Y-%m-%d-%H:%M",time.localtime())

# 在README.md中插入信息文章索引信息，更容易获取google的收录
def insert_index_info_in_readme(readme_file, insert_info):
    # 替换 ---start---
    insert_info = "---start---\n\n## 目录(" + time.strftime('%Y年%m月%d日') + "更新)" +"\n\n" + insert_info
    original_str = re.compile(r'---star[\s\S]*?更新\)') 
    with open(readme_file, "r+", encoding="UTF-8") as f:
        # 读取文件内容
        content = f.read()
        # 替换内容
        content = re.sub(original_str, insert_info, content)
        # 将指针移动到文件开头
        f.seek(0)
        # 清空文件
        f.truncate()
        # 将修改后的内容写入文件
        f.write(content)
        # 关闭文件
        f.close()
    return True


if __name__ == "__main__":
    os_slash = '\\' if (os.name =='nt') else '/'
    base_dir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    readme_file = base_dir + os_slash + 'README.md'
    post_title = "两种方法解决 sourcetree 通过 ssh 连接 github Permission denied (publickey)问题"
    post_link ="https://www.rxx0.com/software/liang-chong-fang-fa-jie-jue-sourcetree-tong-guo-ssh-lian-jie-github-permission-denied-publickey-wen-ti.html"
    logging.info(f"文章发布状态：sucess, 文章标题：{post_title}, 文章链接：{post_link}。")
    insert_info = href_info(post_title, post_link)
    insert_index_info_in_readme(readme_file, insert_info)
    pass
