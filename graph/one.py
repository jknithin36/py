# class Graph:
#     def __init__(self, gdict=None):
#         if gdict is None:
#             gdict ={}
#         self.gdict = gdict

    

#     def addEdge(self, vertex,edge):
#         self.gdict[vertex].append(edge)



# customDict ={"a": ["b", "c"],
#              "b":["a", "d", "e"],
#              "c":["a", "e"],
#              "d":["b", "e", "f"],
#              "e":["d","f"],
#              "f":["d","e"]}



# graph = Graph(customDict)
# graph.addEdge("e", "c")
# print(graph.gdict)

# # hfjdjs




# class Graph:
#     def __init__(self, gdict = None):
#         if gdict is None:
#             gdict ={}
#         self.gdict = gdict


#     def addEdge(self, vertex, edge):
#         self.gdict[vertex].append(edge)
    


        


# customDict ={"a": ["b", "c"],
#              "b":["a", "d", "e"],
#              "c":["a", "e"],
#              "d":["b", "e", "f"],
#              "e":["d","f"],
#              "f":["d","e"]}



# graph = Graph(customDict)
# graph.addEdge("e", "c")


# print(graph.gdict)

from collections import deque


class Graph:
    def __init__(self):
        self.adjacency_list = {}
    

    def addVertex(self, vertex):
        # edge case --> if exists 
        if vertex not in self.adjacency_list.keys():
          self.adjacency_list[vertex] = [] # creates an exmpty list 
          return True
        return False
    

    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex, ":", self.adjacency_list[vertex])
    

    # def addEdge(self, vertex,edge):
    #     if vertex not in self.adjacency_list:
    #         return None
    #     if edge in self.adjacency_list[vertex]:
    #         return "Already Connected"
    #     self.adjacency_list[vertex].append(edge)
    #     self.adjacency_list[edge].append(vertex)
    def addEdge(self, vertex, edge):
        # Check if vertex exists
        if vertex not in self.adjacency_list:
            return f"Vertex '{vertex}' not found in graph."

        # If edge node doesn't exist, create it
        if edge not in self.adjacency_list:
            self.adjacency_list[edge] = []

        # Check if already connected
        if edge in self.adjacency_list[vertex]:
            return "Already Connected"

        # Add edge both ways (undirected)
        self.adjacency_list[vertex].append(edge)
        self.adjacency_list[edge].append(vertex)

    # Remove Edge

    def removeEdge(self, vertex, edge):
      if vertex in self.adjacency_list and edge in self.adjacency_list:
        if edge in self.adjacency_list[vertex]:
            self.adjacency_list[vertex].remove(edge)
        if vertex in self.adjacency_list[edge]:
            self.adjacency_list[edge].remove(vertex)
        return True
      return False
    

    def remove_vertex(self, vertex):
        if vertex in self.adjacency_list:
            for otherVertex in self.adjacency_list[list]:
                self.adjacency_list[otherVertex].remove(vertex)
            del self.adjacency_list[vertex] 
            return True
        return False
    

    def bfs(self, vertex):
     if vertex not in self.adjacency_list:
        print("Start vertex not in graph.")
        return

     visited = set()
     queue = deque([vertex])
     visited.add(vertex)

     while queue:
        current_vertex = queue.popleft()
        print(current_vertex)

        for adjacentVertex in self.adjacency_list[current_vertex]:
            if adjacentVertex not in visited:
                visited.add(adjacentVertex)
                queue.append(adjacentVertex)
    






    






        






custom_graph = Graph()

custom_graph.addVertex("A")

custom_graph.addVertex("B")
custom_graph.addEdge("A", "B")

custom_graph.print_graph()

custom_graph.bfs("A")