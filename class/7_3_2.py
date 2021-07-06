"""
改进版的冒泡排序
当一趟比较中 没有元素交换
则说明排序完成，直接停止
复杂度与冒泡排序相同
"""

def shortBubbleSort(alist):
    exchange = True
    passnum = len(alist)-1
    while passnum > 0 and exchange:
        exchange = False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                exchange = True
                alist[i], alist[i+1] = alist[i+1], alist[i]

        passnum = passnum-1

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shortBubbleSort(alist)
print(alist)
