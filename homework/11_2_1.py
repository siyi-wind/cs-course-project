"""
创建无向图，使用邻接列表的方式
所有的顶点组成一个列表，每个顶点的边组成一个单独的列表
ADT graph
顶点类
图类
"""

class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}  # 存储链接的顶点

    def addNeibor(self, nbr, weight):
        self.connectedTo[nbr] = weight

    def __str__(self):  # 这样可以使用print打印
        return str(self.id)+'connectedTo'+str([x.id for x in self.connectedTo])

    def getConnections(self):
        return self.connectedTo.keys()  # 返回连接的顶点

    def getId(self):
        return self.id

    def getWeight(self, nbr):  # 返回与某顶点之间的边值
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.verList = {}
        self.numVertices = 0  # 顶点个数

    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex

    def getVertex(self, n):  # 取顶点类
        if n in self.verList:
            return self.verList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, f, t, cost=0):  # 添加边
        if f not in self.verList:  # 若顶点不存在，先添加
            nv = self.addVertex(f)
        if t not in self.verList:
            nv = self.addVertex(t)
        self.verList[f].addNeibor(self.verList[t], cost)

    def getVertices(self):  # 取所有顶点
        return self.verList.keys()

    def __iter__(self):
        return iter(self.verList.values())


