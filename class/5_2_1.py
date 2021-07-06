"""
进制转换的递归方法
"""

def toStr(n, base): # 转2进制
    ConvertString = [str(i) for i in range(base)]
    if n < base: # 最小规模问题
        return ConvertString[n]
    else:
        return toStr(n//base, base)+ConvertString[n % base]

print(toStr(20, 10))

