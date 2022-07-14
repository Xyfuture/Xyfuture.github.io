from fileinput import filename
import os,sys
import datetime


front_matter_template = """---
title: ""
date: "{}"
draft: false
---
""".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def check_file_name(file_name):
    if '/' not in file_name:
        file_name = './posts/'+file_name
    
    if not file_name.endswith('.md'):
        file_name = file_name + '.md'

    return file_name
    


if __name__ == '__main__':
    default_file_name = "./posts/new_post.md"
    
    if len(sys.argv) == 2:
        default_file_name = sys.argv[1]
    
    file_name = check_file_name(default_file_name)

    if not os.path.exists(file_name):
        with open(file_name,'w') as f:
            f.write(front_matter_template)
    else:
        print("file already exists, create failed")


    

