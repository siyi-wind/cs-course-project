"""
树的遍历方法  递归
前序： 根，左子树，右子树
中序：左子树，根，右子树
后序：左子树，右子树，根
"""
from pythonds.trees.binaryTree import BinaryTree
import operator


# 前序
def preorder(tree):
    if tree:
        print(tree.getRootVal())
        preorder(tree.getLeftChild())
        preorder(tree.getRightChild())


# 中序
def inorder(tree):
    if tree != None:
        inorder(tree.getLeftChild())
        print(tree.getRootVal())
        inorder(tree.getRightChild())


# 后序
def postorder(tree):
    if tree != None:
        postorder(tree.getLeftChild())
        postorder(tree.getRootVal())
        print(tree.getRootVal())


# 使用后序遍历来对表达式求值
opers = {'+': operator.add, '-': operator.sub,
         '*': operator.mul, '/': operator.truediv}


def post_order_eval(tree):
    res1 = None
    res2 = None
    if tree:
        res1 = post_order_eval(tree.getLeftChild())
        res2 = post_order_eval(tree.getRightChild())  # 取左右两子树的值
        if res1 and res2:  # 如果1 2有值  取出根结点进行计算
            return opers[tree.getRootVal()](res1, res2)
        else:
            return tree.getRootVal()


# 中序遍历生成全括号表达式

def print_exp(tree):
    sval = ''
    if tree:
        sval = '(' + str(print_exp(tree.getLeftChild()))
        sval = sval + str(print_exp(tree.getRootVal()))
        sval = sval + str(print_exp(tree.getRightChild()))
    return sval














