"""
快速排序
随意取一个中值  中值后一位为左标，列表末尾是右标
     左标右移，遇到大于中值的停止
     右标左移，遇到小于中值的停止
     交换左右标的数据
继续移动，直到左标移到右标右侧
交换中值和右标的位置
此时中值左半部比中值小 右半部比中值大
"""

def quickSort(alist):
    quickSortHelper(alist, 0, len(alist)-1) # 找列表的首项和末项

def quickSortHelper(alist, first, last):
    if first < last:
        splitpoint = partition(alist, first, last)
        quickSortHelper(alist, first, splitpoint-1) # 排中值左边
        quickSortHelper(alist, splitpoint+1, last) # 排中值右边

def partition(alist, first, last): # 对列表进行分割 并返回中值的位置
    pivotvalue = alist[first] # 选定当前首项为中值

    leftmark = first+1 # 左右标初值
    rightmark = last
    done = False
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark+1
        while leftmark <= rightmark and alist[rightmark] >= pivotvalue:
            rightmark = rightmark-1
        if leftmark > rightmark: # 如果左标在右标的右侧
            done = True
        else: # 左右标数值交换
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    alist[first] = alist[rightmark]
    alist[rightmark] = pivotvalue

    return rightmark # 返回中值当前在的位置索引

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quickSort(alist)
print(alist)

