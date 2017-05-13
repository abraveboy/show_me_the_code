#**第 0005 题：**你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

from PIL import Image
import glob
import os,os.path

IP5_WIDTH = 1366
IP5_HEIGH = 640

def get_pic(path):
    return glob.glob(path)

def save_pic_path(dirname):
    return os.getcwd() + '\\' +dirname

def change_size(pics,dir):
    for pic in pics:

        new_pic = Image.open(pic).resize((IP5_WIDTH, IP5_HEIGH))
        name = os.path.basename(pic)
        print('Modifing {} save...'.format(name))
        new_pic.save(os.path.join(save_pic_path(dir), name))

def creat_dir(dpath):
    #在工作文件夹下创建一个文件夹
    dir = save_pic_path(dpath)
    if os.path.isdir(dir):
        #若文件夹存在则清空
        for file in glob.glob(dir+ '\*.*'):
            os.remove(file)
        print('remove all,{} is empty'.format(dpath))
    else:
        os.mkdir(dirpath)
        print('create {} successful'.format(dir))

if __name__ == '__main__':
    creat_dir('IP5')
    change_size(get_pic('F:\自定义桌面壁纸\新建文件夹\*.jpg'), 'IP5')
