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
        lines = input().splitlines()
    else:
        raise ValueError("Please provide an input file (argument or stdin).")

    # Só a primeira linha é lida separadamente para pegar só o número de vértices
    header = lines[0].strip().split()
    vertex_count = int(header[0])
    g: Graph = Graph(vertex_count)
    for line in lines[1:]:
        data: list[str] = line.strip().split()
        edge: list[int] = [int(x) for x in data]
        vertex_a, vertex_b, street_length = edge
        g.add_edge(vertex_a, vertex_b, street_length)

    distance: int = g.get_minimal_distance(1, vertex_count)
    result = f"Parte 1: {distance}\n"

    minimal_streets: set[int] = g.find_minimal_streets(1, vertex_count)
    result += f"Parte 2: " + " ".join(str(street) for street in sorted(minimal_streets)) + "\n"

    critical_streets: set[int] = g.find_critical_streets(1, vertex_count)
    if len(critical_streets) == 0: 
        result += "Parte 3: -1"
    else: 
        result += f"Parte 3: " + " ".join(str(street) for street in sorted(critical_streets))

    return result 


if __name__ == "__main__":
    output = main()
    print(output) # Para validação no VPL