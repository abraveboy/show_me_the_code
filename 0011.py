#第 0011 题： 敏感词文本文件 filtered_words.txt，里面的内容为以下内容，当用户输入敏感词语时，则打印出 Freedom，否则打印出 Human Rights。
import glob

filter = glob.glob('f*.txt')[0]

filter_words =[]

with open(filter) as wb:
    for line in wb:
        filter_words.append(line.strip())

def judge(word):
    return word in filter_words
if __name__ == '__main__':
    words = input('input:')
    if judge(words):
        print('Freedom')
    else:
        print("Humen Rights")
