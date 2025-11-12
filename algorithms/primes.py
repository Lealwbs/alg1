import math 


class Primes:
    def __init__(self):
        pass

    def is_prime(self, number: int) -> bool:
        if number == 0 or number == 1: return False
        for i in range(2, number):
            if number % i == 0:
                return False
        return True

    def are_relatively_prime(self, a: int, b: int) -> bool:
        if a == 1 or b == 1: return False
        v1: int = max(a, b) - min(a, b)
        v2: int = min(a, b)
        return self.are_relatively_prime(self, v1, v2)

if __name__ == "__main__":
    P: Primes = Primes()

    for i in range(0, 21):
        print(f"{i} is {"not " * (not P.is_prime(i))}prime")