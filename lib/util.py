"""
文件夹列表
"""

import os
import shutil
import sys


def traversalDir_FirstDir(path='./need_post', is_rt_dir=True):
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
            if is_rt_dir:
                if (os.path.isdir(m)):
                    h = os.path.split(m)
                    list.append(h[1])
            else:
                if (os.path.isfile(m)):
                    h = os.path.split(m)
                    list.append(h[1])
        #list.remove('example')
    return list

def move_to_work_folder(cur_path, work_path):
    """
    将work_folder下的所有子目录中的文件移到根目录中：
    :param work_path: 当前工作目录
    :param cur_path: 文件所在目录
    :return:
    """
    for filename in os.listdir(cur_path):
        if os.path.isfile(os.path.join(cur_path, filename)):
            if not os.path.exists(work_path):
                os.makedirs(work_path)
            shutil.move(os.path.join(cur_path, filename), os.path.join(work_path, filename))
        elif os.path.isdir(os.path.join(cur_path, filename)):
            move_to_work_folder(os.path.join(cur_path, filename), os.path.join(work_path, filename))
        else:
            sys.exit("Should never reach here.")
    # remove empty folders
    if cur_path != work_path:
        os.rmdir(cur_path)

is_jpg_file = lambda x: any(x.endswith(extension)
                            for extension in ['.jpg', '.JPG', 'Jpg', 'Jpeg', 'JPEG', 'jpeg',
                                              '.bmp', '.BMP', '.Bmp'])

is_png_file = lambda x: any(x.endswith(extension)
                            for extension in ['.png', '.PNG', 'Png', 'PNg', 'pNG'])

def convert_mb_kb(bytesize):
    """
    把byte长度转换成KB,MB
    """
    if bytesize > 0:
        bytesize = bytesize / 1024
        if bytesize < 1024:
            return "%.fKB" % bytesize
        else:
            return "%.2fMB" % (bytesize / 1024)    
        