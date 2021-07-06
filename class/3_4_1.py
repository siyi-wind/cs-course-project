"""
十进制转为16进制以下的任意进制
"""
from pythonds.basic.stack import Stack

def baseConvert(decNumber, base):
    remStack = Stack()  # 记录的栈
    digits = '0123456789ABCDEF'  # 用于进制的字母

    while decNumber > 0: # 整除法
        rem = decNumber % base
        remStack.push(rem)
        decNumber = decNumber // base

    remstring = ""
    while not remStack.isEmpty():  # 反转
        remstring = remstring+digits[remStack.pop()]

    return remstring

print(baseConvert(25, 2))
