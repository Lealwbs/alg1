class Solver:
    def __init__(self, elf_number):
        self.n = elf_number
        self.adj = [0] * self.n

    def add_conflict(self, a, b):
        ia = int(a)
        ib = int(b)
        self.adj[ia] |= (1 << ib)
        self.adj[ib] |= (1 << ia)

    def is_valid_subset(self, subset):
        """Verifica se um subset não tem conflitos internos"""
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if (self.adj[subset[i]] >> subset[j]) & 1:
                    return False
        return True

    def generate_all_valid_subsets(self, group):
        """Gera todos os subsets independentes de um grupo"""
        result = []
        n = len(group)
        
        for mask in range(1 << n):
            subset = [group[i] for i in range(n) if (mask >> i) & 1]
            if self.is_valid_subset(subset):
                result.append(subset)
        
        return result

    def can_combine(self, subset_a, subset_b):
        """Verifica se dois subsets podem ser combinados"""
        for a in subset_a:
            for b in subset_b:
                if (self.adj[a] >> b) & 1:
                    return False
        return True

    def get_solution(self):
        mid = self.n // 2
        group_a = list(range(mid))
        group_b = list(range(mid, self.n))

        valid_a = self.generate_all_valid_subsets(group_a)
        valid_b = self.generate_all_valid_subsets(group_b)

        best_solution = []
        best_size = 0

        for subset_a in valid_a:
            for subset_b in valid_b:
                if self.can_combine(subset_a, subset_b):
                    combined = sorted(subset_a + subset_b)
                    size = len(combined)
                    
                    if size > best_size:
                        best_size = size
                        best_solution = combined
                    elif size == best_size:
                        if combined < best_solution:
                            best_solution = combined

        return best_solution