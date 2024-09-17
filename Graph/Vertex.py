class Graph:
    def __init__(self):
        self.adj_list = {}
    
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    def print(self):
        for ver in self.adj_list:
            print(ver,":",self.adj_list[ver])

myGraph = Graph()
myGraph.add_vertex('A')
myGraph.print()