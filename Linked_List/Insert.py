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
    
    def append(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.tail
            self.tail = newNode
            temp.next = newNode
        self.length += 1
        return True
    
    def printItems(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def prepend(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.head = newNode
            self.tail = newNode
        else:
            temp = self.head
            self.head = newNode
            newNode.next = temp
        self.length += 1
        return True



    def insert(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        newNode = Node(value)
        temp = self.get(index-1)
        newNode.next = temp.next
        temp.next = newNode
        self.length += 1
        return True

myList = LinkedList(5)
myList.append(10)
myList.append(15)
myList.append(20)
myList.insert(1,100)
myList.printItems()
