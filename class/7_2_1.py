"""
二分查找算法
针对有序表
每次将item和中间的元素进行比对
item更小则找左边 大则找右边
"""

def binarySearch(alist, item):
    first = 0
    last = len(alist)-1
    found = False

    while first <= last and not found:
        midpoint = (last+first)//2
        if alist[midpoint] == item:
            found = True
        elif item < alist[midpoint]:
            last = midpoint-1
        else:
            first = midpoint+1
    return found


# 使用递归解法
def RecursiveBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        midpoint = len(alist)//2
        if item == alist[midpoint]:
            return True
        elif item < alist[midpoint]: # 所以查找前半部分
            return RecursiveBinarySearch(alist[: midpoint], item)
        else:
            return RecursiveBinarySearch(alist[midpoint+1 :], item)


testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
# print(binarySearch(testlist, 17))
print(RecursiveBinarySearch(testlist, 3))
