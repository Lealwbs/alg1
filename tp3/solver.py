class Solver:
    def __init__(self, elf_number):
        self.n: int = elf_number
        # Matriz de adjacência usando bitmasks para performance
        self.adj: list = [0] * self.n

    def add_conflict(self, a, b):
        ia: int = int(a)
        ib: int = int(b)
        self.adj[ia] |= (1 << ib)
        self.adj[ib] |= (1 << ia)

    def get_independent_sets(self, start_index, end_index, base_index=0):
        """
        Gera todos os conjuntos independentes maximais para um intervalo de elfos
        usando backtracking com poda (pruning).
        Retorna uma lista de tuplas: (mask_relativa, tamanho, lista_nos_absoluta)
        """
        result = []
        n_local = end_index - start_index
        
        # Mapeia adjacências para o sistema de coordenadas relativo (0 a n_local-1)
        # para evitar shifts caros durante a recursão
        local_adj = []
        for i in range(start_index, end_index):
            # Pega apenas os bits relevantes para este grupo
            mask = (self.adj[i] >> start_index) & ((1 << n_local) - 1)
            local_adj.append(mask)

        def backtrack(idx, current_mask, forbidden_mask, count, nodes):
            if idx == n_local:
                result.append((current_mask, count, nodes))
                return

            # Opção 1: Não incluir o elfo atual
            backtrack(idx + 1, current_mask, forbidden_mask, count, nodes)

            # Opção 2: Incluir o elfo atual (apenas se não for proibido)
            if not ((forbidden_mask >> idx) & 1):
                # O novo forbidden inclui os vizinhos deste elfo (localmente)
                new_forbidden = forbidden_mask | local_adj[idx]
                # Pequena otimização: se, mesmo incluindo este nó, não for possível
                # superar o melhor count (heurística), poderíamos cortar, 
                # mas aqui queremos listar todos os válidos para a DP.
                
                # Lista imutável na recursão é mais seguro/limpo em Python
                backtrack(idx + 1, current_mask | (1 << idx), new_forbidden, count + 1, nodes + [base_index + idx])

        backtrack(0, 0, 0, 0, [])
        return result

    def get_solution(self):
        mid = self.n // 2
        
        # --- Passo 1: Resolver Grupo A (0 até mid) ---
        # Gera todas as combinações válidas de A
        valid_a = self.get_independent_sets(0, mid, 0)

        # --- Passo 2: Resolver Grupo B (mid até n) ---
        n_b = self.n - mid
        # Gera todas as combinações válidas de B
        # O retorno é (mask_relativa_B, tamanho, lista_absoluta)
        valid_b = self.get_independent_sets(mid, self.n, mid)

        # --- Passo 3: Pré-processamento de B com SOS DP (Sum Over Subsets) ---
        # dp[mask] armazenará a MELHOR tupla (tamanho, lista_de_elfos) 
        # que pode ser formada usando APENAS subconjuntos dos bits ativos em 'mask'.
        limit_b = 1 << n_b
        # Inicializa com um valor sentinela neutro
        dp = [(0, []) for _ in range(limit_b)]

        # Preenche com os conjuntos válidos encontrados
        for mask, size, nodes in valid_b:
            dp[mask] = (size, nodes)

        # Propagação (SOS DP)
        # Complexidade O(n_b * 2^n_b) - muito mais rápido que iterar submasks
        for i in range(n_b):
            bit = 1 << i
            for mask in range(limit_b):
                if mask & bit:
                    # Compara a solução atual com a solução sem o bit 'i'
                    # Queremos maximizar tamanho, e depois critério de desempate léxico
                    prev_size, prev_nodes = dp[mask ^ bit]
                    curr_size, curr_nodes = dp[mask]
                    
                    # Lógica de comparação: Maior tamanho ganha.
                    # Se tamanhos iguais, menor lista (lexicograficamente) ganha.
                    if prev_size > curr_size:
                        dp[mask] = (prev_size, prev_nodes)
                    elif prev_size == curr_size:
                        if prev_nodes < curr_nodes: # Python compara listas elemento a elemento
                            dp[mask] = (prev_size, prev_nodes)
        
        # --- Passo 4: Combinar A e B ---
        best_solution = []
        best_size = -1

        # Pré-cálculo das adjacências de A para B para agilizar o loop
        # adj_a_to_b[i] terá a máscara de vizinhos em B (relativa a B) do elfo i (de A)
        adj_a_to_b = []
        mask_b_full = (1 << n_b) - 1
        for i in range(mid):
            rel_adj = (self.adj[i] >> mid) & mask_b_full
            adj_a_to_b.append(rel_adj)

        for mask_a, size_a, elfs_a in valid_a:
            # Calcula quais elfos em B são proibidos dado o conjunto escolhido em A
            forbidden_in_b = 0
            for elf_idx in elfs_a:
                forbidden_in_b |= adj_a_to_b[elf_idx]
            
            # Os permitidos são o inverso dos proibidos
            allowed_mask_b = mask_b_full ^ forbidden_in_b
            
            # Busca a melhor solução de B compatível em O(1)
            size_b, elfs_b = dp[allowed_mask_b]
            
            total_size = size_a + size_b
            
            if total_size > best_size:
                best_size = total_size
                # Concatenação e sort podem ser caros, fazemos apenas se necessário
                best_solution = sorted(elfs_a + elfs_b)
            elif total_size == best_size:
                # Desempate léxico
                candidate = sorted(elfs_a + elfs_b)
                if candidate < best_solution:
                    best_solution = candidate

        return best_solution