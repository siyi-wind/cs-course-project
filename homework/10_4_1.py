"""
AVL树 这是一种平衡树
每次插入key时，都会调整树的结构使其保持为平衡二叉树
每个节点都有平衡因子bf=左子树高度-右子树高度
如果bf>0说明左重，小于说明右重
如果bf在-1到1之间，称为平衡树
调整方法：
左重：如果左子节点右重，先左旋左子节点，再右旋当前节点
右重：如果右子节点左重，先右旋右子节点，再左旋当前节点
"""

from pythonds.trees.bst import BinarySearchTree, TreeNode

class AVLTree(BinarySearchTree):
    # 重新定义_put方法
    def _put(self, key, val, current_node):
        if key < current_node.key:  # 放左子树
            if current_node.hasLeftChild():  # 已有左子节点
                self._put(key, val, current_node.leftChild)
            else:
                current_node.leftChild = TreeNode(key, val, parent=current_node)
                self.updateBalance(current_node.leftChild)  # 对树重新进行平衡
        else:  # 放右子树
            if current_node.hasRightChild():  # 已有右子节点
                self._put(key, val, current_node.leftChild)
            else:
                current_node.rightChild = TreeNode(key, val, parent=current_node)
                self.updateBalance(current_node.rightChild)  # 对树重新进行平衡

    def updateBalance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:  # 出现不平衡
            self.rebalance(node)  # 进行平衡
            return
        if node.parent != None:  # 平衡因子的更新是否传递
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1

            if node.parent.balanceFactor != 0:  # 平衡因子为0后不需要继续更新
                self.updateBalance(node.parent)  # 继续向上传递调整

    def rebalance(self, node):
        if node.balanceFactor < 0:  # 当前节点右重
            if node.rightChild.balanceFactor > 0:  # 右子节点左重
                self.rotateRight(node.rightChild)  # 先右旋右子节点
                self.rotateLeft(node)  # 再左旋当前节点
            else:
                self.rotateLeft(node)
        elif node.balanceFactor > 0:  # 当前节点左重
            if node.leftChild.balanceFactor < 0:  # 左子节点右重
                self.rotateLeft(node.leftChild)  # 先左旋左子节点
                self.rotateRight(node)  # 右旋当前节点
            else:
                self.rotateRight(node)

    def rotateLeft(self, rotRoot):  # 左旋
        newRoot = rotRoot.rightChild  # 以当前节点的右子节点作为新的中间节点
        rotRoot.rightChild = newRoot.leftChild  # 右子节点的左子节点变为当前节点的右子节点
        if newRoot.leftChild != 0:
            newRoot.leftChild.parent = rotRoot
        newRoot.parent = rotRoot.parent

        if rotRoot.isRoot():  # 如果当前节点是根结点
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():  # 当前节点是左节点
                rotRoot.parent.leftChild = newRoot
            else:  # 当前节点是右节点
                rotRoot.parent.rightChild = newRoot
        newRoot.leftChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor+1-min(newRoot.balanceFactor, 0)  # 计算方法看课件
        newRoot.balanceFactor = newRoot.balanceFactor+1+max(rotRoot.balanceFactor, 0)

    def rotateRight(self,rotRoot):
        newRoot = rotRoot.leftChild
        rotRoot.leftChild = newRoot.rightChild
        if newRoot.rightChild != None:
            newRoot.rightChild.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isRightChild():
                rotRoot.parent.rightChild = newRoot
            else:
                rotRoot.parent.leftChild = newRoot
        newRoot.rightChild = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor - 1 - max(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor - 1 + min(rotRoot.balanceFactor, 0)
