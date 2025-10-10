import os
import sys
from graph import Graph


# Usado para caso os arquivos de teste .txt estejam em uma pasta diferente do main.py
def get_filepath(filename: str) -> str:
    candidate_paths = [
        filename,
        os.path.join("tp1", filename),
        os.path.join("tp1", "tests", filename)
    ]

    for path in candidate_paths:
        if os.path.exists(path):
            return path

    raise FileNotFoundError(f"File not found in any location: {filename}")


def main(argv=sys.argv) -> str:
    # Adaptação para ler tanto do arquivo (argumento) quanto do stdin (no vpl)
    if len(argv) > 1: 
        filepath = get_filepath(argv[1]) 
        with open(filepath, "r") as file:
            lines = file.readlines()
    elif not sys.stdin.isatty():
        lines = sys.stdin.readlines()
    else:
        raise ValueError("Please provide an input file (argument or stdin).")

    # Só a primeira linha é lida separadamente para pegar o número de vértices e arestas
    header: list[str] = lines[0].strip().split()
    vertex_count: int = int(header[0])
    edges_count: int = int(header[1])
    g: Graph = Graph(vertex_count, edges_count)

    # Lê as linhas da entrada, e adiciona as arestas (com o indice certo) ao grafo
    for index_edge, line in enumerate(lines[1:], start=1): 
        data: list[str] = line.strip().split()
        if not data:
            continue
        edge: list[int] = [int(x) for x in data]
        vertex_a, vertex_b, street_length = edge
        g.add_edge(index_edge, vertex_a, vertex_b, street_length)

    # Constantes armazenando os índices dos vértices de início e fim
    PRACA: int = 1
    PARQUE: int = vertex_count

    # Chamadas das funções que resolvem o problema
    distance: int = g.get_minimal_distance(PRACA, PARQUE)
    minimal_streets: list[tuple] = g.find_minimal_edges(PRACA, PARQUE)
    critical_streets: set[int] = g.find_critical_edges(PRACA, PARQUE)

    # Formatação da saída
    minimal_streets_str = " ".join(str(index) for index, u, v, length in minimal_streets)
    critical_streets_str = " ".join(str(street) for street in critical_streets) if critical_streets else "-1"
    result = f"Parte 1: {distance}\n"
    result += f"Parte 2: {minimal_streets_str}\n"
    result += f"Parte 3: {critical_streets_str}"

    return result 


if __name__ == "__main__":
    # A saída só é impressa no VPL. Nos testes locais (tests.py), o return result é usado para comparação
    output = main()
    print(output) 
    