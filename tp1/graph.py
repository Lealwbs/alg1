from heapq import heappop, heappush

class Graph:
    def __init__(self, vertex_count: int) -> None: 
        self.vertex_count: int = vertex_count 
        self.edge_count: int = 0
        # GRAFO = {vertice1: [(vertice2, distancia), (vertice3, distancia), ...]; ...}
        self.graph: dict[int, list[tuple[int, int]]] = { i: [] for i in range(1, vertex_count + 1) }
        # ARESTAS = [(aresta1, vertice1, vertice2, distancia), (aresta2, vertice1, vertice3, distancia), ...]
        self.edges: list[tuple[int, int, int, int]] = []
        self.minimal_edges: list[tuple[int, int, int, int]] = []


    def __str__(self) -> str:
        result = f"Grafo({self.vertex_count} vertices e {len(self.edges)} arestas):\n"
        for index, from_vertex, to_vertex, length in self.edges:
            result += f"Aresta {index}:  {from_vertex} <--({length})--> {to_vertex}\n"
        return result
        
    
    def add_edge(self, from_vertex: int, to_vertex: int, length: int) -> None:
        self.edge_count += 1
        self.edges.append((self.edge_count, from_vertex, to_vertex, length))
        # O grafo é bidirecionado, com a mesma distancia p/ os 2 lados (ruas)
        self.graph[from_vertex].append((to_vertex, length))
        self.graph[to_vertex].append((from_vertex, length))


    def _dijkstra(self, initial_vertex: int) -> list:
        heap: list[int, int] = [(0, initial_vertex)] # (distância_acumulada, indice_vértice)
        parent: list[int] = [-1] * (self.vertex_count + 1)
        distance: list[int] = [float('inf')] * (self.vertex_count + 1)
        distance[initial_vertex] = 0
        while heap:
            distance_u, u = heappop(heap) # Remove o vértice de menor distancia
            if distance_u > distance[u]:  # Ignorar estados desatualizados
                continue
            for v, edge_uv in self.graph[u]: # Para todos os vértices_v e arestas_uv vizinhos de u
                if distance_u + edge_uv < distance[v]:
                    distance[v] = distance_u + edge_uv
                    parent[v] = u
                    heappush(heap, (distance[v], v))
        return distance


    def get_minimal_distance(self, start: int, end: int) -> int:
        distance: list[int] = self._dijkstra(initial_vertex = start)
        return distance[end]

    
    def find_minimal_edges(self, start: int, end: int) -> list:
        distance_from_start: list[int] = self._dijkstra(start)
        distance_from_end: list[int] = self._dijkstra(end)
        minimal_distance: int = distance_from_start[end]
        for index, u, v, length in self.edges:
            cond1: bool = distance_from_start[u] + length + distance_from_end[v] == minimal_distance
            cond2: bool = distance_from_start[v] + length + distance_from_end[u] == minimal_distance
            if cond1 or cond2:
                self.minimal_edges.append([index, u, v, length])
        return self.minimal_edges


    def find_critical_edges(self, start: int, end: int) -> set:
        if not self.minimal_edges: 
            self.find_minimal_edges(start, end) # Usado para evitar chamadas duplicadas
        minimal_distance: int = self.get_minimal_distance(start, end)
        critical_streets: list[int] = []
        for index, u, v, length in self.minimal_edges:
            # Remover a aresta para depois adicionar novamente
            self.graph[u] = [(w, l) for (w, l) in self.graph[u] if w != v or l != length]
            self.graph[v] = [(w, l) for (w, l) in self.graph[v] if w != u or l != length]
            new_distance: int = self.get_minimal_distance(start, end)
            self.graph[u].append((v, length))
            self.graph[v].append((u, length))
            if new_distance > minimal_distance:
                critical_streets.append(index)
        return critical_streets