"""
文件夹列表
"""

import os
import shutil
import sys
import random
from PIL import Image, ImageDraw, ImageFont


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


def ensure_banner(folder_path, image_files, banner_size=(720, 405), title="Default Banner"):
    banner_path = os.path.join(folder_path, 'banner.png')
    
    # 如果 banner.png 已经存在，直接返回
    if os.path.exists(banner_path):
        print("banner.png already exists.")
        return banner_path
    
    # 如果图片文件列表不为空，找到最大的图片并缩放
    if image_files:
        # 找到最大的图片文件
        largest_image = max(image_files, key=lambda f: os.path.getsize(os.path.join(folder_path, f)))
        largest_image_path = os.path.join(folder_path, largest_image)
        
        # 打开图片并缩放
        with Image.open(largest_image_path) as img:
            img.thumbnail(banner_size, Image.ANTIALIAS)
            img.save(banner_path)
        
        print(f"banner.png created from {largest_image}.")
        return banner_path
    
    # 如果图片文件列表为空，使用标题生成 Banner 图片
    else:
        # 创建一个空白图片
        banner = Image.new('RGB', banner_size, color=(97, 98, 98))  # 背景颜色
        draw = ImageDraw.Draw(banner)
        
        # 设置字体（文泉驿字体）
        try:
            font_path = "wqy-microhei.ttc"  # 文泉驿字体路径
            font = ImageFont.truetype(font_path, 40)  # 初始字体大小
        except IOError:
            print("文泉驿字体未找到，使用默认字体。")
            font = ImageFont.load_default()  # 如果字体不存在，使用默认字体
        
        # 动态调整字体大小以适应 Banner 图片
        max_font_size = 100
        min_font_size = 20
        padding = 20  # 文字与图片边缘的间距
        max_text_width = banner_size[0] - 2 * padding  # 最大文字宽度
        max_text_height = banner_size[1] - 2 * padding  # 最大文字高度
        
        # 调整字体大小
        for font_size in range(max_font_size, min_font_size, -1):
            font = ImageFont.truetype(font_path, font_size) if font_path else ImageFont.load_default()
            text_width, text_height = draw.textsize(title, font=font)
            if text_width <= max_text_width and text_height <= max_text_height:
                break  # 找到合适的字体大小
        
        # 自动换行处理
        lines = []
        words = title.split()
        current_line = words[0]
        for word in words[1:]:
            test_line = current_line + " " + word
            test_width, _ = draw.textsize(test_line, font=font)
            if test_width <= max_text_width:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word
        lines.append(current_line)
        
        # 计算文字的总高度
        total_text_height = len(lines) * text_height
        
        # 计算文字的起始位置（垂直居中）
        text_y = (banner_size[1] - total_text_height) // 2
        
        # 在图片上绘制每一行文字
        for line in lines:
            text_width, _ = draw.textsize(line, font=font)
            text_x = (banner_size[0] - text_width) // 2  # 水平居中
            draw.text((text_x, text_y), line, font=font, fill=(255, 255, 255))  # 文字颜色为白色
            text_y += text_height  # 移动到下一行
        
        # 保存生成的 Banner 图片
        banner.save(banner_path)
        print(f"banner.png created with title: {title}.")
        return banner_path

def get_random_element(data_list): 
    """从非空列表中随机返回一个元素"""
    if not data_list: 
        raise ValueError("列表不能为空")
    return random.choice(data_list)