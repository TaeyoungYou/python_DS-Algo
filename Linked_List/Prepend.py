class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        if value is None:
            self.head = None
            self.tail = None
            self.length = 0
        else:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length = 1

    def printListItems(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value, end=" ")
            tmp = tmp.next
    
    def append(self, value):
        if self.length == 0:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        
        return True

    def myPrepend(self, value):
        if self.length == 0:
            self.__init__(value)
        else:
            newNode = Node(value)
            newNode.next = self.head
            self.head = newNode
            self.length += 1
        return True
    
    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1
        return True

myList = LinkedList(5)
myList.append(10)
myList.append(15)
myList.prepend(1)
myList.printListItems()