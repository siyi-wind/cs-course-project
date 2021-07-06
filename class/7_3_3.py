"""
选择排序
比较元素后只记录索引，每趟得到最大值的索引，然后将该元素与本趟最后一项交换
比对次数 n** 交换次数 n
"""

def selectionSort(alist):
    for fillslot in range(len(alist)-1, 0, -1):
        positionMax = 0
        for location in range(1, fillslot+1):
            if alist[location] > alist[positionMax]:
                positionMax = location
        alist[positionMax], alist[fillslot] = alist[fillslot], alist[positionMax]

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
selectionSort(alist)
print(alist)
