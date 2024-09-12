class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value=None):
        self.head = None
        self.tail = None
        self.length = 0
        if value is not None:
            newNode = Node(value)
            self.head = newNode
            self.tail = newNode
            self.length += 1

    def append(self, value):
        if self.head is None:
            self.__init__(value)
        else:
            newNode = Node(value)
            self.tail.next = newNode
            self.tail = newNode
            self.length += 1
        
        return True
    
    def printNodes(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

    def myPop(self):
        tmp = self.head
        while tmp is not None:
            if tmp.next is self.tail:
                resValue = self.tail
                tmp.next = None
                self.tail = tmp
                self.length -= 1
                return resValue
            tmp = tmp.next
            
        return False
    
    def pop(self):
        if self.length == 0:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp
        


myList = LinkedList()
myList.append(10)
myList.append(20)
myList.append(30)
popped: Node = myList.pop()
print(popped.value, popped.next)

