class Solver:
    def __init__(self, elf_number):
        self.n: int = elf_number
        self.adj: list = [0] * self.n

    def add_conflict(self, a, b):
        ia: int = int(a)
        ib: int = int(b)
        self.adj[ia] |= (1 << ib)
        self.adj[ib] |= (1 << ia)

    def get_independent_sets(self, start, end, adj_remote=None):
        result: list = []
        n_local: int = end - start
        
        # Pre-calcula adjacências locais (0 a n_local-1)
        local_adj: list = []
        remote_impact: list = [] # Impacto que cada nó local tem no grupo remoto

        for i in range(start, end):
            # Máscara de conflito interna (relativa ao grupo)
            mask_l = (self.adj[i] >> start) & ((1 << n_local) - 1)
            local_adj.append(mask_l)
            
            # Máscara de conflito externa (se fornecida)
            if adj_remote:
                remote_impact.append(adj_remote[i])
            else:
                remote_impact.append(0)

        def backtrack(idx, mask, forbidden, remote_forbidden, count):
            if idx == n_local:
                result.append((mask, count, remote_forbidden))
                return

            # Opção 1: não incluir o elfo atual
            backtrack(idx + 1, mask, forbidden, remote_forbidden, count)

            # Opção 2: incluir o elfo (se permitido)
            if not ((forbidden >> idx) & 1):
                # Atualiza restrições locais e remotas bit a bit
                new_forbidden = forbidden | local_adj[idx]
                new_remote = remote_forbidden | remote_impact[idx]
                
                backtrack(idx + 1, mask | (1 << idx), new_forbidden, new_remote, count + 1)

        backtrack(0, 0, 0, 0, 0)
        return result

    def is_lex_smaller(self, mask1, mask2):
        if mask1 == mask2: return False
        diff = mask1 ^ mask2
        lsb = diff & -diff # Pega o bit menos significativo da diferença
        # Se o bit diferente mais baixo está em mask1, então mask1 tem o menor índice
        return (mask1 & lsb) != 0

    def get_solution(self):
        mid: int = self.n // 2
        n_b: int = self.n - mid
        
        # Não precisamos de adj_remote para o grupo B
        valid_b: list = self.get_independent_sets(mid, self.n, adj_remote=None)

        # SOS DP Otimizada: Armazena apenas (tamanho, máscara) -> O(1) espaço por estado
        limit_b: int = 1 << n_b
        # Usar bytearray para 'sizes' economiza ainda mais RAM (tamanhos <= 40 cabem em 1 byte)
        dp_size = bytearray(limit_b) 
        dp_mask = [0] * limit_b

        for mask, size, _ in valid_b:
            dp_size[mask] = size
            dp_mask[mask] = mask

        # Propaga SOS DP
        for i in range(n_b):
            bit: int = 1 << i
            for mask in range(limit_b):
                if mask & bit:
                    prev = mask ^ bit
                    # Lógica de atualização: Maior tamanho ganha, ou desempate léxico
                    if dp_size[prev] > dp_size[mask]:
                        dp_size[mask] = dp_size[prev]
                        dp_mask[mask] = dp_mask[prev]
                    elif dp_size[prev] == dp_size[mask]:
                        if self.is_lex_smaller(dp_mask[prev], dp_mask[mask]):
                            dp_mask[mask] = dp_mask[prev]

        # Prepara adjacências de A para B para cálculo incremental
        mask_b_full: int = (1 << n_b) - 1
        adj_a_to_b: list = [0] * self.n
        for i in range(mid):
            adj_a_to_b[i] = (self.adj[i] >> mid) & mask_b_full

        # Gera A já calculando a máscara de proibição em B
        valid_a: list = self.get_independent_sets(0, mid, adj_remote=adj_a_to_b)

        best_size: int = -1
        best_mask_a: int = 0
        best_mask_b: int = 0

        for mask_a, size_a, forbidden_b in valid_a:
            # Recupera o melhor de B compatível em O(1)
            allowed_b: int = mask_b_full ^ forbidden_b
            size_b: int = dp_size[allowed_b]
            
            total_size: int = size_a + size_b

            if total_size > best_size:
                best_size = total_size
                best_mask_a = mask_a
                best_mask_b = dp_mask[allowed_b]
            elif total_size == best_size:
                # Desempate léxico comparando as máscaras de A
                if self.is_lex_smaller(mask_a, best_mask_a):
                    best_mask_a = mask_a
                    best_mask_b = dp_mask[allowed_b]
                elif mask_a == best_mask_a:
                    # Se A for igual, desempata pelo B
                    if self.is_lex_smaller(dp_mask[allowed_b], best_mask_b):
                        best_mask_b = dp_mask[allowed_b]

        # Só converte bits para lista UMA vez no final
        final_solution: list = []
        
        # Adiciona nós de A
        for i in range(mid):
            if (best_mask_a >> i) & 1:
                final_solution.append(i)
        
        # Adiciona nós de B
        for i in range(n_b):
            if (best_mask_b >> i) & 1:
                final_solution.append(mid + i)

        return sorted(final_solution)