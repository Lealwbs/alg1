class Vertex:
    def __init__(self):
        self.adjacents: list[(int, int)] = []  # (vertex, weight)


class Edge:
    def __init__(self, vertex_a: int, vertex_b: int, weight: int = 0):
        self.vertex_a = vertex_a
        self.vertex_b = vertex_b
        self.weight = weight


class Graph:
    def __init__(self, directed_graph: bool = True, weighted_graph: bool = True):
        self.digraph: bool = directed_graph
        self.weighted: bool = weighted_graph
        self.vertices_count: int = 0
        self.edges_count: int = 0
        self.vertices: dict[Vertex] = {}
        self.edges: dict[Edge] = {}
        pass

    def __str__(self):
        pass

    def add_edge(self):
        pass

    def pop_edge(self):
        pass

    def dfs(self):
        pass

    def bfs(self):
        pass

    def color_graph(self):
        pass

    def kosarajur_sharir(self):
        pass

    def prim(self):
        pass

    def kruskal(self):
        pass

    def dijkstra(self):
        pass

    def bellman_ford(self):
        pass

    def ford_fulkerson(self):
        pass

    def capacity_scaling(self):
        pass

    def edmonds_karp(self):
        pass