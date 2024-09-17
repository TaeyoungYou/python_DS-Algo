class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BST:
    def __init__(self):
        self.root = None
    
    def insert(self, value) -> bool:
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
            return True
        else:
            curPos = self.root
            while True:
                if curPos.value == newNode.value:
                    return False
                if curPos.value < newNode.value:
                    if curPos.right is None:
                        curPos.right = newNode
                        return True
                    curPos = curPos.right
                else:
                    if curPos.left is None:
                        curPos.left = newNode
                        return True
                    curPos = curPos.left
    
    def myContains(self, value):
        curPos = self.root
        while True:
            if curPos is None:
                return False
            if curPos.value == value:
                return True
            if curPos.value < value:
                curPos = curPos.right
            else:
                curPos = curPos.left

    def contains(self, value):
        # if self.root is None:
        #     return False
        temp = self.root
        while temp is not None:
            if value < temp.value:
                temp = temp.left
            elif value > temp.value:
                temp = temp.right
            else:
                return True
        return False

myTree = BST()
myTree.insert(2)
myTree.insert(1)
myTree.insert(3)

print(myTree.myContains(2))