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

    def are_relatively_prime(self, number_1: int, number_2: int) -> bool:
        pass

if __name__ == "__main__":
    P: Primes = Primes()

    for i in range(0, 21):
        print(f"{i} is {"not " * (not P.is_prime(i))}prime")