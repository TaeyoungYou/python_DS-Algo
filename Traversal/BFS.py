def BFS(self):
    curNode = self.root
    queue = []
    result = []
    queue.append(curNode)

    while len(queue) > 0:
        curNode = queue.pop(0)
        result.append(curNode.value)
        if curNode.left is not None:
            queue.append(curNode.left)
        if curNode.right is not None:
            queue.append(curNode.right)
    return result