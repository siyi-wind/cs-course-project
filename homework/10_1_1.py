"""
二叉查找树的实现
比父节点小的都在左子树，比父节点大的key都在右子树
类BST表示二叉树  TreeNode表示一个节点  BST的root引用根结点TreeNode
"""


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key, val):  # 插入一个键值对
        if self.root:  # 如果树不为空
            self._put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)
        self.size += 1

    def _put(self, key, val, current_node):  # put的辅助方法
        if key < current_node.key:  # 插入左子树
            if current_node.hasLeftChild():  # 已有左子节点
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
        else:  # 插入右子树
            if current_node.hasRightChild():  # 已有右子节点
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)

    def __setitem__(self, key, value):  # 这样就不需要调用Put方法，而直接使用mytree[1] = 'red'来赋值
        self.put(key, value)

    def get(self, key):  # 取某个key的值
        if self.root:  # 树不为空
            res = self._get(key, self.root)
            if res:  # 如果树中有该Key
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key, current_node):
        if not current_node:  # 找遍整个树都没有key
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:  # 继续找左子树
            return self._get(key, current_node.left_child)
        else:  # 继续找右子树
            return self._get(key, current_node.right_child)

    def __getitem__(self, key):  # 这样就不用get方法，直接使用mytree[3]来得到值
        return self.get(key)

    def __contains__(self, key):  # 这样可以直接使用key in mytree来得到该key是否在树里
        if self._get(key, self.root):
            return True
        else:
            return False

    def __iter__(self):  # 迭代输出节点
        return self.root.__iter__()

    def delete(self, key):  # 删除一个节点
        if self.size > 1:  # 不是只有根结点
            node_to_remove = self._get(key, self.root)  # 先找到要移除的节点
            if node_to_remove:  # 找到了
                self.remove(node_to_remove)  # 移除节点
                self.size -= 1
            else:
                raise KeyError('Error, key not in tree')
        elif self.size == 1 and self.root.key == key:  # 要删除的节点是根结点
            self.root = None
            self.size -= 1
        else:
            raise KeyError('Error, key not in tree')

    def __delitem__(self, key):  # 这样就不用调用delete 直接用del mytree[3]来删除
        self.delete(key)

    def remove(self, current_node):
        if current_node.isLeaf():  # 该节点没有子节点，直接移除
            if current_node  == current_node.parent.left_child:  # 该节点是左子节点
                current_node.parent.left_child = None
            else:  # 该节点是右子节点
                current_node.parent.right_child = None
        elif current_node.hasBothChildren():  # 有两个子节点
            succ = current_node.findSuccessor()  # 寻找后继节点（右子树中key最小的节点  这个节点要么是叶节点，要么只有右子树）
            succ.spliceOut()  # 删除该节点
            current_node.key = succ.key
            current_node.payload = succ.payload
        else:  # 只有一个子节点
            if current_node.hasLeftChild():  # 有左子节点
                if current_node.isLeftChild():  # 本身是左子节点
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.left_child
                elif current_node.isRightChild():  # 本身是右子节点
                    current_node.left_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.left_child
                else:   # 本身是根结点
                    current_node.replaceNodeData(current_node.left_child.key,
                                                 current_node.left_child.payload,
                                                 current_node.left_child.left_child,
                                                 current_node.left_child.right_child)
            else:  # 有右子节点
                if current_node.isLeftChild():  # 本身是左子节点
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.left_child = current_node.right_child
                elif current_node.isRightChild():  # 本身是右子节点
                    current_node.right_child.parent = current_node.parent
                    current_node.parent.right_child = current_node.right_child
                else:  # 本身是根结点
                    current_node.replaceNodeData(current_node.right_child.key,
                                                 current_node.right_child.payload,
                                                 current_node.right_child.left_child,
                                                 current_node.right_child.right_child)


class TreeNode:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.payload = val  # 值
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def hasLeftChild(self):
        return self.left_child

    def hasRightChild(self):
        return self.right_child

    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        return self.parent and self.parent.right_child == self

    def isRoot(self):
        return not self.parent

    def isLeaf(self):
        return not (self.left_child or self.right_child)

    def hasAnyChildren(self):
        return self.left_child or self.right_child

    def hasBothChildren(self):
        return self.left_child and self.right_child

    def replaceNodeData(self, key, val, lc, rc):
        self.key = key
        self.payload = val
        self.left_child = lc
        self.right_child = rc
        if self.hasLeftChild():
            self.left_child.parent = self
        if self.hasRightChild():
            self.right_child.parent = self
        return

    def __iter__(self):
        if self:  # 当前节点不为空
            if self.hasLeftChild():
                for elem in self.left_child:
                    yield elem
            yield self.key
            if self.hasRightChild():
                for elem in self.right_child:
                    yield elem

    def findSuccessor(self):  # 寻找后继节点
        succ = None
        succ = self.right_child.findMin()
        return succ

    def findMin(self):  # 找到右子树中最小的key 即最左边的节点
        current = self
        while current.hasLeftChild():
            current = current.left_child
        return current

    def spliceOut(self):
        if self.isLeaf():  # 后继节点是叶节点
            self.parent.left_child = None
        elif self.hasAnyChildren():  # 后继节点有子节点  因为只可能有右子树
            self.parent.left_child = self.right_child
            self.right_child.parent = self.parent
