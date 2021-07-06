"""
骑士周游问题
按照走日字的方法，不重复的走完国际象棋的64个格子 每个格子走一次
先将合法走棋次序变成一个图
使用深度优先搜索算法找到长度为 row*col-1 长度的路径，路径上每个顶点出现一次
"""
from pythonds.graphs.adjGraph import Graph


#  合法走棋的走法
def gen_legal_move(x, y, bd_size):  # x列，y行，bdsize是棋盘宽度
    new_move = []
    move_offsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1),
                    (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in move_offsets:
        new_x = x+i[0]
        new_y = y+i[1]
        if legal_cood(new_x, bd_size) and legal_cood(new_y, bd_size):
            new_move.append((new_x, new_y))
    return new_move


#  检查走棋是否在棋盘内
def legal_cood(x, bdsize):
    if 0 <= x < bdsize:
        return True
    else:
        return False


# 构建走棋关系图
def knight_graph(bdsize):
    kt_graph = Graph()  # 建立空图
    for row in range(bdsize):
        for col in range(bdsize):
            node_id = pos2node_id(row, col, bdsize)  # 转化为id
            new_positions = gen_legal_move(row, col, bdsize)  # 产生新位置
            for e in new_positions:
                nid = pos2node_id(e[0], e[1], bdsize)
                kt_graph.addEdge(node_id, nid)
    return kt_graph


# 将行列转换为唯一的id
def pos2node_id(row, col, bdsize):
    return row*bdsize+col


# 深度优先搜索算法 n为层次，path为已经加入的路径，u为当前顶点，limit为搜索总深度
def knight_tour(n, path, u, limit):
    u.setColor('grey')  # 准备搜索
    path.append(u)
    if n < limit:  # 需要继续搜索
        nbr_list = list(u.getConnections())  # 周围合法移动
        i = 0
        done = False
        while i < len(nbr_list) and not done:
            if nbr_list[i].getColor() == 'white':  # 有新节点
                done = knight_tour(n+1, path, nbr_list[i], limit)
            i = i+1
        if not done:  # 说明该节点不通，往上回溯
            path.pop()
            u.setColor('white')
    else:
        done = True
    return done


kt_graph = knight_graph(6)
path = []
knight_tour(1, path, kt_graph.getVertex(5), 36)
count = 0
for k in path:
    print(k.id)
    count += 1
print(count)












