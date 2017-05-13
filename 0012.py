#第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」

import glob
import string

filter = glob.glob('f*.txt')[0]

filter_words =[]

with open(filter) as wb:
    for line in wb:
        filter_words.append(line.strip())

def judge(words):
    for mask in filter_words:
        if mask in words:
            words = words.replace(mask,'*'*len(mask))
    return words


if __name__ == '__main__':
    # print(filter_words)
    words = input('input:')
    print(judge(words))
