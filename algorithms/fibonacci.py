from math import sqrt
from time import time

def get_time(func, param: int) -> float:
    start_time: float = time()
    func(param)
    end_time: float = time()
    result: float = (end_time - start_time)
    return result

class Fibonacci:
    def __init__(self):
        self.saved: int = 2
        self.cache: dict[int:int] = { 0: 0, 1: 1 }

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
        result: float = (a**n + b**n) / sqrt(5) 
        return round(result)

    def fib_cache(self, n: int) -> int:
        if n not in self.cache:
            for i in range(self.saved, n+1):
                self.cache[i] = self.cache[i-1] + self.cache[i-2] 
                self.saved += 1
        return self.cache[n]


if __name__ == "__main__":
    F: Fibonacci = Fibonacci()
    num: int = 35

    for i in range(num):
        print(f"Iteração {i:>3}:")
        print(f"ITERA: {get_time(F.fib_iterative,   i):.6f}") 
        print(f"RECUR: {get_time(F.fib_recursive,   i):.6f}") 
        print(f"EXPON: {get_time(F.fib_exponential, i):.6f}")
        print(f"CACHE: {get_time(F.fib_cache,       i):.6f}")
        print()

