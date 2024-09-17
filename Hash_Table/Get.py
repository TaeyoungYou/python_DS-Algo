class HashTable:
    def __init__(self, size = 7):
        self.hashTable = [None] * size
    
    def __hash(self, key) -> int:
        myHashKey = (len(key) * 23) % len(self.hashTable)
        return myHashKey
    
    def set(self, key, value):
        getKey = self.__hash(key)
        if self.hashTable[getKey] == None:
            self.hashTable[getKey] = []
        self.hashTable[getKey].append([key, value])
    
    def print(self):
        for k, v in enumerate(self.hashTable):
            print(k," : ",v)

    def myGet(self, key):
        getKey = self.__hash(key)
        if self.hashTable[getKey] is not None:
            for v in self.hashTable[getKey]:
                if v[0] == key:
                    return v[1]
        return None
    
    def get(self, key):
        index = self.__hash(key)
        if self.hashTable[index] is not None:
            for i in range(len(self.hashTable[index])):
                if self.hashTable[index][i][0] == key:
                    return self.hashTable[index][i][1]
        return None

myTable = HashTable()
myTable.set('Hello', 1004)
myTable.set('World',1002)
myTable.set('ran',10)

myTable.print()

print(myTable.myGet('Hello'))
print(myTable.myGet('What'))