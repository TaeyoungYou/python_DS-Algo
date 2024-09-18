class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    """
    S(F,x)  - Node()        if node = Node
            - node          if node = value
            - S(F.left, v)  if node > value
            - S(F.right, v) if node < value
    
    각 case에 대한 return 값을 고민 할 필요없음
    왜냐하면 기준을 이 재귀함수의 성공 사례의 return 값과 type을 보면,
    다른 return 값도 쉽게 구할 수 있음
    """
    def myInsert(self, curNode, value) -> Node:
        if curNode is None:
            return Node(value)
        
        if curNode.value < value:
            curNode.right = self.myInsert(curNode.right, value)
            return curNode
        elif curNode.value > value:
            curNode.left = self.myInsert(curNode.left, value)
            return curNode
        else:
            return curNode
    
    def _r_insert(self, curNode, value):
        if curNode is None:
            return Node(value)
        if value < curNode.value:
            curNode.left = self._r_insert(curNode.left, value)
        if value > curNode.value:
            curNode.right = self._r_insert(curNode.right, value)
        return curNode
    
    def r_insert(self, value):
        if self.root is None:
            self.root = Node(value)
        self._r_insert(self.root, value)