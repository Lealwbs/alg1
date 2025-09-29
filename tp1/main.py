import os
import sys
from graph import Graph


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
     
    if len(argv) < 2: 
        raise ValueError("Please provide an input file.")

    # Usado para caso os arquivos de teste .txt estejam em uma pasta diferente do main.py
    filepath = get_filepath(argv[1]) 

    with open(filepath, "r") as file:
        lines = file.readlines()

    # Só a primeira linha é lida separadamente para pegar só número de vértices
    header = lines[0].strip().split()
    vertex_count = int(header[0])

    g: Graph = Graph(vertex_count)

    for line in lines[1:]:
        data_str: list[str] = line.strip().split()
        data_int: list[int] = [int(x) for x in data_str]
        vertex_a, vertex_b, street_length = data_int
        g.add_edge(vertex_a, vertex_b, street_length)


    # print(g)

    ''' # Parte 1
    Praça central continue sendo de rápido acesos para o principal parque ecológico da cidade.
    Qual a distância mínima da praça (região 1) para o parque (região N), considerando todas as ruas da cidade em funcionamento?
    - Saída: String "Parte 1: ", seguida de distancia_minima_da_regiao_1_para_regiao_N (inteiro). É garantido que há >=1 caminho entre as regiões 1 e N.
    - RESUMO: Imprimir a menor distância entre 1 e N. '''

    path: list[int] = g.dijkstra(1, vertex_count)
    result = f"Parte 1: {len(path)}\n"

    ''' # Parte 2
    Identificar todas as ruas que participam de pelo menos uma rota de menor distância da praça para o parque.
    Essas ruas são candidatas importantes (utilizam com mais frequência).
    - Saída: String "Parte 2: ", seguida dos índices das ruas que participam de pelo menos um caminho mínimo entre a região 1 e N.
    - RESUMO: Encontrar todos os caminhos mínimos e imprimir as (índices) arestas que participam desses caminhos. '''

    minimal_streets: set[int] = g.find_minimal_streets(1, vertex_count)
    result += f"Parte 2: {sorted(minimal_streets)}\n"

    ''' # Parte 3
    Identificar quais são as ruas críticas da cidade. Essas ruas não podem ser destruidas, visto que caso destruidas, fariam com que a menor distâcia
    entre 1 e N aumentasse, ou tornaria o acesso impossível.
    - Saída: String "Parte 3: ", seguida dos índices das ruas críticas, em ordem crescente. Os índices são definidos pela ordem 
    em que as ruas foram fornecidas na entrada, começando em 1. Se não houver nenhuma, imprima -1.
    RESUMO: Encontrar todas as (índices) das arestas que, se removidas, fariam com que a distância mínima entre 1 e N aumentasse. "R1 R2 ... RN" '''

    critical_streets: set[int] = g.find_critical_streets(1, vertex_count)
    if len(critical_streets) == 0:
        result += "Parte 3: -1"
    else:
        result += f"Parte 3: {sorted(critical_streets)}"

    return result

if __name__ == "__main__":
    # Eu implementei uma classe de teste (tests.py), desta forma, o código funciona em ambos os casos:
    # "python main.py <inputfile>" ou "python tests.py"
    
    output = main()
    print(output)