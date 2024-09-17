class Graph:
    def __init__(self):
        self.graphList = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.graphList.keys():
            self.graphList[vertex] = []
            return True
        return False
    
    def add_edge(self, v1 ,v2):
        if v1 in self.graphList.keys() and v2 in self.graphList.keys():
            self.graphList[v1].append(v2)
            self.graphList[v2].append(v1)
            return True
        return False
    
    def print(self):
        for v in self.graphList.keys():
            print(v,":",self.graphList[v])

    def remove_edge(self, v1, v2):
        if v1 in self.graphList.keys() and v2 in self.graphList.keys():
            try:
                self.graphList[v1].remove(v2)
                self.graphList[v2].remove(v1)
            except ValueError:
                pass
            return True
        return False
    
    def remove_vertex(self, vertex):
        if vertex in self.graphList.keys():
            for v in self.graphList[vertex]:
                self.graphList[v].remove(vertex)
            del self.graphList[vertex]
            return True
        return False


myGraph = Graph()
myGraph.add_vertex(1)
myGraph.add_vertex(2)
myGraph.add_vertex(3)

myGraph.add_edge(1,2)
myGraph.add_edge(2,3)
myGraph.add_edge(3,1)

myGraph.print()
print()
myGraph.remove_vertex(3)
myGraph.print()