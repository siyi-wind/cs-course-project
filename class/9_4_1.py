"""
使用链表实现二叉树
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.key = root_obj  # 根结点赋值
        self.left_child = None
        self.right_child = None

    def insertLeft(self, new_node):
        if self.left_child == None: # 左子树为空
            self.left_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.left_child = self.left_child
            self.left_child = t

    def insertRight(self, new_node):
        if self.right_child == None: # 左子树为空
            self.right_child = BinaryTree(new_node)
        else:
            t = BinaryTree(new_node)
            t.right_child = self.right_child
            self.right_child = t

    def getRightChild(self):
        return self.right_child

    def getLeftChild(self):
        return self.left_child

    def setRootVal(self, obj):
        self.key = obj

    def getRootVal(self):
        return self.key


r = BinaryTree('a')
r.insertLeft('b')
r.insertRight('c')
r.getRightChild().setRootVal('hello')
r.getLeftChild().insertRight('d')
print(r)
