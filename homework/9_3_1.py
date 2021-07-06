"""
使用嵌套列表法实现二叉树结构
对于中间节点 [root, left, right]
对于叶节点 [root, [], []]
"""

def BinaryTree(r):
    return [r, [], []] # 【根结点，左子树，右子树】

# 插入左子树
def insertLeft(root, newBranch):
    t = root.pop(1) # 得到左子树
    if len(t) > 1: # t不为空
        root.insert(1, [newBranch, t, []])
    else: # t为空表
        root.insert(1, [newBranch, [], []])
    return root

# 插入右子树
def insertRight(root, newBranch):
    t = root.pop(2) # 得到左子树
    if len(t) > 1: # t不为空
        root.insert(2, [newBranch, [], t])
    else: # t为空表
        root.insert(2, [newBranch, [], []])
    return root

# 取根结点
def getRootVal(root):
    return root[0]

# 设置根结点值
def setRootVal(root, newVal):
    root[0] = newVal

# 取左子树
def getLeftChild(root):
    return root[1]

# 取右子树
def getRightChild(root):
    return root[2]

r = BinaryTree(3)
insertLeft(r, 4)
insertLeft(r, 5)
insertLeft(r, 4)
insertRight(r, 6)
insertRight(r, 7)
print(r)
