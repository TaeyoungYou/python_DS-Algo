class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def re_insert(self, curPos, value) -> Node:
        if curPos is None:
            return Node(value)
        
        if curPos.value < value:
            curPos.right = self.re_insert(curPos.right, value)
        if curPos.value > value:
            curPos.left = self.re_insert(curPos.right, value)

        return curPos
    
    def re_contains(self, curPos, value) -> bool:
        if curPos is None:
            return False
        if curPos.value < value:
            return self.re_contains(curPos.right, value)
        elif curPos.value > value:
            return self.re_contains(curPos.left, value)
        else:
            return False
    def delete(self, value):
        self.re_delete(self.root, value)

    def re_delete(self, curNode, value):
        if curNode is None:
            return None
        if value < curNode.value:
            curNode.left = self.re_delete(curNode.left, value)
        elif value > curNode.value:
            curNode.right = self.re_delete(curNode.right, value)
        else:
            # Now implement of all of case deleting
            if curNode.left is None and curNode.right is None:
                return None
            elif curNode.left is None:
                curNode = curNode.right
            elif curNode.right is None:
                curNode = curNode.left
            else:
                sub_tree_min = self.min_value(curNode.right)
                curNode.value = sub_tree_min
                curNode.right = self.re_delete(curNode.right, sub_tree_min)
        return curNode
    
    def min_value(self, curNode):
        while curNode.left is not None:
            curNode = curNode.left
        return curNode.value