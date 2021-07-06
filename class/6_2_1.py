"""
贪心算法解决硬币找零问题
尽可能少的给出硬币
"""
# 输入硬币种类coinList 和钱数money
# 记录硬币种类的字典 changeList  每种硬币作为key
# 循环从大到小取出硬币值，对钱进行取模运算 商存到字典的value n = money%coin
# money = money-n*coin
# 输出每一种硬币的个数



def FindChange(money, coinList):
    changeList = {} # 初始化找零字典
    for coin in coinList:
        n = money//coin # 硬币的个数
        changeList[coin] = n
        money = money-n*coin
    return changeList


coinList = [25, 10, 5, 1] # 硬币的种类 从大到小排序
money = int(input('输入需要找零的钱数'))
changeList = FindChange(money, coinList)
for k, v in changeList.items():
    print(k, ":", v, '\n')
