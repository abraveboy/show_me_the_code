#**第 0004 题：**任一个英文的纯文本文件，统计其中的单词出现的个数。

from collections import Counter

def counter():
    with open('jane.txt') as wb:
        words = wb.read().split()

        return Counter(words)

if __name__ == '__main__':
    print(counter().most_common(10))
    #统计出现频率最高的10个词
