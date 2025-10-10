from heapq import heappop, heappush

class Graph:
    def __init__(self, vertex_count: int, edges_count: int) -> None: 
        self.vertex_count: int = vertex_count
        self.edge_count: int = edges_count

        # GRAFO = {vertice1: [(vertice2, distancia), (vertice3, distancia), ...]; ...}
        self.graph: dict[int, list[tuple[int, int]]] = { i: [] for i in range(1, vertex_count + 1) }
        # ARESTAS = [(aresta1, vertice1, vertice2, distancia), (aresta2, vertice1, vertice3, distancia), ...]
        self.edges: list[tuple[int, int, int, int]] = []
        # Arestas mínimas (entre 1 e N) para evitar chamadas duplicadas
        self.minimal_edges: list[tuple[int, int, int, int]] = []


    def __str__(self) -> str:
        result = f"Grafo({self.vertex_count} vertices e {len(self.edges)} arestas):\n"
        for index, from_vertex, to_vertex, length in self.edges:
            result += f"Aresta {index}:  {from_vertex} <--({length})--> {to_vertex}\n"
        return result
        
    
    def add_edge(self, index: int, from_vertex: int, to_vertex: int, length: int) -> None:
        # Adiciona uma aresta ao grafo (tanto na lista de arestas quanto no dicionário do grafo)
        self.edge_count += 1
        self.edges.append([index, from_vertex, to_vertex, length])
        # O grafo é bidirecionado, com a mesma distancia p/ os 2 lados (ruas)
        self.graph[from_vertex].append((to_vertex, length))
        self.graph[to_vertex].append((from_vertex, length))


    def _dfs(self, initial_vertex: int) -> set:
        # Busca em profundidade para encontrar todos os vértices alcançáveis a partir de um vértice inicial
        stack: list[int] = [initial_vertex]
        visited: set = set()
        
        while stack:
            vertex: int = stack.pop() # Pega o último vértice adicionado
            if vertex not in visited:
                visited.add(vertex)
                for neighbor, length in self.graph[vertex]: # Para todos os vértices vizinhos
                    if neighbor not in visited:
                        stack.append(neighbor)
        return visited


    def _dijkstra(self, initial_vertex: int) -> list:
        # Algoritmo padrão que retorna uma lista com a menor distância de um vértice inicial a todos os outros
        heap: list[(int, int)] = [(0, initial_vertex)] # (distância_acumulada, indice_vértice)
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
        # Obtém a distância mínima entre dois vértices
        distance: list[int] = self._dijkstra(initial_vertex = start)
        return distance[end]

    
    def find_minimal_edges(self, start: int, end: int) -> list:
        # Encontra todas as arestas que pertencem a pelo menos um caminho mínimo entre dois vértices
        self.minimal_edges = []
        distance_from_start: list[int] = self._dijkstra(start)
        distance_from_end: list[int] = self._dijkstra(end)
        minimal_distance: int = distance_from_start[end]

        # Verifica todas as arestas para ver se pertencem ao caminho mínimo
        for index, u, v, length in self.edges:
            cond1: bool = distance_from_start[u] + length + distance_from_end[v] == minimal_distance
            cond2: bool = distance_from_start[v] + length + distance_from_end[u] == minimal_distance
            if cond1 or cond2:
                self.minimal_edges.append([index, u, v, length])
        return sorted(self.minimal_edges)
    
    
    def find_critical_edges(self, start: int, end: int) -> set:
        # Encontra todas as arestas críticas, ou seja, que se removidas desconectam o caminho mínimo entre dois vértices
        if not self.minimal_edges: 
            self.find_minimal_edges(start, end) # Usado para evitar chamadas duplicadas
          
        critical_streets: list[int] = []

        # Cria um outro grafo com apenas as arestas mínimas
        minimal_graph: Graph = Graph(self.vertex_count, len(self.minimal_edges))
        for index, u, v, length in self.minimal_edges:
            minimal_graph.add_edge(index, u, v, length)

        for index, u, v, length in minimal_graph.edges:
            # Remover a aresta
            minimal_graph.graph[u] = [(w, l) for (w, l) in minimal_graph.graph[u] if w != v or l != length]
            minimal_graph.graph[v] = [(w, l) for (w, l) in minimal_graph.graph[v] if w != u or l != length]
            # Verificar se o index final foi alcançado pelo dfs:
            reachable_vertices: set = minimal_graph._dfs(start)
            if end not in reachable_vertices:
                critical_streets.append(index)
            # Adicionar a aresta novamente
            minimal_graph.graph[u].append((v, length))
            minimal_graph.graph[v].append((u, length))
        return sorted(critical_streets)