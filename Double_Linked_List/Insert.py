def insert(self, index, value):
    if index < 0 or index > self.length:
        return False
    if index == 0:
        return self.prepend(value)
    if index == self.length:
        return self.append(value)
    
    newNode = Node(value)
    before = self.get(index-1)
    after = before.next

    newNode.prev = before
    before.next = newNode
    newNode.next = after
    after.prev = newNode

    self.length += 1 
    return True
