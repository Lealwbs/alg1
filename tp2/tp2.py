import os, sys
from builder import Builder
from grid import Grid


# Usado para caso os arquivos de teste .txt estejam em uma pasta diferente do main.py
def get_filepath(filename: str) -> str:
    candidate_paths = [ filename, os.path.join("tp2", filename), os.path.join("tp2", "tests", filename) ]
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

    # O tamanho do vetor de pilhas e nem a quantidade de árvores (linhas 0 e 1) não são necessárias aqui.
    stack_list: list[int] = lines[1].strip().split()
    wall: Builder = Builder(stack_list)
    park: Grid = Grid()

    # Lê as linhas da entrada, e adiciona as coordenadas (com o indice) no Grid.
    for index, line in enumerate(lines[3:], start=1): 
        data: list[float] = line.strip().split()
        if not data: 
            continue
        coord_x, coord_y = float(data[0]), float(data[1])
        park.add_point(index, coord_x, coord_y)

    # Chamadas das funções que resolvem o problema
    max_triangle_height: int = wall.get_maximal_height()
    minimal_perimeter_points: tuple[int, int, int] = park.get_minimal_perimeter_points()
    minimal_perimeter_value: float = park.get_perimeter(*minimal_perimeter_points)

    result = f"Parte 1: {max_triangle_height}\n"
    result += f"Parte 2: {minimal_perimeter_value:.4f} {" ".join(map(str, minimal_perimeter_points))}\n"

    #print(park)
    
    return result  # Parte 2: P A1 A2 A3  (P: com exatamente quatro casas decimais, indices, ordem crescente, lexicograficamente menor)


if __name__ == "__main__":
    # A saída só é impressa no VPL. Nos testes locais (tests.py), o return result é usado para comparação
    output: str = main()
    print(output) 
    


