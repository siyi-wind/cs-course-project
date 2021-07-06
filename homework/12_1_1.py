"""
通用的深度优先搜索
"""

from pythonds.graphs import Graph


class DFSGraph(Graph):
    def __init__(self):
        super().__init__()
        self.time = 0  # 增加一个time  记录当前时间

    def dfs(self):
        for a_vertex in self:  # 初始化所有点节点是白色
            a_vertex.setColor('white')
            a_vertex.setPred(-1)
        for a_vertex in self:
            if a_vertex.getColor() == 'white':  # 对还是白色的节点进行访问
                self.dfsvisit(a_vertex)

    def dfsvisit(self, startVertex):  # 创建单棵深度优先树
        startVertex.setColor('grey')  # 正在探索
        self.time += 1
        startVertex.setDiscovery(self.time)  # 记录开始时间
        for nextVetex in startVertex.getConnections():
            if nextVetex.getColor() == 'white':
                nextVetex.setPred(startVertex)
                self.dfsvisit(nextVetex)  # 递归调用
        startVertex.setColor('black')  # 探索完毕
        self.time += 1
        startVertex.setFinish(self.time)  # 记录结束时间
