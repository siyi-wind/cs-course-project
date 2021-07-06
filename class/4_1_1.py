"""
构造一个队列
"""

class Queue:
    def __init__(self):
        self.items = [] # 存储队列   列表末是队首  列表第一项是队尾
    def isEmpty(self):
        return self.items == []
    def enqueue(self, item):
        self.items.insert(0, item)
    def dequeue(self):
        return self.items.pop()
    def size(self):
        return len(self.items)
