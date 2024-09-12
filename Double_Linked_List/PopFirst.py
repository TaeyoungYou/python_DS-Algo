class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        
        self.length += 1
        return True

    def myPopFirst(self) -> Node:
        if self.length == 0:
            return None
        temp = self.head
        self.head = temp.next
        temp.next = None
        self.head.prev = None
        self.length -= 1
        return temp
    
    def popFirst(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            temp.next = None
        self.length -= 1
        return temp

myList = DoublyLinkedList(1)
myList.append(2)
myList.append(3)
print(myList.myPopFirst().value)
print(myList.myPopFirst().value)
print(myList.myPopFirst().value)