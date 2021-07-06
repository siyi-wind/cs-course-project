"""
变位词判断
"""

def anagramSolution1(s1, s2):
    """
    逐字检查的方法  将s1的字符逐个取出  去s2里进行对比  n*n
    :param s1: 字符串1
    :param s2: 字符串2
    :return: 返回判断结果
    """
    alist = list(s2)  # 因为字符串不能改变 所以复制到列表
    pos1 = 0 # 记录列表1的检查位置
    stillOK = True   # 变位词判断结果
    while pos1<len(s1) and stillOK:
        pos2 = 0  # 记录2的检查位置
        Found = False
        while pos2<len(alist) and not Found:
            if s1[pos1] == alist[pos2]:
                Found = True  # 找到了
            else:
                pos2 += 1  # 没找到继续找
        if Found:
            alist[pos2] = None
            pos1 += 1
        else:
            stillOK = False
    return stillOK


def anagramSolution2(s1, s2):
    """
    逐字检查的方法  将s1的字符逐个取出  去s2里进行对比  找到相同的字符就在s2里面删掉  nlog(n)
    :param s1: 字符串1
    :param s2: 字符串2
    :return: 返回判断结果
    """
    alist = list(s2)  # 因为字符串不能改变 所以复制到列表
    pos1 = 0 # 记录列表1的检查位置
    stillOK = True   # 变位词判断结果
    while pos1<len(s1) and stillOK:
        pos2 = 0  # 记录2的检查位置
        Found = False
        while pos2<len(alist) and not Found:
            if s1[pos1] == alist[pos2]:
                Found = True  # 找到了
            else:
                pos2 += 1  # 没找到继续找
        if Found:
            del alist[pos2]  # 删掉找到的那个数
            pos1 += 1
        else:
            stillOK = False
    return stillOK

print(anagramSolution1('aacd', 'cada'))
