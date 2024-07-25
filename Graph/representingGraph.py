class GraphVertex:
    def __init__(self, key):
        self.value = key
        # self.connectedVertices = []
        self.connectedVertices = set()

class Graph:
    def __init__(self):
        # self.vertices = []
        self.vertices = {}

    def addVertex(self, key):
        if key not in self.vertices:
            # self.vertices.append(GraphVertex(key))        # When using list.
            self.vertices[key] = GraphVertex(key)           # When using dictionary.
        else:
            print(f"Vertex {key} already exists.")


    def addUndirectedEdge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            
            # # When Using List:-

            # vertex_1.connectedVertices.append(vertex_2)
            # # For undirected graph, also add vertex_1 to neighbors (connected vertices) of vertex_2.
            # vertex_2.connectedVertices.append(vertex_1)

                                                    # OR

            # # When using dictionary:-
                # # Each GraphVertex instance has a value and a neighbors (connectedVertices) list/set.
            self.vertices[vertex_1].connectedVertices.add(self.vertices[vertex_2])
                # # For undirected graph, also add vertex_1 to neighbors (connected vertices) of vertex_2.
            self.vertices[vertex_2].connectedVertices.add(self.vertices[vertex_1])
        else:
            print("One or both vertices not present.")

    def addDirectedEdge(self, fromVertex, toVertex):
        if fromVertex in self.vertices and toVertex in self.vertices:
            
            # # Using Dictionary:-
            self.vertices[fromVertex].connectedVertices.add(self.vertices[toVertex])
                # # In case of directed graph, do not connect/add fromVertex to neighbors (connectedVertices) of toVertex.
        
    def addUndirectedWeightedEdge(self, vertex_1, vertex_2, weight):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:

            self.vertices[vertex_1].connectedVertices.add((self.vertices[vertex_2], weight))
            self.vertices[vertex_2].connectedVertices.add((self.vertices[vertex_1], weight))

    def addDirectedWeightedEdge(self, fromVertex, toVertex, weight):
        if fromVertex in self.vertices and toVertex in self.vertices:

            self.vertices[fromVertex].connectedVertices.add((self.vertices[toVertex], weight))
            




# Adjecency matrix

def adjecencyMatrix(graph: Graph):
    totalVertices = len(graph.vertices)
    for i in range(0, totalVertices):
        for j in range(0, totalVertices):
            pass





# Example:-

# Create a new graph
g = Graph()

g.addVertex('a')
g.addVertex('b')
g.addVertex('c')
g.addVertex('d')

g.addUndirectedEdge('a', 'b')
g.addUndirectedEdge('b', 'c')
g.addUndirectedEdge('c', 'd')
g.addUndirectedEdge('d', 'a')


