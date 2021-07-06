"""
无序表的链表实现
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

    def add(self, item): # 使用头插法
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self): # 判断链表大小
        current = self.head # 从表头开始计数
        count = 0
        while current != None:
            count += 1
            current = current.getNext() # 将current移到下一个节点
        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self, item): # 注意要设置一个前节点
        current = self.head
        previous = None
        found = False
        while current != None and not found: # 寻找
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if found:
            if previous == None:  # 如果item是头节点
                self.head = current.setNext() # 把头节点更改为头节点后面一位
            else:
                previous.setNext(current.getNext()) # 如果是别的节点
            return True
        else:
            print('The moving object does not exist')

mylist = UnorderedList()
mylist.add(2)
mylist.add(3)
mylist.add(7)
mylist.add(8)
# print(mylist.size(), '\n')
# print(mylist.search(3), '\n')
# print(mylist.remove(7), '\n')
# print(mylist.size(), '\n')
print(mylist.remove(10), '\n')


