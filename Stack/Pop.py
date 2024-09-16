class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1
    
    def push(self, value):
        newNode = Node(value)
        if self.height == 0:
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        self.height += 1
    
    def myPop(self) -> Node:
        temp = self.top
        if self.height == 0:
            return None
        else:
            self.top = temp.next
            temp.next = None
            self.height -= 1
        return temp
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height -= 1
        return temp

myStack = Stack(3)
myStack.push(2)
myStack.push(1)
print(myStack.myPop().value)
print(myStack.myPop().value)
print(myStack.myPop().value)