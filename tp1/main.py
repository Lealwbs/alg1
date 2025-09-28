import os
import sys
import graph

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
        data = file.read()

    print(data)
    return data


if __name__ == "__main__":
    main()



'''
Somatório possui N regiões (vértices 1-N) e M ruas (arestas).
Todas as ruas são de duplos sentido, e possuem uma distância associada.
3 Perguntas:


# Parte 1
Praça central continue sendo de rápido acesos para o principal parque ecológico da cidade.
Qual a distância mínima da praça (região 1) para o parque (região N), considerando todas as ruas da cidade em funcionamento?
- Saída: String "Parte 1: ", seguida de distancia_minima_da_regiao_1_para_regiao_N (inteiro). É garantido que há >=1 caminho entre as regiões 1 e N.
- RESUMO: Imprimir a menor distância entre 1 e N. 

# Parte 2
Identificar todas as ruas que participam de pelo menos uma rota de menor distância da praça para o parque.
Essas ruas são candidatas importantes (utilizam com mais frequência).
- Saída: String "Parte 2: ", seguida dos índices das ruas que participam de pelo menos um caminho mínimo entre a região 1 e N.
- RESUMO: Encontrar todos os caminhos mínimos e imprimir as arestas que participam desses caminhos.

# Parte 3
Identificar quais são as ruas críticas da cidade. Essas ruas não podem ser destruidas, visto que caso destruidas, fariam com que a menor distâcia
entre 1 e N aumentasse, ou tornaria o acesso impossível.
- Saída: String "Parte 3: ", seguida dos índices das ruas críticas, em ordem crescente. Os índices são definidos pela ordem 
em que as ruas foram fornecidas na entrada, começando em 1. Se não houver nenhuma, imprima -1.
RESUMO: Encontrar todas as arestas que, se removidas, fariam com que a distância mínima entre 1 e N aumentasse.
'''

    
'''

Entrada:
N M         # N regiões (vértices) e M ruas (arestas)
A1 B1 C1    # Ai e Bi regiões que rua i conecta, Ci comprimento da rua i
A2 B2 C2    
...
AM BM CM


Saída:
Parte 1: D              # a distância encontrada na primeira tarefa.
Parte 2: R1 R2 ... RN   # e os índices das ruas encontradas na segunda tarefa, separados por espaço.
Parte 3: R1 R2 ... RN   # e os índices das ruas encontradas na terceira tarefa, separados por espaço.

'''