class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def addVertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print(self):
        for ver in self.adj_list:
            print(ver,":",self.adj_list[ver])
    
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
myGraph = Graph()
myGraph.addVertex(1)
myGraph.addVertex(2)

myGraph.add_edge(1,2)
myGraph.print()