"""
词梯问题
一个单词演变成另一个单词，每一步只能变一个字母
先建立单词图 只相差一个字母的单词有边相连
    创建大量的桶，每个桶可以存放若干单词，桶的标记是去掉一个字母，使用_占空
    所有匹配标记的单词都放在一个桶
    所有单词变成顶点后，对同一个桶中的单词建立边
然后使用广度优先搜索寻找最短路径
"""

from pythonds.graphs.adjGraph import Graph
from pythonds.basic.queue import Queue

word_file = 'fourletterwords.txt'


def build_graph(word_file):
    d = {}  # 桶的集合
    g = Graph()  # 单词图
    with open(word_file, 'r') as f:
        for line in f:
            word = line[:-1]
            for i in range(len(word)):  # 给单词加下划线，并归到不同的桶
                bucket = word[:i]+'_'+word[i+1:]
                if bucket in d:
                    d[bucket].append(word)
                else:
                    d[bucket] = [word]
        for bucket in d.keys():  # 添加边
            for word1 in d[bucket]:
                for word2 in d[bucket]:
                    if word1 != word2:
                        g.addEdge(word1, word2)
    f.close()

    return g


#  广度优先搜索
def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()  # 目前需要探索的顶点队列
    vertQueue.enqueue(start)  # 将起始点放入队列
    while vertQueue.size() > 0:  # 队列不为空时
        current_vert = vertQueue.dequeue()  # 取出一个顶点
        for nbr in current_vert.getConnections():
            if nbr.getColor() == 'white':  # 白色说明还没有探索过
                nbr.setColor('gray')  # 设置为准备探索
                nbr.setDistance(current_vert.getDistance()+1)  # 设置距离
                nbr.setPred(current_vert)  # 设置前驱节点
                vertQueue.enqueue(nbr)  # 将新发现的节点入队
        current_vert.setColor('black')  # 遍历完后将当前节点设为已探索


# 回溯节点  找到最短词梯
def traverse(y):
    x = y
    while x.getPred():
        print(x.getId())
        x = x.getPred()
    print(x.getId())


word_graph = build_graph(word_file)  # 生成单词图
# print(word_graph.getVertex('FOOL'))
bfs(word_graph, word_graph.getVertex('FOOL'))  # 广度搜索
traverse(word_graph.getVertex('NONE'))  # 打印词梯
