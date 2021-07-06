"""
实现有序表  从小到大的顺序排列
"""

class Node:
    def __init__(self, initdata):
        self.data = initdata # 初始赋值
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class OrderedList:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head
        stop = False # 当item比当前节点小  说明后面也不可能有item  停止搜索
        found = False
        while current != None and (not stop) and (not found):
            if current.getData() == item:
                found = True
            elif current.getData() > item:
                stop = True
            else:
                current = current.getNext()
        return found


    def add(self, item):
        current = self.head
        previous = None
        stop = False # 找到位置
        while current != None and not stop:
            if current.getData() > item:
                stop = True
            else:
                previous = current
                current = current.getNext() # 往后移

        temp = Node(item) # 把对象存到节点
        if previous == None:  # 即对象要放在头节点
            temp.setNext(self.head) # 当前头节点放到对象后面
            self.head = temp
        else:
            temp.setNext(current) # 插入到表中
            previous.setNext(temp)

    def isEmpty(self):
        return self.head == None



