
class Graph:
    def __init__(self):
        self.graph = {}

    # Add a vertex
    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    # Add an undirected edge
    def add_edge(self, vertex1, vertex2):
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        self.graph[vertex1].append(vertex2)
        self.graph[vertex2].append(vertex1)

    # Display the graph
    def display(self):
        return self.graph

    # Depth-First Search
    def dfs(self, start):
        visited = []
        self.dfs_helper(start, visited)
        return visited

    def dfs_helper(self, vertex, visited):
        if vertex not in self.graph or vertex in visited:
            return

        visited.append(vertex)

        for neighbor in self.graph[vertex]:
            self.dfs_helper(neighbor, visited)

    # Breadth-First Search
    def bfs(self, start):
        if start not in self.graph:
            return []

        visited = []
        queue = [start]

        while queue:
            vertex = queue.pop(0)

            if vertex not in visited:
                visited.append(vertex)

                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)

        return visited


# Example usage
my_graph = Graph()

my_graph.add_edge("A", "B")
my_graph.add_edge("A", "C")
my_graph.add_edge("B", "D")
my_graph.add_edge("C", "E")

print("Graph:", my_graph.display())
print("DFS:", my_graph.dfs("A"))
print("BFS:", my_graph.bfs("A"))
