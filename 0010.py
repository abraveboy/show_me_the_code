#第 0010 题：使用 Python 生成类似于下图中的字母验证码图片

from PIL import Image,ImageDraw,ImageFont,ImageFilter
import random
import string

WIDTH ,HEIGH = 240, 60

def rnd_coulor_bg():
    return (random.randint(0, 127), random.randint(0, 127), random.randint(0, 127))

def rnd_coulor_code():
    return (random.randint(0,255), random.randint(0,255), random.randint(0,255))

def rnd_char():
    chars = string.ascii_letters + string.digits
    return random.choice(chars)

def font():
    return ImageFont.truetype("arial.ttf",size=50)

int_img = Image.new('RGB', (WIDTH, HEIGH), color=(255,255,255))
bg_img = ImageDraw.Draw(int_img)

for x in range(WIDTH):
    for y in range(HEIGH):
        bg_img.point((x,y),fill=rnd_coulor_bg())

for i in range(4):
    bg_img.text((WIDTH /4 *i ,0),
                text=rnd_char(),
                font=font(),
                fill=rnd_coulor_code())
int_img = int_img.filter(ImageFilter.BLUR)
#模糊背景

int_img.save('security_code_img.jpg')
#int_img.show()
