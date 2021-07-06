"""
动态规划解决找零问题
"""

def dpMakeChange(coinValueList, change, minCoins):
    # 从1开始逐个计算最少硬币数
    for cents in range(1, change+1):
        # 初始化一个最大值
        coinCount = cents
        # 减去每个硬币 向后查最少硬币数  同时记录总的最少数
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] +1 < coinCount: # 如果新算出的硬币数小于之前的
                coinCount = minCoins[cents-j]+1 # 存储最少的数量
        minCoins[cents] = coinCount # 遍历完以后把最小的次数附给当前找零值

    return minCoins[change]


print(dpMakeChange([1, 5, 10, 21, 25], 63, [0]*64))
