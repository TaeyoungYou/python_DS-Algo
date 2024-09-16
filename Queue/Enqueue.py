class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
    
class Queue:
    def __init__(self, value) -> None:
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1
    
    def myEnqueue(self, value):
        newNode = Node(value)
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
        return True
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length += 1
    
    def print(self):
        temp = self.first
        while temp:
            print(temp.value)
            temp = temp.next

myQueue = Queue(1)
myQueue.myEnqueue(2)
myQueue.myEnqueue(3)
myQueue.print()