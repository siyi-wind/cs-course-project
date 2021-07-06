"""
写一个栈的类型
"""

class Stack:
    def __init__(self):
        self.items = []     # 建立一个栈

    def isEmpty(self): # 判断是否为空
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


s = Stack()
s.isEmpty()
s.push(4)
s.push('dog')
print(s.peek())
print(s.pop())
