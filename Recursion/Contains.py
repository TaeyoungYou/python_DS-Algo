class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        cur = self.root
        while cur is not None:
            if cur.value == newNode.value:
                return False
            if cur.value < newNode.value:
                if cur.right is None:
                    cur.right = newNode
                    return True
                cur = cur.right
            else:
                if cur.left is None:
                    cur.left = newNode
                    return True
                cur = cur.left
    
    def my_r_contains(self, cur_node, value):
        if cur_node is None:
            return False
        
        if cur_node.value < value:
            return self.my_r_contains(cur_node.right, value)
        elif cur_node.value > value:
            return self.my_r_contains(cur_node.left, value)
        else:
            return True
        
    def _r_contains(self, cur_node, value):
        if cur_node == None:
            return False
        if value == cur_node:
            return True
        if value < cur_node.value:
            return self._r_contains(cur_node.left, value)
        if value > cur_node.value:
            return self._r_contains(cur_node.right, value)

myTree = BinarySearchTree()
insertList=[5,3,10,6,7,2,1,4,8,9]
for i in insertList:
    myTree.insert(i)
print(myTree.my_r_contains(myTree.root, 1))