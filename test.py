import os
from pypinyin import pinyin, lazy_pinyin

def traversalDir_FirstDir(path='./need_post'):
    # 定义一个列表，用来存储结果
    list = []
    # 判断路径是否存在
    if (os.path.exists(path)):
        # 获取该目录下的所有文件或文件夹目录
        files = os.listdir(path)
        for file in files:
            # 得到该文件下所有目录的路径
            m = os.path.join(path, file)
            # 判断该路径下是否是文件夹
            if (os.path.isdir(m)):
                h = os.path.split(m)
                list.append(h[1])
        return list

lll = traversalDir_FirstDir()
lll.remove('example')
print(lll)

def pinyin_slug(title='There-is-no-title'):
    slug_list = lazy_pinyin(title)
    slug = '-'.join(slug_list)
    
    return slug

print(pinyin_slug())