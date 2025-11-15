# Entrada:
# N  - 1 ≤N ≤50000
# B1 B2 B3 ... BN -  1 ≤Bi ≤N , para 1 ≤i ≤N 

# Saıda:
# Parte 1: H



# Parte 1)
#  um algoritmo guloso

# primeira, ele precisa reconstruir um
# muro de madeira em formato de triˆangulo is ́osceles
# aproveitando ao m ́aximo os blocos j ́a existentes —
# sem desperd ́ıcio e sem adi ̧c ̃oes.

# N pilhas
# Ni tem Bi blocos
# Construir o maior triângulo isóceles possível apenas retirando blocos. 
# Qual altura máxima do triângulo a ser construído.

# Parte 1: num_inteiro_altura_do_maior_triangulo_isosceles_possivel_sem_add_nenhum_bloco

class Builder:
    def __init__(self, blocks):
        self.blocks: list[int] = blocks
    
    def get_maximal_height(self) -> int:
        return 0



