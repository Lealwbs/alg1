from queue import Queue
from heapq import heapify, heappop, heappush

class Graph:
    def __init__(self, vertex_count: int) -> None: 
        self.vertex_count: int = vertex_count 
        #self.edges: list[tuple[int, int, int]] = []

        #dict: {int index_vertex, list[(int conected_vertex, int length)]}
        self.graph: dict[int, list[tuple[int, int]]] = { i: [] for i in range(1, vertex_count + 1) }

    def __str__(self) -> str:
        # Escrever uma forma melhor de representar o grafo:
        result = f"Grafo({self.vertex_count} vertices e {len(self.edges)} arestas):\n"
        for from_vertex, to_vertex, length in self.edges:
            result += f"  {from_vertex} <--({length})--> {to_vertex}\n"
        return result
        
    # Por o grafo ser bidirecionado, a função add_edge já adiciona as duas direções
    def add_edge(self, from_vertex: int, to_vertex: int, length: int) -> None:
        #self.edges.append((from_vertex, to_vertex, length))
        self.graph[from_vertex].append((to_vertex, length))
        self.graph[to_vertex].append((from_vertex, length))


    ''' # Parte 1
    Praça central continue sendo de rápido acesos para o principal parque ecológico da cidade.
    Qual a distância mínima da praça (região 1) para o parque (região N), considerando todas as ruas da cidade em funcionamento?
    - Saída: String "Parte 1: ", seguida de distancia_minima_da_regiao_1_para_regiao_N (inteiro). É garantido que há >=1 caminho entre as regiões 1 e N.
    - RESUMO: Imprimir a menor distância entre 1 e N. '''
    def get_minimal_distance(self, start: int, end: int) -> list:
        parent: list[int] = [-1] * (self.vertex_count + 1)
        marked: list[bool] = [False] * (self.vertex_count + 1)
        label: list[int] = [float('inf')] * (self.vertex_count + 1)
        path: list[int] = []

        self._prim(start, parent, marked, label)

        print(parent)
        v = end
        while v != -1:
            path.append(v)
            v = parent[v]

        path.reverse()
        return label[end]
    
#     Enquanto o heap não estiver vazio
# • Remover o menor elemento (min) e marcá-lo
# • Para cada vértice v adjacente a min
# • Se v não estiver marcado e p(min,v) < rotulo[v]
    # • Antecessor[v] = min
    # • Heap.atualizaChave(v,p(min,v))
    # • rotulo[v] = p(min,v)

    def _dijkstra(self, initial_vertex: int, parent: list[int], distances: list[int])




    def _prim(self, initial_vertex: int, parent: list[int], marked: list[bool], label: list[int]):
        label[initial_vertex] = 0
        heap: list[int, int] = [(0, initial_vertex)]   #(weigth, vertex)
        while heap:
            _, u = heappop(heap)
            marked[u] = True
            for v, length in self.graph[u]: # Adjacentes
                if not marked[v] and length < label[v]:
                    parent[v] = u
                    label[v] = length
                    heappush(heap, (length, v))


    def _bfs(self, initial_vertex: int, parent: list[int], marked: list[bool]):
        marked[initial_vertex] = True  
        queue: Queue[int] = Queue()
        queue.put(initial_vertex)
        while not queue.empty():
            v: int = queue.get()
            for adjacent_vertex_index, length in self.graph[v]:
                u: int = adjacent_vertex_index
                if not marked[u]:
                    marked[u] = True
                    parent[u] = v
                    queue.put(u)


    
    ''' # Parte 2
    Identificar todas as ruas que participam de pelo menos uma rota de menor distância da praça para o parque.
    Essas ruas são candidatas importantes (utilizam com mais frequência).
    - Saída: String "Parte 2: ", seguida dos índices das ruas que participam de pelo menos um caminho mínimo entre a região 1 e N.
    - RESUMO: Encontrar todos os caminhos mínimos e imprimir as (índices) arestas que participam desses caminhos. '''
    def find_minimal_streets(self, start: int, end: int) -> set:
        return {-1}


    ''' # Parte 3
    Identificar quais são as ruas críticas da cidade. Essas ruas não podem ser destruidas, visto que caso destruidas, fariam com que a menor distâcia
    entre 1 e N aumentasse, ou tornaria o acesso impossível.
    - Saída: String "Parte 3: ", seguida dos índices das ruas críticas, em ordem crescente. Os índices são definidos pela ordem 
    em que as ruas foram fornecidas na entrada, começando em 1. Se não houver nenhuma, imprima -1.
    RESUMO: Encontrar todas as (índices) das arestas que, se removidas, fariam com que a distância mínima entre 1 e N aumentasse. "R1 R2 ... RN" '''
    def find_critical_streets(self, start: int, end: int) -> set:
        return {-1}
