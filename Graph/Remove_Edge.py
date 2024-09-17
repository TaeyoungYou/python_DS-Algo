class Graph:
    def __init__(self):
        self.graphList = {}
    
    def addVer(self, ver):
        if ver not in self.graphList.keys():
            self.graphList[ver] = []
            return True
        return False

    def addEdge(self, v1, v2):
        if v1 in self.graphList.keys() and v2 in self.graphList.keys():
            self.graphList[v1].append(v2)
            self.graphList[v2].append(v1)
            return True
        return False
    
    def print(self):
        for v in self.graphList.keys():
            print(v,":",self.graphList[v])

    def removeEdge(self, v1, v2):
        if v1 in self.graphList.keys() and v2 in self.graphList.keys():
            try:
                self.graphList[v1].remove(v2)
                self.graphList[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False

myGraph = Graph()
myGraph.addVer('A')
myGraph.addVer('B')
myGraph.addVer('C')
myGraph.addVer('D')

myGraph.addEdge('A','B')
myGraph.addEdge('B','C')
myGraph.addEdge('C','A')

myGraph.print()
print()

myGraph.removeEdge('A','B')
myGraph.print()
print()

myGraph.removeEdge('D','A')
myGraph.print()