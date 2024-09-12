class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        # create new Node
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

    def append(self, value):
        # create new Node
        # add Node to end
        pass
    def prepend(self, value):
        # create new Node
        # add Node to beginning
        pass
    def insert(self, index, value):
        # create new Node
        # insert Node whatever depends on index
        pass

if __name__ == "__main__":
    myLinkedList = LinkedList(4)
    print(myLinkedList.head.value)