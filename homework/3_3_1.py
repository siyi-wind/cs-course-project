"""
通用括号匹配算法
"""

from pythonds.basic.stack import Stack

def matches(x1, x2):
    left = '({['
    right = ')}]'
    if left.index(x1) == right.index(x2):
        return True
    else:
        return False


def parChecker(symbolString):
    s = Stack()
    balanced = True
    index = 0
    while index < len(symbolString) and balanced:
        if symbolString[index] in '({[': # 如果是左括号 推入
            s.push(symbolString[index])
        else:                        # 如果是右括号
            if s.size() == 0:
                balanced = False  # 栈已空 说明右括号多了
            else:
                top = s.pop()  # pop出最顶的元素
                if not matches(top, symbolString[index]): # 比较左右括号是否匹配
                    balanced = False
        index += 1
    if balanced == True and s.isEmpty():
        return True
    else:
        return False

print(parChecker('{{([][])}()}'))
print(parChecker('[{()]'))





