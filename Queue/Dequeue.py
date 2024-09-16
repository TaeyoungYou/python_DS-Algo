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
    
    def myDequeue(self) -> Node:
        if self.length == 0:
            return None
        temp = self.first
        self.first = self.first.next
        temp.next = None
        self.length -= 1
        return temp
    
    def dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length -= 1
        return temp

myQueue = Queue(1)
myQueue.enqueue(2)
myQueue.enqueue(3)
myQueue.print()

print(myQueue.myDequeue(),'\n')

myQueue.print()
