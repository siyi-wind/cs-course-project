"""
归并排序 n*log_2(n)
使用递归 先对二分的左右两个列表排序，然后对左右半部合并排序
"""
def mergeSort(alist):
    print('Splitting', alist)
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        # 合并操作
        i = j = k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i+1
            else:
                alist[k] = righthalf[j]
                j = j+1
            k = k+1
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            k = k+1
            i = i+1
        while j < len(righthalf):
            alist[k] = righthalf[j]
            k = k+1
            j = j+1
    print('merging', alist)

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergeSort(alist)
print(alist)
