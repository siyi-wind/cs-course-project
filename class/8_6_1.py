"""
使用散列表构造字典结构
"""

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None]*self.size
        self.data = [None]*self.size

    def put(self, key, data): # 存一个键值对
        hashvalue = self.hashfunction(key)

        if self.slots[hashvalue] == None: # 如果没有冲突
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data # 更改值
            else:
                nextslot = self.rehash(hashvalue) # 重新找位置
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                elif self.slots[nextslot] == key:
                    self.data[nextslot] = data # 修改值

    def get(self, key): # 找一个键的值
        startslot = self.hashfunction(key)

        data = None
        stop = False
        found = False
        position = startslot

        while self.slots[position] !=  None and not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position)
                if position == startslot:  # 说明已经搜索到了开始点
                    stop = True

        return data

    def hashfunction(self, key):
        return key % self.size # 使用取余来计算散列值

    def rehash(self, oldhash): # 重新寻找散列值  往后推一位
        return (oldhash+1) % self.size

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)


map = HashTable()
map[22] = "dog"
map[10] = "cat"
map[6] = "eager"
map[33] = "wolf"
print(map[6])
print(map[44])

