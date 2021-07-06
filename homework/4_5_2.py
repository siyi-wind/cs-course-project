"""
使用双端队列判断回文词
两端同时移除字符判断是否相同，知道deque中剩下0或1个字符
"""

from pythonds.basic.deque import Deque

def palchecker(aString):
    charDeque = Deque() # 创建双端队列

    for i in aString:
        charDeque.addRear(i) # 将字符串中的字符加入到队列中

    stillEqual = True
    while charDeque.size() > 1 and stillEqual:
        first = charDeque.removeFront()
        last = charDeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palchecker('radar'))
print(palchecker('lsdkjfskf'))
