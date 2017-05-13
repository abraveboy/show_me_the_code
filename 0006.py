#**第 0006 题：**你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。

import os,os.path
import glob
from collections import Counter

def txt_dir():
    #返回文件夹路径
    return os.path.join(os.getcwd(),'0006')

def counter(imp_word,n=None):
    #得出关注单词的次数，或者得出出现最多的n个词
    cont_word = Counter()
    total = 0
    for file in glob.glob(txt_dir() +'\*.txt'):
        with open(file) as fb:
            for line in fb:
                total +=len(line.strip().split())
                cont_word += Counter(line.strip().split())
    # print(sum(cont_word.values()),total)
    print(cont_word[imp_word])
    if n:
        print(cont_word.most_common(n))

if __name__=="__main__":
    counter('food',10)
