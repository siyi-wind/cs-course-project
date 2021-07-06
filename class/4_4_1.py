"""
打印任务 一个小时有20份作业 页数1-20页随机
模拟在不同的打印速度下 作业的平均等待时间
"""

from pythonds.basic.queue import Queue
import random
import matplotlib.pyplot as plt

random.seed(1)

class Printer: # 打印机类
    def __init__(self, ppm):
        self.pagerate = ppm # 打印机速度  x 页/分钟
        self.currentTask = None # 当前是否有任务
        self.timeRemaining = 0  # 当前任务的剩余打印时间

    def tick(self): # 模拟打印过程
        if self.currentTask:
            self.timeRemaining -= 1
            if self.timeRemaining <= 0:
                self.currentTask = None

    def busy(self):  # 返回打印机是否在忙
        if self.currentTask != None:
            return True
        else:
            return False

    def startNext(self, newtask):
        self.currentTask = True
        self.timeRemaining = newtask.getPages()*60/self.pagerate

class Task:  # 任务类
    def __init__(self, time):
        self.timestamp = time # 创建任务的时间戳
        self.pages = random.randrange(1, 21)

    def getStamp(self):
        return self.timestamp

    def getPages(self):
        return self.pages

    def waitTime(self, currentTime):
        return currentTime-self.timestamp # 开始打印的时间-创建任务的时间

def newPrintTask(): # 判断是否生成新的任务
    num = random.randrange(1, 181)
    if num == 180:   # 每秒钟有1/180的概率生成一个任务
        return True
    else:
        return False

def simulation(numSeconds, pagesPerMinute):  # 模拟器
    labprinter = Printer(pagesPerMinute)  # 创建打印机
    printQueue = Queue() # 创建打印队列
    waitingtimes = [] # 每项任务等待时间的记录表

    for currentSecond in range(numSeconds):
        if newPrintTask(): # 如果该秒有任务生成
            task = Task(currentSecond)
            printQueue.enqueue(task) # 加入打印队列

        if (not labprinter.busy()) and (not printQueue.isEmpty()): # 如果打印机不忙并且打印队列不为空
            nextTask = printQueue.dequeue()
            waitingtimes.append(nextTask.waitTime(currentSecond)) # 记录此作业的等待时间
            labprinter.startNext(nextTask) # 取出队首作业加入打印机


        labprinter.tick() # 打印一次

    return averageWaitTime(waitingtimes) # 返回平均等待时间

def averageWaitTime(waitingtimes):
    return sum(waitingtimes)/len(waitingtimes)


if __name__ == '__main__':
    rateList = [ 5, 6, 7, 8, 10, 11, 12, 13, 14, 15]
    waitingList = []
    for rate in rateList:
        time = simulation(36000, rate) # 每个速度运行十个小时 相当于10次运行一小时
        print(time/10, '\n')
        waitingList.append(time/10)

    plt.figure(1)
    plt.plot(rateList, waitingList)
    plt.show()

