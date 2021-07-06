"""
归并排序 更简洁的写法
"""

def merge_sort(alist):
    # 递归结束条件
    if len(alist) <= 1:
        return alist

    # 分解问题 递归调用
    middle = len(alist) // 2
    left = merge_sort(alist[:middle])
    right = merge_sort(alist[middle:])

    # 合并左右部分
    merged = []
    while left and right: # 左和右不为0
        if left[0] <= right[0]:
            merged.append(left.pop(0))
        else:
            merged.append(right.pop(0))
    merged.extend(right if right else left) # 合并多的项
    return merged

alist = [54, 26, 93, 17, 77, 31, 44, 55, 20]
sort_list = merge_sort(alist)
print(sort_list)



