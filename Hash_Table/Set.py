class HashTable:
    def __init__(self, size = 7):
        self.hashMap = [None] * size
    
    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.hashMap)
        return my_hash
    
    def set_item(self, key, value):
        index = self.__hash(key)
        if self.hashMap[index] == None:
            self.hashMap[index] = []
        self.hashMap[index].append([key, value])

    def print(self):
        for k, v in enumerate(self.hashMap):
            print(k," : ",v)

myHash = HashTable()

myHash.set_item('bolts',1400)
myHash.set_item('washers',50)
myHash.set_item('lumber',70)

myHash.print()