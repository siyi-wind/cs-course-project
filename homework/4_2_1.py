"""
约瑟夫问题  或 热土豆问题
参加游戏一群人，每次传递num次停下的人除去 继续传直到只剩一个人
"""

from pythonds.basic.queue import Queue
def hotPotato(namelist, num):
    simqueue = Queue()  # 创建队列
    for name in namelist:
        simqueue.enqueue(name) # 把人名加入队列

    while simqueue.size() > 1:
        for i in range(num): # 一次游戏
            simqueue.enqueue(simqueue.dequeue())  # 把队首的元素放到队伍后为一次传递
        simqueue.dequeue() # 把拿到土豆的人去掉

    return simqueue.dequeue() # 输出最后剩下的那个人

print(hotPotato(['Bill', 'David', 'Susan', 'Jane', 'Kent', 'Brad'], 7))
