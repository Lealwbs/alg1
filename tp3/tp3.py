import os, sys
from solver import Solver


# Usado para caso os arquivos de teste .txt estejam em uma pasta diferente do main.py
def get_filepath(filename: str) -> str:
    candidate_paths = [ filename, os.path.join("tp2", filename), os.path.join("tp2", "tests", filename) ]
    for path in candidate_paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"File not found in any location: {filename}")


def get_lines(argv: str) -> list[str]:
    # Adaptação para ler tanto do arquivo (argumento) quanto do stdin (no vpl)
    if len(argv) > 1: 
        filepath = get_filepath(argv[1]) 
        with open(filepath, "r") as file:
            return file.readlines()
    if not sys.stdin.isatty():
        return sys.stdin.readlines()
    raise ValueError("Please provide an input file (argument or stdin).")


def main(argv=sys.argv) -> str:
    lines = get_lines(argv)
    S: Solver = Solver()
    
    # # O tamanho do vetor de pilhas e nem a quantidade de árvores (linhas 0 e 1) não são necessárias aqui.
    # stack_list: list[int] = list(map(int, lines[1].strip().split()))
    # wall: Builder = Builder(stack_list)
    # park: Grid = Grid()

    # # Lê as linhas da entrada, e adiciona as coordenadas (com o indice) no Grid.
    # for index, line in enumerate(lines[3:], start=1): 
    #     data: list[float] = line.strip().split()
    #     if not data: 
    #         continue
    #     coord_x, coord_y = float(data[0]), float(data[1])
    #     park.add_point(index, coord_x, coord_y)

    # # Chamadas das funções que resolvem o problema
    # max_triangle_height: int = wall.get_maximal_height()
    # minimal_perimeter_points: tuple[int, int, int] = park.get_minimal_perimeter_points()
    # minimal_perimeter_value: float = park.perimeter(*minimal_perimeter_points)
    # result_points: str = " ".join(map(str, minimal_perimeter_points))

    # result = f"Parte 1: {max_triangle_height}\n"
    # result += f"Parte 2: {minimal_perimeter_value:.4f} {result_points}\n"
    
    return "" #result 


if __name__ == "__main__":
    # A saída só é impressa no VPL. Nos testes locais (tests.py), o return result é usado para comparação
    output: str = main()
    print(output) 