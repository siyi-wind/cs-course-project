"""
最短路径问题
使用广度优先搜索  每个节点记录距离
每次出列距离最小的点
通过更新修改距离和父节点
"""
from pythonds.graphs import PriorityQueue, Graph, Vertex


def dijkstra(a_graph, start):  # dijkstra算法
    pq = PriorityQueue()  # 建立优先队列，存储点
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in a_graph])
    while not pq.isEmpty():  # 队列不为空时
        current_vertex = pq.delMin()  # 取出最小的点
        for next_vertex in current_vertex.getConnections():
            new_dist = current_vertex.getDistance()+current_vertex.getWeight(next_vertex)
            if new_dist < next_vertex.getDistance():  # 距离更小  更新
                next_vertex.setDistance(new_dist)
                next_vertex.setPred(current_vertex)
                pq.decreaseKey(next_vertex, new_dist)

