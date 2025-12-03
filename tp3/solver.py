class Solver:
    def __init__(self, elf_number):
        self.n: int = elf_number
        self.adj: list = [0] * self.n

    def add_conflict(self, a, b):
        ia: int = int(a)
        ib: int = int(b)
        self.adj[ia] |= (1 << ib)
        self.adj[ib] |= (1 << ia)

    def generate_valid_subsets(self, group):
        # Gera todos os subsets independentes válidos usando backtracking
        result: list = []
        n: int = len(group)
        
        def backtrack(idx, mask, selected):
            if idx == n:
                result.append((mask, len(selected), selected[:]))
                return
            
            elf: int = group[idx]
            backtrack(idx + 1, mask, selected)
            
            # Verifica se pode incluir este elfo
            can_include: bool = True
            for other in selected:
                if (self.adj[elf] >> other) & 1:
                    can_include = False
                    break
            
            if can_include:
                selected.append(elf)
                backtrack(idx + 1, mask | (1 << elf), selected)
                selected.pop()
        
        backtrack(0, 0, [])
        return result

    def preprocess_group_b(self, valid_b, group_b):
        # Para cada máscara de "proibidos", armazena o melhor subset de B
        b_len: int = len(group_b)
        best_for_mask: dict = {}
        
        for mask_abs, size, elfs in valid_b:
            # Converte máscara absoluta para máscara relativa de B
            mask_rel: int = 0
            for i in range(b_len):
                if (mask_abs >> group_b[i]) & 1:
                    mask_rel |= (1 << i)
            
            # Atualiza se for melhor
            if mask_rel not in best_for_mask:
                best_for_mask[mask_rel] = (size, elfs)
            else:
                prev_size, prev_elfs = best_for_mask[mask_rel]
                if size > prev_size or (size == prev_size and elfs < prev_elfs):
                    best_for_mask[mask_rel] = (size, elfs)
        
        # DP: propaga melhores soluções para todas as submáscaras
        limit: int = 1 << b_len
        dp: list = [(0, [])] * limit
        
        for mask in range(limit):
            if mask in best_for_mask:
                dp[mask] = best_for_mask[mask]
            
            # Tenta remover cada bit e usar a solução da submáscara
            submask: int = mask
            while submask > 0:
                if submask in best_for_mask:
                    sub_size, sub_elfs = best_for_mask[submask]
                    cur_size, cur_elfs = dp[mask]
                    if sub_size > cur_size or (sub_size == cur_size and sub_elfs < cur_elfs):
                        dp[mask] = (sub_size, sub_elfs)
                submask = (submask - 1) & mask
        
        return dp

    def get_solution(self):
        mid: int = self.n // 2
        group_a: list = list(range(mid))
        group_b: list = list(range(mid, self.n))

        # Gera todos os subsets válidos de cada grupo
        valid_a: list = self.generate_valid_subsets(group_a)
        valid_b: list = self.generate_valid_subsets(group_b)

        # Pré-processa B com DP
        b_len: int = len(group_b)
        dp_b: list = self.preprocess_group_b(valid_b, group_b)

        best_solution: list = []
        best_size: int = 0

        # Para cada subset de A, encontra o melhor subset compatível de B
        for mask_a, size_a, elfs_a in valid_a:
            # Calcula máscara de elfos proibidos em B (relativa)
            forbidden_rel: int = 0
            for elf_a in elfs_a:
                for i in range(b_len):
                    elf_b: int = group_b[i]
                    if (self.adj[elf_a] >> elf_b) & 1:
                        forbidden_rel |= (1 << i)
            
            # Máscara de elfos permitidos em B
            allowed_rel: int = ((1 << b_len) - 1) & (~forbidden_rel)
            
            # Busca melhor subset de B compatível
            size_b, elfs_b = dp_b[allowed_rel]
            
            combined: list = sorted(elfs_a + elfs_b)
            total_size: int = size_a + size_b
            
            if total_size > best_size or (total_size == best_size and combined < best_solution):
                best_size = total_size
                best_solution = combined

        return best_solution