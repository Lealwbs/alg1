# Algoritimo de Maior subpartição com o maior lucro


class AlgBet():
    def __init__(self, arr: list = []) -> None:
        self.values: list[int] = arr
        self.size: int = len(arr)
        pass

    def __str__(self) -> str:
        return f"{self.size} values: {self.values}"
    
    def is_empty(self) -> bool:
        return len(self.values) == 0

    def add_value(self, value: int) -> None:
        self.values.append(value)
        self.size += 1

    def pop_value(self) -> int:
        self.size -= 1
        return self.values.pop(0)

    def get_highest_profit_sequence(self) -> list[int]:
        if self.is_empty: return []
        if self.size == 1: return self.values

        end = size = self.size

        # _highest_profit(0, end)

        return 
    
    def _highest_profit(self, start: int, end: int):
        # if start == end: return 
        # middle: int = size/2
        # self._highest_profit(start, middle)

        pass
    
    def get_highest_profit(self) -> int:
        return len(self.get_highest_profit_sequence())

    def get_highest_loss_sequence(self) -> list[int]:
        pass

    def get_highest_loss(self) -> int:
        return len(self.get_highest_loss_sequence())

if __name__ == "__main__":
    numbers: list[int] = [10, 3, -6, 2, -8, 4, 5, -6, 1, -3, 7, 1, -9, -4, 2, 0, 5, -4, 6, 2]
    A: AlgBet = AlgBet(numbers)
    A.add_value(-5)
    print(A.pop_value())

    print(A)