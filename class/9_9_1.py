"""
二插堆实现
使用一个列表来保存堆数据，可以发现节点p的父节点索引为p//2，左节点为2p，右节点为2p+1
插入节点：插在尾部，然后上浮到合适的位置（与父节点比较大小并交换）
移去最小节点：return根结点的值并移走，然后将其赋值为最后一个节点，然后对该节点进行下沉
    （与子节点比较大小并交换位置） 如果比子节点大，选择较小的一个下沉，如果比两个子节点都小，则停止
建立二叉堆
"""

class BinHeap:
    def __init__(self):
        self.heap_list = [0]  # 不使用0索引
        self.current_size = 0

    def float_up(self, i):  # 上浮函数
        while i//2 > 0:  # 当i不是根结点的时候 就可以继续比较
            if self.heap_list[i] < self.heap_list[i//2]:  # 若当前节点比父节点小，则上浮
                temp = self.heap_list[i//2]
                self.heap_list[i//2] = self.heap_list[i]
                self.heap_list[i] = temp
            i = i//2  # i更新为它的父节点

    def insert(self, k):  # 向二叉堆插入k
        self.heap_list.append(k)  # 先插到末尾
        self.current_size = self.current_size+1
        self.float_up(self.current_size)  # 上浮最后一个数

    def min_child(self, i):  # 返回最小的子节点
        if (i*2+1) > self.current_size:  # 说明i只有一个子节点，直接返回
            return i*2
        else:  # 有两个节点的时候，比较大小
            if self.heap_list[2*i] < self.heap_list[2*i+1]:
                return 2*i
            else:
                return 2*i+1

    def sink_down(self, i):  # 下沉函数
        while i*2 < self.current_size:  # 当i没有子节点
            mc = self.min_child(i)  # 找最小子节点的索引
            if self.heap_list[i] > self.heap_list[mc]:
                temp = self.heap_list[mc]
                self.heap_list[mc] = self.heap_list[i]
                self.heap_list[i] = temp
            i = mc

    def del_min(self, k):  # 返回二叉堆中最小的数
        retval = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]  # 将根结点赋值为最后一个值
        self.heap_list.pop()  # 移除二叉堆列表最后一个值
        self.sink_down(1)  # 下沉
        return retval


