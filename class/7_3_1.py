"""
冒泡排序
复杂度 n**
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1, 0, -1): # 比较的趟数n-1 - 0
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i], alist[i+1] = alist[i+1], alist[i]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(alist)
print(alist)
