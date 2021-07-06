"""
谢尔排序 2^(3/2) 从小到大排列
每次对一定间隔的项进行排序
间隔逐渐减小
最后能够在间隔为1时 仅动少量的项
"""
def shellSort(alist):
    sublistcount = len(alist) // 2  # 间隔设定
    while sublistcount > 0:
        for startposition in range(sublistcount):  # 对子列表进行排序  移动开始的位置
            gapInsertionSort(alist, startposition, sublistcount)
        print('after increments of size', sublistcount, 'this list is', alist)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist, start, gap):
    for i in range(start+gap, len(alist), gap):
        currentvalue = alist[i]  # 需要插入的值
        position = i
        while position > 0 and alist[position-gap] > currentvalue:
            alist[position] = alist[position-gap]
            position = position-gap

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shellSort(alist)
print(alist)


