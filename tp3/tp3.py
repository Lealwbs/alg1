import os, sys
from solver import Solver


# Usado para caso os arquivos de teste .txt estejam em uma pasta diferente do main.py
def get_filepath(filename: str) -> str:
    candidate_paths = [ filename, os.path.join("tp2", filename), os.path.join("tp2", "tests", filename) ]
    for path in candidate_paths:
        if os.path.exists(path):
            return path
    raise FileNotFoundError(f"File not found in any location: {filename}")


# Adaptação para ler tanto do arquivo (argumento) quanto do stdin (no vpl)
def get_lines(argv: str) -> list[str]:
    if len(argv) > 1: 
        filepath = get_filepath(argv[1]) 
        with open(filepath, "r") as file:
            return file.readlines()
    if not sys.stdin.isatty():
        return sys.stdin.readlines()
    raise ValueError("Please provide an input file (argument or stdin).")


def main(argv=sys.argv) -> str:
    lines = get_lines(argv)

    header: list[str] = lines[0].strip().split() # N e M
    elf_number: int = int(header[0])
    elf_conflict: int = int(header[1]) # Desnecessário aqui

    S: Solver = Solver(elf_number)

    # Lê as linhas da entrada, e adiciona os conflitos entre elfos no resolvedor
    for line in lines[2:]: 
        data: list[float] = line.strip().split()
        if not data: 
            continue
        elf_a, elf_b = float(data[0]), float(data[1])
        S.add_conflict(elf_a, elf_b)

    # Chamada da funçõe que resolve o problema
    elfs_list: list[int] = [1, 2, 3] # S.get_solution()

    elfs_result: str = str(len(elfs_list))
    elfs_result += "\n" + " ".join(str(elf) for elf in elfs_list)
    
    return elfs_result


if __name__ == "__main__":
    # A saída só é impressa no VPL. Nos testes locais (tests.py), o return result é usado para comparação
    output: str = main()
    print(output) 