class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 0
    
    def append(self, value):
        newNode = Node(value)
        tmp = self.tail
        tmp.next = newNode
        self.tail = newNode
        self.length += 1

    def printItems(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next
    
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp

    def mySet(self, index, value):
        if index < 0 or index >= self.length:
            return None
        tmp = self.head
        for _ in range(index):
            tmp = tmp.next
        tmp.value = value

    def set(self, index, value) -> bool:
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
        
        
myList = LinkedList(5)
myList.append(10)
myList.append(15)
myList.printItems()
myList.set(1, 100)
myList.printItems()