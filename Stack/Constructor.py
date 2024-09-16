class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self, value):
        newNode = Node(value)
        self.top = newNode
        self.height = 1
    
    def print_stack(self):
        tmp = self.top
        while tmp is not None:
            print(tmp.value)
            tmp = tmp.next

"""
Stack에 bottom이 필요없는 이유:
push or pull 할때, top만 사용해서 하지. bottom은 상관이 없다
"""