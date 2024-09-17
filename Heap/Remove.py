class MaxHeap:
    def __init__(self):
        self.heap = []
    def _left_child(self, index):
        return index*2+1
    def _right_child(self, index):
        return index*2+2
    def __parent(self, index):
        return (index-1)//2
    def __swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]
    def insert(self, value):
        self.heap.append(value)
        curPos = len(self.heap)-1

        while curPos > 0 and self.heap[curPos] > self.heap[self.__parent(curPos)]:
            self.__swap(curPos, self.__parent(curPos))
            curPos = self.__parent(curPos)

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down()

        return max_value
    
    def _sink_down(self, index=0):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)

            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index

            if max_index != index:
                self.__swap(index, max_index)
                index = max_index
            else:
                return

myHeap = MaxHeap()
nodeList = [55,60,50,65,75,80,95]
for i in nodeList:
    myHeap.insert(i)

print(myHeap.heap)

print(myHeap.remove())
print(myHeap.heap)
