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
    
    def append(self, value) -> bool:
        newNode = Node(value)
        temp = self.tail
        self.tail = newNode
        temp.next = newNode
        self.length += 1

        return True
    
    # 스스로 구현 못함..
    def get(self, index) -> Node:
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
myList = LinkedList(1)
myList.append(2)
myList.append(3)
myList.append(4)
print(myList.get(2).value)