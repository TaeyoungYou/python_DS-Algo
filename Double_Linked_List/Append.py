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
    
    def myAppend(self, value):
        newNode = Node(value)
        newNode.prev = self.tail
        self.tail.next = newNode
        self.tail = newNode
        self.length += 1

        return True
    
    def append(self, value) -> bool:
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length += 1
        return True
    
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

myList = DoublyLinkedList(5)
myList.myAppend(6)
myList.myAppend(7)
myList.print_list()

myList.append(10)
myList.append(20)
myList.print_list()