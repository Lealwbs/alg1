class Graph:
    def __init__(self, vertex_count: int): 
        self.vertex_count: int = vertex_count 
        self.edges: list[tuple[int, int, int]] = []
        self.graph: dict[int, list[tuple[int, int, int]]] = { i: [] for i in range(1, vertex_count + 1) }

    def __str__(self):
        # Escrever uma forma melhor de representar o grafo:
        result = f"Grafo({self.vertex_count} vertices e {len(self.edges)} arestas):\n"
        for from_vertex, to_vertex, length in self.edges:
            result += f"  {from_vertex} <--({length})--> {to_vertex}\n"
        return result
        

    # Por o grafo ser bidirecionado, a função add_edge já adiciona as duas direções
    def add_edge(self, from_vertex: int, to_vertex: int, length: int):
        self.edges.append((from_vertex, to_vertex, length))
        self.graph[from_vertex].append((to_vertex, length))
        self.graph[to_vertex].append((from_vertex, length))

    def dijkstra(self, start: int, end: int) -> list[int]:
        return [-1]

    def find_minimal_streets(self, start: int, end: int) -> set[int]:
        return {-1}

    def find_critical_streets(self, start: int, end: int) -> set[int]:
        return {-1}

