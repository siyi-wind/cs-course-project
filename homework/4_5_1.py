"""
建立双端队列 首尾都可以移除和添加
列表末是队首
"""

class Dequeue:
    def __init__(self):
        self.items = [] # 存储
    def addFront(self, item):
        self.items.append(item)
    def addRear(self, item):
        self.items.insert(0, item)
    def removeFront(self):
        return self.items.pop()
    def removeRear(self):
        return self.items.pop(0)
    def isEmpty(self):
        return self.items == []
    def size(self):
        return len(self.items)
