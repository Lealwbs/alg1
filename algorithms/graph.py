class Node:
    def __init__(self, id: int) -> None:
        self.adjacents: list[(int, int)] = []  # (vertex, weight)
        self.id: int = id


    def __str__(self) -> str:
        return f"NODE {self.id}: {self.adjacents}"



class Edge:
    def __init__(self, node_a: int, node_b: int, id: int, weight: int = 0) -> None:
        self.node_a = node_a
        self.node_b = node_b
        self.weight = weight
        self.id = id



class Graph:
    def __init__(self, directed_graph: bool = False, weighted_edges: bool = False):
        self.digraph: bool = directed_graph
        self.weighted: bool = weighted_edges
        self.nodes: dict[Node] = {}
        self.edges: dict[Edge] = {}
        self.nodes_count: int = 0
        self.edges_count: int = 0


    def __str__(self) -> str:
        result = f"GRAPH ({self.nodes_count} NODES and {self.edges_count} EDGES):\n\n"
        arrow: str = self.digraph * ">"
        result += f"EDGE ID: Node From --(Edge Weight)--{arrow} Node To\n"
        for index, edge in self.edges.items():
            result += f"EDGE {index}: {edge.node_a} --({edge.weight}w)--{arrow} {edge.node_b}\n"

        result += f"\nNODE ID: [Adjacent(ID, Weight), ...]"
        for node in self.nodes.values():
            result += f"\n{node}"
        return result
    

    def get_free_edge_id(self, candidate_id: int = -1) -> int:
        if candidate_id != -1 and candidate_id not in self.edges: 
            return candidate_id
        for potential_id in range(self.edges_count+1):
            if potential_id not in self.edges:
                return potential_id


    def add_edge(self, node_from: int, node_to: int, weight: int = 0, id = -1) -> int:
        if not self.weighted: 
            weight = 0

        free_edge_id: int = self.get_free_edge_id(candidate_id = id)
        self.edges[free_edge_id] = (Edge(node_from, node_to, free_edge_id, weight))
        self.edges_count += 1

        if node_from not in self.nodes:
            tmp_node: Node = Node(node_from)
            self.nodes[node_from] = tmp_node
            self.nodes_count += 1

        if node_to not in self.nodes:
            tmp_node: Node = Node(node_to)
            self.nodes[node_to] = tmp_node
            self.nodes_count += 1

        self.nodes[node_from].adjacents.append((node_to, weight))
        if not self.digraph: 
            self.nodes[node_to].adjacents.append((node_from, weight))

        return free_edge_id
        

    def add_node(self):
        pass


    def pop_edge(self, id: int):
        pass
    

    def pop_node(self, id: int):
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



if __name__ == "__main__":
    G: Graph = Graph()

    G.add_edge(0, 1)
    G.add_edge(0, 2)
    G.add_edge(0, 3)
    G.add_edge(1, 2)
    G.add_edge(2, 3)
    G.add_edge(3, 4)
    G.add_edge(4, 5)

    print(G)
