def dfs_pre_order(self):
    result=[]

    def traverse(curNode):
        result.append(curNode.value)
        if curNode.left is not None:
            traverse(curNode.left)
        if curNode.right is not None:
            traverse(curNode.right)
    
    traverse(self.root)
    return result

def dfs_post_order(self):
    result = []

    def traverse(curNode):
        if curNode.left is not None:
            traverse(curNode.left)
        if curNode.right is not None:
            traverse(curNode.right)
        result.append(curNode.value)
    traverse(self.root)
    return result

def dfs_in_order(self):
    result = []

    def traverse(curNode):
        if curNode.left is not None:
            traverse(curNode.left)
        result.append(curNode.value)
        if curNode.right is not None:
            traverse(curNode.right)
    traverse(self.root)
    return result