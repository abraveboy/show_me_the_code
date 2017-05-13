"""**第 0000 题：**将你的 QQ 头像（或者微博头像）右上角加上红色的数字，类似于微信未读信息数量那种提示效果。"""

from PIL import Image,ImageFont,ImageDraw

#设置字体
def font():
    return ImageFont.truetype('arial.ttf',size=40)

#设置数字填充位置
def size(arg):
    width, heigh = arg.size
    return width-40 ,0


portrait = Image.open('head_portrait.jpg')

#创建图像的写对象，进行编辑
img = ImageDraw.Draw(portrait)
img.text(size(portrait), '4' ,fill='red' ,font=font())

#保存增加消息数后的头像
portrait.save('messages_head_ptt.jpg')
# portrait.show()
