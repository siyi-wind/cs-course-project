"""
最小生成树
解决广播问题  所有节点都要收到一次信息
选择具有最小权重的生成树
使用贪心算法 Prim  每次添加一条权重最小的可以添加的边（一端在树里，一端连外面的点）
"""

from pythonds.graphs import PriorityQueue, Graph, Vertex
import sys


def prim(G, start):
    pq = PriorityQueue()  # 建立优先队列
    for v in G:
        v.setDistance(sys.maxsize)
        v.setPred(None)
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in G])
    while not pq.isEmpty():
        current_vertex = pq.delMin()  # 取出当前距离最小的点
        for next_vertex in current_vertex.getConnections():
            new_cost = current_vertex.getWeight(next_vertex)  # current和next之间边的权重
            if next_vertex in pq and new_cost < next_vertex.getDistance():  # 确保加入的节点不再当前生成树里
                next_vertex.setPred(current_vertex)
                next_vertex.setDistance(new_cost)
                pq.decreaseKey(next_vertex, new_cost)
