# GRAPH - Vertices joid using Edges. "Collection/set of objects joined together using edges".
    # Vertices/Node - object
    # Edges - Represent relationship between two vertices. Connect 2 vertices.

# TYPE OF GRAPHS - 
    # DIRECTED
    # UNDIRECTED
    # WEIGHTED
    # UNWEIGHTED

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
            

    def removeUndirectedEdge(self, vertex_1, vertex_2):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:
            
            # # When Using List:-

            # vertex_1.connectedVertices.pop(vertex_2)
            # # For undirected graph, also remove vertex_1 to neighbors (connected vertices) of vertex_2.
            # vertex_2.connectedVertices.pop(vertex_1)

                                                    # OR

            # # When using dictionary:-
                # # Each GraphVertex instance has a value and a neighbors (connectedVertices) list/set.
            self.vertices[vertex_1].connectedVertices.remove(self.vertices[vertex_2])
            # # For undirected graph, also remove vertex_1 to neighbors (connected vertices) of vertex_2.
            self.vertices[vertex_2].connectedVertices.remove(self.vertices[vertex_1])
        else:
            print("One or both vertices not present.")

    def removeDirectedEdge(self, fromVertex, toVertex):
        if fromVertex in self.vertices and toVertex in self.vertices:
            
            # # Using Dictionary:-
            self.vertices[fromVertex].connectedVertices.remove(self.vertices[toVertex])
            # # In case of directed graph, do not remove fromVertex to neighbors (connectedVertices) of toVertex.
        
    def removeUndirectedWeightedEdge(self, vertex_1, vertex_2, weight):
        if vertex_1 in self.vertices and vertex_2 in self.vertices:

            self.vertices[vertex_1].connectedVertices.remove((self.vertices[vertex_2], weight))
            self.vertices[vertex_2].connectedVertices.remove((self.vertices[vertex_1], weight))

    def removeDirectedWeightedEdge(self, fromVertex, toVertex, weight):
        if fromVertex in self.vertices and toVertex in self.vertices:

            self.vertices[fromVertex].connectedVertices.remove((self.vertices[toVertex], weight))


# Example:-

# Create a new graph
g = Graph()

# Add vertices
g.addVertex('A')
g.addVertex('B')
g.addVertex('C')
g.addVertex('D')

# # Add undirected edges
# g.addUndirectedEdge('A', 'B')
# g.addUndirectedEdge('A', 'C')
# g.addUndirectedEdge('B', 'D')
# g.addUndirectedEdge('C', 'D')
# # g.addUndirectedEdge('C', 'E')

# Add directed edges
g.addDirectedEdge('A', 'B')
g.addDirectedEdge('B', 'D')
g.addDirectedEdge('D', 'C')
g.addDirectedEdge('C', 'A')

# Print graph representation
print(g)





# TOPICS TO COVER:
    # Connected, non-connected graphs
    # degree- indegree and outdegree
    # Representation - Adjecency Matrix and Adjecency List
    # Traversing and Printing Graph-Vertex's value.