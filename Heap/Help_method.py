"""
아무리 Parent보다 값이 큰 노드가 들어와도, 힙의 특성상 Complete 구조를 만들어야
하기 때문에 아래 노드에 왼쪽부터 차례대로 쌓인다
이후, 큰 순서대로 노드를 스왑 한다
"""

class MaxHeap:
    def __init__(self):
        self.heap = []
    def _left_child(self, index):
        return 2*index+1
    def _right_child(self, index):
        return 2*index+2
    def _parent(self, index):
        return (index-1)//2
    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]