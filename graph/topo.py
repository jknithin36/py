from collections import defaultdict

class Graph:
    def __init__(self,numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    
    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    
    def topo(self, v, visited, stack):
        visited.append(v)
        for i in self.graph[v]:
            self.topo(i, visited, stack)
        stack.insert(0,v)
        
        