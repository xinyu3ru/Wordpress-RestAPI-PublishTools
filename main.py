"""
列表 need_post文件夹下的所有文件夹，然后一一发表。
发表完成一个，更新一个链接，然后把文件夹复制到posted文件夹，然后删除本文件夹
"""

import logging
import os

from lib.upload import upload_post
from lib.update_readme import href_info, insert_index_info_in_readme
from lib.util import traversalDir_FirstDir, move_to_work_folder
from lib.compress import compress_pic

os_slash = '\\' if (os.name =='nt') else '/'

def main():
    base_dir = os.path.dirname(__file__)
    need_post_dir = base_dir + os_slash + 'need_post'
    readme_file = base_dir + os_slash + 'README.md'
    os.chdir(need_post_dir)
    dir_list = traversalDir_FirstDir(need_post_dir)
    if type(dir_list) == None:
        logging.info("There is no new blog")
        exit()
    for dir in dir_list:
        pic_dir = need_post_dir + os_slash + '' + dir + os_slash + 'images'
        pic_li = traversalDir_FirstDir(pic_dir, False)
        pic_list = list(pic_dir + os_slash + '' + i for i in pic_li)
        compress_pic(pic_list)
        (is_sucess, post_title, post_link) =  upload_post(need_post_dir + os_slash + '' + dir)
        if (is_sucess==0):
            logging.info(f"文章发布状态：sucess, 文章标题：{post_title}, 文章链接：{post_link}。")
            insert_info = href_info(post_title, post_link)
            insert_index_info_in_readme(readme_file, insert_info)
            move_to_work_folder((need_post_dir + os_slash + '' + dir), (base_dir + os_slash + 'posted' + os_slash +dir))
        else:
            logging.info("文章发布状态：failed。")


if __name__ == "__main__":
    main()
