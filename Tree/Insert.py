class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def myInsert(self, value) -> bool:
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else:
            cur = self.root
            while cur is not None:
                if cur.value == newNode.value:
                    return False
                elif cur.value < newNode.value:
                    cur = cur.right
                else:
                    cur = cur.left
            cur = newNode
        return True

    def insert(self, value):
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        temp = self.root
        while True:
            if newNode.value == temp.value:
                return False
            if newNode.value < temp.value:
                if temp.left is None:
                    temp.left = newNode
                    return True
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = newNode
                    return True
                temp = temp.right

myTree = BST()
myTree.insert(2)
myTree.insert(3)
myTree.insert(1)

print(myTree.root.value)
print(myTree.root.left.value)
print(myTree.root.right.value)
