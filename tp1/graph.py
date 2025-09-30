from queue import Queue
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, vertex_count: int) -> None: 
        self.vertex_count: int = vertex_count 
        self.edge_count: int = 0
        
        # GRAFO = {vertice1: [(vertice2, distancia), (vertice3, distancia), ...]; ...}
        self.graph: dict[int, list[tuple[int, int]]] = { i: [] for i in range(1, vertex_count + 1) }
        
        # ARESTAS = [(aresta1, vertice1, vertice2, distancia), (aresta2, vertice1, vertice3, distancia), ...]
        self.edges: list[tuple[int, int, int, int]] = []


    def __str__(self) -> str:
        result = f"Grafo({self.vertex_count} vertices e {len(self.edges)} arestas):\n"
        for index, from_vertex, to_vertex, length in self.edges:
            result += f"Edge {index}:  {from_vertex} <--({length})--> {to_vertex}\n"
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
            for v, edge_uv in self.graph[u]: # Para todos os vértices_v e arestas_uv vizinhos de u
                if distance_u + edge_uv < distance[v]:
                    distance[v] = distance_u + edge_uv
                    parent[v] = u
                    heappush(heap, (distance[v], v))
        return distance


    def _bfs(self, initial_vertex: int, parent: list[int], marked: list[bool]):
        marked[initial_vertex] = True  
        queue: Queue[int] = Queue(initial_vertex)
        while not queue.empty():
            v: int = queue.get()
            for adjacent_vertex_index, length in self.graph[v]:
                u: int = adjacent_vertex_index
                if not marked[u]:
                    marked[u] = True
                    parent[u] = v
                    queue.put(u)


    # Parte 1 - Calcular a menor distância entre 1 e N.
    def get_minimal_distance(self, start: int, end: int) -> int:
        distance: list[int] = self._dijkstra(initial_vertex = start)

        return distance[end]
    

    # Parte 2 - Encontrar todas as arestas (índices) que fazem parte de algum caminho mínimo.
    def find_minimal_streets(self, start: int, end: int) -> list:  #-> set:
        minimal_streets: list[int] = []
        minimal_distance: int = self.get_minimal_distance(start, end)
        distance_from_start: list[int] = self._dijkstra(start)
        distance_from_end: list[int] = self._dijkstra(end)
        for index, u, v, length in self.edges: # Para todas as arestas (index, vertice1, vertice2, distancia) do grafo
            cond1: bool = distance_from_start[u] + length + distance_from_end[v] == minimal_distance
            cond2: bool = distance_from_start[v] + length + distance_from_end[u] == minimal_distance
            if cond1 or cond2:
                minimal_streets.append(index)
        return minimal_streets


    # Parte 3 - Encontrar as ruas críticas que aumentariam a distância mínima entre 1 e N.
    ''' Identificar quais são as ruas críticas da cidade. Essas ruas não podem ser destruidas, visto que caso destruidas, fariam com que a menor distâcia
    entre 1 e N aumentasse, ou tornaria o acesso impossível.
    - Saída: String "Parte 3: ", seguida dos índices das ruas críticas, em ordem crescente. Os índices são definidos pela ordem 
    em que as ruas foram fornecidas na entrada, começando em 1. Se não houver nenhuma, imprima -1.
    RESUMO: Encontrar todas as (índices) das arestas que, se removidas, fariam com que a distância mínima entre 1 e N aumentasse. "R1 R2 ... RN" '''
    def find_critical_streets(self, start: int, end: int) -> set:
        critical_streets: list[int] = []
        return critical_streets
