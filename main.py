"""
列表 need_post文件夹下的所有文件夹，然后一一发表。
发表完成一个，更新一个链接，然后把文件夹复制到posted文件夹，然后删除本文件夹
"""

import logging
import os
import re
import subprocess
import time


from wordpress_markdown_blog_loader import posts
from lib.update_readme import href_info, insert_index_info_in_readme
from lib.util import traversalDir_FirstDir, move_to_work_folder, init_ini






def main():
    host_server = init_ini()
    base_dir = os.path.dirname(__file__)
    need_post_dir = base_dir + '/need_post'
    readme_file = base_dir + '/README.md'
    os.chdir(need_post_dir)
    dir_list = traversalDir_FirstDir(need_post_dir)
    if type(dir_list) == None:
        logging.info("There is no new blog")
        exit()
    shell_command = ''
    for dir in dir_list:
        shell_command = "cd " + need_post_dir + " && python3 -m wordpress_markdown_blog_loader posts upload " + dir +" --host " + host_server
        p = subprocess.Popen(shell_command, stdout=subprocess.PIPE, shell=True)
        (output, err) = p.communicate()  
        p.wait(30)
        logging.info(output)
        if 'INFO: uploaded blog' in output:
            title_list = re.findall("uploaded\sblog\s'(.+?)'\sas", output)
            if len(title_list):
                title = title_list[0]
            link_list = re.findall("as\spost\s(.+?)\n", output)
            if len(link_list):
                link = link_list[0]
            logging.info(title + link)
            insert_info = href_info(title, link)
            insert_index_info_in_readme(readme_file, insert_info)
        shell_command1 = "mv -f " + need_post_dir + '/' + dir + ' ' + base_dir + '/' + 'posted'  + '/' + dir
        p1 = subprocess.Popen(shell_command1, stdout=subprocess.PIPE, shell=True)
        # upload([dir, '--host', DEFAULT_INFO['host']])
        # new_info = href_info(g_title, g_link)
        # print(new_info)
        
        # if g_new_post:
        #     insert_index_info_in_readme(new_info)
        # source_dir = need_post_dir + '/' + dir
        # posted_dir = base_dir + '/posted'

if __name__ == "__main__":
    main()
