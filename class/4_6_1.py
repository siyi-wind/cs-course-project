"""
创建无序表的节点  使用链表的方式
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

class UnorderedList: # 无序表
    def __init__(self):
        self.head = None  # 表头

mylist = UnorderedList()

print(mylist.head)
