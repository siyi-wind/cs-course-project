"""
动态规划解决找零问题的扩展算法
需要得出每种硬币的个数
在生成最优列表的同时跟踪记录所选硬币的币值
得到最后的解后，减去选择的硬币币值，回溯到表格之前的部分找零
"""

def dpMakeChange(coinValueList, change, minCoins, coinUsed):
    for cents in range(1, change+1):
        coinCount = cents
        newCoin = 1 # 初始化一下新加的硬币
        for j in [c for c in coinValueList if c <= cents]: # 遍历每种硬币 找到使当前的找零最优的加一个硬币的方法
            if minCoins[cents-j]+1 < coinCount:
                coinCount = minCoins[cents-j]+1
                newCoin = j # 对应最小数量 所减的硬币
        minCoins[cents] = coinCount
        coinUsed[cents] = newCoin  # 记录本找零加的最后一个硬币种类
    return minCoins[change]

def printCoins(coinUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinUsed[coin]
        print(thisCoin)
        coin = coin-thisCoin

amnt = 63
clist = [1, 5, 10, 21, 25]
coinUsed = [0]*(amnt+1)
coinCount = [0]*(amnt+1)

print('Making chage for', amnt, 'requires')
print(dpMakeChange(clist, amnt, coinCount, coinUsed), 'coins')
print("They are:")
printCoins(coinUsed, amnt)
print('The used list is as follows:')
print(coinUsed)

