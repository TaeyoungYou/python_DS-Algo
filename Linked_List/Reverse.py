"""
head                    tail
Node1 > Node2 > Node3 > Node4

reverse()
tail                    head
Node1 < Node2 < Node3 < Node4
"""

def reverse(self):
    temp = self.head
    self.head = self.tail
    self.tail = temp

    after = temp.next
    before = None

    for _ in range(self.length):
        after = temp.next
        temp.next = before
        before = temp
        temp = after