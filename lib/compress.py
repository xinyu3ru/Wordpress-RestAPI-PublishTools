"""_summary_
作者：xinyu3ru 
代码部分参考https://www.jianshu.com/p/649cf285b21b，代码备份./test.py
"""

import logging
import os
import threading

from PIL import Image

from lib.util import convert_mb_kb, is_jpg_file, is_png_file

def compress_pic(path_list):
    # 压缩线程数组
    threads = []
    # 当前路径下所有的图片加入压缩线程
    for childFile in path_list:
    # 创建压缩线程
        compressThread = CompressThread(childFile)
        compressThread.start()
        threads.append(compressThread) # type: ignore
    # 开始遍历执行压缩线程
    for thread in threads:
        thread.join()

def compress_jpg(path, width=720,quality=85):
    img: Image.Image = Image.open(path)
    w, h = img.size
    byteSizeBefore = len(img.fp.read())
    if w > width:
        h = int(h*width/w)
        w = width
        logging.info(f"图片宽度超过 { width } px,调整为{ w }x{ h } px。")
    else:
        w = int(w)
        h = int(h)
    img = img.resize((w,h), Image.LANCZOS)
    img.save(path, quality=quality, optimize=True)
    byteSizeAfter = os.path.getsize(path)
    logging.info(f"{ path } , 压缩前：, { str(convert_mb_kb(byteSizeBefore)) }, 压缩后：, { str(convert_mb_kb(byteSizeAfter)) }。")

def compress_png(path):
    if os.system("pngquant --version") != 0:
        logging.info("\n未检测到pngquant命令行环境，请参照pngquant官网搭建命令行环境：https://pngquant.org/")
    else:
        cmd = "pngquant 256 --quality=65-80 --skip-if-larger --force --ext .png " + path
        os.system(cmd)

# 压缩线程（同步压缩）
class CompressThread(threading.Thread):
    # 构造方法
    def __init__(self, compressPath) -> None:
        threading.Thread.__init__(self)
        self.threadLock = threading.Lock()
        self.path = compressPath

    # 运行方法
    def run(self) -> None:
        logging.info(f"\n线程开始运行，压缩图片路径为：{ self.path }")
        # 获得锁
        self.threadLock.acquire() # type: ignore
        if is_jpg_file(self.path):
            compress_jpg(self.path)
        elif is_png_file(self.path):
            compress_png(self.path)
        else:
            pass
        # # 重命名后缀
        # if self.extension == 'jpg' or self.extension == 'jpeg':
        #     os.remove(self.path)
        #     os.rename(os.path.join(self.root, self.compressFile + ".png"),
        #               os.path.join(self.root, self.compressFile))
        # 释放锁
        self.threadLock.release() # type: ignore
        logging.info(f"\n线程结束运行，压缩图片路径为：{ self.path }")




