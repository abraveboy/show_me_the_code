#第 0013 题： 用 Python 写一个爬图片的程序，爬http://tieba.baidu.com/p/2166231880里的图片

import re
import requests
import os

def get_page_url():
    return "http://tieba.baidu.com/p/2166231880"

def get_pics():
    request = requests.get(get_page_url())
    page = request.text

    pattern = "<img pic_type=\"0\" class=\"BDE_Image\" src=\"(.*?)\".*?>"
    return re.findall(pattern,page)

def save_pics():
    pic_num = 0
    for each in get_pics():
        pic = requests.get(each).content
        path = os.getcwd() + '\\0013'
        if not os.path.exists(path):
            os.mkdir(path)
        pic_name = '{}.jpg'.format(pic_num)
        print('from{} download {}'.format(each, pic_name))

        with open(path + '\\'+ pic_name, 'wb') as wb:
            wb.write(pic)
        pic_num +=1

if __name__ == '__main__':
    save_pics()
