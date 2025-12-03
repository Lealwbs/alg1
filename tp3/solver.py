class Solver:
    def __init__(self, elf_number):
        self.n: int = elf_number
        # Matriz de adjacência usando bitmasks
        self.adj: list = [0] * self.n

    def add_conflict(self, a, b):
        ia: int = int(a)
        ib: int = int(b)
        # Adiciona conflito bidirecional usando OR bitwise
        self.adj[ia] |= (1 << ib)
        self.adj[ib] |= (1 << ia)

    def get_independent_sets(self, start, end, base):
        # Gera todos os conjuntos independentes válidos usando backtracking
        result: list = []
        n_local: int = end - start
        
        # Pré calcula adjacências locais para evitar shifts repetidos
        local_adj: list = [(self.adj[i] >> start) & ((1 << n_local) - 1) for i in range(start, end)]

        def backtrack(idx, mask, forbidden, count, nodes):
            if idx == n_local:
                result.append((mask, count, nodes[:]))
                return

            # Opção 1: não incluir o elfo atual
            backtrack(idx + 1, mask, forbidden, count, nodes)

            # Opção 2: incluir o elfo se não conflita com nenhum já selecionado
            if not ((forbidden >> idx) & 1):
                nodes.append(base + idx)
                backtrack(idx + 1, mask | (1 << idx), forbidden | local_adj[idx], count + 1, nodes)
                nodes.pop()

        backtrack(0, 0, 0, 0, [])
        return result

    def get_solution(self):
        # Divide elfos em dois grupos para aplicar meet in the middle
        mid: int = self.n // 2
        
        valid_a: list = self.get_independent_sets(0, mid, 0)
        valid_b: list = self.get_independent_sets(mid, self.n, mid)

        # SOS DP: para cada máscara, armazena melhor subset de B compatível
        n_b: int = self.n - mid
        limit_b: int = 1 << n_b
        dp: list = [(0, []) for _ in range(limit_b)]

        # Inicializa DP com os subsets válidos de B
        for mask, size, nodes in valid_b:
            dp[mask] = (size, nodes)

        # Propaga melhores soluções por submáscaras usando SOS DP
        for i in range(n_b):
            bit: int = 1 << i
            for mask in range(limit_b):
                if mask & bit:
                    prev_size, prev_nodes = dp[mask ^ bit]
                    curr_size, curr_nodes = dp[mask]
                    
                    # Atualiza se submáscara tem solução melhor
                    if prev_size > curr_size or (prev_size == curr_size and prev_nodes < curr_nodes):
                        dp[mask] = (prev_size, prev_nodes)

        # Pré calcula quais elfos de B cada elfo de A proíbe
        mask_b_full: int = (1 << n_b) - 1
        adj_a_to_b: list = [(self.adj[i] >> mid) & mask_b_full for i in range(mid)]

        best_solution: list = []
        best_size: int = -1

        # Combina cada subset de A com o melhor subset compatível de B
        for mask_a, size_a, elfs_a in valid_a:
            # Calcula quais elfos de B são proibidos por este subset de A
            forbidden_b: int = 0
            for elf in elfs_a:
                forbidden_b |= adj_a_to_b[elf]
            
            # Busca melhor subset de B usando apenas elfos permitidos
            allowed_b: int = mask_b_full ^ forbidden_b
            size_b, elfs_b = dp[allowed_b]
            total_size: int = size_a + size_b

            # Atualiza melhor solução com desempate lexicográfico
            if total_size > best_size:
                best_size = total_size
                best_solution = sorted(elfs_a + elfs_b)
            elif total_size == best_size:
                candidate: list = sorted(elfs_a + elfs_b)
                if candidate < best_solution:
                    best_solution = candidate

        return best_solution