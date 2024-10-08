def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.PopFirst()
    if index == self.length - 1:
        return self.pop()
    prev = self.get(index-1)
    temp = prev.next
    prev.next = temp.next
    temp.next = None
    self.length -= 1
    return temp