from math import sqrt

def calcular_altura_triangulo(pilhas):
    """Calcula a altura máxima do triângulo isósceles usando algoritmo guloso"""
    pilhas_ordenadas = sorted(pilhas, reverse=True)
    altura = 0
    
    while True:
        largura_necessaria = 2 * altura + 1
        if len(pilhas_ordenadas) < largura_necessaria:
            break
        
        # Verifica se há blocos suficientes para a próxima linha
        blocos_necessarios = sum(range(1, largura_necessaria + 1))
        blocos_disponiveis = sum(pilhas_ordenadas[:largura_necessaria])
        
        if blocos_disponiveis >= blocos_necessarios:
            altura += 1
        else:
            break
    
    return altura

def distancia(p1, p2):
    """Calcula distância euclidiana entre dois pontos"""
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def perimetro(p1, p2, p3):
    """Calcula perímetro de um triângulo"""
    return distancia(p1, p2) + distancia(p2, p3) + distancia(p3, p1)

def encontrar_menor_perimetro(pontos):
    """Força bruta para encontrar o menor perímetro"""
    n = len(pontos)
    min_perim = float('inf')
    melhor_tripla = (1, 2, 3)
    
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                perim = perimetro(pontos[i], pontos[j], pontos[k])
                if perim < min_perim:
                    min_perim = perim
                    melhor_tripla = (i + 1, j + 1, k + 1)  # Índices começam em 1
                elif abs(perim - min_perim) < 1e-9:  # Considera empate
                    candidato = (i + 1, j + 1, k + 1)
                    if candidato < melhor_tripla:
                        melhor_tripla = candidato
    
    return min_perim, melhor_tripla

def gerar_caso(num, pilhas, pontos, descricao=""):
    """Gera entrada e saída para um caso de teste e salva em arquivos"""
    print(f"\nGerando Caso {num}: {descricao}")
    
    # Gerar arquivo de entrada
    in_filename = f"in{num:02d}.txt"
    with open(in_filename, 'w') as f:
        f.write(f"{len(pilhas)}\n")
        f.write(' '.join(map(str, pilhas)) + '\n')
        f.write(f"{len(pontos)}\n")
        for x, y in pontos:
            f.write(f"{x} {y}\n")
    
    # Calcular respostas
    altura = calcular_altura_triangulo(pilhas)
    perim, tripla = encontrar_menor_perimetro(pontos)
    
    # Gerar arquivo de saída
    out_filename = f"out{num:02d}.txt"
    with open(out_filename, 'w') as f:
        f.write(f"Parte 1: {altura}\n")
        f.write(f"Parte 2: {perim:.4f} {tripla[0]} {tripla[1]} {tripla[2]}\n")
    
    print(f"  ✓ Criado {in_filename} e {out_filename}")

# ===== GERAR TODOS OS CASOS =====

print("="*60)
print("GERADOR DE CASOS DE TESTE - TP2 ALGORITMOS I")
print("="*60)

# CASO 04: Triângulo equilátero perfeito
gerar_caso(4, 
    [6, 5, 4, 3, 2, 1],
    [(0, 0), (4, 0), (2, 3)],
    "Pequeno - Triângulo quase equilátero")

# CASO 05: Pontos muito próximos
gerar_caso(5,
    [3, 3, 3, 3, 3],
    [(0, 0), (1, 0), (2, 0), (0, 1)],
    "Pequeno - Pontos próximos com um afastado")

# CASO 06: Grid regular
gerar_caso(6,
    [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6],
    [(i, j) for i in range(4) for j in range(4)],
    "Médio - Grid 4x4 regular")

# CASO 07: Pontos esparsos com triângulo pequeno no meio
gerar_caso(7,
    [15] * 20,
    [(0, 0), (10, 0), (5, 8), (3, 3), (7, 3), (5, 1), (2, 5), (8, 5)],
    "Médio - Pontos esparsos")

# CASO 08: Diagonal crescente
gerar_caso(8,
    [2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [(i * 2, i) for i in range(10)],
    "Médio - Pontos em diagonal")

# CASO 09: Coordenadas negativas
gerar_caso(9,
    [8, 7, 6, 5, 4, 3, 2, 1, 9, 8, 7, 6, 5, 4, 3, 2, 1],
    [(-5, -5), (-2, -2), (0, 0), (2, 2), (5, 5), (-3, 3), (3, -3)],
    "Médio - Coordenadas negativas")

# CASO 10: Pontos duplicados
gerar_caso(10,
    [12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 10, 9, 8],
    [(1, 1), (1, 1), (2, 2), (3, 3), (10, 1), (1, 10)],
    "Médio - Pontos duplicados (teste de robustez)")

print("\n" + "="*60)
print("✓ TODOS OS 7 CASOS GERADOS COM SUCESSO!")
print("  Arquivos criados: in04.txt até in10.txt")
print("                    out04.txt até out10.txt")
print("="*60)