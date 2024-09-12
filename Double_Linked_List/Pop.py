class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, val):
        newNode = Node(val)
        self.head = newNode
        self.tail = newNode
        self.length = 1
    
    def append(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1

        return True
    
    def myPop(self) -> Node:
        if self.length == 0:
            return None
        if self.head is self.tail:
            temp = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return temp
        temp = self.tail
        self.tail = self.tail.prev
        temp.prev = None
        self.tail.next = None
        self.length -= 1

        return temp
    
    def pop(self) -> Node:
        if self.length == 0:
            return None
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            temp.prev = None
        self.length -= 1

        return temp

    
myList = DoublyLinkedList(5)
myList.append(6)
myList.append(7)
print(myList.myPop().val)