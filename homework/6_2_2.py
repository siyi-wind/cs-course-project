"""
用递归解决找零问题
"""
def recDC(coinValueList, change, knowResults):
    """
    :param coinValueList: 硬币种类列表
    :param change:  需要找零的钱
    :param knnowResults:  存储中间部分找零的最优解
    :return: 最少的硬币数
    """
    minCoins = change
    if change in coinValueList: # 递归结束条件 找零钱数=硬币币值
        knowResults[change] = 1 # 记录最优解
        return 1
    elif knowResults[change] > 1: # 已经计算过最优值
        return knowResults[change]
    else:
        for i in [c for c in coinValueList if c < change]: # 排除比找零大的币值
            numCoins = 1+recDC(coinValueList, change-i, knowResults)
            if numCoins < minCoins:
                minCoins = numCoins
            knowResults[change] = minCoins
    return minCoins

print(recDC([1, 5, 10, 21, 25], 64, [0]*70))
