class Builder:
    def __init__(self, blocks):
        self.blocks: list[int] = blocks
    
    def get_maximal_height(self) -> int:
        return 0


# Algorítmo Guloso
# Construir o maior triângulo isóceles possível apenas retirando blocos. 
# Qual altura máxima do triângulo a ser construído.