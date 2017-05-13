"""做为 Apple Store App 独立开发者，你要搞限时促销，为你的应用生成激活码（或者优惠券），使用 Python 如何生成 200 个激活码（或者优惠券）？"""

import random
import string

chars = string.ascii_letters +string.digits

def act_code(arg):
    all_code = set()
    #采用集合，避免重复激活码
    while True:
        one_code = ''.join([random.choice(arg) for i in range(10)])
        #生成长度为10的随机激活码
        if len(all_code) ==200 :
            break
        else:
            all_code.add(one_code)
    return all_code

if __name__ == "__main__":
    with open('activation_code.txt','w') as wb:
        for code in act_code(chars):
            wb.write(code +'\n')
