"""
使用二叉树对全括号表达式建立表达式解析树
使用表达式解析树求值
"""
from pythonds.trees.binaryTree import BinaryTree
from pythonds.basic.stack import Stack
import operator


# 建立表达式解析树
def buildParseTree(fpexp):
    f_split = fpexp  # 将表达式转换为列表
    tree_stack = Stack()  # 为了取父节点 造的栈
    exp_tree = BinaryTree('')  # 建立树
    tree_stack.push(exp_tree)
    current_tree = exp_tree

    for i in f_split:
        if i == '(':  # 表达式开始
            current_tree.insertLeft('')  # 创造左子节点
            tree_stack.push(current_tree)  # 入栈当前节点
            current_tree = current_tree.getLeftChild()  # 下降
        elif i not in ['+', '-', '*', '/', ')']:  # 操作数
            current_tree.setRootVal(int(i))  # 设定当前值
            parent = tree_stack.pop()  # 上升 取父节点
            current_tree = parent
        elif i in ['+', '-', '*', '/']:  # 操作符
            current_tree.setRootVal(i)  # 设定当前值
            current_tree.insertRight('')  # 创造右子节点
            tree_stack.push(current_tree)  # 入栈
            current_tree = current_tree.getRightChild()  # 下降
        elif i in [')']:  # 表达式结束
            current_tree = tree_stack.pop()
        else:
            raise ValueError

    return exp_tree


# 使用递归的方法
# 基本结束条件：没有左右子节点
# 缩小规模： 将表达式分为左右子树
# 调用自身
opers = {'+': operator.add, '-': operator.sub,
         '*': operator.mul, '/': operator.truediv}


def evaluate(parseTree):
    left_tree = parseTree.getLeftChild()
    right_tree = parseTree.getRightChild()
    if left_tree and right_tree:  # 如果左右子树不为空
        fn = opers[parseTree.getRootVal()]
        return fn(evaluate(left_tree), evaluate(right_tree))
    else:
        return parseTree.getRootVal()


# 9_7_1的方法 后序方法计算树
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


# 9_7_1的方法 由树恢复回全括号表达式
def print_exp(tree):
    sval = ''
    if tree:
        left_num = tree.getLeftChild()
        operator = tree.getRootVal()
        right_num = tree.getRightChild()
        if left_num and right_num:
            sval = '(' + print_exp(tree.getLeftChild())
            sval = sval + str(tree.getRootVal())
            sval = sval + print_exp(tree.getRightChild()) + ')'
        else:
            sval = str(tree.getRootVal())
    return sval


a = "((6-(5+(3*4)))/2)"
h = buildParseTree(a)
print(evaluate(h))
print(post_order_eval(h))
print(print_exp(h))

