"""
插入排序 n**
把后面的项一项一项地插入到前面排好地序列中
由小到达排序
"""

def insertionSort(alist):
    for index in range(1, len(alist)):  # [1, n)
        currentvalue = alist[index]  # 需要插入的项
        position = index  # 记录位置

        while position > 0 and alist[position-1] > currentvalue:  # 如果前一项比后面的项大 把前一项赋到后面
            alist[position] = alist[position-1]  # 大的项往后移
            position = position-1

        alist[position] = currentvalue

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
insertionSort(alist)
print(alist)

