class Node:
    def __init__(self, val):
        self.value = val
        self.next = None

class LinkedList:
    def __init__(self, val=None):
        if val is not None:   
            newNode = Node(val)
            self.head = newNode
            self.tail = newNode
            self.length = 1
        else:
            self.head = None
            self.tail = None
            self.length = 0
    
    def append(self, val):
        newNode = Node(val)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1
        return True

    def printList(self):
        tmp = self.head
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next


if __name__ == "__main__":
    myLinked = LinkedList()
    myLinked.append(10)
    myLinked.append(20)
    myLinked.printList()