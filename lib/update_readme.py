import re
import time



def href_info(title, link):
    return "[" + title + "](" + link + ")&emsp; &emsp; " + time.strftime("发布时间： %Y-%m-%d-%H:%M",time.localtime())

# 在README.md中插入信息文章索引信息，更容易获取google的收录
def insert_index_info_in_readme(readme_file, insert_info):
    # 替换 ---start---
    insert_info = "---start---\n## 目录(" + time.strftime('%Y年%m月%d日') + "更新)" +"\n" + insert_info +"\n"
    with open(readme_file, "r+", encoding="UTF-8") as f:
        # 读取文件内容
        content = f.read()
        # 替换内容
        content = re.sub(r'---start---.*?更新)', insert_info, content)
        # 将指针移动到文件开头
        f.seek(0)
        # 清空文件
        f.truncate()
        # 将修改后的内容写入文件
        f.write(content)
        # 关闭文件
        f.close()
    return True