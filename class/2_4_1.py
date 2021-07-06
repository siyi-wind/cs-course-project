"""
变位词判断
"""

def anagramSolution4(s1, s2):
    """
    计数比较 给s1 s2两个列表的字母进行计数  最后比较26个字母计数是否相同  n
    :param s1: 字符串
    :param s2: 字符串
    :return: 判断是否为变位词
    """
    c1 = [0]*26 # 计数用的表
    c2 = [0]*26
    for i in range(len(s1)):
        pos1 = ord(s1[i])-ord('a')  # 算出是第几个字母  ord是取编码
        c1[pos1] = c1[pos1]+1
    for i in range(len(s2)):
        pos2 = ord(s2[i])-ord('a')
        c2[pos2] = c2[pos2]+1

    stillOK = True
    j = 0
    while j<26 and stillOK:
        if c1[j] == c2[j]:
            j += 1
        else:
            stillOK = False

    return stillOK

print(anagramSolution4('aacd', 'cada'))
