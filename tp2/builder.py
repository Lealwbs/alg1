class Builder:
    def __init__(self, blocks: list[int]) -> None:
        self.stacks: list[int] = blocks
        self.left: list[int] = [0 for _ in self.stacks]
        self.right: list[int] = [0 for _ in self.stacks]
        self.height: list[int] = [0 for _ in self.stacks]

    
    def get_maximal_height(self) -> int:
        maximal_height: int = 0
        size: int = len(self.stacks)

        # Pulando o primeiro índice da lista normal (esquerda -> direita)
        self.left[0] = 1
        for i in range(1, size):
            self.left[i] = min(self.left[i-1] + 1, self.stacks[i])

        # Pulando o último índice e percorrendo a lista invertida (esquerda <- direita)
        self.right[size-1] = 1
        for i in range(size-2, -1, -1):
            self.right[i] = min(self.right[i+1] + 1, self.stacks[i])

        # Pegando a maior altura do triângulo possível em cada índice e o máximo global
        for i in range(size):
            self.height[i] = min(self.left[i], self.right[i]) 
            maximal_height = max(maximal_height, self.height[i])

        return maximal_height