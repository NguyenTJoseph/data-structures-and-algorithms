class Vertex:
    def __init__(self, value):
        self.value = value
        self.neighbors = []

class Neighbor:
    def __init__(self, vertex, weight):
        self.vertex = vertex
        self.weight = weight

class Graph:
    def __init__(self):
        self.nodes = []
    
    def add_node(self, value):
        node = Vertex(value)
        self.nodes.append(node)
        return node

    def size(self):
        return len(self.nodes)

    def get_nodes(self):
        return self.nodes

    def add_edge(self, node1, node2, weight = 0):
        if node1 in self.nodes and node2 in self.nodes:
            node1.neighbors.append(Neighbor(node2, weight))
        else: 
            raise KeyError

    def get_neighbors(self, value):
        for node in self.nodes:
            if node == value:
                return node.neighbors
    
    def breadth_first(self, vertex):
        nodes = []
        queue = [vertex]
        visited = {vertex}

        while queue:
            front = queue.pop(0)
            nodes.append(front)

            for neighbor in front.neighbors:
                vert = neighbor.vertex
                if vert not in visited:
                    visited.add(vert)
                    queue.append(vert)

        return nodes