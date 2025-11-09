from math import sqrt, pow
from time import time
from tests import Test

class Fibonacci:
    def __init__(self) -> None:
        self.saved: int = 2
        self.cache: dict[int:int] = { 0: 0, 1: 1 }

    def reset_cache(self) -> None:
        self.saved = 2
        self.cache = { 0: 0, 1: 1 }

    def fib_iterative(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        sum: int = 0
        a: int = 1
        b: int = 0
        for i in range(2, n+1):
            sum = a + b
            b = a
            a = sum
        return sum

    def fib_recursive(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        return self.fib_recursive(n-1) + self.fib_recursive(n-2)

    def fib_exponential(self, n: int) -> int:
        if n == 0: return 0
        if n == 1: return 1
        a: float = (1 + sqrt(5))/2 
        b: float = (1 - sqrt(5))/2
        result: float = (pow(a, n) + pow(b, n)) / sqrt(5) 
        return round(result)

    def fib_cache(self, n: int) -> int:
        if n not in self.cache:
            for i in range(self.saved, n+1):
                self.cache[i] = self.cache[i-1] + self.cache[i-2] 
                self.saved += 1
        return self.cache[n]
    
    def print_fib_iterations(self, start: int, end: int) -> None:
        for i in range(start, end+1):
            print(f"Iteração {i:>3}:")
            print(f"ITERA: {self.get_time(self.fib_iterative,   i):.6f}") 
            print(f"RECUR: {self.get_time(self.fib_recursive,   i):.6f}") 
            print(f"EXPON: {self.get_time(self.fib_exponential, i):.6f}")
            print(f"CACHE: {self.get_time(self.fib_cache,       i):.6f}")
            print()

    def get_time(self, func, param: int) -> float:
        start_time: float = time()
        func(param)
        end_time: float = time()
        result: float = (end_time - start_time)
        return result


if __name__ == "__main__":
    #F.print_fib_iterations(0, 20)
    F: Fibonacci = Fibonacci()
    T: Test = Test("Fibonacci Unit Test")

    # ==========================================
    # SEÇÃO 1: CASOS BASE E EDGE CASES
    # ==========================================
    
    # Teste n=0 (primeiro caso base)
    T.assert_equals(F.fib_iterative(0), 0, "Iterative: n=0 should return 0")
    T.assert_equals(F.fib_recursive(0), 0, "Recursive: n=0 should return 0")
    T.assert_equals(F.fib_exponential(0), 0, "Exponential: n=0 should return 0")
    T.assert_equals(F.fib_cache(0), 0, "Cache: n=0 should return 0")

    # Teste n=1 (segundo caso base)
    T.assert_equals(F.fib_iterative(1), 1, "Iterative: n=1 should return 1")
    T.assert_equals(F.fib_recursive(1), 1, "Recursive: n=1 should return 1")
    T.assert_equals(F.fib_exponential(1), 1, "Exponential: n=1 should return 1")
    T.assert_equals(F.fib_cache(1), 1, "Cache: n=1 should return 1")

    # Teste n=2 (primeiro caso calculado)
    T.assert_equals(F.fib_iterative(2), 1, "Iterative: n=2 should return 1")
    T.assert_equals(F.fib_recursive(2), 1, "Recursive: n=2 should return 1")
    T.assert_equals(F.fib_exponential(2), 1, "Exponential: n=2 should return 1")
    T.assert_equals(F.fib_cache(2), 1, "Cache: n=2 should return 1")

    # ==========================================
    # SEÇÃO 2: SEQUÊNCIA BÁSICA (0-20)
    # ==========================================
    
    fibonacci_sequence = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 
                         377, 610, 987, 1597, 2584, 4181, 6765]
    
    for n, expected in enumerate(fibonacci_sequence):
        T.assert_equals(F.fib_iterative(n), expected, f"Iterative: fib({n}) = {expected}")
    
    for n, expected in enumerate(fibonacci_sequence):
        T.assert_equals(F.fib_recursive(n), expected, f"Recursive: fib({n}) = {expected}")
    
    for n, expected in enumerate(fibonacci_sequence):
        T.assert_equals(F.fib_exponential(n), expected, f"Exponential: fib({n}) = {expected}")
    
    for n, expected in enumerate(fibonacci_sequence):
        T.assert_equals(F.fib_cache(n), expected, f"Cache: fib({n}) = {expected}")

    # ==========================================
    # SEÇÃO 3: VALORES MÉDIOS (21-50)
    # ==========================================
    
    medium_values = {
        21: 10946,
        25: 75025,
        30: 832040,
        35: 9227465,
        40: 102334155,
        45: 1134903170,
        50: 12586269025
    }
    
    for n, expected in medium_values.items():
        T.assert_equals(F.fib_iterative(n), expected, f"Iterative: medium value fib({n})")
        T.assert_equals(F.fib_exponential(n), expected, f"Exponential: medium value fib({n})")
        T.assert_equals(F.fib_cache(n), expected, f"Cache: medium value fib({n})")

    # ==========================================
    # SEÇÃO 4: CONSISTÊNCIA ENTRE MÉTODOS
    # ==========================================
    
    # Teste consistência para n=0 até n=32 (recursive fica lento depois)
    for n in range(0, 32):
        iter_val = F.fib_iterative(n)
        rec_val = F.fib_recursive(n)
        exp_val = F.fib_exponential(n)
        cache_val = F.fib_cache(n)
        
        T.assert_equals(iter_val, rec_val, f"Consistency: iter==recursive (n={n})")
        T.assert_equals(iter_val, exp_val, f"Consistency: iter==exponential (n={n})")
        T.assert_equals(iter_val, cache_val, f"Consistency: iter==cache (n={n})")

    # ==========================================
    # SEÇÃO 5: PROPRIEDADES MATEMÁTICAS
    # ==========================================
    
    # Propriedade: F(n+1) = F(n) + F(n-1)
    for n in range(2, 30):
        fn_plus_1 = F.fib_cache(n + 1)
        fn = F.fib_cache(n)
        fn_minus_1 = F.fib_cache(n - 1)
        T.assert_equals(fn_plus_1, fn + fn_minus_1, 
                       f"Property: F({n+1}) = F({n}) + F({n-1})")

    # Propriedade: F(2n) = F(n) * [2*F(n+1) - F(n)]
    test_indices = [5, 10, 15, 20, 25]
    for n in test_indices:
        f_2n = F.fib_cache(2 * n)
        f_n = F.fib_cache(n)
        f_n_plus_1 = F.fib_cache(n + 1)
        expected = f_n * (2 * f_n_plus_1 - f_n)
        T.assert_equals(f_2n, expected, 
                       f"Property: F(2*{n}) = F({n}) * [2*F({n+1}) - F({n})]")

    # Propriedade: soma dos primeiros n números de Fibonacci
    # F(0) + F(1) + ... + F(n) = F(n+2) - 1
    for n in range(5, 25, 5):
        sum_fib = sum(F.fib_cache(i) for i in range(n + 1))
        expected = F.fib_cache(n + 2) - 1
        T.assert_equals(sum_fib, expected, 
                       f"Property: Sum of first {n+1} Fibonacci = F({n+2}) - 1")

    # ==========================================
    # SEÇÃO 6: CACHE FUNCTIONALITY
    # ==========================================
    
    # Teste: cache inicial tem 2 elementos
    F_new = Fibonacci()
    T.assert_equals(len(F_new.cache), 2, "Cache: initial size should be 2")
    T.assert_equals(F_new.saved, 2, "Cache: initial saved index should be 2")
    
    # Teste: cache cresce ao calcular novos valores
    initial_size = len(F_new.cache)
    F_new.fib_cache(10)
    T.assert_equals(len(F_new.cache), 11, "Cache: should have 11 entries after fib(10)")
    T.assert_equals(len(F_new.cache) > initial_size, True, "Cache: should grow")
    
    # Teste: valores já calculados não expandem cache
    size_before = len(F_new.cache)
    F_new.fib_cache(5)
    T.assert_equals(len(F_new.cache), size_before, "Cache: shouldn't grow for cached values")
    
    # Teste: cache mantém valores corretos
    for i in range(11):
        T.assert_equals(i in F_new.cache, True, f"Cache: should contain key {i}")
    
    # Teste: cálculo não-sequencial expande cache corretamente
    F_new2 = Fibonacci()
    F_new2.fib_cache(20)
    T.assert_equals(len(F_new2.cache), 21, "Cache: should have 21 entries after fib(20)")
    
    # Teste: reset de cache funciona
    F_new2.reset_cache()
    T.assert_equals(len(F_new2.cache), 2, "Cache: reset should return to size 2")
    T.assert_equals(F_new2.saved, 2, "Cache: reset should restore saved to 2")

    # ==========================================
    # SEÇÃO 7: VALORES GRANDES (PERFORMANCE)
    # ==========================================
    
    large_values = [100, 200, 500, 1000]
    
    for n in large_values:
        # Iterativo
        start = time()
        val_iter = F.fib_iterative(n)
        time_iter = time() - start
        T.assert_equals(isinstance(val_iter, int), True, 
                       f"Iterative: fib({n}) should return int")
        T.assert_equals(time_iter < 0.1, True, 
                       f"Iterative: fib({n}) should be fast (<0.1s)")
        
        # Exponencial
        start = time()
        val_exp = F.fib_exponential(n)
        time_exp = time() - start
        T.assert_equals(isinstance(val_exp, int), True, 
                       f"Exponential: fib({n}) should return int")
        T.assert_equals(time_exp < 0.1, True, 
                       f"Exponential: fib({n}) should be fast (<0.1s)")
        
        # Cache
        start = time()
        val_cache = F.fib_cache(n)
        time_cache = time() - start
        T.assert_equals(isinstance(val_cache, int), True, 
                       f"Cache: fib({n}) should return int")
        T.assert_equals(time_cache < 0.1, True, 
                       f"Cache: fib({n}) should be fast (<0.1s)")
        
        
    before_cache_size = len(F.cache)
    F.fib_cache(10000)
    after_cache_size = len(F.cache)
    T.assert_equals(after_cache_size > before_cache_size, True, "Cache increases after computation")

    # --- Teste de grandes valores (só pra checar performance leve) ---
    start = time()
    val = F.fib_cache(1000)
    duration = time() - start
    T.assert_equals(isinstance(val, int), True, "Cache handles large Fibonacci numbers")
    T.assert_equals(duration < 0.1, True, "Cache is efficient for n=1000")

    # ==========================================
    # SEÇÃO 8: COMPARAÇÃO DE PERFORMANCE
    # ==========================================
    
    # Cache deve ser mais rápido em chamadas repetidas
    F_perf = Fibonacci()
    
    # Primeira chamada (preenche cache)
    start = time()
    F_perf.fib_cache(100)
    first_call = time() - start
    
    # Segunda chamada (do cache)
    start = time()
    F_perf.fib_cache(100)
    second_call = time() - start
    
    T.assert_equals(second_call < first_call, True, 
                   "Cache: second call should be faster than first")
    T.assert_equals(second_call < 0.001, True, 
                   "Cache: cached value should be retrieved very fast")

    # ==========================================
    # SEÇÃO 9: VALORES ESPECÍFICOS CONHECIDOS
    # ==========================================
    
    known_values = {
        60: 1548008755920,
        70: 190392490709135,
        80: 23416728348467685,
        90: 2880067194370816120,
    }
    
    for n, expected in known_values.items():
        T.assert_equals(F.fib_iterative(n), expected, 
                       f"Known value: fib({n}) = {expected}")
        T.assert_equals(F.fib_cache(n), expected, 
                       f"Cache known value: fib({n}) = {expected}")

    # ==========================================
    # SEÇÃO 10: PADRÕES NA SEQUÊNCIA
    # ==========================================
    
    # Todo terceiro número de Fibonacci é par
    for n in range(3, 30, 3):
        val = F.fib_cache(n)
        T.assert_equals(val % 2, 0, f"Pattern: F({n}) should be even")
    
    # Todo quarto número é divisível por 3
    for n in range(4, 32, 4):
        val = F.fib_cache(n)
        T.assert_equals(val % 3, 0, f"Pattern: F({n}) should be divisible by 3")
    
    # Todo quinto número termina em 0 ou 5
    for n in range(5, 35, 5):
        val = F.fib_cache(n)
        last_digit = val % 10
        T.assert_equals(last_digit in [0, 5], True, 
                       f"Pattern: F({n}) should end in 0 or 5")

    # ==========================================
    # SEÇÃO 11: CRESCIMENTO DA SEQUÊNCIA
    # ==========================================
    
    # Fibonacci cresce exponencialmente: F(n+1) > F(n)
    for n in range(2, 50):
        fn = F.fib_cache(n)
        fn_plus_1 = F.fib_cache(n + 1)
        T.assert_equals(fn_plus_1 > fn, True, 
                       f"Growth: F({n+1}) should be greater than F({n})")
    
    # Razão entre números consecutivos aproxima-se de phi (golden ratio)
    # Para números grandes, F(n+1)/F(n) ≈ 1.618
    phi = (1 + sqrt(5)) / 2
    for n in [20, 30, 40, 50]:
        fn = F.fib_cache(n)
        fn_plus_1 = F.fib_cache(n + 1)
        ratio = fn_plus_1 / fn
        diff = abs(ratio - phi)
        T.assert_equals(diff < 0.01, True, 
                       f"Golden ratio: F({n+1})/F({n}) ≈ phi (diff={diff:.4f})")

    # ==========================================
    # SEÇÃO 12: EDGE CASES ADICIONAIS
    # ==========================================
    
    # Teste múltiplas instâncias de Fibonacci
    F1 = Fibonacci()
    F2 = Fibonacci()
    
    F1.fib_cache(15)
    F2.fib_cache(10)
    
    T.assert_equals(len(F1.cache), 16, "Instance 1: cache should be independent")
    T.assert_equals(len(F2.cache), 11, "Instance 2: cache should be independent")
    
    # Caches não devem interferir um com o outro
    val1 = F1.fib_cache(15)
    val2 = F2.fib_cache(15)
    T.assert_equals(val1, val2, "Different instances should return same values")
    T.assert_equals(len(F1.cache), 16, "Instance 1: cache unchanged")
    T.assert_equals(len(F2.cache), 16, "Instance 2: cache now updated")

    # ==========================================
    # SEÇÃO 13: INTEGRIDADE DOS DADOS
    # ==========================================
    
    # Todos os valores devem ser não-negativos
    for n in range(0, 50):
        val = F.fib_cache(n)
        T.assert_equals(val >= 0, True, f"Non-negative: F({n}) should be >= 0")
    
    # Tipo de retorno deve ser sempre int
    for n in [0, 1, 10, 50, 100]:
        T.assert_equals(type(F.fib_iterative(n)), int, 
                       f"Type: iterative fib({n}) should return int")
        T.assert_equals(type(F.fib_exponential(n)), int, 
                       f"Type: exponential fib({n}) should return int")
        T.assert_equals(type(F.fib_cache(n)), int, 
                       f"Type: cache fib({n}) should return int")