def remove(self, index):
    if index < 0 or index >= self.length:
        return None
    if index == 0:
        return self.popFirst()
    if index == self.length - 1:
        return self.pop()
    temp = self.get(index)

    temp.prev.next = temp.next
    temp.next.prev = temp.prev
    temp.next = None
    temp.prev = None

    self.length -= 1
    return temp