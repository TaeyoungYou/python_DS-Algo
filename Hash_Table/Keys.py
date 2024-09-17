class HashTable:
    def __init__(self, size=7):
        self.table = [None] * size
    
    def __hash(self, key):
        hashKey = 0
        for c in key:
            hashKey = (hashKey + ord(c) * 23) % len(self.table)
        return hashKey
    
    def set(self, key, value):
        hashKey = self.__hash(key)
        if self.table[hashKey] is None:
            self.table[hashKey] = []
        self.table[hashKey].append([key, value])
    
    def get(self, key):
        hashKey = self.__hash(key)
        if self.table[hashKey] is not None:
            for e in self.table[hashKey]:
                if e[0] == key:
                    return e[1]
        return None
    
    def keys(self):
        all_keys = []
        for i in self.table:
            if i is not None:
                for j in i:
                    all_keys.append(j[0])
        return all_keys

myTable = HashTable()

myTable.set('bolts',1400)
myTable.set('washers',50)
myTable.set('lumber',70)

print(myTable.keys())