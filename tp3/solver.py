class Solver:
    def __init__(self, elf_number: int) -> None:
        self.n: int = elf_number
        self.conflicts: set[tuple[int, int]] = set()

    def add_conflict(self, a: int, b: int) -> None:
        ia: int = int(a)
        ib: int = int(b)
        if ia > ib:
            ia, ib = ib, ia
        self.conflicts.add((ia, ib))

    def has_conflict(self, a: int, b: int) -> bool:
        if a == b:
            return False
        if a > b:
            a, b = b, a
        return (a, b) in self.conflicts

    def is_valid_subset(self, subset: list[int]) -> bool:
        for i in range(len(subset)):
            for j in range(i + 1, len(subset)):
                if self.has_conflict(subset[i], subset[j]):
                    return False
        return True

    def generate_all_valid_subsets(self, group: list[int]) -> list[list[int]]:
        result: list[list[int]] = []
        n = len(group)
        
        # Itera por todas as máscaras possíveis
        for mask in range(1 << n):
            subset = [group[i] for i in range(n) if (mask >> i) & 1]
            if self.is_valid_subset(subset):
                result.append(subset)
        
        return result

    def can_combine(self, subset_a: list[int], subset_b: list[int]) -> bool:
        for a in subset_a:
            for b in subset_b:
                if self.has_conflict(a, b):
                    return False
        return True

    def get_solution(self) -> list[int]:
        # Divide em dois grupos
        mid = self.n // 2
        group_a = list(range(mid))
        group_b = list(range(mid, self.n))

        # Gera todos os subsets válidos de cada grupo
        valid_a = self.generate_all_valid_subsets(group_a)
        valid_b = self.generate_all_valid_subsets(group_b)

        best_solution: list[int] = []
        best_size: int = 0

        # Tenta combinar cada subset de A com cada subset de B
        for subset_a in valid_a:
            for subset_b in valid_b:
                if self.can_combine(subset_a, subset_b):
                    combined = sorted(subset_a + subset_b)
                    size = len(combined)
                    
                    if size > best_size:
                        best_size = size
                        best_solution = combined
                    elif size == best_size:
                        # Desempate lexicográfico
                        if combined < best_solution:
                            best_solution = combined

        return best_solution


if __name__ == "__main__":
    S = Solver(8)
    pairs = [
        (0, 1),
        (2, 3),
        (4, 5),
        (6, 7),
        (0, 2),
        (2, 4),
        (4, 6),
        (1, 3),
        (3, 5),
        (5, 7),
    ]
    for a, b in pairs:
        S.add_conflict(a, b)

    sol = S.get_solution()
    print(len(sol))
    print(" ".join(map(str, sol)))