"""
列表 need_post文件夹下的所有文件夹，然后一一发表。
发表完成一个，更新一个链接，然后把文件夹复制到posted文件夹，然后删除本文件夹
"""

import logging
import os
import re
import time

from os.path import expanduser
from wordpress_markdown_blog_loader import posts
from lib.dir import traversalDir_FirstDir

def href_info(title, link):
    return "<br/><br/><br/>\n\n\n\n## 本文永久更新地址: \n[" + title + "](" + link + ")&emsp; &emsp; " + time.strftime("-%Y-%m-%d-%H:%M",time.localtime())

# 在README.md中插入信息文章索引信息，更容易获取google的收录
def insert_index_info_in_readme(insert_info):
    # 替换 ---start---
    insert_info = "---start---\n## 目录(" + time.strftime('%Y年%m月%d日') + "更新)" +"\n" + insert_info +"\n"
    with open(os.path.join(os.getcwd(), "README.md"), "r+", encoding="UTF-8") as f:
        # 读取文件内容
        content = f.read()
        # 替换内容
        content = re.sub(r'---start---.*', insert_info, content)
        # 将指针移动到文件开头
        f.seek(0)
        # 清空文件
        f.truncate()
        # 将修改后的内容写入文件
        f.write(content)
        # 关闭文件
        f.close()
    return True

# 为了使用 wordpress_markdown_blog_loader 这个库，需要把账号密码信息存储到~/.wordpress.ini
DEFAULT_INFO = {'host':'','username':'','password':''}
try:
    if(os.environ["USERNAME"]):
        DEFAULT_INFO['username'] = os.environ["USERNAME"]
    if(os.environ["PASSWORD"]):
        DEFAULT_INFO['password'] = os.environ["PASSWORD"]
    if(os.environ["HOST"]):
        DEFAULT_INFO['host'] = os.environ["HOST"]
except:
    print("无法获取github的secrets配置信息，无法继续执行后续指令。")
    exit()
    
def save_to_ini():
    if os.path.exists(expanduser("~/.wordpress.ini")):
        return
    else:
        content = f'''[DEFAULT]
host = {DEFAULT_INFO['host']}

[{DEFAULT_INFO['host']}]
username = {DEFAULT_INFO['username']}
password = {DEFAULT_INFO['password']}'''
        with open(expanduser("~/.wordpress.ini"), "r+", encoding = "UTF-8") as f:
            # 将指针移动到文件开头
            f.seek(0)
            # 清空文件
            f.truncate()
            # 将修改后的内容写入文件
            f.write(content)
            # 关闭文件
            f.close()
    return

def main():
    base_dir = os.path.dirname(__file__)
    need_post_dir = base_dir + '/need_post'
    os.chdir(need_post_dir)
    dir_list = traversalDir_FirstDir(need_post_dir)
    if type(dir_list) == None:
        logging.info("There is no new blog")
        exit()
    for dir in dir_list:
        m_title, m_link, new_post = posts(['upload', dir, '--host', DEFAULT_INFO['host']])
        new_info = href_info(m_title, m_link)
        if new_post:
            insert_index_info_in_readme(new_info)
        source_dir = need_post_dir + '/' + dir
        posted_dir = base_dir + '/posted'

if __name__ == "__main__":
    main()
