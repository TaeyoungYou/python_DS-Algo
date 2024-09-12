class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

    def myPopFirst(self):
        if self.length == 0:
            return None
        else:
            tmp = self.head
            self.head = tmp.next
            tmp.next = None
            self.length -= 1
            return tmp.value
    
    def popFirst(self) -> Node:
        if self.length == 0:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

myNode = LinkedList(5)
myNode.append(10)
myNode.append(15)
print(myNode.myPopFirst())
