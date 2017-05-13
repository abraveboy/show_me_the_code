#**第 0007 题：**有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。

import os,os.path
from collections import Counter

total = 0
blank = 0
annotations = 0


def get_code_dirpath():
    return "F:\python3\py3_work\.idea\show_me_the_code"

def counter_code():
    global total
    global blank
    global annotations
    #用全局变量申明

    for prgm in os.listdir(get_code_dirpath()):
        file = get_code_dirpath()+'\\' +prgm
        ext = os.path.splitext(prgm)[1]
        if ext =='.py':
            #print('now conter {}...'.format(prgm))
            with open(file,encoding='utf8') as wb:
                for line in wb:
                    if line.strip() =='':
                        blank +=1
                    elif line.strip()[0] =='#' or line[0]=="\"":
                        #必须要排除空行，不然空行[0]会报错
                        annotations +=1
                    total +=1
    return total, blank, annotations

if __name__ == '__main__':
    counter_code()
    print("共计{}行，空行{}行，注释{}行".format(total, blank, annotations))