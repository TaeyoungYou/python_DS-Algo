def set_value(self, index, value):
    temp = self.get(index)
    if temp:
        temp.value = value
        return True
    return False
"""
Set method depends on Get method
Below how get method does, Set method works differently
"""